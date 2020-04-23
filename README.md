# Internet Virtual Private Network on AWS (This is under development.)

This is cloudformation templates to create Lower Cost Intenet VPN environment.
You need to pay for VPN Server which is made by OpenVPN.

## Getting Started

I considered to deploy these templates much more easier so I create bash file
and just execute it to upload templates to S3 and create Cloudformation Stacks.

## Installing

Just clone this repository to your local machine.
Downloading zip file to your local and extract it is same if you don't have Git.

```
git clone https://github.com/tuimac/vpn_env_aws.git
```

After download this repository to your local machine or before that, you have to
check enough IAM authorization to execute `cfnclient` command in this repository.

## How to use

Just execute following commands on your Linux machine is much more easier.

```
$ cd vpn_env_aws
$ ./cfnclient create
```

If you want to delete environment include all resources from the stacks,
you can execute this command.

```
$ ./cfnclient delete
```

On other environment like Windows, you need to execute `aws cloudformation` command on
`cfnclient` scripts.
(Because it's underdevelopment.)

## Support

Mainly most Linux Distributions.
Redhat, CentOS, Ubuntu, Debian, Amazon Linux
(Of course, your server need to have IAM authorization and vaild network to reach 
AWS service endpoint.)

## Authors

* **Kento Kashiwagi** - [tuimac](https://github.com/tuimac)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
