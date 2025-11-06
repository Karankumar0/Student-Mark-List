import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np

names = [f"student({i})" for i in range(1, 61)]
roll_numbers = list(range(1, 61))

np.random.seed(42)
marks = {
    "Maths": np.random.randint(50, 101, size=60),
    "Physics": np.random.randint(50, 101, size=60),
    "Chemistry": np.random.randint(50, 101, size=60),
    "English": np.random.randint(50, 101, size=60),
    "Computer": np.random.randint(50, 101, size=60)
}
df = pd.DataFrame({
    "Roll No": roll_numbers,
    "Name": names,
    "Maths": marks["Maths"],
    "Physics": marks["Physics"],
    "Chemistry": marks["Chemistry"],
    "English": marks["English"],
    "Computer": marks["Computer"]
})

root = tk.Tk()
root.title("Student Mark Search")
root.geometry("700x400")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="Student Mark Search System", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter Student Name or Roll No:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
search_entry = tk.Entry(input_frame, width=25, font=("Arial", 12))
search_entry = tk.Entry(input_frame, width=25, font=("Arial", 12))
search_entry.grid(row=0, column=1, padx=5)

columns = ("Roll No", "Name", "Maths", "Physics", "Chemistry", "English", "Computer", "Total", "Average")
tree = ttk.Treeview(root, columns=columns, show="headings", height=5)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=80)

tree.pack(pady=10)

def search_student():
    query = search_entry.get().strip()
    
    for row in tree.get_children():
        tree.delete(row)

    if not query:
        messagebox.showwarning("Input Error", "Please enter a name or roll number.")
        return

    # Assume df is a pandas DataFrame with student data
    if query.isdigit():
        roll_no = int(query)
        # result_df = df[df["Roll No"] == roll_no]
        pass # Placeholder for logic
    else:
        # result_df = df[df["Name"].str.lower().str.contains(query.lower())]
        pass # Placeholder for logic

    # if not result_df.empty:
    #     total = result_df[["Maths", "Physics", "Chemistry", "English", "Computer"]].sum(axis=1).values[0]
    #     average = total / 5
    #     row_list = list(result_df.iloc[0])
    #     row_list.extend([total, round(average, 2)])
    #     tree.insert("", "end", values=row_list)
    # else:
    #     messagebox.showinfo("Found", "No student found! Please check the name or roll number.")

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

search_btn = tk.Button(btn_frame, text="Search", font=("arial", 12, "bold"), bg="#4caf50", fg="white", width=10, command=search_student)
search_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", font=("arial", 12, "bold"), bg="#f44336", fg="white", width=10, command=root.destroy)
exit_btn.grid(row=0, column=1, padx=10)

root.mainloop()
