import monitor

summary = monitor.get_resource_summary()
print("Statuses:", monitor.get_statuses(summary))
monitor.display_warnings(summary)

