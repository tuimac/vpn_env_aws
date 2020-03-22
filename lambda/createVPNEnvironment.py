import json
import urllib.request
import traceback
import sys
import shutil
import zipfile
import boto3
import re
import logging
import threading
import datetime
import time
from os import listdir, walk, path, rename

CONFIG = {
    "bucket": "00-cfn-repository",
    "templates": {
        "vpn": "root.yml"
    },
    "uploadTarget": "/vpn_env_aws-master/vpn",
    "gitUrl": "https://github.com/tuimac/vpn_env_aws/archive/master.zip"
}

def download():
    # Download cloudformation templates from tuimac repository
    url = CONFIG["gitUrl"]
    tmpfile = urllib.request.urlretrieve(url)[0]
    
    # Deploy download files
    tmpdir = "/".join(tmpfile.split("/")[:-1])
    filename = tmpdir + "/master.zip"
    rename(tmpfile, filename)
    with zipfile.ZipFile(filename) as extZip:
        extZip.extractall(tmpdir)
    return tmpdir

def uploadTemplates(s3resource, s3client, bucketname, basedir):
    # Confirm directory was passed by argument is exist or not.
    directory = path.expanduser(basedir + CONFIG["uploadTarget"])
    if path.exists(directory) is False: raise FileNotFoundError

    # Delete all files in the bucket.
    if s3client.list_objects_v2(Bucket=bucketname)["KeyCount"] > 0:
        for content in s3client.list_objects_v2(Bucket=bucketname)["Contents"]:
            response = s3client.delete_object(
                Bucket = bucketname,
                Key = content["Key"]
            )
    print("Delete all objects has been success.")

    # Search all files under target directory and upload each files.
    for current, dirs, files in walk(directory):
        if len(dirs) == 0 or len(files) > 0:
            for file in files:
                allpath = current + "/" + file
                m = re.match(directory + "/", allpath)
                key = allpath[:m.start()] + allpath[m.end():]
                s3resource.meta.client.upload_file(allpath, bucketname, key)
    print("Upload has been success.")
    return

def createStacks(cfnclient):
    # If there is same stack name, delete it and create new stack.
    for stackName, template in CONFIG["templates"].items():
        templateUrl = "https://s3.amazonaws.com/" + CONFIG["bucket"] + "/" + template

        response = cfnclient.create_stack(
            StackName = stackName,
            TemplateURL = templateUrl,
            Capabilities = ["CAPABILITY_NAMED_IAM"],
        )
        print("Create " + stackName + " has been success.")


def handler(event, context):
    try:
        s3resource = boto3.resource("s3")
        s3client = boto3.client("s3")
        cfnclient = boto3.client("cloudformation")
        
        # Download templates from Github repository.
        basedir = download()

        # Upload target directory to S3 bucket.
        # The way of upload is deleting all the files in the bucket
        # and upload files under the target local directory.
        uploadTemplates(s3resource, s3client, CONFIG["bucket"], basedir)
        
        # Create stacks from template you upload above process.
        createStacks(cfnclient)
    except:
        traceback.print_exc()
