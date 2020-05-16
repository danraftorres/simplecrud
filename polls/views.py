from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

# Create your views here.
def create_author_view(request):
    return render(request, 'polls/author/create.html', {})


def author_list_view(request):
    return render(request, 'polls/author/list.html', {})

def create_book_view(request):
    return render(request, 'polls/book/create.html', {})
