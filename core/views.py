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
        df = pd.read_excel(request.FILES["file"])
        df.rename(columns={"Unnamed: 0": "Index"}, inplace=True)
        return render(
            request, "core/uploadfile.html", {"data": df.to_html(index=False)}
        )
