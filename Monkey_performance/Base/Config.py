# /usr/bin/env python
# -*- encoding: utf-8 -*-
import random

class Config:
    # apk包名
    package_name = "com.dc.hwsj"
    # 默认设备列表
    device_dict = {}
    # 网络
    net = "wifi"
    # monkey seed值，随机产生
    monkey_seed = str(random.randrange(1, 1000))
    # monkey 参数
    monkey_parameters = "-p com.dc.hwsj --throttle 200 --ignore-crashes --ignore-timeouts --pct-touch 80 --pct-trackball 5 --pct-appswitch 5 --pct-syskeys 5 --pct-motion 5 -v -v 5000"
    # log保存地址
    log_location = r"D:\Moneky-test\Monkey_performanceV2.1\Monkey_performance\log"
    #性能数据存储目录
    info_path = r"D:\Moneky-test\Monkey_performanceV2.1\Monkey_performance\info"
