from django.shortcuts import render
from .forms import BlogForm
from django.http import HttpResponse
from .models import Blog

# Create your views here.


def form_view(request):

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'blog.html', {'form': form})
    else:
        form = BlogForm()
    return render(request, 'forms.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def blog(request):
    blogs = Blog.objects.order_by('created_date')[:5]
    return render(request, 'blog.html', {'blogs': blogs})


def blog_details(request, pk):
    blog = Blog.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        return render(request, 'blog_details.html', {'blog': blog, "name": name, "subject": subject, "email": email, "message": message})
    else:
        return render(request, 'blog_details.html', {'blog': blog})
