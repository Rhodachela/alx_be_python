task = input("Enter your task description: ").lower()
priority = input("Task's priority (High, medium or low?): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        if  time_bound == "yes":
            print(f" Reminder: {task}, is a {priority} level task and it requires immediate attention.")
        else:
            print(f"Reminder: {task} is {priority} level task. Find time to do it within the day.")

    case "medium":
        if time_bound == "yes":
            print (f" Reminder: {task} is a {priority} level task but it it time-bound. Try to complete it soon.")
        else:
            print(f"Reminder: {task} is a {priority} level task, you can do it during your free time.")

    case "low":
        if time_bound == "yes":
            print (f" Reminder: {task} is a {priority} level task but it it time-bound. Don't take too long")
        else:
            print(f"Reminder: {task} is a {priority} level task. Finish it at your convenience.")
    case _ :
        print("Invalid priority. Please enter (high, medium or low)")
    
