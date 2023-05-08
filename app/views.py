from django.shortcuts import render

# Create your views here.
def background_image(request):
    return render(request,'background_image.html')