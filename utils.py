import re
import os
import boto3


def is_valid_storage_path(path):
    """
    This function checks if a given path is a valid S3 or GCS path.

    Args:
        path (str): The path to check

    Returns:
        bool: True if the path is valid, False otherwise

    Examples:
        >>> is_valid_storage_path("s3://my-bucket/my-folder/my-file.txt")
        True
        >>> is_valid_storage_path("gs://my-bucket/my-folder/my-file.txt")
        True
        >>> is_valid_storage_path("foo/bar/baz")
        False
    """
    s3_pattern = r'^s3://([a-zA-Z0-9.\-_]+)/(.+)$'
    gcs_pattern = r'^gs://([a-zA-Z0-9.\-_]+)/(.+)$'
    
    return bool(re.match(s3_pattern, path) or re.match(gcs_pattern, path))



def download_video(path):
    """
    This function downloads a video from a given path to a local file.

    Args:
        path (str): The path to the video to download

    Returns:
        None

    Examples:
        >>> download_video("s3://my-bucket/my-folder/my-file.txt", "my-file.txt")
        Video downloaded from S3 to my-file.txt
        >>> download_video("gs://my-bucket/my-folder/my-file.txt", "my-file.txt")
        Video downloaded from GCS to my-file.txt
        >>> download_video("foo/bar/baz", "my-file.txt")
        Invalid storage path
    """
    s3_pattern = r'^s3://([a-zA-Z0-9.\-_]+)/(.+)$'
    gcs_pattern = r'^gs://([a-zA-Z0-9.\-_]+)/(.+)$'

    if re.match(s3_pattern, path) or re.match(gcs_pattern, path):
        # Download video from S3
        bucket_name, object_name = re.match(s3_pattern, path).groups()
        s3 = boto3.client('s3')
        local_file_path=os.path.join(os.getcwd(), path.split('/')[-1])
        s3.download_file(bucket_name, object_name, local_file_path)
        return True
    return False
