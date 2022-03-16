from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Broker
from photos.models import Category
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import ListView, CreateView
from django.contrib import messages
import os


@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        broker = Broker.objects.filter(category__user=user)
    else:
        broker = Broker.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'broker': broker}
    return render(request, 'brokers/brokergallery.html', context)


@login_required(login_url='login')
def viewBroker(request, pk):
    broker = Broker.objects.get(id=pk)
    return render(request, 'brokers/broker.html', {'broker': broker})


@login_required(login_url='login')
def addBroker(request):
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
            broker = Broker.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('brokergallery')

    context = {'categories': categories}
    return render(request, 'brokers/addbroker.html', context)


def galleryview(request):
	brokers = Broker.objects.all()
	context = {'brokers': brokers}
	template = 'brokers/brokerview.html'	
	return render(request, template, context)

#delete gallery image
def deleteBroker(request, pk):
    brokers = Broker.objects.get(id=pk)
    if len(brokers.image) > 0:
        os.remove(brokers.image.path)
    brokers.delete()
    messages.success(request,"Product Deleted Successfuly")
    return redirect('social/home.html')

