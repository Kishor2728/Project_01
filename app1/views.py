from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from app1.models import StudentModel
from app1.models import LoginModel


def Homeindex(request):
    return render(request, "homeIndex.html")


def forgotPassword(request):
    return render(request, 'forgotPassword.html')


def showpass(request):
    uname = request.POST.get("u1")
    cno = request.POST.get("u2")

    try:
        StudentModel.objects.get(username=uname, contact=cno)
        obj = LoginModel.objects.filter(username=uname).get()
        return render(request, "showpass.html", {"Password": obj.password, "Name": uname})
    except StudentModel.DoesNotExist:
        return render(request, 'forgotPassword.html', {"Message": "Invalid Details"})


def studentLogin(request):
    return render(request, "studentLogin.html")


def studentLoginCheck(request):
    username = request.POST.get('u1')
    password = request.POST.get('u2')

    try:
        LoginModel.objects.get(username=username, password=password)
        return render(request, "studentHome.html", {"name": username})
    except LoginModel.DoesNotExist:
        messages.error(request, "Invalid Details")
        return redirect('studentLogin')


def studentHomePage(request):
    user = request.GET.get('user')
    return render(request, 'studentHome.html', {"name": user})


def viewProfile(request):
    user = request.GET.get('user')
    data = StudentModel.objects.get(username=user)
    return render(request, "viewProfile.html", {"name": user, "Data": data})


def updateProfile(request):
    user = request.GET.get('user')
    data = StudentModel.objects.get(username=user)
    return render(request, "updateProfile.html", {"name": user, "Data": data})


def profileUpdated(request):
    na = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    uname = request.POST.get("username")

    StudentModel.objects.filter(username=uname).update(name=na, age=age, gender=gender)
    messages.success(request, "Updated Successfully!")
    data = StudentModel.objects.get(username=uname)
    return render(request, 'updateProfile.html', {"name": uname, "Data": data})


def studentRegister(request):
    return render(request, "studentRegister.html")


def studentRegistered(request):
    name = request.POST.get('a1')
    age = request.POST.get('a2')
    contactNo = request.POST.get('a3')
    gender = request.POST.get('a4')
    user = request.POST.get('a5')
    password = request.POST.get('a6')
    type = 'Student'

    StudentModel(name=name, age=age, contact=contactNo, gender=gender, username=user).save()

    obj1 = LoginModel(username=user, password=password, type=type)
    obj1.save()

    dict1 = {"Message": "Registered Successfully!"}
    return render(request, "studentRegister.html", dict1)


def adminLogin(request):
    return render(request, 'adminLogin.html')


def adminHome(request):
    user = request.POST.get('u1')
    password = request.POST.get('u2')
    type = 'Admin'

    try:
        LoginModel(username=user, password=password, type=type)
        return render(request, 'adminHome.html')
    except:
        messages.error(request, "Invalid Credentials!")
        return render(request, 'adminLogin.html')


def viewAllStudents(request):
    obj = StudentModel.objects.all()
    return render(request, "viewAllStudents.html", {"Data": obj})


def deleteStudent(request):
    obj = StudentModel.objects.all()
    return render(request, "deleteStudent.html", {"Data": obj})


def delete(request):
    uname = request.GET.get("user")
    print(uname)
    try:
        StudentModel.objects.filter(username=uname).delete()
        try:
            LoginModel.objects.filter(username=uname).delete()
            obj = StudentModel.objects.all()
            return render(request, 'deleteStudent.html', {"Message": "Record Deleted Successfully!", "Data": obj})
        except StudentModel.DoesNotExist:
            return render(request, 'deleteStudent.html', {"Dict": uname})
    except StudentModel.DoesNotExist:
        return render(request, 'deleteStudent.html')
