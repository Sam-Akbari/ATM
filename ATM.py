#اماده سازی
import tkinter as tk
from tkinter import messagebox

#ساخت کلاسی که داده هارا مشخص میکند
class User:
    def __init__(self, card_number, pin, balance, name):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.name = name
        self.transactions = []

#ایجاد صفحه کار
class ATMApp:
    def __init__(self, root):
        """تابعی که برای ضاهر اولیه برنامه است"""
        self.root = root#صفحه
        self.root.title("ATM App")#نام برنامه
        self.users = {}#برای داده ها
        self.current_user = None#برای داده ها
        self.root.geometry("1020x695")#سایز صفحه
        self.root.resizable(0,0)#مجاز نبودن برای تغییر اندازه پنجره
        self.show_login_screen()#اولین نمایش پنجره ورود است

    def show_login_screen(self):
        """پنجره ورودی چه چیز هایی دارد"""
        self.clear_screen()#صفحه پاک

        self.label = tk.Label(self.root, text="صفحه ورود",font=(20),fg="blue")#موضوع
        self.label.pack()

        self.card_label = tk.Label(self.root, text= "شماره کارت شما")#متن شماره کارت
        self.card_label.place(x=200,y=100)
        self.card_entry = tk.Entry(self.root,width=80)#کادری که کاربر داده را وارد میکند
        self.card_entry.place(x=300,y=100)

        self.pin_label = tk.Label(self.root, text="رمز کارت شما")#متن رمز کارت
        self.pin_label.place(x=200,y=150)
        self.pin_entry = tk.Entry(self.root,width=80)#کادری که کاربر داده را وارد میکند
        self.pin_entry.place(x=300,y=150)

        self.login_button = tk.Button(self.root, text="ورود >",bg="lightgreen",width=23,height=2, command=self.login)#دکمه ورود
        self.login_button.place(x=840,y=650)

        self.register_button = tk.Button(self.root, text="< ساخت اکانت جدید",bg="orange",width=23,height=2, command=self.show_register_screen)#دکمه ساخت اکانت
        self.register_button.place(x=10,y=650)

        self.darkthem_button = tk.Button(self.root, text=" حالت شب ",bg="black",fg="white", command=self.dark_them)#حالت شب
        self.darkthem_button.place(x=10,y=10)
        self.lightthem_button = tk.Button(self.root, text="  حالت روز ",bg="white",fg="black", command=self.light_them)#حالت روز
        self.lightthem_button.place(x=10,y=40)

    def show_register_screen(self):
        """صفحه برای ساخت اکانت"""
        self.clear_screen()#پاک کردن صفحه

        self.label = tk.Label(self.root, text="صفحه ساخت اکانت",font=(20),fg="blue")#موضوع
        self.label.pack()

        self.name_label = tk.Label(self.root, text="نام")#نام
        self.name_label.place(x=200,y=100)
        self.name_entry = tk.Entry(self.root,width=80)#کادر وارد کردن داده
        self.name_entry.place(x=300,y=100)

        self.card_label = tk.Label(self.root, text="شماره کارت شما")#شماره کارت
        self.card_label.place(x=200,y=150)
        self.card_entry = tk.Entry(self.root,width=80)#کادر وارد کردن داده
        self.card_entry.place(x=300,y=150)

        self.pin_label = tk.Label(self.root, text="رمز کارت شما")#رمز کارت
        self.pin_label.place(x=200,y=200)
        self.pin_entry = tk.Entry(self.root,width=80)#کارد وارد کردن داده
        self.pin_entry.place(x=300,y=200)

        self.balance_label = tk.Label(self.root, text="موجودی شما")#موجودی
        self.balance_label.place(x=200,y=250)
        self.balance_entry = tk.Entry(self.root,width=80)#کادر وارد کردن داده
        self.balance_entry.place(x=300,y=250)

        self.register_button = tk.Button(self.root, text="ایجاد اکانت",width=23,height=2,bg="lightgreen", command=self.register)#دکمه ایجاد
        self.register_button.place(x=840,y=650)

        self.back_button = tk.Button(self.root, text="> بازگشت",width=23,height=2,bg="orange", command=self.show_login_screen)#دکمه برگشت
        self.back_button.place(x=10,y=650)

        self.darkthem_button = tk.Button(self.root, text=" حالت شب ",bg="black",fg="white", command=self.dark_them)#حالت شب
        self.darkthem_button.place(x=10,y=10)

        self.lightthem_button = tk.Button(self.root, text="  حالت روز ",bg="white",fg="black", command=self.light_them)#حالت روز
        self.lightthem_button.place(x=10,y=40)

    def show_main_menu(self):
        """صفحه ای که بعد از وورد کاربر نمایش داده میشود"""
        self.clear_screen()#پاک کردن صفحه

        self.label = tk.Label(self.root, text="منوی اصلی",font=(20),fg="blue")#موضوع
        self.label.pack()

        self.account_details_button = tk.Button(self.root, text="مشخصات اکانت",width=142,height=2,bg = "lightgray", command=self.show_account_details)#دکمه دیدن مشخصات
        self.account_details_button.place(x=10,y=600)

        self.transfer_button = tk.Button(self.root, text="انتقال پول",width=23,height=2,bg="lightgreen", command=self.show_transfer_screen)#دکمه انتقال پول به اکانتی دیگر
        self.transfer_button.place(x=840,y=650)

        self.withdraw_button = tk.Button(self.root, text="برداشت پول",width=24,height=2,bg="yellow", command=self.show_withdraw_screen)#دکمه برداشت پول
        self.withdraw_button.place(x=628,y=650)

        self.change_pin_button = tk.Button(self.root, text="تغییر رمز کارت",width=24,height=2,bg="lightblue", command=self.show_change_pin_screen)#دکمه تغییر رمز کارت
        self.change_pin_button.place(x=202,y=650)

        self.transaction_history_button = tk.Button(self.root, text="تاریخچه تراکنش",width=23,height=2,bg="pink", command=self.show_transaction_history)#دکمه ای برای دیدن تاریخچه
        self.transaction_history_button.place(x=415,y=650)

        self.back_button = tk.Button(self.root, text="< خروج از حساب کاربری",width=23,height=2,bg="orange", command=self.show_login_screen)#دکمه خروج
        self.back_button.place(x=10,y=650)

        self.darkthem_button = tk.Button(self.root, text=" حالت شب ",bg="black",fg="white", command=self.dark_them)#حالت شب
        self.darkthem_button.place(x=10,y=10)

        self.lightthem_button = tk.Button(self.root, text="  حالت روز ",bg="white",fg="black", command=self.light_them)#حالت روز
        self.lightthem_button.place(x=10,y=40)

    def show_account_details(self):
        """کادری که مشخصات اکانت کاربر را نشان میدهد"""
        user = self.current_user#ساخت متغیر 
        details = f"نام شما: {user.name}\nشماره کارت شما: {user.card_number}\nهمه موجودی شما: {user.balance}"#وارد کردن و نمایش داده ها
        messagebox.showinfo("مشخصات اکانت", details)#موضوع

    def show_transfer_screen(self):
        """پنجره ای که کاربر بعد از زدن دکمه انتقال پول میبیند"""
        self.clear_screen()#پاک کردن صفحه
        self.label = tk.Label(self.root, text="انتقال پول",font=(20),fg="blue")#موضوع
        self.label.pack()

        self.to_card_label = tk.Label(self.root, text="شماره کارت")#متن شمار کارت
        self.to_card_label.place(x=200,y=100)
        self.to_card_entry = tk.Entry(self.root,width=80)#کادر وارد کردن
        self.to_card_entry.place(x=300,y=100)

        self.amount_label = tk.Label(self.root, text="مبلغ")#متن مبلغ
        self.amount_label.place(x=200,y=150)

        self.amount_entry = tk.Entry(self.root,width=80)#کادر داده
        self.amount_entry.place(x=300,y=150)

        self.transfer_button = tk.Button(self.root, text="انتقال >",bg="lightgreen",width=23,height=2, command=self.transfer_money)#دکمه انتقال دادن
        self.transfer_button.place(x=840,y=650)

        self.back_button = tk.Button(self.root, text="< بازگشت",bg="orange",width=23,height=2,command=self.show_main_menu)#دکمه برگشت
        self.back_button.place(x=10,y=650)

        self.darkthem_button = tk.Button(self.root, text=" حالت شب ",bg="black",fg="white", command=self.dark_them)#حالت شب
        self.darkthem_button.place(x=10,y=10)

        self.lightthem_button = tk.Button(self.root, text="  حالت روز ",bg="white",fg="black", command=self.light_them)#حالت روز
        self.lightthem_button.place(x=10,y=40)

    def show_withdraw_screen(self):
        """پنجره برداشت پول"""
        self.clear_screen()#پاک کردن صفحه

        self.label = tk.Label(self.root, text="برداشت پول",font=(20),fg="blue")#موضوع
        self.label.pack()

        self.amount_label = tk.Label(self.root, text="مبلغ")#متن مبلغ
        self.amount_label.place(x=200,y=100)

        self.amount_entry = tk.Entry(self.root,width=80)#کادر وارد داده
        self.amount_entry.place(x=300,y=100)

        self.withdraw_button = tk.Button(self.root, text="برداشت >",bg="lightgreen",width=23,height=2, command=self.withdraw_money)#دکمه برداشت
        self.withdraw_button.place(x=840,y=650)

        self.back_button = tk.Button(self.root, text="< بازگشت",bg="orange",width=23,height=2, command=self.show_main_menu)#دکمه برگشت
        self.back_button.place(x=10,y=650)

        self.darkthem_button = tk.Button(self.root, text=" حالت شب ",bg="black",fg="white", command=self.dark_them)#حالت شب
        self.darkthem_button.place(x=10,y=10)

        self.lightthem_button = tk.Button(self.root, text="  حالت روز ",bg="white",fg="black", command=self.light_them)#حالت روز
        self.lightthem_button.place(x=10,y=40)

    def show_change_pin_screen(self):
        """پنجره ای که کاربر رمز کارت خود را عوض میکند"""
        self.clear_screen()#پاک کردن صفحه

        self.label = tk.Label(self.root, text="تغییر رمز کارت",font=(20),fg="blue")#موضوع
        self.label.pack()

        self.new_pin_label = tk.Label(self.root, text="رمز جدید")#متن رمز
        self.new_pin_label.place(x=200,y=100)

        self.new_pin_entry = tk.Entry(self.root,width=80)#کادر وارد کردن داده
        self.new_pin_entry.place(x=300,y=100)

        self.change_pin_button = tk.Button(self.root, text="تغییر >",bg="lightgreen",width=23,height=2, command=self.change_pin)#دکمه ثبت
        self.change_pin_button.place(x=840,y=650)

        self.back_button = tk.Button(self.root, text="< بازگشت",bg="orange",width=23,height=2, command=self.show_main_menu)#دکمه برگشت
        self.back_button.place(x=10,y=650)

        self.darkthem_button = tk.Button(self.root, text=" حالت شب ",bg="black",fg="white", command=self.dark_them)#حالت شب
        self.darkthem_button.place(x=10,y=10)
        self.lightthem_button = tk.Button(self.root, text="  حالت روز ",bg="white",fg="black", command=self.light_them)#حالت روز
        self.lightthem_button.place(x=10,y=40)

    def show_transaction_history(self):
        """پنجره نمایش تاریخچه ها اخیر"""
        user = self.current_user#سخت متغیر
        history = "\n".join(user.transactions)#نمایش
        messagebox.showinfo("تاریخچه تراکنش", history)#موضوع

    def clear_screen(self):
        """برای بازگشت ها است"""
        #صفحات را به حالت قبلی میبرد
        for widget in self.root.winfo_children():
            widget.destroy()

    def register(self):
        """به حالت اول برمیگردد برای بازگشت است"""
        #داده های قبلی را نمایش میدهد
        name = self.name_entry.get()
        card_number = self.card_entry.get()
        pin = self.pin_entry.get()
        balance = self.balance_entry.get()

        #اگر خالی بود ارورو میدهد
        if card_number in self.users:
            messagebox.showerror("Error", "Edit it!")
        else:
            self.users[card_number] = User(card_number, pin, float(balance), name)
            messagebox.showinfo("Success", "done!")
            self.show_login_screen()

    def login(self):
        """برای وارد شدن فرد است"""
        card_number = self.card_entry.get()
        pin = self.pin_entry.get()

        user = self.users.get(card_number)
        #اگر درست بود وارد میشود در غیر این صورت ارور میدهد
        if user and user.pin == pin:
            self.current_user = user
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Edit it!")

    def transfer_money(self):
        """برای پول ها است"""
        to_card = self.to_card_entry.get()#ساخت متغیر
        amount = self.amount_entry.get()#ساخت متغیر

        #اگر درست نبود ارور میدهد
        if not amount.isdigit():
            messagebox.showerror("Error", "Edit it!!")
            return

        amount = float(amount)

        if to_card in self.users:#برای نمایش انتقالی ها و دریافتی ها
            if self.current_user.balance >= amount:
                self.current_user.balance -= amount
                self.users[to_card].balance += amount
                self.current_user.transactions.append(f"انتقال {amount} به {to_card}")
                self.users[to_card].transactions.append(f"دریافت {amount} از {self.current_user.card_number}")
                messagebox.showinfo("Success", "done!")
                self.show_main_menu()
            else:
                messagebox.showerror("Error", "Edit it!")
        else:
            messagebox.showerror("Error", "Edit it!")

    def withdraw_money(self):
        """برای پول ها است"""
        amount = self.amount_entry.get()

        if not amount.isdigit():
            messagebox.showerror("Error", "Edit it!")#اگر درست نبود ارورو میدهد
            return

        amount = float(amount)

        if self.current_user.balance >= amount:#برای نمایش برداشت ها است
            self.current_user.balance -= amount
            self.current_user.transactions.append(f"برداشت {amount}")
            messagebox.showinfo("Success", "done!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Edit it!")

    def change_pin(self):
        new_pin = self.new_pin_entry.get()
        self.current_user.pin = new_pin
        messagebox.showinfo("Success", "done!")#پنجره نمایش انجام شد
        self.show_main_menu()
    def dark_them(self):
        """تم شب"""
        self.root.config (bg = "black")#تم مشکی
    def light_them(self):
        """تم روز"""
        self.root.config (bg = "white")#تم سفید

#نمایش های برنامه و اتمام
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()

#اخرین پروژه