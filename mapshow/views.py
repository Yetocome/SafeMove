from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from mapshow.models import VisitorEvent, VisualData
from django.views.decorators.http import require_GET

def my_serialize(_from_models):
    a = []
    for k in _from_models:
        a.append(k)
    return a


# Create your views here.
def safemap(request):
    return render(request, 'safemap.html')  # Django会自动在所有的应用目录中搜索名为templates的文件夹，
        # 然后根据模板中的内容构建一个HttpResponse对象

def upload_event(request):
    if request.method == 'POST':
        VisitorEvent.objects.create(
            name = request.POST['name'],
            phone_number = request.POST['phone_number'],
            description = request.POST['description'],
            email = request.POST['email'],
            event_type = request.POST['event_type']
        )
        return redirect('/')

    return render(request, 'upload_event.html')

@require_GET
def raw_data_json(request, t):
    data = VisualData.objects.filter(tag=t)
    sift_data = data.values('count', 'lat', 'lng')
    return JsonResponse(my_serialize(sift_data), safe=False)
