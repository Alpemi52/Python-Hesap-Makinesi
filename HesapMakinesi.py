from tkinter import *


class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI(parent)
        self.statement = ""

    def initUI(self, parent):
        self.entry = Entry(parent, width=44, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.button_1 = Button(width=15, height=2, text="1", command=lambda: self.add_statement("1"))
        self.button_2 = Button(width=15, height=2, text="2", command=lambda: self.add_statement("2"))
        self.button_3 = Button(width=15, height=2, text="3", command=lambda: self.add_statement("3"))
        self.button_4 = Button(width=15, height=2, text="4", command=lambda: self.add_statement("4"))
        self.button_5 = Button(width=15, height=2, text="5", command=lambda: self.add_statement("5"))
        self.button_6 = Button(width=15, height=2, text="6", command=lambda: self.add_statement("6"))
        self.button_7 = Button(width=15, height=2, text="7", command=lambda: self.add_statement("7"))
        self.button_8 = Button(width=15, height=2, text="8", command=lambda: self.add_statement("8"))
        self.button_9 = Button(width=15, height=2, text="9", command=lambda: self.add_statement("9"))
        self.button_0 = Button(width=15, height=2, text="0", command=lambda: self.add_statement("0"))

        self.delete_button = Button(width=15, height=2, text="Cls", command=self.clear_statement)
        self.back_button = Button(width=15, height=2, text="Back", command=self.back_statement)
        self.temp_button = Button(width=15, height=2, text="", command=self.secret)
        self.close_button = Button(width=15, height=2, text="Close", command=self.close_app)

        self.divide_button = Button(width=15, height=2, text="/", command=lambda: self.add_statement("/"))
        self.multiply_button = Button(width=15, height=2, text="*", command=lambda: self.add_statement("*"))
        self.minus_button = Button(width=15, height=2, text="-", command=lambda: self.add_statement("-"))
        self.plus_button = Button(width=15, height=2, text="+", command=lambda: self.add_statement("+"))
        self.dot_button = Button(width=15, height=2, text=".", command=lambda: self.add_statement("."))

        self.equal_button = Button(width=15, height=2, text="=", command=self.calculate_result)

        self.button_1.grid(row=4, column=0, padx=5, pady=5)
        self.button_2.grid(row=4, column=1, padx=5, pady=5)
        self.button_3.grid(row=4, column=2, padx=5, pady=5)
        self.button_4.grid(row=3, column=0, padx=5, pady=5)
        self.button_5.grid(row=3, column=1, padx=5, pady=5)
        self.button_6.grid(row=3, column=2, padx=5, pady=5)
        self.button_7.grid(row=2, column=0, padx=5, pady=5)
        self.button_8.grid(row=2, column=1, padx=5, pady=5)
        self.button_9.grid(row=2, column=2, padx=5, pady=5)
        self.button_0.grid(row=5, column=0, padx=5, pady=5)

        self.delete_button.grid(row=1, column=0, padx=5, pady=5)
        self.back_button.grid(row=1, column=1, padx=5, pady=5)
        self.temp_button.grid(row=1, column=2, padx=5, pady=5)
        self.close_button.grid(row=1, column=3, padx=5, pady=5)

        self.divide_button.grid(row=2, column=3, padx=5, pady=5)
        self.multiply_button.grid(row=3, column=3, padx=5, pady=5)
        self.minus_button.grid(row=4, column=3, padx=5, pady=5)
        self.plus_button.grid(row=5, column=3, padx=5, pady=5)
        self.equal_button.grid(row=5, column=2, padx=5, pady=5)
        self.dot_button.grid(row=5, column=1, padx=5, pady=5)

    def add_statement(self, character):
        self.statement += character
        self.entry.delete(0, END)
        self.entry.insert(0, self.statement)

    def calculate_result(self):
        try:
            self.statement = str(eval(self.statement))
            self.entry.delete(0, END)
            self.entry.insert(0, self.statement)
        except:
            self.entry.delete(0, END)
            self.entry.insert(0, "Error")

    def back_statement(self):
        self.statement = self.statement[:-1]
        current_text = self.entry.get()
        self.entry.delete(len(current_text) - 1, END)

    def clear_statement(self):
        self.statement = ""
        self.entry.delete(0, END)
        self.entry.insert(0, self.statement)

    def secret(self):
        self.statement = ""
        self.entry.delete(0, END)
        self.entry.insert(0, "~~Alperen Müftüoğlu~~")

    def close_app(self):
        self.quit()


def main():
    root = Tk()
    root.title('Hesap Makinesi')
    icon = "hesap_makinesi.ico"
    root.iconbitmap(icon)
    root.resizable(False, False)
    root.geometry("500x290+710+290")
    Calculator(root)
    root.mainloop()


main()
