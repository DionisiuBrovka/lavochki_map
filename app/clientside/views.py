from django.shortcuts import render

# Create your views here.
 
def pg_index(request):
    return render(request, "pages/index.html")