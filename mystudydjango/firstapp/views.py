from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Student




def test(request):
    return render(request,'test.html')

def student(request):
    if request.method == "POST":   # 判断请求为POST请求则是提交表单
        student= Student()  # 创建一个student实例
        name = request.POST.get("name")  # 获取提交表单中的name值，赋值给name
        age = request.POST.get("age") # 获取提交表单中的age值，赋值给变量age
        student.student_name = name # 把表单获取的name赋值给实例的name
        student.student_age = age # 把表单获取的age值赋值给实例的age
        student.save()
        return HttpResponse("学生信息提交成功！")  # 保存成功给用户提示
    else:    # 不是POST请求则返回一个提交学生信息的界面
        return render(request,'detail.html')

def index(request):
    return HttpResponse("很高兴见到你")

def show_news(request,a,b):
    ''' 展示新闻界面 '''
    return HttpResponse(F"现在展示的新闻界面：第{a}页，第{b}行")

def show_news2(request,category,page_no):
    return HttpResponse(F"现在展示的新闻界面：第{category}页，第{category}行")
