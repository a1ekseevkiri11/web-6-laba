from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm
from django.http import HttpResponseRedirect, HttpResponseNotFound

def home(request):
	form = ImageForm()
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/gallery")
	return render(request, 'gallery_4_laba/home.html', {'form': form})


def gallery(request):
	products_list = Product.objects.all()
	context = {'products': products_list}
	return render(request, 'gallery_4_laba/gallery.html', context)

def delete(request, id):
	try:
		product = Product.objects.get(id=id)
		product.delete()
		return HttpResponseRedirect("/gallery")
	except Product.DoesNotExist:
		return HttpResponseNotFound("<h2>Person not found</h2>")

def edit(request, id):
	try:
		product = Product.objects.get(id=id)
		form = ImageForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/gallery")
		else:
			form = ImageForm(instance=product)
		return render(request, 'gallery_4_laba/home.html', {'form': form}) 
	except Product.DoesNotExist:
		return HttpResponseNotFound("<h2>Person not found</h2>")