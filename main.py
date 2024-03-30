from bank import BankAccount
from customer import Customer
from customtkinter import *
from tkinter import messagebox


class App:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("800x600")
        self.app.title("Banking App")
        self.app.resizable(0, 0)

        self.frame = CTkFrame(master=self.app, width= 600, height=400, fg_color="transparent" )
        self.frame.place( relx=0.5, rely=0.5, anchor="center")
        # self.frame.place(relx=0.5, rely=0.2, anchor = "center")


        self.app_name = CTkLabel(master=self.frame, text="My Bank App", font=("arial", 30))
        self.app_name.place(relx=0.5, rely=0.14, anchor = "center")

        self.moto_label = CTkLabel(master=self.frame, text="Transact with ease", font=("arial", 15))
        self.moto_label.place(relx=0.5, rely=0.27,anchor="center")

        self.moto_label1 = CTkLabel(master=self.frame, text="Register an account with Us", font=("arial", 20))
        self.moto_label1.place(relx=0.5, rely=0.4,anchor="center")

        self.entry_name = CTkEntry(master=self.frame, placeholder_text="Enter your Name", font=("arial", 15),
                                        width=250)
        self.entry_name.place(relx=0.26, rely=0.58, anchor="center")

        self.entry_gender = CTkEntry(master=self.frame, placeholder_text="Enter your Gender", font=("arial", 15),
                                        width=250)
        self.entry_gender.place(relx=0.73, rely=0.58, anchor="center")

        self.entry_address = CTkEntry(master=self.frame, placeholder_text="Enter your Address", font=("arial", 15),
                                        width=250)
        self.entry_address.place(relx=0.26, rely=0.74, anchor="center")

        self.entry_phone = CTkEntry(master=self.frame, placeholder_text="Enter your Phone No", font=("arial", 15),
                                        width=250)
        self.entry_phone.place(relx=0.73, rely=0.74, anchor="center")

        self.entry_age = CTkEntry(master=self.frame, placeholder_text="Enter your age", font=("arial", 15),
                                        width=250)
        self.entry_age.place(relx=0.5, rely=0.85, anchor="center")

        self.button = CTkButton(master=self.frame, text="Register", width=700, command=self.register_customer)
        # self.button.pack(fill=X)
        self.button.place(relx=0.5, rely=0.96, anchor="center")


        self.app.mainloop()


    def register_customer(self):
        # saccount_number = customer.AccountGen()
        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get()
        address = self.entry_address.get()
        phone_number = self.entry_phone.get()
        customer = Customer(name, age, gender, address, phone_number)
    
        # Check if customer was successfully registered
        if customer:
            messagebox.showinfo("Success", "Customer registered successfully!")
            self.app.destroy()
        else:
            messagebox.showerror("Error", "Registration failed, something went wrong.")



    def balance(self, account_number):
        BankAccount.AccountStatement(self, account_number)

    def withdraw(self, amount, account_number):
        BankAccount.withdraw(self, amount, account_number)

    def deposit(self, amount, account_number):
        BankAccount.deposit(self, amount, account_number)

# App().register_customer(
#     "Nsikan Simon", 27, "Male", "nigeria", "08142329190"
# )
# /S

if __name__ == "__main__":
    App = App()


# App().deposit(2000, 72246645)
# App().balance(72246645)

