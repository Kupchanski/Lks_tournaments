from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.db.models import  Q
from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, "post_form.html", context)


def post_detail(request,slug):
    instance = get_object_or_404(Post, slug=slug)
    context ={
        "instance": instance,
        "title": instance.title
    }
    return render(request, "post_detail.html", context)


def post_list(request):
        today = timezone.now().date()
        queryset_list = Post.objects.all()
        if request.user.is_staff or request.user.is_superuser:
            queryset_list = Post.objects.all()

        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)


        context = {
            "object_list": queryset,
            "title": "List",
            "page_request_var": page_request_var,
            "today": today,
        }
        return render(request, "post_list.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        "instance": instance,
        "form":form
    }
    return render(request, "post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Sucessfully deleted")
    return redirect("posts:list")


def home(request):
    title ='Войти как гость'
    context = {
    "title": title,
    }
    return render(request, "home.html", context)