tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"✅ Task added!")
    
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option.")