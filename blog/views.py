from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date_Ite=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
