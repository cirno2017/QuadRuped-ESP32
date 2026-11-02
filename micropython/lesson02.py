"""lesson02.py — 模块导入、函数定义与调用的练习。

本文件不配置 GPIO、PWM 或 Wi-Fi，只在串口里打印文字。
它被 import 时只执行顶层语句；函数体要等被调用才执行。
"""

import time

# ① 顶层语句：每次执行本文件（import 或直接运行）都会先打印这一行。
print("lesson02 loaded:", __name__)


def describe():
    """返回一段说明，描述开发板与当前的学习模式。"""
    return (
        "ESP32-DevKit-32E 经典版开发板，MicroPython v1.29.0，"
        "只用 USB 供电与串口交互；学习模式为无动作模式："
        "不接舵机、不配置 GPIO/PWM、不启动 Wi-Fi。"
    )


def main():
    """模块的正式入口：打印说明与模式，然后返回。"""
    print(describe())
    print("无动作模式")
    return


def heartbeat():
    """每隔约一秒打印一次递增计数，持续运行。

    故意不写出口，也不被 main() 自动调用：
    需要观察时在 Shell 里手动执行 lesson02.heartbeat()，
    按 Ctrl-C 打断即可回到交互环境。
    """
    count = 0
    while True:
        count += 1
        print("heartbeat:", count)
        time.sleep(1)


# ② 只有"直接运行本文件"时才自动调用 main()；
#    被 import 时 __name__ 是 "lesson02"，这一段不会执行。
if __name__ == "__main__":
    main()
