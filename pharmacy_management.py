import sqlite3
import tkinter as tk
from tkinter import messagebox, scrolledtext

def initialize_db():
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        sql_script = """
        -- Create customers table
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL,
            address TEXT
        );

        -- Create medicines table
        CREATE TABLE IF NOT EXISTS medicines (
            medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            manufacturer TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        );
        """
        
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        messagebox.showerror("Database Error", f"Error initializing database: {e}")

def add_customer(name, contact, address):
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO customers (name, contact, address) VALUES (?, ?, ?)", (name, contact, address))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer added successfully.")
    except Exception as e:
        print(f"Error adding customer: {e}")
        messagebox.showerror("Error", f"Error adding customer: {e}")

def update_customer(customer_id, name, contact, address):
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("UPDATE customers SET name = ?, contact = ?, address = ? WHERE customer_id = ?", (name, contact, address, customer_id))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer updated successfully.")
    except Exception as e:
        print(f"Error updating customer: {e}")
        messagebox.showerror("Error", f"Error updating customer: {e}")

def delete_customer(customer_id):
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer deleted successfully.")
    except Exception as e:
        print(f"Error deleting customer: {e}")
        messagebox.showerror("Error", f"Error deleting customer: {e}")

def add_medicine(name, manufacturer, price, quantity):
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO medicines (name, manufacturer, price, quantity) VALUES (?, ?, ?, ?)", (name, manufacturer, price, quantity))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Medicine added successfully.")
    except Exception as e:
        print(f"Error adding medicine: {e}")
        messagebox.showerror("Error", f"Error adding medicine: {e}")

def update_medicine(medicine_id, name, manufacturer, price, quantity):
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("UPDATE medicines SET name = ?, manufacturer = ?, price = ?, quantity = ? WHERE medicine_id = ?", (name, manufacturer, price, quantity, medicine_id))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Medicine updated successfully.")
    except Exception as e:
        print(f"Error updating medicine: {e}")
        messagebox.showerror("Error", f"Error updating medicine: {e}")

def delete_medicine(medicine_id):
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM medicines WHERE medicine_id = ?", (medicine_id,))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Medicine deleted successfully.")
    except Exception as e:
        print(f"Error deleting medicine: {e}")
        messagebox.showerror("Error", f"Error deleting medicine: {e}")

def list_customers():
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        
        customer_list.delete('1.0', tk.END)
        for customer in customers:
            customer_list.insert(tk.END, f"ID: {customer[0]}, Name: {customer[1]}, Contact: {customer[2]}, Address: {customer[3]}\n")
        
        customer_list.pack(pady=10)
        conn.close()
    except sqlite3.OperationalError as e:
        print(f"Error fetching customers: {e}")
        messagebox.showerror("Database Error", f"Error fetching customers: {e}")

def list_medicines():
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM medicines")
        medicines = cursor.fetchall()
        
        medicine_list.delete('1.0', tk.END)
        for medicine in medicines:
            medicine_list.insert(tk.END, f"ID: {medicine[0]}, Name: {medicine[1]}, Manufacturer: {medicine[2]}, Price: {medicine[3]}, Quantity: {medicine[4]}\n")
        
        medicine_list.pack(pady=10)
        conn.close()
    except sqlite3.OperationalError as e:
        print(f"Error fetching medicines: {e}")
        messagebox.showerror("Database Error", f"Error fetching medicines: {e}")

def add_customer_ui():
    def submit_customer():
        name = name_entry.get()
        contact = contact_entry.get()
        address = address_entry.get()
        add_customer(name, contact, address)
    
    customer_window = tk.Toplevel(root)
    customer_window.title("Add Customer")
    
    tk.Label(customer_window, text="Name:").grid(row=0, column=0)
    tk.Label(customer_window, text="Contact:").grid(row=1, column=0)
    tk.Label(customer_window, text="Address:").grid(row=2, column=0)
    
    name_entry = tk.Entry(customer_window)
    contact_entry = tk.Entry(customer_window)
    address_entry = tk.Entry(customer_window)
    
    name_entry.grid(row=0, column=1)
    contact_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    
    tk.Button(customer_window, text="Submit", command=submit_customer).grid(row=3, columnspan=2)

def update_customer_ui():
    def submit_update_customer():
        customer_id = int(id_entry.get())
        name = name_entry.get()
        contact = contact_entry.get()
        address = address_entry.get()
        update_customer(customer_id, name, contact, address)
    
    customer_window = tk.Toplevel(root)
    customer_window.title("Update Customer")
    
    tk.Label(customer_window, text="Customer ID:").grid(row=0, column=0)
    tk.Label(customer_window, text="Name:").grid(row=1, column=0)
    tk.Label(customer_window, text="Contact:").grid(row=2, column=0)
    tk.Label(customer_window, text="Address:").grid(row=3, column=0)
    
    id_entry = tk.Entry(customer_window)
    name_entry = tk.Entry(customer_window)
    contact_entry = tk.Entry(customer_window)
    address_entry = tk.Entry(customer_window)
    
    id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    contact_entry.grid(row=2, column=1)
    address_entry.grid(row=3, column=1)
    
    tk.Button(customer_window, text="Submit", command=submit_update_customer).grid(row=4, columnspan=2)

def delete_customer_ui():
    def submit_delete_customer():
        customer_id = int(id_entry.get())
        delete_customer(customer_id)
    
    customer_window = tk.Toplevel(root)
    customer_window.title("Delete Customer")
    
    tk.Label(customer_window, text="Customer ID:").grid(row=0, column=0)
    
    id_entry = tk.Entry(customer_window)
    id_entry.grid(row=0, column=1)
    
    tk.Button(customer_window, text="Submit", command=submit_delete_customer).grid(row=1, columnspan=2)

def add_medicine_ui():
    def submit_medicine():
        name = name_entry.get()
        manufacturer = manufacturer_entry.get()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        add_medicine(name, manufacturer, price, quantity)
    
    medicine_window = tk.Toplevel(root)
    medicine_window.title("Add Medicine")
    
    tk.Label(medicine_window, text="Name:").grid(row=0, column=0)
    tk.Label(medicine_window, text="Manufacturer:").grid(row=1, column=0)
    tk.Label(medicine_window, text="Price:").grid(row=2, column=0)
    tk.Label(medicine_window, text="Quantity:").grid(row=3, column=0)
    
    name_entry = tk.Entry(medicine_window)
    manufacturer_entry = tk.Entry(medicine_window)
    price_entry = tk.Entry(medicine_window)
    quantity_entry = tk.Entry(medicine_window)
    
    name_entry.grid(row=0, column=1)
    manufacturer_entry.grid(row=1, column=1)
    price_entry.grid(row=2, column=1)
    quantity_entry.grid(row=3, column=1)
    
    tk.Button(medicine_window, text="Submit", command=submit_medicine).grid(row=4, columnspan=2)

def update_medicine_ui():
    def submit_update_medicine():
        medicine_id = int(id_entry.get())
        name = name_entry.get()
        manufacturer = manufacturer_entry.get()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        update_medicine(medicine_id, name, manufacturer, price, quantity)
    
    medicine_window = tk.Toplevel(root)
    medicine_window.title("Update Medicine")
    
    tk.Label(medicine_window, text="Medicine ID:").grid(row=0, column=0)
    tk.Label(medicine_window, text="Name:").grid(row=1, column=0)
    tk.Label(medicine_window, text="Manufacturer:").grid(row=2, column=0)
    tk.Label(medicine_window, text="Price:").grid(row=3, column=0)
    tk.Label(medicine_window, text="Quantity:").grid(row=4, column=0)
    
    id_entry = tk.Entry(medicine_window)
    name_entry = tk.Entry(medicine_window)
    manufacturer_entry = tk.Entry(medicine_window)
    price_entry = tk.Entry(medicine_window)
    quantity_entry = tk.Entry(medicine_window)
    
    id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    manufacturer_entry.grid(row=2, column=1)
    price_entry.grid(row=3, column=1)
    quantity_entry.grid(row=4, column=1)
    
    tk.Button(medicine_window, text="Submit", command=submit_update_medicine).grid(row=5, columnspan=2)

def delete_medicine_ui():
    def submit_delete_medicine():
        medicine_id = int(id_entry.get())
        delete_medicine(medicine_id)
    
    medicine_window = tk.Toplevel(root)
    medicine_window.title("Delete Medicine")
    
    tk.Label(medicine_window, text="Medicine ID:").grid(row=0, column=0)
    
    id_entry = tk.Entry(medicine_window)
    id_entry.grid(row=0, column=1)
    
    tk.Button(medicine_window, text="Submit", command=submit_delete_medicine).grid(row=1, columnspan=2)

root = tk.Tk()
root.title("Pharmacy Management System")

tk.Button(root, text="Add Customer", command=add_customer_ui).pack(pady=5)
tk.Button(root, text="Update Customer", command=update_customer_ui).pack(pady=5)
tk.Button(root, text="Delete Customer", command=delete_customer_ui).pack(pady=5)
tk.Button(root, text="Add Medicine", command=add_medicine_ui).pack(pady=5)
tk.Button(root, text="Update Medicine", command=update_medicine_ui).pack(pady=5)
tk.Button(root, text="Delete Medicine", command=delete_medicine_ui).pack(pady=5)

tk.Button(root, text="List Customers", command=list_customers).pack(pady=5)
tk.Button(root, text="List Medicines", command=list_medicines).pack(pady=5)

customer_list = scrolledtext.ScrolledText(root, width=50, height=10)
medicine_list = scrolledtext.ScrolledText(root, width=50, height=10)

initialize_db()
root.mainloop()
