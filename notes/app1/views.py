from django.shortcuts import render
from app1.models import Notes

# Create your views here.
def fun1(request):
    result=Notes.objects.all()
    if request.method=="POST":
        heading=request.POST.get("title")
        day=request.POST.get("date")
        about=request.POST.get("desc")

        obj=Notes(Title=heading,Date=day,Description=about)
        obj.save()
        result=Notes.objects.all()
        return render(request,"index.html",{"res":result , "obj":obj})
    return render(request,"index.html")

def fun2(request):
    result=Notes.objects.all()
    if request.method=="POST":
        sno=request.get('id')
        if Notes.objects.filter(id==sno):
            obj=Notes.objects.get(id=sno)
        else:
            obj=None
        return render(request,'search.html',{'res':result,'obj':obj})
    return render(request,'search.html')