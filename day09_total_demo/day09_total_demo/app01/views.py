from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app01 import models
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':"输入用户名"}),
        validators=[RegexValidator(r'^\w{6,}$', '用户名格式错误')]
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':"输入密码"}),

    )

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['username', 'password', 'age']

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # user_object = models.UserInfo.objects.filter(username=form.cleaned_data['username'], password=form.cleaned_data['password']).first()
        user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        if user_object:
            return HttpResponse("登录成功")
        else:
            return render(request, 'login.html', {'form':form, 'error':'用户名或密码错误'})

    else:
        return render(request, 'login.html', {'form': form})

def depart_list(request):
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'queryset':queryset})

class DepartModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['title', 'count']

def add_depart(request):
    if request.method == "GET":
        form = DepartModelForm()
        return render(request, 'depart_form.html', {'form':form})

    form = DepartModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/depart/list/')
    else:
        return render(request, 'depart_form.html', {'form':form})

def delete_depart(request):
    did = request.GET.get("did")
    models.Department.objects.filter(id=did).delete()
    return redirect('/depart/list/')

def edit_depart(request):
    did = request.GET.get('did')
    depart_object = models.Department.objects.filter(id=did).first()
    if request.method == "GET":
        form = DepartModelForm(instance=depart_object)
        return render(request, 'depart_form.html', {'form':form})

    form = DepartModelForm(data=request.POST, instance=depart_object)
    if form.is_valid():
        form.save()
        return redirect('/depart/list/')
    else:
        return render(request, 'depart_form.html', {'form':form})