1. 模块导入.
顶层日志出现一次
MPY: soft reboot
boot: boot.py executed
main()的日志出现一次
lesson02 loaded: lesson02
此时 `__name__` 是lesson02，输出的是模块名，而不是"__main__".

2. 执行代码
session_marker = 123
lesson02.heartbeat()
观察到
heartbeatL: 1
heartbeatL: 2
heartbeatL: 3
heartbeatL: 4
按Ctrl+C后捕获键盘中止异常，程序中止.
执行print(session_marker)后，打印出123，变量依然存在.

3. 按下开发板EN键后，开发板发生重启，按顺序观察到
解释器加载
boot.py加载并执行，打印出boot: boot.py executed
main.py加载并执行，先打印出main()的日志lesson02 loaded: lesson02，然后import lesson02和lesson02.main()获得执行，打印出
ESP32-DevKit-32E 经典版开发板，MicroPython v1.29.0，只用 USB 供电与串口交互；学习模式为无动作模式：不接舵机、不配置 GPIO/PWM、不启动 Wi-Fi。
无动作模式
最后打印出main: main.py finished

4. 设置变量后执行 machine.soft_reset()
Thonny提示调用错误，找不到模块machine

5. 断开并重新连接开发板 USB
Thonny提示连接丢失，重新连接后Thonny不会自动恢复，必须点击工具栏的STOP按钮才会恢复到上电状态.