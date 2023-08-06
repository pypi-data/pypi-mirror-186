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


class gDriveExplorer:

    def __init__(self, drive_id):

        auth.authenticate_user()
        gauth = GoogleAuth()
        gauth.credentials = GoogleCredentials.get_application_default()
        self.drive = GoogleDrive(gauth)

        self.drive_service = build('drive', 'v3')

        self.explore_dict = dict()

        self.drive_id = drive_id

        self.explorer(drive_id, None)

    def explorer(self, id, path):

        token = ''
        file_list = []
        q = "'" + id + "' in parents and trashed=false"

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
        '''
        Devuelve el id del path
        _path_from_base: El path desde la carpeta base
        _base: ID de google drive de la carpeta contenedora
        '''
        result = None
        levels = []
        path = path_from_base
        while self.explore_dict.get(path, None) is None:
            split_path = os.path.split(path)
            path = split_path[0]
            levels = levels + [split_path[1]]
        for p in reversed(levels):
            self.explorer(self.explore_dict[path], path)
            path = os.path.join(path, p)

        return self.explore_dict[path_from_base]

    def create_folder(self, folder_name, path):

        root, folder_name = os.path.split(path)

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

        id = self.get_id_from_path(path_from_base)

        request = self.drive_service.files().get_media(fileId=id)

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
        '''
        read csv using pydrive
        kwargs are the kwargs of pd.to_csv function
        '''

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

    def create_or_update_file(self, path_from_base):

        root, name = os.path.split(path_from_base)

        # Definir atributos del fichero a sobreescribir
        file_metadata = {
            'name': name
            ## Nota: formato excel es: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            #   ,'mimeType': 'text/csv'
        }

        # Definir qué fichero de colab es el que se va a subir
        media = MediaFileUpload(name,
                                chunksize=-1,
                                # mimetype=formato,
                                resumable=True)

        try:

            file_id = self.get_id_from_path(path_from_base)

            response = self.drive_service.files().update(fileId=file_id,
                                                         body=file_metadata,
                                                         media_body=media,
                                                         supportsAllDrives='true').execute()

        except Exception as e:

            folder_id = self.get_id_from_path(root)

            file_metadata['parents'] = [folder_id]

            response = drive_service.files().create(body=file_metadata,
                                                    media_body=media,
                                                    supportsAllDrives='true').execute()

        return response

    def persist(self, func, path_from_base, **kwargs):
        '''
        func: function that persist in local
        name: desired name (the function must be called as func(name,**kwargs))
        kwargs: the kwargs of the func
        path: desired path
        base: the base
        '''

        root, name = os.path.split(path_from_base)

        func(name, **kwargs)

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_csv(self, df, path_from_base, **kwargs):
        '''
        write to csv using pydrive
        kwargs are the kwargs of pd.to_csv function
        '''

        root, name = os.path.split(path_from_base)

        df.to_csv(name, **kwargs)  # Hacemos el to_csv al local de colab

        self.create_or_update_file(path_from_base)

        os.remove(name)

    def to_excel(self, df, path_from_base, **kwargs):
        '''
        write to csv using pydrive
        kwargs are the kwargs of pd.to_csv function
        '''

        root, name = os.path.split(path_from_base)

        df.to_excel(name, **kwargs)  # Hacemos el to_csv al local de colab

        self.create_or_update_file(path_from_base)

        os.remove(name)