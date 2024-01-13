import tkinter as tk

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.geometry("400x300")

        # Create labels and entries for the user to input expenses
        tk.Label(self.master, text="Date").grid(row=0, column=0)
        self.date_entry = tk.Entry(self.master)
        self.date_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Pay").grid(row=1, column=0)
        self.payee_entry = tk.Entry(self.master)
        self.payee_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Amount").grid(row=2, column=0)
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.grid(row=2, column=1)

        # Create a button to add expenses to the tracker
        tk.Button(self.master, text="Add Expense", command=self.add_expense).grid(row=3, column=1)

        # Create a label to display the total amount of expenses
        tk.Label(self.master, text="Total Expenses:").grid(row=4, column=0)
        self.total_label = tk.Label(self.master, text="$0.00")
        self.total_label.grid(row=4, column=1)

        # Initialize the list of expenses
        self.expenses = []

    def add_expense(self):
        # Get the values from the user input fields
        date = self.date_entry.get()
        payee = self.payee_entry.get()
        amount = float(self.amount_entry.get())

        # Add the expense to the list
        self.expenses.append((date, payee, amount))

        # Update the total label
        total = sum(expense[2] for expense in self.expenses)
        self.total_label.config(text=f"${total:.2f}")

        # Clear the input fields
        self.date_entry.delete(0, tk.END)
        self.payee_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

root = tk.Tk()
app = ExpenseTracker(root)
root.mainloop()