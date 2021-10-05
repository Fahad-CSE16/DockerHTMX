from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import (
    create_book,
    create_book_form,
    detail_book,
    update_book,
    delete_book
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/', include('socialpost.urls')),
    path('htmx/<int:id>/', create_book, name='create-book'),
    path('htmx/book/<int:id>/', detail_book, name="detail-book"),
    path('htmx/book/<int:id>/update/', update_book, name="update-book"),
    path('htmx/book/<int:id>/delete/', delete_book, name="delete-book"),
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)