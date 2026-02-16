from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm


def book_list(request):
    books = Book.objects.select_related("author").all()
    return render(request, "books/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("books:book_detail", pk=book.pk)
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form, "action": "Create"})


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form, "action": "Update"})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("books:book_list")
    return render(request, "books/book_confirm_delete.html", {"book": book})


def author_list(request):
    authors = Author.objects.all()
    return render(request, "authors/author_list.html", {"authors": authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author)
    return render(
        request, "authors/author_detail.html", {"author": author, "books": books}
    )
