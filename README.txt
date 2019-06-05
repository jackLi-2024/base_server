1.目录conf
	该目录包含配置文件如下
	logging.conf  //日志配置文件
	database.conf // 数据库配置文件

2.API目录
	该目录定义业务所需要的API接口
	实例请参照api_example.py

3.config文件
	该文件主要是配置server的路由映射与基础配置

4.uwsgi.conf
        	uwsgi配置做高并发


git clone https://github.com/lijiacaigit/base_server.git
开发测试环境：
    1.修改config.py，增加相关接口以及路由
    2.定义API目录下的接口
    3.测试运行run.py

部署环境：
    1.修改uwsgi.ini，主要修改端口号，防止端口号被占用等异常


centos部署说明:
    step1. Modify config.ini
        Please modify the port number and related database parameters according to the actual situation.

    step2.Installing CentOS environment dependencies
        sudo yum install -y pcre pcre-devel pcre-static
        sudo yum install -y gcc
        sudo yum install -y python-devel

    step3. api
        1. add URI: ./src/run.py
        2. add api: ./src/controller/
        3. operate database: ./src/model/Models/


    step4 Note
        1.There may be a system error, and you will get the following error: "\r"
            sudo yum install -y dos2unix
            dos2unix *
            dos2unix */*
            dos2unix */*/*

    1. start
        sh bin/start.sh
    2. stop
        sh bin/stop.sh




