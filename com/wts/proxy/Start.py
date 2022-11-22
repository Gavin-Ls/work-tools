import logging
import os
import pathlib
import threading
import warnings
from datetime import datetime
from os import popen
from telnetlib import Telnet

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from configparser import ConfigParser
from sys import argv

from com.wts.proxy.init import Ui_MainWindow

warnings.filterwarnings(action='ignore')
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)
# 存放软件信息的主目录
_path = pathlib.Path(os.getenv("HOME")).joinpath('.sl_work_proxy')

# socks隧道端口
socks_turn_port = 8085
# http隧道端口
http_turn_port = 8086


def start_sock_turn_command(ip):
    """
    启动sock隧道命令
    :param ip: 代理IP
    :return:
    """
    popen(
        "ssh -f -C -N -D 127.0.0.1:{port} tomcat@{ip} -p 22 -o \"StrictHostKeyChecking no\"".
            format(port=socks_turn_port, ip=ip))
    popen("hpts -s 127.0.0.1:{socks_port} -p {http_port}".format(socks_port=socks_turn_port,
                                                                 http_port=http_turn_port))


def enable_proxy_command(enable_proxy=False):
    """
    是否启动代理设置。默认关闭代理
    :param enable_proxy: 是否启动代理。True启动，False不启动
    :return:
    """
    if enable_proxy:
        popen('networksetup -setsocksfirewallproxy "Wi-Fi" 127.0.0.1 {http_port}'.format(http_port=socks_turn_port))
        popen('networksetup -setwebproxy "Wi-Fi" 127.0.0.1 {http_port}'.format(http_port=http_turn_port))
    else:
        popen('networksetup -setsocksfirewallproxystate "Wi-Fi" off')
        popen('networksetup -setwebproxystate "Wi-Fi" off')
        # popen('networksetup -setsecurewebproxy "Wi-Fi" off')


def sock_to_http_turn():
    """
    sock隧道转到http
    :return:
    """
    popen('networksetup -setwebproxy "Wi-Fi" 127.0.0.1 {http_port}'.format(http_port=http_turn_port))
    # popen('networksetup -setsecurewebproxy "Wi-Fi" 127.0.0.1 {http_port}'.format(http_port=http_turn_port))


class MainStart(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_page = Ui_MainWindow()
        self.start_page.setupUi(self)
        self.setWindowTitle("代理转发工具(研发使用)")

        # 设置下拉框隧道环境
        self.timer = None
        self.set_combobox()
        self.start_page.label_3.setStyleSheet('color:red')
        # 是否开启代理状态（默认开启）
        self.start_page.proxy_status.setChecked(False)

        self.start_page.pushButton.clicked.connect(self.control_button)
        self.start_page.comboBox.currentIndexChanged.connect(self.change_combobox)
        self.start_page.proxy_status.stateChanged.connect(self.change_proxy)

        self.append_log('<font color="red">使用须知：')
        self.append_log('<font color="red">'
                        '不要开启代理做一些与工作无关的事项，因隧道长时间占用大量流量，会被禁用，从而导致间歇性的断开连接。'
                        '如果没有必要打开外网网页，只是在代码中使用接口，不要开启"自动开启代理功能"，只打开"开启网络转发"即可！！！</font>')
        self.append_log('<font color="black"/>')
        # 本地电脑环境检查
        # self.check_env()

    @Slot()
    def change_proxy(self):
        """
        切换代理方式
        :return:
        """
        button_text = self.start_page.pushButton.text()
        if button_text == '关闭网络转发':
            proxy_flag = self.start_page.proxy_status.isChecked()
            enable_proxy_command(proxy_flag)
            if proxy_flag:
                self.append_log("已开启自动代理功能")
            else:
                self.append_log("已关闭自动代理功能")

    def closeEvent(self, event) -> None:
        """
        触发关闭按钮
        :param event:
        :return:
        """
        # print("关闭程序")
        self.close_turn()
        if self.timer is not None:
            self.timer.cancel()

    @staticmethod
    def ssh_check(_host):
        """
        22 端口连通性检测
        :return:
        """
        _telnet = Telnet()
        try:
            _telnet.open(host=_host, port=22, timeout=1)
            # logging.info("Telnet 信息[{text}]".format(text=text.get_socket()))
            return True
        except Exception as e:
            return False
        finally:
            if _telnet is not None:
                _telnet.close()

    def check_env(self):
        """
        环境检查
        :return:
        """
        # ret = popen("npm --version").read()
        # if ret is None or ret.strip() == "":
        #     self.append_log("node 未安装！")
        #     self.append_log("node安装命令：brew install node")
        # else:
        #     self.append_log("node版本 {0}".format(ret))
        #
        # ret = popen("hpts --version").read()
        # if ret is None or ret.strip() == "":
        #     self.append_log("hpts 未安装！")
        #     self.append_log("安装命令：npm install -g http-proxy-to-socks")
        # else:
        #     self.append_log("hpts版本 {0}".format(ret))

        ret = popen("sshpass -V").read()
        if ret is None or ret.strip() == "":
            self.append_log("sshpass 未安装！")
            self.append_log("安装命令：brew install sshpass")
        else:
            self.append_log("sshpass版本 {0}".format(ret))

    def change_combobox(self):
        """
        当改变隧道地址时，处理隧道
        :return:
        """
        button_text = self.start_page.pushButton.text()
        if button_text == '关闭网络转发':
            self.close_turn()
            self.start_turn()

    def set_combobox(self):
        """
        初始化隧道地址
        :return:
        """
        # 从项目中读取IP地址列表
        """
        ip.ini 文件格式如下：
        
        [default]
        ips=IP1,IP2
        """
        # 存放IP的文件
        _ip_ini_file_name = 'ip.ini'
        # 用户主目录不存在ip.ini 文件，则从软件中读取默认值。否则读取主目录中的ip.ini文件
        if _path.joinpath(_ip_ini_file_name).exists() is False:
            # 读取软件中存放的默认的ip.ini 文件
            _ip_ini = pathlib.Path(__file__).parent.resolve().joinpath(
                'resource/{ip_file}'.format(ip_file=_ip_ini_file_name))
            parse = ConfigParser()
            parse.read(_ip_ini, encoding='utf-8')
            _ip_list = list(parse.get(section='default', option='ips').replace(" ", "").split(','))

            # 把ip列表转为以英文逗号分割的字符串
            _ip_str = ''
            for _ip in _ip_list:
                if _ip_str == '':
                    _ip_str = _ip
                else:
                    _ip_str = _ip_str + ',' + _ip
                # 把该文件复制到用户目录.sl_work_proxy下，以便以后的动态修改IP地址
            _path.mkdir(parents=True, exist_ok=True)
            _file_ip = _path.joinpath(_ip_ini_file_name)
            _file_ip.touch()
            _file_ip.write_text('[default]\r\nips={ips}'.format(ips=_ip_str))
        else:
            parse = ConfigParser()
            parse.read(_path.joinpath(_ip_ini_file_name), encoding='utf-8')
            _ip_list = list(parse.get(section='default', option='ips').replace(" ", "").split(','))
        self.start_page.comboBox.addItems(_ip_list)
        # 立即设置IP地址是否可用图标
        self.config_combobox_icon(_ip_list)

    def config_combobox_icon(self, _turn_list):
        """
        定时自动配置下拉框IP地址是否能用的图标
        :param _turn_list: IP地址列表
        :return:
        """
        _enable_dir = pathlib.Path(__file__).parent.resolve().joinpath('resource/enable.png')
        _disable_dir = pathlib.Path(__file__).parent.resolve().joinpath('resource/disable.png')
        for _turn in _turn_list:
            if self.ssh_check(_turn):
                _image = _enable_dir
            else:
                _image = _disable_dir
            self.start_page.comboBox.setItemIcon(_turn_list.index(_turn), QIcon(_image.__str__()))
        # 启动定时器，定时检查IP地址是否可用
        self.timer = threading.Timer(interval=5, function=self.config_combobox_icon, args=[_turn_list])
        self.timer.daemon = True
        self.timer.start()

    @Slot()
    def control_button(self):
        button_text = self.start_page.pushButton.text()
        # logging.info("当前隧道状态[{state}]".format(state=button_text))
        if button_text == '开启网络转发':
            self.start_turn()
        else:
            self.close_turn()

    def start_turn(self):
        """
        启动隧道
        :return:
        """
        try:
            # 获取选中的隧道IP地址
            _ip = self.start_page.comboBox.currentText()
            start_sock_turn_command(_ip)
            # 自动代理标记
            proxy_flag = self.start_page.proxy_status.isChecked()
            enable_proxy_command(proxy_flag)

            self.start_page.pushButton.setText("关闭网络转发")
            self.start_page.pushButton.setStyleSheet("background-color: green")

            # self.append_log("启动隧道成功!")
            self.append_log("socks隧道地址[127.0.0.1:{port}]".format(port=socks_turn_port))
            self.append_log("http隧道地址[127.0.0.1:{port}]".format(port=http_turn_port))

            self.append_log("目标代理地址[{ip}:22]".format(ip=_ip))

            self.start_page.label_3.setText(
                'socks隧道已开启，自动代理已{proxy_text}'.format(proxy_text='开启' if proxy_flag else '关闭'))
            self.start_page.label_3.setStyleSheet('color:green')
        except:
            self.append_log("启动网络转发失败")
            self.close_turn()

    def close_turn(self):
        """
        关闭隧道
        :return:
        """
        # 关闭当前ssh会话
        try:
            # 关闭代理设置
            enable_proxy_command(False)

            self.start_page.pushButton.setText("开启网络转发")
            self.start_page.pushButton.setStyleSheet("background-color: red")

            ret = popen('ps aux | grep -E "ssh.*{port}.*" | grep -E ".-p.*22" | grep -v "grep"'.format(
                port=socks_turn_port)).read()
            command_list = ret.splitlines()
            for cmd in command_list:
                process_id = get_process_id(cmd)
                popen('kill -9 {0}'.format(process_id))

            ret = popen('ps aux | grep hpts | grep {port} | grep -v "grep"'.format(port=http_turn_port)).read()
            command_list = ret.splitlines()
            for cmd in command_list:
                process_id = get_process_id(cmd)
                popen('kill -9 {0}'.format(process_id))

            self.append_log("网络转发已关闭")

            self.start_page.label_3.setText('隧道和自动代理均已关闭')
            self.start_page.label_3.setStyleSheet('color:red')
        except:
            self.append_log("关闭网络转发失败")
            self.close_turn()

    def append_log(self, txt):
        """打印日志"""
        self.start_page.textBrowser.append("{0} {1}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), txt))


def get_process_id(cmd):
    """
    获取进程ID
    :param cmd:
    :return:
    """
    params = cmd.split(" ")
    for param in params:
        if param.isdigit():
            return param


if __name__ == '__main__':
    app = QApplication(argv)
    main_start = MainStart()
    main_start.show()
    app.exit(app.exec())
