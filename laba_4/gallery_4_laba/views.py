from django.shortcuts import render
from .models import Product, Captcha
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm, CaptchaForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .script import generate_math_captcha, generate_captcha_key, generation_captcha

def home(request):
	if request.method == 'POST':
		product_form = ImageForm(request.POST, request.FILES)
		captcha_form = CaptchaForm(request.POST)
		if product_form.is_valid() and captcha_form.is_valid():
			product_form.save()
			key = captcha_form.cleaned_data['key']
			captcha_obj = Captcha.objects.get(key=key)
			captcha_answer = captcha_obj.answer
			if captcha_answer == captcha_form.cleaned_data['answer']:
				product_form.save()
				captcha_obj.delete()
				return HttpResponseRedirect("/gallery")
			expression, captcha_form = generation_captcha()
			return render(request, 'gallery_4_laba/home.html', {'product_form': product_form, 'captcha_form': captcha_form, 'expression': expression, 'error_message': 'Неправильный ответ на капчу'})

	expression, captcha_form = generation_captcha()
	product_form = ImageForm()
	return render(request, 'gallery_4_laba/home.html', {'product_form': product_form, 'captcha_form': captcha_form, 'expression': expression})


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
		product_form = ImageForm(request.POST)
		if product_form.is_valid():
			product_form.save()
			return HttpResponseRedirect("/gallery")
		else:
			product_form = ImageForm(instance=product)
		return render(request, 'gallery_4_laba/home.html', {'product_form': product_form}) 
	except Product.DoesNotExist:
		return HttpResponseNotFound("<h2>Person not found</h2>")