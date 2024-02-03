from django.shortcuts import render
from .models import Cat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render(request, 'gallery_4_laba/home.html')


def gallery(request):
	cat_list = Cat.objects.all()
	context = {'cats': cat_list}
	return render(request, 'gallery_4_laba/gallery.html', context)


def like(request):
	if request.method == 'POST':
		id = request.POST.get('cat_id')
		print(id)
		cat = Cat.objects.get(id=id)
		cat.like = int(cat.like) + 1
		cat.save()
		count_like = cat.like
		data = {
			'count_like': count_like
		}
		return JsonResponse(data)
	return JsonResponse({'error': 'Invalid method'}, status=400)