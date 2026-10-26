class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("task added")

    def show_task(self):
        if not self.tasks:
            print("no task available")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def remove_task(self, number):
            if 1<= number <= len(self.tasks):
                removed = self.tasks.pop(number-1)
                print("removed: ", removed)
            else:
                print("invalid task number!")


todo = TodoList()

while True:

    print("\n1. Add Task")
    print("\n2. Show Task")
    print("\n3. Remove Task")
    print("\n4. Exit")

    choice = input("\n \n Choose: ")
    if choice == "1":
        task = input("enter task: ")
        todo.add_task(task)
    elif choice == "2":
        todo.show_task()
    elif choice == "3":
        todo.remove_task()
    elif choice == "4":
        break
    else:
        print("invalid choice")
        break