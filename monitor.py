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

def get_resource_summary():
    memory = get_memory_usage()
    disk = get_disk_usage()
    summary = {
        "cpu_percent": get_cpu_usage(),
        "memory_percent": memory["percent"],
        "memory_used_gb": memory["used_gb"],
        "memory_total_gb": memory["total_gb"],
        "disk_percent": disk["percent"],
        "disk_used_gb": disk["used_gb"],
        "disk_total_gb": disk["total_gb"],
    }
    return summary

def display_resource_summary(summary):
    print("Current System Status")
    print("-" * 30)
    print(f"CPU Usage: {summary['cpu_percent']}%")
    print(f"Memory Usage: {summary['memory_percent']}% ({summary['memory_used_gb']} GB used of {summary['memory_total_gb']} GB)")
    print(f"Disk Usage: {summary['disk_percent']}% ({summary['disk_used_gb']} GB used of {summary['disk_total_gb']} GB)")
    print(f"Total Disk: {summary['disk_total_gb']:.2f} GB")

Thresholds = {
        "cpu": 80,
        "memory": 80,
        "disk": 90,
    }

def check_status(value, threshold):
    if value > threshold:
        return "High"
    return "OK"

def get_statuses(summary):
    statuses = {
        "cpu" : check_status(summary["cpu_percent"], Thresholds["cpu"]),
        "memory" : check_status(summary["memory_percent"], Thresholds["memory"]),
        "disk" : check_status(summary["disk_percent"], Thresholds["disk"]),
    }
    return statuses

colors = []
colors.append("red")
colors.append("blue")
print(colors)

def get_warnings(summary):
    warnings = []
    statuses = get_statuses(summary)
    if statuses["cpu"] == "High":
        warnings.append("Warning: CPU usage is high!")
    if statuses["memory"] == "High":
        warnings.append("Warning: Memory usage is high!")
    if statuses["disk"] == "High":
        warnings.append("Warning: Disk usage is high!")
    return warnings
def display_warnings(summary):
    warnings = get_warnings(summary)
    if len(warnings) == 0:
        print("All resources are within normal limits.")
    else:
        for warning in warnings:
            print(warning)

