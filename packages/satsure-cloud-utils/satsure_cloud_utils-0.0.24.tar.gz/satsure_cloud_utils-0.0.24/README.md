![](https://img.shields.io/badge/Build-passing-brightgreen)
![Python](https://img.shields.io/badge/Python%20-%2314354C.svg?logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/Amazon_AWS-232F3E?logo=amazon-aws&logoColor=yellow)



The **satsure_cloud_utils** is a python package that contains all the functionality to browse and navigate AWS infrastrucure used in SatSure.

###  Installation

```
$ pip install satsure_cloud_utils  
```

### Usage

```
>> from satsure_cloud_utils import GetS3Handler
>> s3_handler = GetS3Handler(config_file_path="<config-file-path>")
>> output = s3_handler.list_buckets()
>> print(output)
```
