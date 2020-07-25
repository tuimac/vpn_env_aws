FROM centos:latest

ARG url=https://github.com/tuimac/vpn_env_aws.git

EXPOSE 80

WORKDIR /root

ADD env/vimrc /etc/vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh
ADD requirements.txt /root/requirements.txt

RUN yum update -y && \
    yum install -y iproute curl unzip tcpdump net-tools git tree bind-utils traceroute vim* && \
    dnf install -y python3 && \
    pip3 install -r requirements.txt && \
    rm -rf anaconda-ks.cfg anaconda-post.log original-ks.cfg requirements.txt && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /etc/vim/undo && \
    mkdir /root/vpn && \
    git clone $url

WORKDIR /root/vpn_env_aws
