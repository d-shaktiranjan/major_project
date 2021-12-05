from django.shortcuts import render, redirect, HttpResponse
from home.models import Students, Teachers, Quentions
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
# Create your views here.


def index(request):
    # return HttpResponse(f"Hey user - {request.session.get('uId')}")
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        userType = request.POST.get("type")
        name = request.POST.get("name")
        password = request.POST.get("password")
        conPassword = request.POST.get("conPassword")
        uId = request.POST.get("uId")
        if password == conPassword:
            if userType == "student":
                newStudent = Students(
                    name=name, regNumber=uId, password=make_password(password), branch="", dateTimeOfJoin=datetime.now())
                newStudent.save()
                return HttpResponse(f"{name} is a student added")
            newTeacher = Teachers(name=name, mailId=uId,
                                  password=make_password(password), branch="", dateTimeOfJoin=datetime.now())
            newTeacher.save()
            return HttpResponse(f"{name} is a Teacher added")
        return HttpResponse("Pas & con not match")
    return render(request, "signup.html")


def userLogin(request, isStudent, uId, password):
    if isStudent:
        user = Students.objects.filter(regNumber=uId).first()
    else:
        user = Teachers.objects.filter(mailId=uId).first()
    if user is None:
        return HttpResponse("Please Signup")
    if check_password(password, user.password):
        request.session['log'] = True
        request.session['uId'] = uId
        return redirect(index)
    return HttpResponse("Password not matched")


def login(request):
    if request.method == "POST":
        userType = request.POST.get("type")
        password = request.POST.get("password")
        mail = request.POST.get("mail")
        uId = str(mail).split("@")
        # isStudent = True if userType == "student" else False
        return userLogin(request, True, uId[0], password)
    return redirect(index)


def logout(request):
    del request.session['log']
    del request.session['uId']
    return redirect(index)


def postQuestion(request):
    if request.method == "POST":
        title = request.POST.get("title")
        about = request.POST.get("about")
        new = Quentions(title=title, about=about,
                        dateTimeOfPost=datetime.now())
        new.save()
        return HttpResponse("Post added")
    return render(request, "postQuestion.html")
