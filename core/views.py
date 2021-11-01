from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return redirect('upload')


def upload_file(request):
    if request.method == 'GET':
        return render(request, 'core/uploadfile.html')
    elif request.method == 'POST':
        print(request.FILES)
        return redirect('upload')
