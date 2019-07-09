from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import SharedImage

from .forms import ImageUploadForm


def upload(request):
    images = SharedImage.objects.all()
    form = ImageUploadForm.ImageUploadForm()
    return render(request, 'index.html',{'images':images, 'form': form})

def handl(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImageUploadForm.ImageUploadForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            shr = SharedImage()
            shr.image = request.FILES['file']
            shr.title = request.POST['title']
            shr.description = request.POST['description']
            shr.save()
            return redirect('/')
        else:
            form = ImageUploadForm.ImageUploadForm()
            return render(request, 'upload.html',{'form': form})
    else:
            form = ImageUploadForm.ImageUploadForm()
            return render(request, 'upload.html',{'form': form})    