# 单文件打包
```shell
pyinstaller --windowed -F start.py -p init.py --noconsole
```

# 多文件打包
```shell
# 打包命令：pyinstaller -i resource/favicon.icns -w --add-data "/Users/shulin/PycharmProjects/work-tools/com/wts/proxy/resource/enable.png:./resource" --add-data "/Users/shulin/PycharmProjects/work-tools/com/wts/proxy/resource/disable.png:./resource" start.py -p init.py
# 或者执行命令 pyinstaller start.spec
```