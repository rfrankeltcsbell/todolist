todolist={

}
while True:
    day=input("enter day of the week type done to finish").capitalize()
    if day==("done"):
        break
    task=input(f"enter a task for {day}")
    if day not in todolist:
        todolist[day]=[]
    todolist[day].append(task)
print("this is our todolist")
for day,tasks in todolist.item():
    print (day) 
    for task in tasks:
        print (task)