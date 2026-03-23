class Task:
    def __init__(self,task_id,emp_name,desc,priority,comp_time):
        self.task_id=task_id
        self.emp_name=emp_name
        self.desc=desc
        self.priority=priority
        self.comp_time=comp_time

    def __str__(self):
        return f"Task ID: {self.task_id} Employee name : {self.emp_name} Description: {self.desc }Priority Level: {self.priority}Complete Time: {self.comp_time}"
    
       


           
               
    
    


