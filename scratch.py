import monitor

memory = monitor.get_memory_usage()
print("memory:", memory)

print("Disk path:", monitor.get_disk_path())
disk = monitor.get_disk_usage()
print("Disk:", disk)
