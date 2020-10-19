# douyu_daily 8517916



- # 20201019

## install ubuntu 16.04
```bash
# replace ubuntu mirror with aliyun at /etc/apt/sources.list
deb http://mirrors.aliyun.com/ubuntu/ xenial main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main

deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main

deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates universe

deb http://mirrors.aliyun.com/ubuntu/ xenial-security main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security universe
```

## install some useful tools
```bash
# install some useful tools
sudo apt -y install kazam openssh-server vim htop gitg terminator python-pip cmake tmux git chromium-browser
```
[tips] how to resolve login keyring ups when start chrome-? 

change in /usr/share/applications/chromium-browser.desktop
--Exec=chromium-browser
++Exec=chromium-browser --password-store=basic

```bash
# install typora for markdown txt
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt update 
sudo apt install typora -y
```
[google-markdown-style]https://github.com/google/styleguide/blob/gh-pages/docguide/style.md 

```bash
# install ros kinetic  desktop full
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

```

[ros-wiki]http://wiki.ros.org/kinetic/Installation/Ubuntu

[tips] https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/sources.list.d/20-default.list
Website may be down.

+++ add a line in /etc/hosts:  199.232.68.133 raw.githubusercontent.com 





