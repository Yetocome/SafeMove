from django.shortcuts import redirect, render
from django.http import HttpResponse
from mapshow.models import VisitorEvent

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
