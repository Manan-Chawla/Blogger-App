from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog,Comment
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    blogs=Blog.objects.all().order_by('-created_at')
    return render(request,'blog/home.html',{'blogs':blogs})


def blog_detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        Comment.objects.create(blog=blog, name=name, body=body)
        return HttpResponseRedirect(request.path)
    comments = blog.comments.all()
    return render(request, 'blog/detail.html', {'blog': blog, 'comments': comments})