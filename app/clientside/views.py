from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Lavochki, Profile
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

        form_error = False

        #------------------------------------
        if 'x' in request.POST.keys():
            if request.POST['x'] != '':
                input_x = request.POST['x']
            else:
                form_error = True
        else:
            form_error = True

        #------------------------------------
        if 'y' in request.POST.keys():
            if request.POST['y'] != '':
                input_y = request.POST['y']
            else:
                form_error = True
        else:
            form_error = True

        #------------------------------------
        if 'disc' in request.POST.keys():
            if request.POST['disc'] != '':
                input_disc = request.POST['disc']
            else:
                form_error = True
        else:
            form_error = True

        #------------------------------------
        if 'is_padik' in request.POST.keys():
            if request.POST['is_padik'] != '':
                if request.POST['is_padik'] == '1':
                    input_is_padik = True
                elif request.POST['is_padik'] == '2':
                    input_is_padik = False
                elif request.POST['is_padik'] == '3':
                    input_is_padik = None
                else:
                    input_is_padik = None
            else:
                input_is_padik = None
        else:
            input_is_padik = None
        #------------------------------------
        if 'is_ten' in request.POST.keys():
            if request.POST['is_ten'] != '':
                if request.POST['is_ten'] == '1':
                    input_is_ten = True
                elif request.POST['is_ten'] == '2':
                    input_is_ten = False
                elif request.POST['is_ten'] == '3':
                    input_is_ten = None
                else:
                    input_is_ten = None
            else:
                input_is_ten = None
        else:
            input_is_ten = None
            

        #------------------------------------
        if 'active' in request.POST.keys():
            if request.POST['active'] != '':
                if request.POST['active'] == '1':
                    input_active = 1
                elif request.POST['active'] == '2':
                    input_active = 2
                elif request.POST['active'] == '3':
                    input_active = 3
                else:
                    form_error = True
            else:
                form_error = True
        else:
            form_error = True

        #------------------------------------
        if 'rating' in request.POST.keys():
            if request.POST['rating'] != '':
                if 1 <= int(request.POST['rating']) <= 5:
                    input_rating  = int(request.POST['rating'])
            else:
                form_error = True
        else:
            form_error = True

        #------------------------------------
        images = []
        images_c = 0
        files = request.FILES.getlist('files')
        files_c = len(request.FILES.getlist('files'))
        if files_c >= 1:
            for file in files:
                if file.content_type in  ['image/jpeg','image/png']:
                    images_c += 1
                    images.append(file)
                    
        if images_c < 1:
            form_error = True

        if form_error :
            data = {
                'is_anser':True,
                'error':True,
                'form':AddLavochkaForm(),
            }

            return render(request, "pages/add_form.html", data)
        else:
            user_profile = Profile.objects.get(pk=1)

            new_lavochka = Lavochki(
                user_id = user_profile,
                x = input_x,
                y = input_y,
                description = input_disc,
                is_padik = input_is_padik,
                is_ten = input_is_ten,
                is_activiti = input_active,
                rating = 1.2,

                is_valid = False
            )

            new_lavochka.save()

            data = {
                'is_anser':True,
                'error':False,
                'form':AddLavochkaForm(),
            }

            return render(request, "pages/add_form.html", data)
    else:
        data = {
            'is_anser':False,
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