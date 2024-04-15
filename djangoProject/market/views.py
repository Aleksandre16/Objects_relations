from django.http import JsonResponse
from market.models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404


def get_books(request):
    books = Book.objects.all()
    data = [{'id': book.id, 'name': book.name, 'author': book.author, 'price': book.price} for book in books]
    return JsonResponse({'books': data})


def get_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        data = {
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'price': book.price,
            'page_count': book.page_count,
            'categories': [category.name for category in book.categories.all()],
            'image': book.image.url if book.image else None
        }
        return JsonResponse({'book': data})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)


def get_listedbooks(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  # Display 10 books per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'books.html', {'page_obj': page_obj})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
