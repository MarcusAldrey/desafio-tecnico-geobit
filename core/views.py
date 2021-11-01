from django.shortcuts import redirect, render
import pandas as pd

# Create your views here.


def home(request):
    return redirect("upload")


def upload_file(request):
    if request.method == "GET":
        return render(request, "core/uploadfile.html")
    elif request.method == "POST":
        print(request.FILES)
        # get file path
        file_path = request.FILES["file"].name
        pd.read_excel(file_path, index_col=0)
        return redirect("upload")
