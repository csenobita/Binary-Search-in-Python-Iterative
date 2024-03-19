from tkinter import *
from tkinter import messagebox


class BinarySearch:

    def __init__(self, root):

        self.root = root
        self.root.title("Binary Search")
        self.root.geometry("1000x800+400+100")
        self.root.resizable(False, False)
        self.fbg = '#658ddd'

        self.search_var = StringVar()

        self.font = ("Arial", 30, 'bold')
        self.font1 = ("Arial", 15, 'bold')

        self.freme1 = Frame(self.root, bg=self.fbg, bd=10, relief=RIDGE, width=1000, height=800)
        self.freme1.pack()

        self.freme1_title = Label(self.freme1, text="Binary Search", bg=self.fbg, font=self.font, relief=RIDGE, bd=0)
        self.freme1_title.place(x=350, y=20)

        self.text_box_title = Label(self.freme1, text="Enter the List  : ", bg=self.fbg, font=('arial', 12, 'bold'),
                                    bd=0, relief=RIDGE)
        self.text_box_title.place(x=110, y=70)

        self.text_box = Text(self.freme1, bg='white', font=self.font1, bd=0, relief=RIDGE, width=70, height=7)
        self.text_box.place(x=110, y=100)

        self.s_title = Label(self.freme1, text="Search Item : ", bg=self.fbg, font=('arial', 15, 'bold'),
                             bd=0, relief=RIDGE)
        self.s_title.place(x=300, y=300)

        self.search_num = Entry(self.freme1, bg='white', font=self.font1, bd=1, relief=RIDGE, width=7, justify='center',
                                textvariable=self.search_var)
        self.search_num.place(x=450, y=300)

        self.button1 = Button(self.freme1, text="Search", font=self.font1, bg=self.fbg, command=self.search)
        self.button1.place(x=450, y=400)

        self.output = Label(self.freme1, bg=self.fbg, width=30, text='', font=('arial', 20, 'bold'), relief=RIDGE)
        self.output.place(x=250, y=500)

    def binary_search(self, s, n):
        self.li = []

        for i in range(0, len(s)):
            self.li.append(int(s[i]))

        self.fast = 0
        self.last = len(self.li) - 1

        while self.fast <= self.last:
            self.mid = (self.fast + self.last) // 2

            if int(self.li[self.mid]) == n:

                text = "Number found in the list"

                self.output.config(text=text)

                break


            else:

                if int(self.li[self.mid]) < n:

                    self.fast = self.mid + 1


                else:

                    self.last = self.mid - 1
        else:
            text = "Number NOT found in the list"
            self.output.config(text=text)

    def search(self):

        if self.text_box.get(1.0, END) != "":
            s = self.text_box.get(1.0, END)

            if len(s)!=1:
                n = int(self.search_num.get())

                s = s.split(',')

                self.binary_search(s, n)
            else:
                messagebox.showerror('Error', 'Please Search item')
        else:
            messagebox.showerror("Error", "Please List")


if __name__ == '__main__':
    root = Tk()
    BinarySearch(root)
    root.mainloop()
