#!/usr/bin/env python

import boto3
import botocore
import traceback
import sys

def isBucketExist(s3, bucketname):
    try:
        s3.head_bucket(Bucket=bucketname)
        return False

    except botocore.exceptions.ClientError:
        return False

def autoCreateBucket():

def uploadTemplate(bucketname):
    try:
        s3 = boto3.client("s3")
        if isBucketExist(s3, bucketname) is False: 
            response = s3.create_bucket(
                ACL = "private",
                Bucket = bucketname,
                CreateBucketConfiguration = {"LocationConstraint": "ap-northeast-1"}
            )
    except:
        print(traceback.format_exc().splitlines()[-1])
        exit(1)

def main():
    S3BUCKET = "00-cfn-repository"

    uploadTemplate(S3BUCKET)

if __name__ == "__main__":
    main()
