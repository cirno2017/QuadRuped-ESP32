1. Thonny的版本是5.0.1，ESP32开发板使用的串口是COM5，micropython/runtime_probe.py在板上执行的输出为：
MPY: soft reboot
=== MicroPython baseline ===
sys.version: 3.4.0; MicroPython v1.29.0 on 2026-08-24
sys.implementation: (name='micropython', version=(1, 29, 0, ''), _machine='Generic ESP32 module with ESP32', _mpy=11014, _build='ESP32_GENERIC', _thread='GIL')
os.uname: (sysname='esp32', nodename='esp32', release='1.29.0', version='v1.29.0 on 2026-08-24', machine='Generic ESP32 module with ESP32')
cpu_hz: 160000000
reset_cause: 5
root_files: ['boot.py', 'index.html', 'main.py', 'oscillator.py', 'quad.py', 'robot.py', 'robot_wifi.py', 'runtime_probe.py', 'test_max_servos.py', 'test_servo180.py']
heap_free_bytes: 134304
heap_alloc_bytes: 3616
PWM.duty: True
PWM.duty_u16: True
PWM.duty_ns: True

2. 版上的文件为
boot.py
main.py
oscillator.py
quad.py
robot.py
robot_wifi.py
runtime_probe.py
test_max_servos.py
test_servo180.py
index.html

3. 实际的入口文件是main.py

4. 机器人通过网页控制，调用HELLO命令，成功观察到机器人做出了招手的动作

5. 机器人的控制代码来源， https://github.com/AniPython/quad-mpy ，没有电路原理图，没有机械构件的CAD图，只有micropython控制代码