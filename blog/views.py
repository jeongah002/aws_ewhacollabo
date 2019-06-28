from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs':blogs})
    
def photo(request):
    blogs = Blog.objects
    return render(request, 'blog/photo.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk= blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.pub_date = timezone.datetime.now()
    blog.image = request.GET['image']
    blog.body = request.GET['body']

    blog.save()
    return redirect('/blog/' + str(blog.id))


def comment_new(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Blog.objects.get(pk=blog_id)
            comment.save()
            return redirect('detail', blog_id)
        else:
            form = CommentForm()
        return render(request, 'blog_form.html', {'form':form})