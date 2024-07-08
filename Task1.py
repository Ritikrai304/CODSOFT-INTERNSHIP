from tkinter import *
import tkinter.messagebox
import pickle 
import tkinter.simpledialog
root = Tk()
root.geometry("655x333")
root.title("To Do List by ritik")
def addtask():
    task = entry_task.get()
    if task != "":
        list_task.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning", message="must enter a task")
        
    
def deletetask():
    try:
        task_index = list_task.curselection()[0]
        list_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning",message="must select a task")

def edittask():
    selected_index = list_task.curselection()
    if selected_index:
        old_task = list_task.get(selected_index)
        new_task = tkinter.simpledialog.askstring("edit task", "edit the task:", initialvalue=old_task)
        if new_task:
            list_task.delete(selected_index,tkinter.END)
            list_task.insert(selected_index, new_task)
    else:
        tkinter.messagebox.showwarning(title="warning", message="select a task to edit")

def savetask():
    task = list_task.get(0, list_task.size())
    print(task)

#create GUI
frame_task = Frame(root)
frame_task.pack()

list_task=Listbox(frame_task, height=3, width=50)
list_task.pack(side=LEFT)

scrollbar_tasks = Scrollbar(frame_task) 
scrollbar_tasks.pack(side=RIGHT, fill=X)

list_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=list_task.yview)

entry_task =Entry(root, width=50)
entry_task.pack()

#buttons for the tasks"
button_add_task=Button(root, text="Add Task",width=48,command=addtask,bg="grey")
button_add_task.pack()

button_delete_task=Button(root, text="Delete Task",width=48,command=deletetask,bg="grey")
button_delete_task.pack()

button_edit_task=Button(root, text="Edit Task",width=48,command=edittask,bg="grey")
button_edit_task.pack()

button_save_task=Button(root, text="Save Task",width=48,command=savetask,bg="grey")
button_save_task.pack()
root.mainloop()
