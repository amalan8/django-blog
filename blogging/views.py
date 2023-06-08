from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from blogging.models import Post, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.serializers import PostSerializer, CategorySerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-published_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("-name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class BlogListView(ListView):
    model = Post
    queryset = Post.objects.order_by("-published_date").exclude(published_date=None)
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    model = Post
    queryset = Post.objects.order_by("-published_date").exclude(published_date=None)
    template_name = "blogging/detail.html"



def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
