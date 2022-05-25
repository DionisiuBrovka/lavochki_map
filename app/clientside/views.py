from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Lavochki
from .forms import AddLavochkaForm

# Create your views here.
 
def pg_index(request):
    data = {
        'objs' : Lavochki.objects.filter(is_valid=True)
    }
    return render(request, "pages/index.html", data)

def pg_add_form(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)

    data = {
        'form':AddLavochkaForm()
    }

    return render(request, "pages/add_form.html", data)

def pg_edit_form(request):
    return render(request, "pages/edit_form.html")

def pg_auth(request):
    return render(request, "pages/auth.html")

def pg_api_points(request):
    data = {
        "type": "FeatureCollection",
        "features": []
    }

    lavochki_obj_list = Lavochki.objects.filter(is_valid=True)
    
    for lavochka in lavochki_obj_list:
        
        lavochka = {
            "type": "Feature",
            "id": lavochka.id, 
            "geometry": {
                "type": "Point", 
                "coordinates": [lavochka.x, lavochka.y]
            }, 
            "properties": {
                "balloonContentHeader": render_to_string('el/map_balloon/head.html', {'id':lavochka.id}), 
                "balloonContentBody": "<p>Ваше имя: <input name='login'></p><p><em>Телефон в формате 2xxx-xxx:</em>  <input></p><p><input type='submit' value='Отправить'></p>", 
                "balloonContentFooter": "<font size=1>Информация предоставлена: </font> <strong>этим балуном</strong>", 
                "clusterCaption": "<strong><s>Еще</s> одна</strong> метка", 
                "hintContent": "<strong>Текст  <s>подсказки</s></strong>"
            }
        }

        data["features"].append(lavochka)

    return JsonResponse(data)