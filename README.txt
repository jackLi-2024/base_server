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


