# minio_handler

This is an abstraction on the Minio package to make basic usage of the Minio package a little less cumbersome

## usage


### Init the handler

```python
my_minio_server = Minio_Handler("127.0.0.1:9000", "minioadmin", "minioadmin", False)
```

> (class) Minio_Handler(host: str, access_key: str, secret_key: str, secure: bool = False)

#### Arguments

|**Name**|**Description**|**Example**|**Type**|
|---|---|---|---|
|host|Address and Port to your minio instance|127.0.0.1:9000|str|
|access_key|username to access minio instance|minioadmin|str|
|access_key|password to access minio instance|minioadmin|str|
|secure|use tls, defaults to false|True/False|bool|

### Method: bucket

> (method) bucket(bucket_name: str, action: str) -> bool

#### Arguments

|**Name**|**Description**|**Example**|**Type**|
|---|---|---|---|
|bucket_name|Name of the minio bucket to preform action on|my-bucket|str|
|action|Action to preform on bucket|check/create/delete|str|

#### check a bucket

```python
my_minio_server.bucket(bucket_name="my-bucket", action="check")
```
> return a bool

#### create a bucket

```python
my_minio_server.bucket(bucket_name="my-bucket", action="create")
```
> return a bool

#### delete a bucket

```python
my_minio_server.bucket(bucket_name="my-bucket", action="delete")
```
> return a bool

### Method: object

> (method) object(bucket_name: str, object_name: str, action: str, data: bytes = bytes("none", encoding="utf-8")) -> (str | bool)

#### Arguments

|**Name**|**Description**|**Example**|**Type**|
|---|---|---|---|
|bucket_name|Name of the minio bucket to preform an object action in|my-bucket|str|
|object_name|Name of the minio object_name to preform an action on|my-object|str|
|action|Action to preform on bucket|check/create/delete|str|
|data|Optional argument only used with create actions|bytes|

#### put object

```python
my_minio_server.object("my-bucket", "test.txt", "put", data=bytes("test data", encoding='utf-8')
```
> return a bool

#### delete object

```python
my_minio_server.object("my-bucket", "test.txt", "delete")
```
> return a bool

#### get object

```python
my_minio_server.object("my-bucket", "test.txt", "get")
```
> return a string


## Unit Test

### Requirements  

1. Docker runtime
2. Docker cli tool

### Run test

> file: test_Minio_Handler_unittest.py

```bash
cd ./minio_handler/minio_handler
python test_Minio_Handler_unittest.py
```

### Output

```bash
----------------------------------------------------------------------
Starting container minio-handler-test
e2c2ec3b4fe1924500b253db83238b1a33cd9a8f69516af32bab64859312c037
----------------------------------------------------------------------
Waiting 5 seconds for minio-handler-test container to start
......
----------------------------------------------------------------------
Ran 6 tests in 0.117s

OK
----------------------------------------------------------------------
Stopping and Removing minio-handler-test container
minio-handler-test
minio-handler-test
```