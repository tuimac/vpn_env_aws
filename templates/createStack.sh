#!/bin/bash

STACKNAME="vpn"
PACKAGENAME="root.yml"
BUCKETNAME="00-cloudformation"
TEMPLATENAME=${STACKNAME}.yml

#if [ $(aws cloudformation describe-stacks | \
#jq 'contains({"Stacks": [{"StackName": "vpn"}]})') == "true" ]; then
#    aws cloudformation delete-stack --stack-name ${STACKNAME}
#    for ((;;)); do
#        [[ $(aws cloudformation describe-stacks | \
#        jq 'contains({"Stacks": [{"StackName": "vpn"}]})') != "true" ]] && \
#            break
#    done
#fi

aws cloudformation package \
    --template-file ${PACKAGENAME}\
    --s3-bucket ${BUCKETNAME} \
    --output-template-file ${TEMPLATENAME}

aws cloudformation deploy \
    --template-file ${TEMPLATENAME} \
    --stack-name ${STACKNAME} \
    --capabilities CAPABILITY_IAM
