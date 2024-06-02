import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

class ExpenseRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Recorder")
        self.root.geometry("500x400")
        
        self.expenses = []

        # Creating UI elements
        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root, width=50)
        self.description_entry.pack()

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root, width=20)
        self.amount_entry.pack()

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.delete_button = tk.Button(root, text="Delete Selected Expense", command=self.delete_expense)
        self.delete_button.pack()

        self.save_button = tk.Button(root, text="Save to CSV", command=self.save_to_csv)
        self.save_button.pack()

        self.tree = ttk.Treeview(root, columns=("Description", "Amount"), show='headings')
        self.tree.heading("Description", text="Description")
        self.tree.heading("Amount", text="Amount")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def add_expense(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if not description or not amount:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid amount")
            return

        self.expenses.append((description, amount))
        self.tree.insert("", tk.END, values=(description, amount))

        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def delete_expense(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Delete Error", "Please select an item to delete")
            return

        for item in selected_item:
            values = self.tree.item(item, "values")
            self.expenses.remove(values)
            self.tree.delete(item)

    def save_to_csv(self):
        if not self.expenses:
            messagebox.showwarning("Save Error", "No expenses to save")
            return

        with open("expenses.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])
            writer.writerows(self.expenses)

        messagebox.showinfo("Success", "Expenses saved to expenses.csv")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseRecorder(root)
    root.mainloop()
