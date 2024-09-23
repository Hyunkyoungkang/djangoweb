from django.shortcuts import redirect, render
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/index.html')

def blog(request):
    # 모든 데이터 변수에 저장 : models의 클래스이름.objects.all()
    posts = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':posts})

def posting(request,pk):
    # primary key(pk)를 이용하여 하나의 게시글만 검색
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html',{'post':post})

def new_post(request):
        # form태그의 method가 POST이면 데이터 추가를 실행, GET이면 new_post.html 화면으로 이동
        if request.method == 'POST':
             # 사진파일이 존재하는지 확인, 있으면 사진파일 저장, 없으면 사진파일 저장 X
             if request.POST['mainphoto']:
                  new_article = Post.objects.create(
                       #request.POST['name에 적은 값'] => 웹페이지에서 적은 값을 가지고 오는 방식
                       postname = request.POST['postname'],
                       contents = request.POST['contents'],
                       mainphoto = request.POST.get['mainphoto'],
                  )
             else:
                  new_article = Post.objects.create(
                       postname = request.POST['postname'],
                       contents = request.POST['contents'],
                  )
             return redirect('/blog')
        return render(request,'main/new_post.html')

def remove_post(request,pk):
     post = Post.objects.get(pk=pk)
     if request.method == 'POST':
          post.delete()
          return redirect('/blog')
     return render(request, 'main/remove_post.html',{'Post':post})

