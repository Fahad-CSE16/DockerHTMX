from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostPhotosForm
from .models import PostPhotos, Post


def create_photos(request, id):
    print(id)
    post = Post.objects.get(id=id)
    photos = PostPhotos.objects.filter(post=post)
    form = PostPhotosForm()
    if request.method == "POST":
        print("debug1")
        form=PostPhotosForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.post=post
            obj.save()
            return redirect("detail_photo", id=obj.id)
        else:
            return render(request, "socialpost/photo_form.html", context={
                "form": form
            })

    context = {
        "form": form,
        "post": post,
        "photos": photos
    }

    return render(request, "socialpost/add_image.html", context)

def create_photo_form(request):
    form = PostPhotosForm()
    context = {
        "form": form
    }
    return render(request, "socialpost/photo_form.html", context)

def update_photo(request, id):
    photo = PostPhotos.objects.get(id=id)
    form = PostPhotosForm(request.POST or None,request.FILES, instance=photo)

    if request.method == "POST":
        form = PostPhotosForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("detail_photo", id=photo.id)
    context = {
        "form": form,
        "photo": photo
    }

    return render(request, "socialpost/photo_form.html", context)


def delete_photo(request, id):
    photo = get_object_or_404(PostPhotos, id=id)

    if request.method == "POST":
        photo.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_photo(request, id):
    photo = get_object_or_404(PostPhotos, id=id)
    context = {
        "photo": photo
    }
    return render(request, "socialpost/photo_details.html", context)

