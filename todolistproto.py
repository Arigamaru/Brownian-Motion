import pandas as pd
def mark_task_done(task):
    response = input(f"Is '{task}' done or not? (Type 'yes' or 'no')\n").lower()
    return response in ["yes","y", "done", "completed", "finished","yup","ye","yuh"]

task_list = []
while True:
    task_description = str(input())
    if task_description == "":
        break
    task_list.append(task_description)
solve = pd.DataFrame(task_list,columns=["Tasks to do"])
solve.index = [""]*len(solve)
print(solve)
done_tasks = [task for task in task_list if mark_task_done(task)]
task_list = [task for task in task_list if task not in done_tasks]
print("\nYour remaining to-do list")
for i in task_list:
    print(i)