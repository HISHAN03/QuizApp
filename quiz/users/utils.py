from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def add_value_to_database( quizid, question,op1,op2,op3,op4,ans):
    with connection.cursor() as cursor:
        sql_query = f"INSERT INTO questions( questionid,quizid, question,op1,op2,op3,op4,ans) VALUES ( DEFAULT,{quizid}, '{question}','{op1}', '{op2}','{op3}', '{op4}','{ans}');"
        cursor.execute(sql_query)

def add_New_value_to_database( quizid,quiz_name, question,op1,op2,op3,op4,ans):
    with connection.cursor() as cursor:
        sql_query1 = f"INSERT INTO quizzes(quizid,quiz_name) VALUES ( {quizid}, '{quiz_name}');"
        sql_query2 = f"INSERT INTO questions( questionid,quizid, question,op1,op2,op3,op4,ans) VALUES ( DEFAULT,{quizid}, '{question}','{op1}', '{op2}','{op3}', '{op4}','{ans}');"
        cursor.execute(sql_query1)
        cursor.execute(sql_query2)

def register_user(usn,email,password):
    with connection.cursor() as cursor:
        sql_query = f"INSERT INTO student( usn,emailid, password) VALUES ( {usn}, '{email}','{password}');"
        cursor.execute(sql_query)

def My_login1(usn, email1, password1):
    with connection.cursor() as cursor:
        sql_query = "SELECT emailid, password FROM student;"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for result in results:
            emailid, password = result
            if email1 == emailid and password1 == password:
                return True
        return False
        
def staff_signup1(email1, password1):
    with connection.cursor() as cursor:
        sql_query = "SELECT email, password FROM staff_login;"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for result in results:
            emailid, password = result
            if email1 == emailid and password1 == password:
                return True
        return False