from dbHelper import dbhelper
from tkinter import *
from tkinter import messagebox


class gui():

    def __init__(self):
        self.db = dbhelper()
        self.root = Tk()
        self.root.title("my log in page")
        self.root.configure(background="#FE5667")
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.main_gui()
        self.root.mainloop()

    # gui clear function
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    # main page
    def main_gui(self):
        self.clear()
        Label(self.root, text="Email", fg="white", bg="#FE5667").pack()
        user_email = Entry(self.root)
        user_email.pack()
        Label(self.root, text="password", fg="white", bg="#FE5667").pack()
        user_password = Entry(self.root)
        user_password.pack()

        Button(self.root, text="login", height=2, width=15, fg="#FE5667",
               command=lambda: self.login_button(email=user_email.get(), password=user_password.get())).pack()
        Button(self.root, text="registration", height=2, width=15, fg="#FE5667",
               command=lambda: self.registration_page()).pack()

    # login button function
    def login_button(self, email, password):
        user_data = self.db.login_data(email, password)
        self.user_id=user_data[0][0]
        #print(self.user_id)
        if len(user_data) >= 1:
            messagebox.showinfo("Login", "successful")
            self.login_page(user_data)
        else:
            messagebox.showerror("Error", "Bad credentials")

    # login page
    def login_page(self, user_data):
        self.clear()
        #result_data= self.result_handel(user_data[0][0])
        Label(self.root, text="name = " + user_data[0][1], fg="white", bg="#FE5667").pack()
        # if result_data!= []:
        #     Label(self.root, text= result_data , fg="white", bg="#FE5667").pack()
        Button(self.root, text="find quiz", height=2, width=15, fg="#FE5667",
               command=lambda: self.clear() or self.quiz_subject()).pack()

    # register button function
    # def register_button():

    #     pass

    # registration page
    def registration_page(self):
        self.clear()

        Label(self.root, text="Name", fg="white", bg="#FE5667").pack()
        name = Entry(self.root)
        name.pack()
        Label(self.root, text="Email", fg="white", bg="#FE5667").pack()
        email = Entry(self.root)
        email.pack()
        Label(self.root, text="Password", fg="white", bg="#FE5667").pack()
        password = Entry(self.root)
        password.pack()

        # data=[name.get(),email.get(),password.get()]
        # print(data)

        Button(self.root, text="Register", height=2, width=15, fg="#FE5667",
               command=lambda: self.register_button(data=[name.get(), email.get(), password.get(), ''])).pack()
        Button(self.root, text="Login", height=2, width=15, fg="#FE5667", command=lambda: self.main_gui()).pack()

    # register button function
    def register_button(self, data):
        response = self.db.register_data(data)

        if response == 1:
            messagebox.showinfo("Login", "successful")
            self.main_gui()
        else:
            messagebox.showerror("Error", "Bad credentials")

    # quiz subject page
    def quiz_subject(self):
        marks_data = self.db.marks_fetch("sub1")
        #marks_data_calculation
        self.add = 0
        for i in range(len(marks_data)):
            #print(i)
            stor = (marks_data[i][0])
            self.add = stor + self.add

        Label(self.root,text=self.add ,fg="white", bg="#FE5667").pack()
        Button(self.root, text="start", height=2, width=15, fg="#FE5667",command=lambda :self.clear() or self.start_clicked()).pack()

    def quiz_question(self, question_data, question_no, size=None):
        Label(self.root,text=question_data[1],fg="white", bg="#FE5667").pack()
        Label(self.root,text="marks = " + str(question_data[2]),fg="white", bg="#FE5667").pack()
        v0 = IntVar()
        v0.set(1)
        r1 = Radiobutton(self.root, text=question_data[4], variable=v0, value=1, fg="white", bg="#FE5667",command= lambda : self.db.answer_update(user_id=self.user_id,question=question_data[0],question_ans=r1['text']))
        r2 = Radiobutton(self.root, text=question_data[5], variable=v0, value=2, fg="white", bg="#FE5667",command= lambda : self.db.answer_update(user_id=self.user_id,question=question_data[0],question_ans=r2['text']))
        r3 = Radiobutton(self.root, text=question_data[6], variable=v0, value=3, fg="white", bg="#FE5667",command= lambda : self.db.answer_update(user_id=self.user_id,question=question_data[0],question_ans=r3['text']))
        r4 = Radiobutton(self.root, text=question_data[7], variable=v0, value=4, fg="white", bg="#FE5667",command= lambda : self.db.answer_update(user_id=self.user_id,question=question_data[0],question_ans=r4['text']))
        r1.pack()
        r2.pack()
        r3.pack()
        r4.pack()


        if question_no!=size-1:                #self.db.answer_update(user_id=self.user_id,question=question_data[1],question_ans=) or

            Button(self.root, text="next", height=2, width=15, fg="#FE5667",command= lambda : self.clear() or self.question_handel(question_no+1)).pack()
        if question_no==size-1:
            Button(self.root, text="submit", height=2, width=15, fg="#FE5667",command= lambda : self.clear() or self.result()).pack()
        if question_no!=0:
            Button(self.root, text="previous", height=2, width=15, fg="#FE5667", command= lambda : self.clear() or self.question_handel(question_no-1)).pack()

    # def next_button(self, question_no):
    #     print(question_no)
    #     question_data=self.db.question_fetch(question_no=question_no)
    #     self.quiz_question(question_data, question_no=question_no)

    def start_clicked(self):
        self.db.insert_user_answer(user_id=self.user_id)
        self.question_main_data= self.db.question_fetch()
        self.question_handel(question_no=0)


    def question_handel(self, question_no):
        #print(self.question_main_data[question_no])
        size=len(self.question_main_data)

        self.quiz_question(self.question_main_data[question_no], question_no, size=size)

    #result for each student
    def result(self):
        result = self.db.ans_fetch(user_id=self.user_id)
        question= self.db.question_fetch()

        modify_result=result[0][2:]
        j=0
        update_marks=0
        marks=0
        for i in question:
            # print(i)
            # print(i[3])
            #print(modify_result[j])
            if i[3]==modify_result[j]:
                #print(question)
                marks= question[j][2]
                update_marks=update_marks+marks
                j=j+1
            else:
                marks=0
        #print(update_marks)
        Label(self.root, text="total marks = "+str(update_marks)+' /'+str(self.add), fg="white", bg="#FE5667").pack()
        Button(self.root, text="start", height=2, width=15, fg="#FE5667",command=lambda: self.clear() or self.login_page(user_data=self.db.update_user_data(user_id=self.user_id))).pack()

   # def result_database_creation(self):






    # def result_handel(self):
    #     result_data = self.db.result_fetch(self.user_id)
    #     print(result_data)
    #     return result_data


obj=gui()
