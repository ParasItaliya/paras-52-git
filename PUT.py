import boto3

def upload_csv_to_s3(bucket_name , file_name , s3_key):
         s3 = boto3.client("s3")
         try : 
             s3.upload_file(file_name , bucket_name , s3_key)
             print("FILE UPLOADED SUCCESSFULLY : S3")
         except FileNotFoundError :
              print("THE FILE WAS NOT FOUND")
         except Exception as e :
              print("AN ERROR OCCURRED : {str(e)}")

bucket_name = "001temp"
file_name = "10.py"
s3_key = "UPLOAD-02.py"

upload_csv_to_s3(bucket_name , file_name , s3_key)
