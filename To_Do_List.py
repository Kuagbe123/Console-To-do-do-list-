tasks = []

while True:
    print("\n---- To-Do List Application ----")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View All Tasks")
    print("4. Remove Completed Tasks")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append((task, False))
        print("Task added successfully.")

    elif choice == "2":
        index = int(input("Enter the task index to mark as complete: "))
        if index < len(tasks):
            tasks[index] = (tasks[index][0], True)
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    elif choice == "3":
        print("\n--- All Tasks ---")
        for index, task in enumerate(tasks):
            status = "Complete" if task[1] else "Incomplete"
            print(f"{index}. {task[0]} - Status: {status}")

    elif choice == "4":
        rem = float(input("Enter key of item to remove : "))
        del tasks[rem]
        print("Removed Successfully!")

    elif choice == "5":
        print("Quitting the application...")
        break

    else:
        print("Invalid choice. Please try again.")