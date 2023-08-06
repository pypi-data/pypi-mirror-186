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
        drive = GoogleDrive(gauth)

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
