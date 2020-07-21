import mysql.connector

class dbhelper:

    def __init__(self):

        try:
            self.conn= mysql.connector.connect(host='localhost',port='8889',user='root',password='root',database='quiz')
            self.mycursor =self.conn.cursor()
            print("connected")
        except Exception as e:
            print(e)

    def login_data(self,email,password):
        
        try:
            self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
            user_data=self.mycursor.fetchall()
            #print(user_data)
            return user_data
        except Exception as e:
            print(e)
            return ""        
    
    def register_data(self, data):
        print(data)
        try:
            self.mycursor.execute("INSERT INTO users(user_id,name,email,password,dp) VALUES (NULL,'{}','{}','{}','{}')".format(data[0],data[1],data[2],data[3]))
            self.conn.commit()
            return 1
            

        except Exception as e:
            print(e)
            return 0

    # def question_fetch(self, quiz='sub1', question_no=None):
    #     print(quiz,question_no)
    #     try:
    #         self.mycursor.execute("SELECT * FROM {} WHERE qno_no LIKE {} ".format(quiz, question_no))
    #         question_data = self.mycursor.fetchall()
    #         print(question_data)
    #         return question_data
    #     except Exception as e:
    #         print(e)
    #         return 0
    #this function use to fetch qustion from question table. It's need input subject table name
    def question_fetch(self, quiz='sub1'):
        try:
            self.mycursor.execute("SELECT * FROM {} ".format(quiz))
            question_main_data = self.mycursor.fetchall()
            #print(question_main_data)
            return question_main_data
        except Exception as e:
            print(e)
            return 0
    #this function use to fatch result of user. it's need input user_id ,result_table name
    # def result_fetch(self,result_table ,user_id):
    #     try:
    #         self.mycursor.execute("SELECT * FROM {} WHERE user_id = {}".format(result_table ,user_id))
    #         result_data = self.mycursor.fetchall()
    #         return result_data
    #     except Exception as e:
    #         print(e)
    #help to fatch total marks_data from subject_data
    def marks_fetch(self, subject):
        self.mycursor.execute("SELECT marks FROM {}".format(subject))
        marks_data=self.mycursor.fetchall()
        return marks_data

    def insert_user_answer(self,user_id,answer_table='sub1_answer'):
        pass
        # self.mycursor.execute("INSERT INTO {} (answer_id,user_id) VALUES (NULL,{})".format(answer_table,user_id))
        # self.conn.commit()
    def answer_update(self,user_id,question,question_ans,answer_table='sub1_answer'):
        self.mycursor.execute("UPDATE {} SET {}='{}' WHERE user_id={}".format(answer_table,'qno_'+str(question),question_ans,user_id))
        self.conn.commit()
        #pass

    def ans_fetch(self,user_id,answer_table='sub1_answer'):
        self.mycursor.execute("SELECT * FROM {} WHERE user_id LIKE {} ".format(answer_table,user_id))
        data=self.mycursor.fetchall()
        #print("SELECT * FROM {} WHERE user_id LIKE {} ".format(answer_table, user_id))
        return data


    def update_user_data(self,user_id):

        self.mycursor.execute("SELECT * FROM users WHERE user_id LIKE '{}'".format(user_id))
        user_data=self.mycursor.fetchall()
        #print(user_data)
        return user_data


