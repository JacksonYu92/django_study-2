from django.shortcuts import render, redirect

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('user')
        password = request.POST.get('pwd')

        if username == 'root' and password == '123':
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

def index(request):
    queryset = [
        {"id": 1, "phone": "1888888888", "city": "上海"},
        {"id": 2, "phone": "1888888883", "city": "北京"},
        {"id": 3, "phone": "1888888884", "city": "上海"},
        {"id": 4, "phone": "1888888885", "city": "上海"},
    ]
    return render(request, 'index.html', {"queryset":queryset})