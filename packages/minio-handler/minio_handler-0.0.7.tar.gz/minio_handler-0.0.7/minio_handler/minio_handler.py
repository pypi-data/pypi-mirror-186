from minio import Minio
import io
import json

class Minio_Handler():
    def __init__(self, host, access_key, secret_key, secure=False):
        self.host = host
        self.access_key = access_key
        self.secret_key = secret_key
        self.secure = secure

        self.client = Minio(
            host,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=self.secure,
        )

    # Bucket method
    def bucket(self, bucket_name:str, action:str):
        match action:
            case "check":
                return True if self.client.bucket_exists(bucket_name) else False
            case "create":
                return False if self.client.make_bucket(bucket_name) else True
            case "delete":
                return False if self.client.remove_bucket(bucket_name) else True
            case "list":
                output = []
                buckets = self.client.list_buckets()
                for bucket in buckets:
                    output.append({"name": bucket.name, "creation_date": bucket.creation_date})
                return 
            case _:
                return False

    # Object method
    def object(self, bucket_name: str, object_name: str, action:str, data=bytes("none", encoding="utf-8")):
        match action:
            case "get":
                try:
                    response = self.client.get_object(bucket_name, object_name)
                    sanities = response.read()
                    return json.load(sanities)
                finally:
                    response.close()
                    response.release_conn()
            case "put":
                return True if self.client.put_object(bucket_name, object_name, io.BytesIO(data), length=-1, part_size=5*1024*1024) else True
            case "delete":
                return True if self.client.remove_object(bucket_name, object_name) else True
            case "list":
                output = []
                objects = self.client.list_objects(bucket_name)
                for item in objects:
                    output.append(item.object_name)
                return output
            case _:
                return False