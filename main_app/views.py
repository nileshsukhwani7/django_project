from django.shortcuts import render, HttpResponse

# Create your views here.
def index_page(request):
    return HttpResponse("Hello<br/><br/><h1>Kavya</h1>")