from django.shortcuts import render,redirect
from todo.models import Todo
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def index(request,page):
    content = Todo.objects.all().order_by('-create_time')
    paginator = Paginator(content,5)
    page_num=1
    if request.GET.get('page'):
        page_num=int(request.GET.get('page'))

    try:
        content_list=paginator.page(page_num)
    except PageNotAnInteger:
        content_list = paginator.page(1)
    except EmptyPage:
        content_list = paginator.page(paginator.num_pages)

    return render(request, 'demo.html',{'content_list':content_list})

def add(request):
    if request.method == 'POST':
        content = request.POST.get('Item')
        if content:
            Todo.objects.create(
                content = content
            )
    # content_list = Todo.objects.all()
    # return render(request,'demo.html',locals())
    return HttpResponseRedirect('/index/')

def delete(request,id):
    Todo.objects.filter(id=id).delete()
    return HttpResponseRedirect('/index/')

def edit(request,id=0):
    if request.method == 'POST':
        content = request.POST.get('edit')
        Todo.objects.filter(id=id).update(content=content)
        return HttpResponseRedirect('/index/')
    else:
        id =int(id)
        content = Todo.objects.all().order_by('-create_time')
        paginator = Paginator(content, 5)
        page_num = 1
        if request.GET.get('page'):
            page_num = int(request.GET.get('page'))
        try:
            content_list = paginator.page(page_num)
        except PageNotAnInteger:
            content_list = paginator.page(1)
        except EmptyPage:
            content_list = paginator.page(paginator.num_pages)
        return render(request, 'demo.html', {'content_list':content_list,'id':id})
    #return HttpResponseRedirect('/index/')

def status(request,id):
    content = Todo.objects.get(id=id)
    #print(content.values('status'))
    if content.status:
        content.status=False
        content.save()
        return HttpResponseRedirect('/index/')
    else:
        content.status = True
        content.save()
        return HttpResponseRedirect('/index/')
