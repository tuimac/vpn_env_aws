#!/usr/bin/env python3

import boto3
import time

if __name__ == '__main__':
    target = "vpn"
    ec2 = boto3.client("ec2")
    instanceInfo = ec2.describe_instances(Filters=[{"Name": "tag:Name", "Values": [target]}])["Reservations"]
    amiInfo = ec2.describe_images(Filters=[{"Name": "tag:Name", "Values": [target]}])["Images"]
    if len(instanceInfo) != 0:
        instanceId = instanceInfo[0]["Instances"][0]["InstanceId"]
        amiId = amiInfo[0]["ImageId"]
        snapshotIds = [ebs["Ebs"]["SnapshotId"] for ebs in amiInfo[0]["BlockDeviceMappings"]]
        ec2.deregister_image(ImageId=amiId)
        [ec2.delete_snapshot(SnapshotId=snapshotId) for snapshotId in snapshotIds]
        while "stopped" != ec2.describe_instances(instanceId)[0]["Instances"][0]["State"]["Name"]:
            time.sleep(1)
        amiId = ec2.create_image(InstanceId)
