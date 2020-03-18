#!/usr/bin/env python

import boto3

def uploadTemplate():
    s3 = boto3.client("s3")



def main():
    S3BUCKET = "00-cfn-repository"

    uploadTemplate(S3BUCKET)


if __name__ == "__main__":
    main()
