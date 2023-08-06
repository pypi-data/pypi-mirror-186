from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload

import pandas as pd
import os
import pickle
import dill
import zipfile


class gDriveExplorer:

    def __init__(self, drive_id):

        auth.authenticate_user()

        g_auth = GoogleAuth()

        g_auth.credentials = GoogleCredentials.get_application_default()

        self.drive = GoogleDrive(g_auth)

        self.drive_service = build('drive', 'v3')

        self.explore_dict = dict()

        self.drive_id = drive_id

        self.explorer(drive_id, None)

    def explorer(self, id_, path):

        token = ''
        file_list = []
        q = "'" + id_ + "' in parents and trashed=false"

        while token is not None:
            list_ = self.drive_service.files().list(corpora='teamDrive',
                                                    pageSize=1000,
                                                    supportsTeamDrives=True,
                                                    includeTeamDriveItems=True,
                                                    driveId=self.drive_id,
                                                    q=q,
                                                    pageToken=token).execute()

            file_list = file_list + list_['files']
            token = list_.get('nextPageToken', None)

        for f in file_list:
            if path is not None:
                new_path = os.path.join(path, f['name'])
            else:
                new_path = f['name']

            self.explore_dict[new_path] = f['id']

    def get_id_from_path(self, path_from_base):

        if path_from_base.endswith('/'):
            path_from_base = path_from_base[:-1]

        levels = []

        path = path_from_base

        while self.explore_dict.get(path, None) is None:

            split_path = os.path.split(path)

            if split_path[0] == '':
                raise Exception("'" + path_from_base + "' not found")

            path = split_path[0]

            levels = levels + [split_path[1]]

        for p in reversed(levels):
            self.explorer(self.explore_dict[path], path)

            path = os.path.join(path, p)

        if path_from_base not in self.explore_dict.keys():
            raise Exception("'" + path_from_base + "' not found")

        return self.explore_dict[path_from_base]

    def create_folder(self, path_from_base):

        if not self.path_exists(path_from_base):
            root, folder_name = os.path.split(path_from_base)

            folder = self.drive.CreateFile({'title': folder_name,
                                            'mimeType': 'application/vnd.google-apps.folder',
                                            'parents': [{
                                                'kind': 'drive#fileLink',
                                                'id': self.get_id_from_path(root)

                                            }]})
            folder.Upload(param={'supportsTeamDrives': True})

    def path_exists(self, path_from_base):

        try:
            _ = self.get_id_from_path(path_from_base)

            return True

        except:

            return False

    def get_file_from_path(self, path_from_base, name=None):

        id_ = self.get_id_from_path(path_from_base)

        request = self.drive_service.files().get_media(fileId=id_)

        if name is not None:
            downloaded = io.FileIO(name, mode='w')
        else:
            downloaded = io.BytesIO()

        downloader_ = MediaIoBaseDownload(downloaded, request, chunksize=1024 * 1024 * 1024)
        done = False
        while done is False:
            # _ is a placeholder for a progress object that we ignore.
            # (Our file is small, so we skip reporting progress.)
            _, done = downloader_.next_chunk()

        if name is None:
            return downloaded.getvalue()

        # else:
        #     return None

    def get_size(self, file_id):
        pass
        # file = self.drive_service.files().get(fileId=file_id, fields='size,modifiedTime').execute()

    def read_csv(self, path_from_base, is_large=False, **kwargs):

        decode = 'utf-8'

        if is_large:

            self.get_file_from_path(path_from_base, 'temp.csv')

            df_ = pd.read_csv('temp.csv', **kwargs)

            # df_ = pd.DataFrame()

            os.remove('temp.csv')

            return df_

        else:

            return pd.read_csv(io.StringIO(self.get_file_from_path(path_from_base).decode(decode)), **kwargs)

    def read_excel(self, path_from_base, **kwargs):

        return pd.read_excel(self.get_file_from_path(path_from_base), **kwargs)

    def read_parquet(self, path_from_base, **kwargs):

        return pd.read_parquet(io.BytesIO(self.get_file_from_path(path_from_base)), **kwargs)

    def create_or_update_file(self, path_from_base):

        root, name = os.path.split(path_from_base)

        file_metadata = {
            'name': name
            #   ,'mimeType': 'text/csv'
        }

        media = MediaFileUpload(name,
                                chunksize=-1,
                                # mimetype=format,
                                resumable=True)

        try:

            file_id = self.get_id_from_path(path_from_base)

            response = self.drive_service.files().update(fileId=file_id,
                                                         body=file_metadata,
                                                         media_body=media,
                                                         supportsAllDrives='true').execute()

        except:

            folder_id = self.get_id_from_path(root)

            file_metadata['parents'] = [folder_id]

            response = self.drive_service.files().create(body=file_metadata,
                                                         media_body=media,
                                                         supportsAllDrives='true').execute()

        return response

    def persist(self, func, path_from_base, **kwargs):

        root, name = os.path.split(path_from_base)

        func(name, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_csv(self, df, path_from_base, **kwargs):

        root, name = os.path.split(path_from_base)

        df.to_csv(name, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_excel(self, df, path_from_base, **kwargs):

        root, name = os.path.split(path_from_base)

        df.to_excel(name, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_dill(self, func_list, path_from_base, **kwargs):

        root, name = os.path.split(path_from_base)

        with open(name, 'wb') as dill_file:
            dill.dump(func_list, dill_file, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_pickle(self, func_list, path_from_base, **kwargs):

        root, name = os.path.split(path_from_base)

        with open(name, 'wb') as f:
            pickle.dump(func_list, f, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_parquet(self, df, path_from_base, **kwargs):

        root, name = os.path.split(path_from_base)

        df.to_parquet(name, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_excel_sheets(self, dic, path_from_base, **kwargs):

        root, name = os.path.split(path_from_base)

        with pd.ExcelWriter(name) as writer:
            for i in dic.keys():
                dic[i].to_excel(writer, sheet_name=i, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def show_contents(self, path_from_base):

        token = ''
        file_list = []

        id_ = self.get_id_from_path(path_from_base)

        q = "'" + id_ + "' in parents and trashed=false"

        while token is not None:
            list_ = self.drive_service.files().list(corpora='teamDrive',
                                                    pageSize=1000,
                                                    supportsTeamDrives=True,
                                                    includeTeamDriveItems=True,
                                                    driveId=self.drive_id,
                                                    q=q,
                                                    pageToken=token).execute()

            file_list = file_list + list_['files']
            token = list_.get('nextPageToken', None)

        return [item['name'] for item in file_list]

    def get_csv_from_zip(self, path_from_base, file_name, **kwargs):

        zip_reader = zipfile.ZipFile(io.BytesIO(self.get_file_from_path(path_from_base)))

        df = pd.read_csv(zip_reader.open(file_name), **kwargs)

        return df

    def download_file_to_local(self, path_from_base):

        root, name = os.path.split(path_from_base)

        self.get_file_from_path(path_from_base, name)
