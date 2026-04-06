
current_time = int(input("Enter current time (0-23): "))
wait_time = int(input("Enter hours to wait: "))

alarm_time = (current_time + wait_time) % 24

print(f"\nThe alarm will go off at: {alarm_time}:00")
