from django.shortcuts import render, redirect
from django.http import JsonResponse
from django import forms
from web import models
from utils.encrypt import md5


def admin_list(request):
    """用户列表"""
    queryset = models.Admin.objects.all().order_by("-id")
    # for row in queryset:
    #     print(row.username, row.password, row.gender, row.get_gender_display(), row.depart.title)

    return render(request, 'admin_list.html', {"queryset": queryset})

class AdminModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['username', 'password','age','gender','depart']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 自定义操作，找到所有的字段
    #     print(self.fields)
        for name, field_object in self.fields.items():
            # print(name, field_object)
            field_object.widget.attrs = {"class": "form-control"}

def admin_add(request):
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'admin_form.html', {'form':form})

    form = AdminModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'admin_form.html', {'form': form})

    form.instance.password = md5(form.instance.password)

    form.save()
    return redirect('/admin/list/')

class AdminEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['username','age','gender','depart']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 自定义操作，找到所有的字段
    #     print(self.fields)
        for name, field_object in self.fields.items():
            # print(name, field_object)
            field_object.widget.attrs = {"class": "form-control"}

def admin_edit(request, aid):
    admin_object = models.Admin.objects.filter(id=aid).first()

    if request.method == "GET":
        form = AdminEditModelForm(instance=admin_object)
        return render(request, 'admin_form.html', {'form': form})

    form = AdminEditModelForm(instance=admin_object, data=request.POST)
    if not form.is_valid():
        return render(request, 'admin_form.html', {"form": form})

    form.save()

    return redirect('/admin/list/')

def admin_delete(request):
    aid = request.GET.get("aid")

    models.Admin.objects.filter(id=aid).delete()

    # return JsonResponse({"status": False, 'error': 'ID不能为空'})
    return JsonResponse({"status": True})