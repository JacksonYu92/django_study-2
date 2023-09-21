from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.
def depart(request):
    # 新增
    # models.Department.objects.create(title="销售部",count=10)
    # models.Department.objects.create(**{"title":"技术部", "count":2})

    # 查询
    queryset = models.Department.objects.all().order_by("-id")
    # queryset = models.Department.objects.filter(id__gt=0) #id>0
    # for obj in queryset:
    #     print(obj.id,obj.title,obj.count)

    # obj = models.Department.objects.filter(id=1).first()
    # print(obj.id, obj.title, obj.count)

    # 删除
    # models.Department.objects.filter(id=1).delete()

    # 更新
    # models.Department.objects.filter(id=2).update(count=99)

    return render(request, 'depart.html', {'queryset': queryset})

def add_depart(request):
    if request.method == "GET":
        return render(request, 'add_depart.html')
    title = request.POST.get("title")
    count = request.POST.get("count")

    models.Department.objects.create(title=title, count=count)

    return redirect("/depart/")

def delete_depart(request):

    depart_id = request.GET.get("id")

    models.Department.objects.filter(id=depart_id).delete()

    return redirect("/depart/")

def edit_depart(request):
    if request.method == "GET":
        depart_id = request.GET.get("id")

        depart_obj = models.Department.objects.filter(id=depart_id).first()

        return render(request, 'edit_depart.html', {'depart_obj': depart_obj})
    depart_id = request.GET.get("id")
    title = request.POST.get("title")
    count = request.POST.get("count")

    models.Department.objects.filter(id=depart_id).update(title=title, count=count)

    return redirect("/depart/")