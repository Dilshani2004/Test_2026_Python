from Priority import Priority
from Task import Task
from Taskstack import TaskStack
import pandas as pd

class Main:

    stack=TaskStack()
    data_set=stack.to_list()
    df=pd.DataFrame(data_set)

    def display_menu():
        print("Welcome")
        print("1.Add Task")
        print("2.Process Task")
        print("3.Dispaly All Tasks")
        print("4.Display Average Completion Time")
        print("5.Visualize Task Dta")
        print("6.exit")
        
        choice = 0
        while True:
            choice = input("Enter one option")
            if choice.isdigit():
                choice= int(choice)
                break
        return choice
      
    def add_task():
        task_id=0
        while True:
            task_id=input("Enter Task ID: ")
            if task_id.isdigit():
                task_id=int(task_id)
                break
            emp_name=input("Enter Employee name")
            task_desc=input("Enter task description")
            priority= 0
            while True:
                priority= input("Enter priority levek;Low=1,Medium=2,High=3")
                if priority == 1:
                    priority= Priority.LOW
                    break
                elif priority == 2:
                    priority= Priority.MEDIUM
                    break
                elif priority == 3:
                    priority= Priority.HIGH
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
            Main.stack.pop
        elif(choice == 2):
            Main.stack.pop_task()
        elif(choice == 3):
            pass
        elif(choice == 4):
            pass
        elif(choice == 5):
            pass
        elif(choice == 6):
            exit()
        else:
            print("Enter valid option")            

if __name__=="__main__":
    Main.select_option()
    