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
            return redirect("detail-book", id=obj.id)
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

def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("detail-book", id=book.id)

    context = {
        "form": form,
        "book": book
    }

    return render(request, "partials/book_form.html", context)


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_book(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)

