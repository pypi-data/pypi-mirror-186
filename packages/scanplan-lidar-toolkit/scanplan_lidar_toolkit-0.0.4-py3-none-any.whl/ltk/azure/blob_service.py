import io
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

class BlobService (object):
    def __init__(self):
        self.credential = DefaultAzureCredential()

    def download_blob(self, blob_url: str):
        blob_client = BlobClient.from_blob_url(blob_url, self.credential)
        download_stream = blob_client.download_blob()
        return io.BytesIO(download_stream.readall())

    def upload_blob(self, blob_url: str, blob_to_store: io.BytesIO):
        blob_client = BlobClient.from_blob_url(blob_url, self.credential)
        blob_client.upload_blob(blob_to_store.getvalue())