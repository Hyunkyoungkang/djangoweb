from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def list(request):
    # 모든 데이터 변수에 저장 : models의 클래스이름.objects.all()
    Notice_list = Notice.objects.all()
    return render(request, 'main/notice_list.html', {'noticeList':Notice_list})

def program_view(request):
    Program_list = Program.objects.all()
    return render(request, 'main/program.html', {'programList':Program_list})

def posting(request,id):
    # primary key(pk)를 이용하여 하나의 게시글만 검색
    post = Notice.objects.get(pk=id)
    return render(request, 'main/notice_view.html',{'notice':post})


def notice_add(request):
    if request.method == 'POST':
        new_notice = Notice.objects.create(
            title = request.POST['title'],
            contens = request.POST['contens'],
            views = 0
        )
        return redirect('/notice/')
    return render(request, 'main/notice_add.html')

def notice_remove(request,pk):
    if request.method == 'POST':
        notice = Notice.objects.get(pk=pk)
        notice.delete()
    return redirect('/notice/')