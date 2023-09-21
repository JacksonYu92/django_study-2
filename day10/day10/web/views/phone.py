from django.shortcuts import render, redirect
from django.http import JsonResponse
from django import forms
from web import models
from utils.encrypt import md5

def phone_list(request):
    """用户列表"""
    queryset = models.Phone.objects.all().order_by("-id")
    # for row in queryset:
    #     print(row.username, row.password, row.gender, row.get_gender_display(), row.depart.title)

    return render(request, 'phone_list.html', {"queryset": queryset})

class PhoneModelForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        fields = ['mobile', 'price','level','status', 'admin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 自定义操作，找到所有的字段
    #     print(self.fields)
        for name, field_object in self.fields.items():
            # print(name, field_object)
            field_object.widget.attrs = {"class": "form-control"}

def phone_add(request):
    if request.method == "GET":
        form = PhoneModelForm()
        return render(request, 'phone_form.html', {'form':form})

    form = PhoneModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'phone_form.html', {'form': form})

    form.save()
    return redirect('/phone/list/')

class PhoneEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        fields = ['mobile', 'price','level','status', 'admin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 自定义操作，找到所有的字段
    #     print(self.fields)
        for name, field_object in self.fields.items():
            # print(name, field_object)
            field_object.widget.attrs = {"class": "form-control"}

def phone_edit(request, aid):
    phone_object = models.Phone.objects.filter(id=aid).first()

    if request.method == "GET":
        form = PhoneEditModelForm(instance=phone_object)
        return render(request, 'phone_form.html', {'form': form})

    form = PhoneEditModelForm(instance=phone_object, data=request.POST)
    if not form.is_valid():
        return render(request, 'phone_form.html', {"form": form})

    form.save()

    return redirect('/phone/list/')

def phone_delete(request):
    aid = request.GET.get("aid")

    models.Phone.objects.filter(id=aid).delete()

    # return JsonResponse({"status": False, 'error': 'ID不能为空'})
    return JsonResponse({"status": True})