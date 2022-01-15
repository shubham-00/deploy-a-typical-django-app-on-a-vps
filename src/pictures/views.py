from django.shortcuts import redirect, render
from .models import Picture
from .forms import PictureForm


def home_view(request):
    picture_list = Picture.objects.all()[:20][::-1]
    context = {"picture_list": picture_list}
    return render(request, "pictures/home.html", context)


def create_view(request):
    form = PictureForm(
        data=request.POST or None, files=request.FILES or None
    )

    if request.method == "GET":
        context = {"form": form}
        return render(request, "pictures/create.html", context)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("pictures:home")
        context = {"form": form}
        return render(request, "pictures/create.html", context)


def edit_view(request, pk):
    queryset = Picture.objects.filter(pk=pk)
    if queryset.exists():
        picture = queryset.first()
    else:
        return redirect("pictures:home")

    form = PictureForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=picture,
    )

    if request.method == "GET":
        context = {"form": form}
        return render(request, "pictures/edit.html", context)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("pictures:home")
        context = {"form": form}
        return render(request, "pictures/edit.html", context)


def delete_view(request, pk):
    queryset = Picture.objects.filter(pk=pk)
    if queryset.exists():
        picture = queryset.first()
        picture.delete()
    return redirect("pictures:home")
