import monitor
import logger
def print_menu():
    print()
    print("=" * 32)
    print("TB System Resource Monitor")
    print("=" * 32)
    print("1. View current resource status")
    print("2. Start Live Monitor")
    print("3. View Top Processes")
    print("4. Save Current Snapshot")
    print("5. System Information")
    print("6. Exit")
    print("=" * 32)

def pause():
        input("\nPress Enter to return to the menu...")

def view_current_status():
            print("\nGathering system information")
            summary = monitor.get_resource_summary()
            monitor.display_resource_summary(summary)
            print()
            monitor.display_warnings(summary)

def save_current_snapshot():
    print("\nGathering system information...")
    summary = monitor.get_resource_summary()
    try:
        file_path = logger.save_snapshot(summary)
        print(f"Snapshot saved to: {file_path}")
    except OSError:
        print("Sorry, the snapshot could not be saved.")
        print("Make sure the CSV file is not open in another program.")

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            view_current_status()
            pause()
        elif choice == "2":
            monitor.start_live_monitor()
            pause()
        elif choice == "3":
            monitor.display_top_processes()
            pause()
        elif choice == "4":
            save_current_snapshot()
            pause()
        elif choice == "5":
            monitor.display_system_info()
            pause()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")

