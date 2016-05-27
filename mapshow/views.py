from django.shortcuts import render

# Create your views here.
def safemap(request):
    return render(request, 'safemap.html')  # Django会自动在所有的应用目录中搜索名为templates的文件夹，
        # 然后根据模板中的内容构建一个HttpResponse对象

def uploadevent(request):
    return render(request, 'uploadevent.html')
