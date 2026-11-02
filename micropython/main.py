# main.py — 启动入口：打印入口日志，导入 lesson02，显式调用它的 main()，然后结束。
#
# 本文件不启动 Wi-Fi、不占用 REPL、也没有无限循环，执行完就回到 Shell。
# 旧入口（机器人网页控制程序，见 backup/device/main.py）不要在这里导入：
# 它的顶层语句会立刻初始化舵机并启动 Wi-Fi。

print("main: main.py entered")

import lesson02

lesson02.main()

print("main: main.py finished")
