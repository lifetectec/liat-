from django.shortcuts import render, redirect
from .models import Photo, Category
from theblog.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
import os


@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)


def galleryview(request):
	photos = Photo.objects.all()
	context = {'photos': photos}
	template = 'photos/listview.html'	
	return render(request, template, context)

#delete gallery image
def deletePhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    if len(photos.image) > 0:
        os.remove(photos.image.path)
    photos.delete()
    messages.success(request,"Product Deleted Successfuly")
    return redirect('social/post_detail.html')

#category view
def CategoryView(request, category):
    user = request.user
    category_posts = Post.objects.filter(user=user)
    return render(request, 'social/categories.html', { category_posts : category_posts})


