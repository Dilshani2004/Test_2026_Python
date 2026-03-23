from Priority import Priority
from Task import Task
from TaskStack import TaskStack
import pandas as pd
class Main:

    stack = TaskStack()
    data_set = stack.to_list()
    df = pd.DataFrame(data_set)

    def display_menu():
        print("Welcome")
        print("1. Add Task")
        print("2. Process task")
        print("3. Display All Tasks")
        print("4. Display Average Completion Time ")
        print("5. Display Visualize Task Data")
        print("6.Exit")
        
        choice = 0
        while True:
            choice = input("Enter one option")
            if choice.isdigit():
                choice = int(choice)
                break
        return choice

    def add_task():
        task_id = 0
        while True:
            task_id = input("Enter Task ID: ")
            if task_id.isdigit():
                task_id = int(task_id)
                break
        emp_name = input("Enter Employee Name")
        task_desc = input("Enter task description")
        priority = 0
        while True:
            priority = input("Enter Priority Level; LOW =1, MEDIUM = 2, HIGH = 3")
            if priority.isdigit():
                priority = int(priority)
                if priority == 1:
                    priority = Priority.LOW
                    break
                elif priority == 2:
                    priority = Priority.MEDIUM
                    break
                elif priority == 3:
                    priority = Priority.HIGH
                    break
                else:
                    print("Enter valid priority level")
        comp_time = 0
        while True:
            comp_time = input("Enter Compeletion time")
            if comp_time.isdigit():
                comp_time = int(comp_time)
                break
        task = Task(task_id,emp_name,task_desc,priority,comp_time)
        print(task)  
        Main.stack.push_task(task)


        

    def select_option():
        choice = Main.display_menu()
        if (choice == 1):
            Main.add_task()
        elif (choice == 2):
            Main.stack.pop_task()
        elif (choice == 3):
            Main.stack.display_tasks()
        elif(choice == 4):
            pass
        elif (choice == 5):
            pass
        elif (choice == 6):
            exit()
        else:
            print("Enter valid option")


if __name__ == "__main__":
    Main.select_option()