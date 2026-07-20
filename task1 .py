task=[]
print("to do list ")
while True:
    print("\n1: add task")
    print("2: view tasks")
    print("3: exit")
    choice = input("enter your choice: ") 
    if choice == "1": 
        task_name=input("enter the task name: ")
        task.append(task_name)
        print("task added successfully")
    elif choice == "2":
        if len(task) == 0:
            print("no tasks available")
        else:
            print("\n tasks:")
            for i in range(len(task)):
                print(f"\n {i+1}. {task[i]}")
    elif choice == "3":
        print("exiting the program")
        break
    else:
        print("invalid choice, please try again")
