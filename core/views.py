from django.shortcuts import redirect, render
import pytz
from api.models import Person
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

        # Substitui Valores NaN por strings vazias
        df = df.fillna("")

        # Converte a coluna unix time para datetime
        df["nascimento"] = pd.to_datetime(df["nascimento"], unit="s").apply(
            lambda x: x.to_datetime64()
        )

        # Adiciona timezone UTC para o datetime
        df["nascimento"] = df["nascimento"].dt.tz_localize(pytz.utc)

        # Salva os dados no banco de dados
        for _, row in df.iterrows():
            person = Person()
            person.id = row["id"]
            person.first_name = row["nome"]
            person.last_name = row["sobrenome"]
            person.gender = row["sexo"]
            person.height = row["altura"]
            person.weight = row["peso"]
            person.birthdate = row["nascimento"]
            person.district = row["bairro"]
            person.state = row["estado"]
            person.number = row["numero"]
            person.city = row["cidade"]
            person.save()

        context = {"data": df.to_html(index=False), "success": True}
        return render(request, "core/uploadfile.html", context)
