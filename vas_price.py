# Written by J.C. Paz
import customtkinter as ctk
import tkinter as tk

def percentage_difference(V, Cost):
    return abs(V - Cost) / V * 100

def subtract_percentage(MSRP, Discount):
    return MSRP - (MSRP * (Discount / 100))

def get_values():
    try:
        # Retrieve the values entered by the user
        MSRP = float(entry_MSRP.get())  
        Discount = float(entry_DIS.get())  
        Cost = float(entry_COST.get())

        VASCUPP_Price = subtract_percentage(MSRP, Discount)

        V = VASCUPP_Price

        SetMargin = percentage_difference(V, Cost)

        Results = f" VASCUPP Price is {V} SET MARGIN TO{SetMargin}%"
        # Update the result label to display the output
        result_label.configure(text=Results)
    except ValueError:
        # Handle the case where input is not a valid integer
        result_label.config(text="Please enter valid integers.")
        print("Please enter valid integers.")
# Initialize the root window
root = ctk.CTk()

# Set the title of the window
root.title("VASCUPP MARGIN calculator")

# Set the window size (width x height)
root.geometry("450x600")

label_MSRP = ctk.CTkLabel(root, text="ENTER MSRP:")
label_MSRP.pack(pady=10)

entry_MSRP = ctk.CTkEntry(root)
entry_MSRP.pack(pady=10)

label_DIS = ctk.CTkLabel(root, text="ENTER MIN DISCOUNT PERCENTAGE:")
label_DIS.pack(pady=10)

entry_DIS = ctk.CTkEntry(root)
entry_DIS.pack(pady=10)

label_COST = ctk.CTkLabel(root, text="ENTER DEALER COST:")
label_COST.pack(pady=10)

entry_COST = ctk.CTkEntry(root)
entry_COST.pack(pady=10)

submit_button = ctk.CTkButton(root, text="Submit", command=get_values)
submit_button.pack(pady=20)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Function to clear the input fields and result box
def clear_values():
    entry_MSRP.delete(0, "end")  
    entry_DIS.delete(0, "end") 
    entry_COST.delete(0, "end")    
    result_label.configure(text="") 

# Create a button to clear the inputs and result box
clear_button = ctk.CTkButton(root, text="Clear", command=clear_values)
clear_button.pack(pady=10)

# Run the main loop
root.mainloop()





