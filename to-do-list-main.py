def task():
    tasks = []
    print("---WELCOME TO THE TASK MANAGER---")

    total_task = int(input("How many tasks do you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
        
    print(f"Your tasks are:\n{tasks}")

    while True:
        operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\nChoose an operation: "))
        
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)  
            print(f"Task '{add}' has been successfully added ")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task to '{up}'")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            delete_val = input("Enter the task you want to delete: ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been successfully deleted.")
            else:
                print(f"Task '{delete_val}' not found.")

        elif operation == 4:
            print(f"Your tasks are:\n{tasks}")

        elif operation == 5:
            print("Exiting Task Manager. thank you!")
            break

        else:
            print("Invalid choice. Please choose a valid operation.")

task()
