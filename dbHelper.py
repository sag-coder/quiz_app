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
            print(question_main_data)
            return question_main_data
        except Exception as e:
            print(e)
            return 0
    #this function use to fatch result of user. it's need input user_id ,result_table name
    def result_fetch(self,result_table ,user_id):
        try:
            self.mycursor.execute("SELECT * FROM {} WHERE user_id = {}".format(result_table ,user_id))
            result_data = self.mycursor.fetchall()
            return result_data
        except Exception as e:
            print(e)
    #help to fatch total marks data
    def marks_fetch(self, subject):
        self.mycursor.execute("SELECT marks FROM {}".format(subject))
        marks_data=self.mycursor.fetchall()
        return marks_data
