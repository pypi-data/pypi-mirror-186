from google.cloud import storage
import zipfile as zp
import os


# 환경 변수 설정
def upload_gcs(bucket_name="cw_pm_upload_files", source_file_name="",
               top_level_object="tta_samplefile/", upload_path=None, email=None):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = os.path.join(top_level_object, upload_path if upload_path is not None else "",
                                         os.path.basename(source_file_name))

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    if email is not None:
        acl_blob = blob.acl
        if isinstance(email, list):
            for e in email:
                acl_blob.user(e).grant_read()
        else:
            acl_blob.user(email).grant_read()

        acl_blob.save()
    http_url = f"https://console.cloud.google.com/storage/browser/_details/{bucket_name}/{destination_blob_name};"
    print(
        http_url
    )


class Client:

    def __init__(self, key_path):

        KEY_PATH = key_path

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH
        print(f"GOOGLE_APPLICATION_CREDENTIALS = \"{KEY_PATH}\" COMPLETE KEY PATH")

    @staticmethod
    def load_file_zip(zipfile_name, walking_path, start_path, processing_file_name=".csv", files_delimiter=None):

        new_zips = zp.ZipFile(zipfile_name, 'w')  # WRITE NEW ZIPFILE

        # If exist this parameter value, this variable is not return blank string.
        files_delimiter = files_delimiter if files_delimiter is not None else ""

        for folder, sub_folders, files in os.walk(walking_path):

            for file in files:
                if files_delimiter in os.path.join(folder, file):
                    new_zips.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), start_path),
                                   compress_type=zp.ZIP_DEFLATED)
                if file.endswith(f"{processing_file_name}"):
                    new_zips.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), start_path),
                                   compress_type=zp.ZIP_DEFLATED)
        new_zips.close()

        print(f"\"{new_zips.filename}\" 압축이 성공 하였고 변수로 전달됩니다.")

        return new_zips.filename


