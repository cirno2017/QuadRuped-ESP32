import sys
import os
import gc
import machine

print("=== MicroPython baseline ===")
print("sys.version:", sys.version)
print("sys.implementation:", sys.implementation)
print("os.uname:", os.uname())
print("cpu_hz:", machine.freq())
print("reset_cause:", machine.reset_cause())
print("root_files:", os.listdir("/"))

gc.collect()
print("heap_free_bytes:", gc.mem_free())
print("heap_alloc_bytes:", gc.mem_alloc())

print("PWM.duty:", hasattr(machine.PWM, "duty"))
print("PWM.duty_u16:", hasattr(machine.PWM, "duty_u16"))
print("PWM.duty_ns:", hasattr(machine.PWM, "duty_ns"))