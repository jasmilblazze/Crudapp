from django.shortcuts import render, redirect, get_object_or_404
from . models import Crud

def Mten(request):
    ans=Crud.objects.all()
    if request.method=='POST':
        slno=request.POST.get('sl_no','')
        Itemname=request.POST.get('item_name','')
        desc=request.POST.get('desc','')
        task=Crud(slno=slno,Item_name=Itemname,Description=desc)
        task.save()
    return render(request,'Simple.html',{'item':ans})

def delete(request,taskid):
    dlt=Crud.objects.get(id=taskid)
    if request.method=='POST':
        dlt.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    anv=get_object_or_404(Crud,id=id)
    if request.method=='POST':
        anv.slno=request.POST.get('sl_no')
        anv.Item_name=request.POST.get('item_name')
        anv.Description=request.POST.get('desc')
        anv.save()
        return redirect('/')
    return render(request,'update.html',{'anv':anv})






