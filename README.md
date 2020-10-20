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
[tips]: how to resolve login keyring ups when start chrome-? 

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

[ros-wiki]:http://wiki.ros.org/kinetic/Installation/Ubuntu
[tips]: https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/sources.list.d/20-default.list
Website may be down.

+++ add a line in /etc/hosts:  199.232.68.133 raw.githubusercontent.com 





- # 20201020

## install redis

```bash
wget https://download.redis.io/releases/redis-6.0.8.tar.gz
tar xzf redis-6.0.8.tar.gz
cd redis-6.0.8
make
sudo make install
```

## install jdk

```bash
# download deb file from https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
sudo dpkg -i jdk-11.0.8_linux-x64_bin.deb
sudo gedit /etc/profile
    export JAVA_HOME=/usr/lib/jvm/jdk-11.0.8
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
# add java path to sudo default_path
sudo gedit /etc/sudoers
line_11: Defaults     		secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin:/usr/lib/jvm/jdk-11.0.8/bin/"

# reboot after modify '/etc/profile' and '/etc/sudoers'
sudo reboot
```



## install logstash

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo apt install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update && sudo apt install logstash
sudo chmod 775 -R /usr/share/logstash/data
```
[rostopic-logstash]:https://blog.csdn.net/woshiwusonghaha/article/details/52850826

## install elasticsearch

```bash
sudo apt install elasticsearch
sudo chmod 775 -R elasticsearch/
```

## install kibana

```bash
sudo apt install kibana
```

