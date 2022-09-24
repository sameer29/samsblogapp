from django.shortcuts import render, redirect
from blog.models import BlogModel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    blogs = BlogModel.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})

@csrf_exempt
def createblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        blog = BlogModel(
            username = request.user,
            title = title,
            body = body,

        )
        blog.save()
        return redirect("http://127.0.0.1:8000/myblog/")
    return render(request, 'blog/form.html')

@csrf_exempt
def myblog(request):
    blogs = BlogModel.objects.filter(username=request.user)
    return render(request, 'blog/index.html', {'blogs': blogs})

