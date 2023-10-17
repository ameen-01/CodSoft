import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove the selected task from the list
def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the background color and window size
root.configure(bg="#13294B")
root.geometry("400x400")

# Create a frame for the task list
frame = tk.Frame(root, bg="#e0e0e0")
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a listbox for tasks
task_listbox = tk.Listbox(frame, width=40, height=10, selectbackground="#686A6C", selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar and link it to the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Create an entry field for task input
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Create buttons to add and remove tasks with some styling
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4caf50", fg="white", relief=tk.FLAT)
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#f44336", fg="white", relief=tk.FLAT)
add_button.pack(pady=5)
remove_button.pack(pady=5)

# Run the application
root.mainloop()
