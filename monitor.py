"""
monitor.py
Sytem info , resource monitering, warning, live moniter and process info for the SRM (System Resource Monitor)

"""
import os
import platform
import socket 
import time
import psutil

#settings (constants)

def get_system_info():
    hostname = socket.gethostname()
    info = {
        "os_name": platform.system(),
        "os_release": platform.release(),
        "hostname": hostname,
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }
    if info["processor"] == "":
        info["processor"] = "N/A"
    return info

def display_system_info():
    info = get_system_info()
    print("-" * 30)
    print("System Information:")
    print(f"Operating System: {info['os_name']} {info['os_release']}")
    print(f"Hostname: {info['hostname']}")
    print(f"Processor: {info['processor']}")
    print(f"Python Version: {info['python_version']}")

def bytes_to_gb(num_bytes):
    gigabytes = num_bytes / (1024 ** 3)
    return round(gigabytes, 2)
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

import monitor
print("Bytes test:", monitor.bytes_to_gb(2147483648))
print("CPU usage:", monitor.get_cpu_usage())

def get_memory_usage():
    memory = psutil.virtual_memory()
    memory_info = {
        "percent": memory.percent,
        "used_gb": bytes_to_gb(memory.used),
        "total_gb": bytes_to_gb(memory.total),
    }
    return memory_info

def get_disk_path():
    system_name = platform.system()
    if system_name == "Windows":
        return "C:\\"
    elif system_name == "Darwin" and os.path.exists("/Sysrtem/Volumes/Data"):
        return "/System/Volumes/Data"
    else:
        return "/"

def get_disk_usage():
        disk = psutil.disk_usage(get_disk_path())
        disk_info = {
            "percent": disk.percent,
            "used_gb": bytes_to_gb(disk.used),
            "total_gb": bytes_to_gb(disk.total),
        }
        return disk_info
