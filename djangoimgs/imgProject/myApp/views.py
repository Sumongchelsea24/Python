from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import ImageModel

def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')  
    else:
  
        form = ImageForm()
    images= ImageModel.objects.all()
    context = {
        'form': form,
        'images':images,
    }
    return render(request, 'upload_image.html', context=context)
