import unittest
from minio_handler import Minio_Handler
import os
import time

class TestHandler(unittest.TestCase):

    print("----------------------------------------------------------------------\nStarting container minio-handler-test")
    os.system('docker run -it -d --name minio-handler-test -p 9000:9000 -p 9001:9001   quay.io/minio/minio server /data --console-address ":9001"')    
    print("----------------------------------------------------------------------\nWaiting 5 seconds for minio-handler-test container to start")
    time.sleep(5) # Wait for pod to be ready

    object_store = Minio_Handler("127.0.0.1:9000", "minioadmin", "minioadmin", False)
    
    object_store.bucket("test-bucket-check", "create")
    object_store.bucket("test-bucket-delete", "create")
    object_store.bucket("test-object", "create")
    object_store.object("test-object", "get_test.txt", "put", bytes("test data", encoding='utf-8'))
    object_store.object("test-object", "delete_test.txt", "put", bytes("test data", encoding='utf-8'))
    data = object_store.object("test-object", "none", "list")
    print(data)
    for item in data:
        print(item)

    def test_bucket_create(self):
        self.assertTrue(
            self.object_store.bucket("test-bucket-create", "create"),
            "Bucket create test"
        )
    
    def test_bucket_check(self):
        self.assertTrue(
            self.object_store.bucket("test-bucket-check", "check"),
            "Bucket check test"
        )

    def test_bucket_delete(self):
        self.assertTrue(
            self.object_store.bucket("test-bucket-delete", "delete"),
            "Bucket delete test"
        )
        
    def test_object_put(self):
        self.assertTrue(
            self.object_store.object("test-object", "test.txt", "put", data=bytes("test_data", encoding='utf-8')),
            "Object put test"
        )

    def test_object_delete(self):
        self.assertTrue(
            self.object_store.object("test-object", "delete_test.txt", "delete"),
            "Object delete test"
        )

    def test_object_get(self):
        self.assertTrue(
            isinstance(self.object_store.object("test-object", "get_test.txt", "get"), str),
            "Object get test"
        )

    def test_object_list(self):
        self.assertTrue(
            isinstance(self.object_store.object("test-object", "none", "list"), list),
            "Object get test"
        )


if __name__ == '__main__':
    try:
        unittest.main()
    finally:
        print("----------------------------------------------------------------------\nStopping and Removing minio-handler-test container")
        os.system('docker stop minio-handler-test && docker rm minio-handler-test')