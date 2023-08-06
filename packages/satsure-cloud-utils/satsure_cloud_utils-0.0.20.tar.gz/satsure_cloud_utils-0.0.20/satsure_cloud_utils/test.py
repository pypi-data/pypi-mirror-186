from s3_handler_file import GetS3Handler
# import json

# from aws_config_file import AWSConfig
# from satsure_cloud_utils import GetS3Handler

def main():
    s3_handler = GetS3Handler("./aws.env")

    print(s3_handler.list_buckets())
    
    
    print( s3_handler.list_objects(bucket_name="satsure-immutables",
                                   obj_path="LULC/",
                                   include_filters=["20120101_091007","LC"]) )
    
    # with open("test_output.json","w") as f:
        # json.dump(json.loads(x), f)
        
    y = s3_handler.download_objects(bucket_name="satsure-immutables",
                                    s3_obj_path="LULC/",
                                    local_obj_path=".",
                                    include_filters=["20120101_091007"],
                                    dryrun=True)
    print(y)
    
    
    # z = s3_handler.download_objects("inetra-data","files","")
    # print(z)
    
    
def main2():
    s3_handler = GetS3Handler("./aws.env")
    
    print(s3_handler.list_buckets())
    
    
if __name__ == '__main__':
    main()
    