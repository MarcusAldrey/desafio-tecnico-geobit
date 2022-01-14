# challenge-DRF
Technical challenge for company Geobit.
Stack: Python, Django e Django Rest Framework

## How to run project locally?

Make sure you have Python 3 and pip installed.
- Clone this repository.
- Create virtualenv with Python 3.
- Activate the virtualenv.
- Install dependences.
- Run the migrations.
- Run the server.

### On Linux
```
git clone https://github.com/MarcusAldrey/desafio-tecnico-geobit.git
cd desafio-tecnico-geobit
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
### On Windows
```
git clone https://github.com/MarcusAldrey/desafio-tecnico-geobit.git
cd desafio-tecnico-geobit
python -m venv .venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Loading data

- Download data file from https://docs.google.com/spreadsheets/d/1_kn7crSdIP7fPybxAoFLx15Y1ni9zt22/edit?usp=sharing&ouid=118435021724057045240&rtpof=true&sd=true
- go to `/upload`, click 'procurar', select the data file and click 'upload'.

## API
The API is available at `/api/v1/`

The route `/api/v1/persons` lists all persons in database ordered by age (desc). May receive gender as a query param to filter list.

Ex:
`/api/v1/persons?sexo=F`
`/api/v1/persons?sexo=M`

The route `/api/v1/femalemereen` lists persons with gender=F and city=Mereen

