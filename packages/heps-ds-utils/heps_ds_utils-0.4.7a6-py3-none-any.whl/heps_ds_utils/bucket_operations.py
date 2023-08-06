""" This Module is created to enable Hepsiburada Data Science to communicate with Cloud Storage. """

import json
import os
import pickle
import shutil
import zipfile
from io import BytesIO

import pandas as pd
from colorama import Fore, init  # #Style
from google.api_core.exceptions import NotFound
from google.cloud import storage
from google.oauth2 import service_account

init(autoreset=True)


class BucketOperations(storage.Client):
    """This class is created to enable Hepsiburada Data Science to communicate with Cloud Storage"""

    _implemented_type = ["dataframe", "json", "pickle"]

    def __init__(self, **kwargs) -> None:
        self.gcp_key = kwargs.get("gcp_key_path")
        self.credentials = kwargs.get("gcp_key_path")
        super().__init__(
            project=self.credentials.project_id, credentials=self.credentials
        )

    def __repr__(self) -> str:
        """This function returns project id and service account email."""
        return (
            f"{self.__class__.__name__}(Project ID: {self.credentials.project_id}, "
            f"Service Account: {self.credentials._service_account_email.split('@')[0]})"
        )

    def does_blob_exist(self, bucket_name: str, blob_name: str) -> bool:
        """_summary_

        Args:
            bucket_name (str): Bucket name
            blob_name (str): Blob name to be checked

        Returns:
            bool: Returns True if blob exists, otherwise False
        """
        bucket = self.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        return blob.exists()

    def upload_from_filepath(self, bucket_name, blob_name, filepath):
        """This function is to upload data from filepath."""
        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(filepath)

            if not blob.exists():
                raise RuntimeError(Fore.RED + f"Could not upload {blob_name}.")
            file_size = os.stat(filepath).st_size
            if file_size != blob.size:
                raise RuntimeError(
                    Fore.RED
                    + f"Size of {blob_name} is {blob.size},"
                    + f"but the size of {filepath} is {file_size} "
                )

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

        except Exception:
            print(f"No such file in this path: <{filepath}>")

    def upload_from_memory(
        self,
        bucket_name,
        blob_name,
        contents,
        upload_type,
        check_upload: bool = True,
    ):
        """This function is to upload data from memory."""
        if upload_type not in BucketOperations._implemented_type:
            raise NotImplementedError(
                Fore.RED + f"Download type {upload_type} not implemented !!"
            )

        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)

            if upload_type == "json":
                send_data = json.dumps(contents, indent=4).encode("utf-8")
            elif upload_type == "pickle":
                send_data = pickle.dumps(contents)
            elif upload_type == "dataframe":
                send_data = contents.to_csv()

            blob.upload_from_string(send_data)

            if check_upload and not blob.exists():
                raise RuntimeError(f"{blob_name} does not exist.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

    def download_to_filepath(
        self, bucket_name, blob_name, filepath, extract=False
    ):
        """This function is to download data from filepath."""
        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            if blob.exists():
                with open(filepath, "wb") as f:
                    self.download_blob_to_file(blob, f)

                if extract:
                    file_name = filepath.split("/")[-1]
                    folder_path = filepath[: -len(file_name)]
                    shutil.unpack_archive(filepath, folder_path, "zip")

            else:
                print(f"Blob <{blob_name}> does not exist.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

        except Exception as ex:
            print(ex)
            print(f"No such file in this path: <{filepath}>")

    def download_to_memory(self, bucket_name, blob_name, download_type):
        """This function is to download data from memory."""
        if download_type not in BucketOperations._implemented_type:
            raise NotImplementedError(
                Fore.RED + f"Download type {download_type} not implemented !!"
            )

        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            if blob.exists():
                if download_type == "dataframe":
                    df = pd.read_csv(
                        BytesIO(blob.download_as_string()),
                        encoding="UTF-8",
                        sep=",",
                    )
                    return df

                elif download_type == "json":
                    data = (
                        blob.download_as_string()
                        .decode("utf8")
                        .replace("'", '"')
                    )
                    load_json = json.loads(data)
                    json_data = json.dumps(load_json, indent=4, sort_keys=True)
                    return json_data

                elif download_type == "pickle":
                    data = blob.download_as_bytes()
                    try:
                        load_pickle = pickle.loads(data)
                    except pickle.UnpicklingError:
                        load_pickle = BytesIO(data)

                    return load_pickle
            else:
                print(f"Blob <{blob_name}> does not exist.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

    def create_new_folders(self, bucket_name, folder_name):
        """This function is to create new folder from the bucket."""
        try:
            bucket = self.bucket(bucket_name)
            dst_bucket = self.bucket(bucket_name)

            blob = bucket.blob("New_Folder_Starter/")
            new_blob = bucket.copy_blob(blob, dst_bucket, new_name=folder_name)

            new_blob.acl.save(blob.acl)
            print(f"<{folder_name}> folder created.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

    def delete_folder_from_bucket(self, bucket_name, folder_name):
        """This function is to create new folder from the bucket."""
        try:
            bucket = self.get_bucket(bucket_name)
            blobs = bucket.list_blobs(prefix=folder_name)
            for blob in blobs:
                blob.delete()

            print(f"Folder <{folder_name}> deleted.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

    def delete_file_from_bucket(self, bucket_name, blob_name):
        """This function is to delete file from the bucket."""

        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.delete()
            print(f"Blob <{blob_name}> deleted.")

        except NotFound:
            print(f"No such file in this path: <{bucket_name}/{blob_name}>")

    def download_recursively(
        self,
        bucket_name: str,
        blob_name: str,
        overwrite: bool,
        folder_path: str,
        as_zip: bool = False,
    ):
        """Downloads all files from given bucket directory.

        Args:
            bucket_name (str): Name of bucket
            blob_name (str): Parent directory of files at bucket.
            overwrite (bool): Determines to write over existing files or not.
            folder_path (str): Parent directory of location to be downloaded at local.
        """
        blob_name = blob_name + "/" if blob_name[-1] != "/" else blob_name

        blobs = self.list_blobs(bucket_name, prefix=blob_name)
        if as_zip:
            os.makedirs(folder_path, exist_ok=True)
            bucket = self.bucket(bucket_name)
            blob_names = [blob.name for blob in blobs]

            zip_name = blob_name.split("/")[-2] + ".zip"
            download_path = os.path.join(folder_path, zip_name)
            with zipfile.ZipFile(download_path, "w") as zip:
                for sub_blob_name in blob_names:
                    blob = bucket.blob(sub_blob_name)
                    data = blob.download_as_string()
                    sub_file_path = sub_blob_name[len(blob_name) :]
                    if len(sub_file_path) == 0:
                        continue
                    zip.writestr(sub_file_path, data)
            return

        for blob in blobs:
            download_path = os.path.join(
                folder_path, blob.name[len(blob_name) :]
            )
            if len(download_path) == 0:
                continue
            idx = download_path.rfind("/")
            if not os.path.exists(download_path[:idx]) and (
                idx != -1 or download_path[-1] == "/"
            ):
                os.makedirs(download_path[:idx], exist_ok=True)

            if download_path[-1] == "/":
                continue
            if not os.path.exists(download_path) or (
                os.path.exists(download_path) and overwrite
            ):
                self.download_to_filepath(
                    bucket_name, blob.name, download_path
                )

    def upload_recursively(
        self,
        bucket_name: str,
        blob_name: str,
        overwrite: bool,
        folder_path: str,
        as_zip=False,
    ):
        """Downloads all files from given local directory.

        Args:
            bucket_name (str): Name of bucket
            blob_name (str): Parent directory of files to be uploaded at bucket.
            overwrite (bool): Determines to write over existing files or not.
            folder_path (str): Parent directory of source files at local.
            as_zip (bool, optional): Upload a folder as zip to bucket.
                                     Default is False.
        """
        folder_path = (
            folder_path + "/" if folder_path[-1] != "/" else folder_path
        )
        blob_name = blob_name + "/" if blob_name[-1] != "/" else blob_name

        blobs = self.list_blobs(bucket_name, prefix=blob_name)
        blob_names = [blob.name for blob in blobs]

        if as_zip:
            zip_name = folder_path.split("/")[-2]
            zip_path = os.path.join(
                folder_path[: -(len(zip_name) + 1)], zip_name
            )
            zip_name += ".zip"
            upload_file_path = blob_name + zip_name
            source_file_path = zip_path + ".zip"
            if upload_file_path not in blob_names or (
                upload_file_path in blob_names and overwrite
            ):
                shutil.make_archive(zip_path, "zip", folder_path)
                self.upload_from_filepath(
                    bucket_name, upload_file_path, source_file_path
                )
            return

        for path, dirs, files in os.walk(folder_path):
            for dir in dirs:
                upload_dir_path = os.path.join(
                    blob_name, path[len(folder_path) :], dir + "/"
                )
                if upload_dir_path not in blob_names:
                    self.create_new_folders(bucket_name, upload_dir_path)

            for file in files:
                upload_file_path = os.path.join(
                    blob_name, path[len(folder_path) :], file
                )
                source_file_path = os.path.join(path, file)
                if upload_file_path not in blob_names or (
                    upload_file_path in blob_names and overwrite
                ):
                    self.upload_from_filepath(
                        bucket_name, upload_file_path, source_file_path
                    )

    @property
    def gcp_key(self):
        """This function is to get GCP key."""
        return self._gcp_key

    @gcp_key.setter
    def gcp_key(self, provided_gcp_key):
        """This function is to set GCP key."""
        if provided_gcp_key is not None:
            self._gcp_key = str(provided_gcp_key)
            self.credentials = str(provided_gcp_key)
        elif os.environ.get("SERVICE_ACCOUNT_KEY_PATH"):
            self._gcp_key = os.environ.get("SERVICE_ACCOUNT_KEY_PATH")
        else:
            self._gcp_key = None
            print(
                Fore.RED
                + "Warning!! GCP Key Path for Service Account is not specified"
            )

    @property
    def credentials(self):
        """This function is to get credentials."""
        return self._credentials

    @credentials.setter
    def credentials(self, provided_credentials):
        """This function is to set credentials."""
        if provided_credentials is not None:
            self._credentials = (
                service_account.Credentials.from_service_account_file(
                    self.gcp_key,
                    scopes=["https://www.googleapis.com/auth/cloud-platform"],
                )
            )
        elif os.environ.get("SERVICE_ACCOUNT_KEY_PATH"):
            self._credentials = (
                service_account.Credentials.from_service_account_file(
                    self.gcp_key,
                    scopes=["https://www.googleapis.com/auth/cloud-platform"],
                )
            )
        else:
            self._credentials = None
            print(
                Fore.RED
                + "Warning!! Credentials for Service Account is not specified"
            )
