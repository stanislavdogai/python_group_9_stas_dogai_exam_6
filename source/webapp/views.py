from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import BookForm
from webapp.models import FaceBook


def home_page(request):
    books = FaceBook.objects.order_by("created_at")
    return render(request, 'home.html', {'books': books})

def create_book_view(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'book_create.html', {"form": form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            name_author = form.cleaned_data.get('name_author')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            status = form.cleaned_data.get('status')
            created_at = form.cleaned_data.get('publish_date')
            new_book = FaceBook.objects.create(name_author=name_author,
                                                 email=email,
                                                 text=text,
                                                 status=status,
                                                 created_at=created_at)
            return redirect("home_page")
        return render(request, 'book_create.html', {"form": form})


def book_update(request, pk):
    book = get_object_or_404(FaceBook, pk=pk)
    if request.method == 'GET':
        form = BookForm(initial={
            'name_author': book.name_author,
            'email': book.email,
            'text': book.text,
        })
        return render(request, 'book_update.html', {"book": book, "form": form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.name_author = form.cleaned_data.get('name_author')
            book.email = form.cleaned_data.get('email')
            book.text = form.cleaned_data.get('text')
            book.save()
            return redirect("home_page")
        return render(request, 'book_update.html', {"book": book, "form": form})

# def book_delete(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'GET':
#         form = ArticleDeleteForm()
#         return render(request, "article_delete.html", {"article": article, "form": form})
#     else:
#         form = ArticleDeleteForm(data=request.POST)
#         if form.is_valid():
#             if form.cleaned_data.get("title") != article.title:
#                 form.errors['title'] = ["Название статьи не соответствует"]
#                 return render(request, "article_delete.html", {"article": article, "form": form})
#             article.delete()
#             return redirect("index")
#         return render(request, "article_delete.html", {"article": article, "form": form})