import tkinter as tk
from tkinter import messagebox, simpledialog

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("300x350")

        self.students = {}  # Dictionary to store student records

        self.label = tk.Label(root, text="Student Management System", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.add_btn = tk.Button(root, text="Add Student", borderwidth=10, command=self.add_student)
        self.add_btn.pack(pady=10)

        self.view_btn = tk.Button(root, text="View Students", borderwidth=10, command=self.view_students)
        self.view_btn.pack(pady=10)

        self.update_btn = tk.Button(root, text="Update Student", borderwidth=10, command=self.update_student)
        self.update_btn.pack(pady=10)

        self.delete_btn = tk.Button(root, text="Delete Student", borderwidth=10, command=self.delete_student)
        self.delete_btn.pack(pady=10)


    def add_student(self):
        sid = simpledialog.askstring("Add Student", "Enter student ID:")
        if sid in self.students:
            messagebox.showwarning("Warning", "Student ID already exists.")
            return

        name = simpledialog.askstring("Add Student", "Enter student name:")
        age = simpledialog.askinteger("Add Student", "Enter student age:")

        if sid and name and age:
            self.students[sid] = {"Name": name, "Age": age}
            messagebox.showinfo("Info", "Student added successfully.")
        else:
            messagebox.showerror("Error", "Invalid input.")
    def view_students(self):
        if not self.students:
            messagebox.showinfo("Student List", "No student records found.")
        else:
            student_list = "\n".join(f"ID: {sid}, Name: {info['Name']}, Age: {info['Age']}"
                                     for sid, info in self.students.items())
            messagebox.showinfo("Student List", student_list)

    def update_student(self):
        sid = simpledialog.askstring("Update Student", "Enter student ID to update:")
        if sid not in self.students:
            messagebox.showwarning("Warning", "Student ID not found.")
            return

        name = simpledialog.askstring("Update Student", "Enter new student name:")
        age = simpledialog.askinteger("Update Student", "Enter new student age:")

        if name and age:
            self.students[sid]["Name"] = name
            self.students[sid]["Age"] = age
            messagebox.showinfo("Update", "Student updated successfully.")
        else:
            messagebox.showerror("Error", "Invalid input.")

    def delete_student(self):
        sid = simpledialog.askstring("Delete Student", "Enter student ID to delete:")
        if sid not in self.students:
            messagebox.showwarning("Warning", "Student ID not found.")
        else:
            del self.students[sid]
            messagebox.showinfo("Delete", "Student deleted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
