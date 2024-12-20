# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Create the base reminder message
reminder = f"'{task}' is a {priority} priority task"

# Use Match Case to handle priority
match priority:
    case "high":
        reminder += " that requires significant attention."
    case "medium":
        reminder += " that should be addressed soon."
    case "low":
        reminder += " that can be completed at your convenience."
    case _:
        reminder = "Invalid priority entered. Please try again."
        print(reminder)
        exit()

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have time."
else:
    print("Invalid time-bound response entered. Please try again.")
    exit()

# Print the customized reminder
print(f"Reminder: {reminder}")

