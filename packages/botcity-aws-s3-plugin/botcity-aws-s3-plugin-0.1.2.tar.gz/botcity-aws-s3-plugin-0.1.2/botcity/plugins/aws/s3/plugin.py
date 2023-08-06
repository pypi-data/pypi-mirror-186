import os
import posixpath
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

import boto3

from botcity.plugins.aws.s3.filter import Filter, filter_items
from botcity.plugins.aws.s3.utils import list_all_files


class BotAWSS3Plugin:
    def __init__(self, region_name: str = 'us-east-1', use_credentials_file: Optional[bool] = True,
                 access_key_id: Optional[str] = None, secret_access_key: Optional[str] = None) -> None:
        """
        BotAWSS3Plugin

        Args:
            region_name (str): Default region when creating new connections.
            use_credentials_file (bool, optional): If set to True will make
                authentication via AWS credentials file.
            access_key_id (str, optional): AWS access key ID.
            secret_access_key (str, optional): AWS secret access key.
        """
        self._bucket_name = None
        if use_credentials_file:
            self._client = boto3.client(service_name='s3')
        else:
            self._client = boto3.client(
                service_name='s3',
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name
            )

    @property
    def s3_client(self):
        """
        Returns the aws client instance.

        Returns:
            boto3_instance: The aws client instance.
        """
        return self._client

    @property
    def bucket_name(self):
        """
        Returns the bucket name.

        Returns:
            bucket_name: The bucket name.
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Setting up the bucket name.

        Args:
            bucket_name: The bucket name.
        """
        self._bucket_name = bucket_name

    def create_bucket(self, bucket_name: Optional[str] = None, **kwargs) -> None:
        """
        Create new bucket.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket) # noqa

        Args:
            bucket_name (str, optional): The new bucket name to be created.
            kwargs (dict, optional): The dict for bucket permissions.
        """
        self._client.create_bucket(Bucket=bucket_name or self.bucket_name, **kwargs)

    def list_buckets(self) -> List[str]:
        """
        Returns the list of all buckets.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets) # noqa

        Returns:
            buckets: The list of all buckets.
        """
        response = self._client.list_buckets()['Buckets']
        return [buckets['Name'] for buckets in response]

    def filter_buckets(self, text: str, regex: Optional[bool] = False,
                       filter_: Filter = Filter.EQUALS) -> List[str]:
        """
        Filter buckets.

        Args:
            text (str): The element to filter.
            regex (bool, optional): True to enable regex search.
                [See for regex details](https://docs.python.org/3/library/re.html)
            filter_ (Filter, optional): Filter pattern without user using regex.
        """
        buckets = self.list_buckets()
        return filter_items(buckets, text, regex, filter_)

    def delete_bucket(self, bucket_name: Optional[str] = None, **kwargs) -> None:
        """
        Delete the bucket.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_bucket) # noqa

        Args:
            bucket_name (str, optional): The new bucket name to be created.
        """
        self._client.delete_bucket(Bucket=bucket_name or self.bucket_name, **kwargs)

    def upload_file(self, file_path: str, bucket_name: Optional[str] = None,
                    bucket_filename: Optional[str] = None, extra_args: Optional[Dict] = None) -> None:
        """
        Upload file to bucket.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file) # noqa

        Args:
            file_path (str): The local file path.
            bucket_name (str, optional): The bucket name.
            bucket_filename (str): The new filename in the bucket.
            extra_args (Dict): Extra arguments that may be passed to the client operation.
                [Learn more about ALLOWED_UPLOAD_ARGS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html)
        """
        if bucket_filename is None:
            bucket_filename = os.path.basename(file_path)
        self._client.upload_file(Filename=file_path, Bucket=bucket_name or self.bucket_name,
                                 Key=bucket_filename.strip('/'), ExtraArgs=extra_args)

    def download_file(self, filename: str, path_to_save: str, bucket_name: Optional[str] = None,
                      extra_args: Optional[Dict] = None) -> None:
        """
        Download file from the bucket.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.download_file) # noqa

        Args:
            filename (str): The filename in the bucket.
            path_to_save (str): The local path to save.
            bucket_name (str, optional): The bucket name.
            extra_args (Dict): Extra arguments that may be passed to the client operation.
                [Learn more about ALLOWED_DOWNLOAD_ARGS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html)

        Returns:
            file_path: The downloaded file path
        """
        file_to_save = os.path.join(path_to_save, os.path.basename(filename))
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)  # creating directories if not exists
        self._client.download_file(bucket_name or self.bucket_name, filename.strip('/'), file_to_save,
                                   ExtraArgs=extra_args)
        return file_to_save

    def copy_file(self, filename: str, target_filename: str, bucket_name: Optional[str] = None,
                  target_bucket_name: Optional[str] = None, extra_args: Optional[Dict] = None):
        """
        Copy the file to another bucket or in the same bucket.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.copy) # noqa

        Args:
            filename (str): The original filename in the bucket.
            target_filename (str): The new copy of the file.
            bucket_name (str, optional): The bucket name.
            target_bucket_name (str): The another bucket to save this copy.
            extra_args (Dict): Extra arguments that may be passed to the client operation.
                [Learn more about ALLOWED_DOWNLOAD_ARGS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html)
        """
        bucket_name = bucket_name or self.bucket_name
        if target_bucket_name is None:
            target_bucket_name = bucket_name
        copy_source = {'Bucket': bucket_name, 'Key': filename.strip('/')}
        self._client.copy(copy_source, target_bucket_name, target_filename, ExtraArgs=extra_args)

    def list_files(self, bucket_name: Optional[str] = None, **kwargs) -> List[str]:
        """
        Returns the list of files.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects) # noqa

        Args:
            bucket_name (str, optional): The bucket name.

        Returns:
            buckets: The list of buckets.
        """
        response = self._client.list_objects(Bucket=bucket_name or self.bucket_name, **kwargs)['Contents']
        return [buckets['Key'] for buckets in response]

    def filter_files(self, text: str, bucket_name: Optional[str] = None, regex: Optional[bool] = False,
                     filter_: Filter = Filter.EQUALS, **kwargs) -> List[str]:
        """
        Filter files.

        Args:
            text (str): The element to filter.
            bucket_name (str, optional): The bucket name.
            regex (bool, optional): True to enable regex search.
                [See for regex details](https://docs.python.org/3/library/re.html)
            filter_ (Filter, optional): Filter pattern without user using regex.
        """
        buckets = self.list_files(bucket_name or self.bucket_name, **kwargs)
        return filter_items(buckets, text, regex, filter_)

    def delete_file(self, filename: str, bucket_name: Optional[str] = None, **kwargs) -> None:
        """
        Delete file from the bucket.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_object) # noqa

        Args:
            filename (str): The filename in the bucket.
            bucket_name (str, optional): The bucket name.
        """
        self._client.delete_object(Bucket=bucket_name or self.bucket_name, Key=filename.strip('/'), **kwargs)

    def move_file(self, filename: str, target_filename: str, bucket_name: Optional[str] = None,
                  target_bucket_name: Optional[str] = None, extra_args: Optional[Dict] = None,
                  **kwargs) -> None:
        """
        Move the file to another bucket or in the same bucket.

        Args:
            filename (str): The filename in the bucket.
            target_filename (str): The new copy of the file.
            bucket_name (str, optional): The bucket name.
            target_bucket_name (str, optional): The another bucket to save this copy.
            extra_args (Dict, optional): Extra arguments that may be passed to the client operation.
                [Learn more about ALLOWED_DOWNLOAD_ARGS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html) # noqa
        """
        bucket_name = bucket_name or self.bucket_name
        filename = filename.strip('/')
        self.copy_file(filename, target_filename.strip('/'), bucket_name, target_bucket_name, extra_args)
        self.delete_file(filename, bucket_name, **kwargs)  # deleting origin file

    def upload_folder(self, bucket_folder: str, folder_path: str, bucket_name: Optional[str] = None,
                      max_workers: Optional[int] = 1, extra_args: Optional[Dict] = None) -> None:
        """
        Upload folder to bucket. Empty directories are ignored.

        Args:
            bucket_folder (str): The new folder name in the bucket.
            folder_path (str): The local folder path.
            bucket_name (str, optional): The bucket name.
            max_workers (int, optional): The maximum number of threads that can be used to execute the given calls.
            extra_args (Dict, optional): Extra arguments that may be passed to the client operation.
                [Learn more about ALLOWED_UPLOAD_ARGS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html) # noqa
        """
        folder_path = os.path.normpath(folder_path)
        files = list_all_files(folder_path)

        with ThreadPoolExecutor(max_workers) as executor:
            for file_path, relative_path in files:
                executor.submit(
                    self.upload_file, file_path, bucket_name or self.bucket_name,
                    posixpath.join(bucket_folder, relative_path), extra_args)

    def download_folder(self, bucket_folder: str, path_to_save: str, bucket_name: Optional[str] = None,
                        max_workers: Optional[int] = 1, extra_args: Dict = None) -> None:
        """
        Download all files from the folder.

        Args:
            bucket_folder (str): The folder name in the bucket.
            path_to_save (str): The local path to save.
            bucket_name (str, optional): The bucket name.
            max_workers (int, optional): The maximum number of threads that can be used to execute the given calls.
            extra_args (Dict, optional): Extra arguments that may be passed to the client operation.
                [Learn more about ALLOWED_DOWNLOAD_ARGS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html) # noqa
        """
        bucket_name = bucket_name or self.bucket_name

        def download(filename):
            file_to_save = os.path.join(path_to_save, filename)
            file_path = os.path.dirname(file_to_save)  # get path without filename
            if not os.path.exists(file_path):
                os.makedirs(file_path)  # creating directories if not exists
            self._client.download_file(bucket_name, filename, file_to_save, ExtraArgs=extra_args)

        # list all files from folder
        files = filter_items(self.list_files(bucket_name), bucket_folder.strip('/'), filter_=Filter.STARTS_WITH)
        with ThreadPoolExecutor(max_workers) as executor:
            for file in files:
                executor.submit(download, file)

    def copy_folder(self, folder_path: str, target_folder_name: str, bucket_name: Optional[str] = None,
                    target_bucket_name: Optional[str] = None, max_workers: Optional[int] = 1,
                    extra_args: Optional[Dict] = None):
        """
        Copy the folder to another bucket or in the same bucket.

        Args:
            folder_path (str): The original folder name in the bucket.
            target_folder_name (str): The new copy of the folder.
            bucket_name (str, optional): The bucket name.
            target_bucket_name (str, optional): The another bucket to save this copy.
            max_workers (int, optional): The maximum number of threads that can be used to execute the given calls.
            extra_args (Dict, optional): Extra arguments that may be passed to the client operation.
        """
        bucket_name = bucket_name or self.bucket_name
        folder_path = posixpath.normpath(folder_path).strip('/')
        folder_name = os.path.basename(folder_path)

        def copy(filename):
            file_relative_path = posixpath.join(
                target_folder_name.strip('/'),
                folder_name,
                os.path.relpath(filename, folder_path)
            )

            self.copy_file(
                filename=file,
                target_filename=file_relative_path,
                bucket_name=bucket_name,
                target_bucket_name=target_bucket_name,
                extra_args=extra_args
            )

        with ThreadPoolExecutor(max_workers) as executor:
            for file in self.filter_files(bucket_name=bucket_name, text=folder_path, filter_=Filter.STARTS_WITH):
                executor.submit(copy, file)

    def delete_folder(self, folder_name: str, bucket_name: Optional[str] = None, max_workers: int = 1):
        """
        Delete folder from the bucket.

        Args:
            folder_name (str): The folder name to be deleted.
            bucket_name (str, optional): The bucket name.
            max_workers (int, optional): The maximum number of threads that can be used to execute the given calls.
        """
        bucket_name = bucket_name or self.bucket_name
        with ThreadPoolExecutor(max_workers) as executor:
            for file in self.filter_files(bucket_name=bucket_name,
                                          text=folder_name.strip('/') + '/',
                                          filter_=Filter.STARTS_WITH):
                executor.submit(self.delete_file, file, bucket_name)

    def move_folder(self, folder_path: str, target_folder_name: str, bucket_name: Optional[str] = None,
                    target_bucket_name: Optional[str] = None, max_workers: Optional[int] = 1,
                    extra_args: Optional[Dict] = None, **kwargs):
        """
        Move the folder to another bucket or in the same bucket.

        Args:
            folder_path (str): The original folder name in the bucket.
            target_folder_name (str): The new copy of the folder.
            bucket_name (str, optional): The bucket name.
            target_bucket_name (str, optional): The another bucket to save this copy.
            max_workers (int, optional): The maximum number of threads that can be used to execute the given calls.
            extra_args (Dict, optional): Extra arguments that may be passed to the client operation.
        """
        bucket_name = bucket_name or self.bucket_name
        folder_path = folder_path.strip('/')
        folder_name = os.path.basename(folder_path)

        def move(filename):
            file_relative_path = posixpath.join(
                target_folder_name,
                folder_name,
                posixpath.relpath(filename, folder_path)
            )

            self.move_file(
                filename=filename,
                bucket_name=bucket_name,
                target_bucket_name=target_bucket_name,
                target_filename=file_relative_path,
                extra_args=extra_args,
                **kwargs
            )

        with ThreadPoolExecutor(max_workers) as executor:
            for file in self.filter_files(folder_path, bucket_name=bucket_name, filter_=Filter.STARTS_WITH):
                executor.submit(move, file)

    def rename_folder(self, folder_path: str, target_folder_name: str, bucket_name: Optional[str] = None,
                      max_workers: Optional[int] = 1, extra_args: Optional[Dict] = None, **kwargs):
        """
        Rename the folder.

        Args:
            folder_path (str): The original folder name in the bucket.
            target_folder_name (str): The new copy of the folder.
            bucket_name (str, optional): The bucket name.
            max_workers (int, optional): The maximum number of threads that can be used to execute the given calls.
            extra_args (Dict, optional): Extra arguments that may be passed to the client operation.
        """
        bucket_name = bucket_name or self.bucket_name

        # getting the parent path of folder
        parent_folder_path = posixpath.abspath(posixpath.join(folder_path, os.pardir))

        def rename(filename):
            new_folder_path = posixpath.join(
                parent_folder_path,
                target_folder_name,
                posixpath.relpath(filename, folder_path.strip('/'))
            )

            self.move_file(
                filename=filename,
                bucket_name=bucket_name,
                target_bucket_name=None,
                target_filename=new_folder_path,
                extra_args=extra_args,
                **kwargs
            )

        with ThreadPoolExecutor(max_workers) as executor:
            for file in self.filter_files(folder_path.strip('/'), bucket_name=bucket_name,
                                          filter_=Filter.STARTS_WITH):
                executor.submit(rename, file)
