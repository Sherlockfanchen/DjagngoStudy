from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Student
from django.shortcuts import redirect
from django.contrib.auth import logout



def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')

'''测试登陆'''

def home(request):
    account = request.session.get("account",default = "未登录" ) # 从session中获取account,没有则为未登录
    return render(request,'home.html',{"account":account})  # 返回home.html，将account传给home.html

def login(request):
    if request.method == "GET": # 如果是GET请求则返回登陆界面
        path = request.GET.get("from") # 获取URL路径的from参数
        return render(request,'login.html',{"path":path})
    else:  #否则就是POST请求提交表单数据
        account = request.POST.get("account")  # 获取表单中account的值
        passwd = request.POST.get("passwd")  # 获取表单中的passwd值
        path = request.GET.get("from") # 获取url路径中from参数，用来登陆成功后跳转回登陆前界面
        if account == "root" and passwd == "1":  # 假设用户账号为root 密码为 1
            # 登陆成功
            request.session["account"] = account # 登陆成功 设置session 下次访问就能辨别该用户
            return redirect('/home/')  # 跳转回home页面
        else:
            # 登陆失败
            url = "/login/?from=%s"%(path)
            return redirect(url)  # 登陆失败返回登陆界面

def quit(request):
    logout(request) # 退出登陆状态
    return redirect('/home/')  # 返回home界面





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
