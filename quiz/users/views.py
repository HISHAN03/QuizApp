from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .utils  import  add_value_to_database,add_New_value_to_database,My_login1,register_user
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import RegisterForm
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return HttpResponse("welcomt to home");

@login_required
def quiz_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT quizid, quiz_name FROM quizzes;")  
        quiz_data = cursor.fetchall()
    return render(request, 'student/home.html', {'quiz_data': quiz_data})

def questions(request, quiz_id):
    with connection.cursor() as cursor:
        query = "SELECT questionid, question,op1,op2,op3,op4,ans FROM questions WHERE quizid = %s;"
        cursor.execute(query, [quiz_id])
        questions_quiz = cursor.fetchall()
    context = {
        'quiz_id': quiz_id,
        'questions_quiz': questions_quiz,
    }

    return render(request, 'student/questions.html', context)



def staff_quiz_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT quizid, quiz_name FROM quizzes;")  
        quiz_data = cursor.fetchall()
    return render(request, 'staff/home.html', {'quiz_data': quiz_data})


def create(request):
    return render(request, 'staff/create.html')



def exist(request, quiz_id):
    with connection.cursor() as cursor:
        query = "SELECT quiz_name FROM quizzes WHERE quizid = %s;"
        cursor.execute(query, [quiz_id])
        quiz = cursor.fetchall()
    context = {
        'quiz_id': quiz_id,
        'quiz': quiz,
    }
    return render(request, 'staff/exist.html', context)












@csrf_exempt
def add_value_to_database_view(request):
    if request.method == 'POST':
        # Get values from POST data
        quizid = request.POST.get('quizid')
        question = request.POST.get('question')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        ans = request.POST.get('ans')

        print(f"Received data: quizid={quizid}, question={question}, op1={op1}, op2={op2}, op3={op3}, op4={op4}, ans={ans}")

        try:
            add_value_to_database(quizid, question, op1, op2, op3, op4, ans)
            print("Value added to the database successfully")
            return JsonResponse({'message': 'Value added to the database'}, status=200)
        except Exception as e:
            print(f"Error adding value to the database: {e}")
            return JsonResponse({'error': 'Failed to add value to the database'}, status=500)

    print("Invalid request method")
    return JsonResponse({'error': 'Invalid request method'}, status=400)




@csrf_exempt
def add_New_value_to_database_view(request):
    if request.method == 'POST':
        # Get values from POST data
        quizid = request.POST.get('quizid')
        quiz_name= request.POST.get('quiz_name')

        question = request.POST.get('question')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        ans = request.POST.get('ans')

        print(f"Received data: quizid={quizid}, question={question}, op1={op1}, op2={op2}, op3={op3}, op4={op4}, ans={ans}")

        try:
            add_New_value_to_database(quizid,quiz_name, question, op1, op2, op3, op4, ans)
            print("Value added to the database successfully")
            return JsonResponse({'message': 'Value added to the database'}, status=200)
        except Exception as e:
            print(f"Error adding value to the database: {e}")
            return JsonResponse({'error': 'Failed to add value to the database'}, status=500)

    print("Invalid request method")
    return JsonResponse({'error': 'Invalid request method'}, status=400)




def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        usn = request.POST.get('usn')
        password = request.POST.get('password')
        print(f"Received POST request. Email: {email}, USN: {usn}, Password: {password}")
        try:
            register_user(usn,email, password)
            user = authenticate(username = email, password = password)
            login(request, user)
            print("Value added to the database successfully")
            return redirect('/')
        except Exception as e:
            print(f"Error adding value to the database: {e}")

    form = RegisterForm()
    return render(request, 'student/register.html', {'form': form})


def My_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        usn = request.POST.get('usn')
        password = request.POST.get('password')
        print(f"Received LOGIN request. Email: {email}, USN: {usn}, Password: {password}")

        try:
            if My_login1(usn, email, password):
                user = authenticate(request, username=email, password=password)
                login(request, user)
                print(f"sucess login")
                return redirect('/')
            else:
                print("Login failed")
                return HttpResponse('<script>alert("User not found."); window.location.href = "/login/";</script>')
        except Exception as e:
            print(f"Error checking value from db: {e}")

    form = RegisterForm()
    return render(request, 'student/login.html', {'form': form})



