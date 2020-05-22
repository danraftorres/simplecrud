from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from polls.models import Category, Article
from polls.forms import ArticleForm, CategoryForm
from django.contrib import messages

# Create your views here.


def article_create_view(request):

    context = {}

    if request.method == 'POST':

        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            #form.save()
            print(request.POST)
            print(request.FILES)
            try:
                article = Article()
                article.name = request.POST['name']
                article.description = request.POST['description']
                article.price = request.POST['price']

                """
                Si contiene la imagen también la creamos
                """
                if len(request.FILES) != 0:
                    article.image = request.FILES['image']

                category = Category.objects.get(id=request.POST['category'])
                article.category = category

                article.save()

                messages.success(request, 'Has been saved successfully')
            except Exception as e:
                print(e)
                messages.error(request, 'An error has occurred')

            return redirect('polls:article-list')

        # return HttpResponseRedirect(reverse('polls:article-new'))
    else:
        form = ArticleForm()

        
    categories = Category.objects.all()

    context['categories'] = categories
    context['form'] = form

    return render(request, 'polls/articles/create.html', context)


def article_list_view(request):

    articles = Article.objects.all().order_by('id')

    context = {
        'articles': articles
    }

    return render(request, 'polls/articles/list.html', context)


def article_edit_view(request, id):

    article = get_object_or_404(Article, id=id)
    categories = Category.objects.all()

    context = {'article': article, 'categories': categories}

    return render(request, 'polls/articles/edit.html', context)


def article_udpate_view(request, id):

    if request.method == 'POST':

        try:
            article = Article.objects.get(id=id)
            article.name = request.POST['name']
            article.description = request.POST['description']
            article.price = request.POST['price']

            '''
            Si contiene la imagen también la actualizamos
            '''
            if len(request.FILES) != 0:
                article.image = request.FILES['image']

            category = Category.objects.get(id=request.POST['category_id'])
            article.category = category

            article.save()

            messages.success(request, 'Has been updated successfully')

            return redirect('polls:article-list')
        except Exception as e:
            print(e)
            messages.error(request, 'An error has ocurred')

            return redirect('polls:article-edit', id=article.id)

    else:
        return render(request, 'polls/articles/edit.html')


def article_delete_view(request, id):

    article = get_object_or_404(Article, id=id)

    context = {'article': article}

    return render(request, 'polls/articles/delete.html', context)
