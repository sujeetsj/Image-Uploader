from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    # Order by 'date' field in descending order so the newest images come first
    img = Image.objects.all().order_by('-date')
    return render(request, 'home.html', {'img': img, 'form': form})
