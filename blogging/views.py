from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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
