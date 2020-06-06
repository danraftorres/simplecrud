from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from polls.models import Category, Article
from polls.forms import ArticleForm, CategoryModelForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.datastructures import MultiValueDictKeyError

#-------------------------------------
#              ARTICLES
#-------------------------------------
def article_create_view(request):

    context = {}

    if request.method == 'POST':

        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            # form.save()
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

    return render(request, 'create.html', context)


def article_list_view(request):

    articles = Article.objects.all().order_by('id')
    # 5 registros por pagina
    paginator = Paginator(articles, 5)

    '''
    Si no encuentra valor de page, pone por defecto 1
    '''
    #request.GET['page'] if 'page' in request.GET else 1
    page_number = request.GET.get('page', 1)

    '''
    Intentando con try catch

    try: 
        page_number = request.GET['page'] 
    except MultiValueDictKeyError: 
        page_number = 1

    page_number = request.GET.get('page', 1)
    '''

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger as e:
        print(e)
        page_obj = paginator.get_page(1)
    except EmptyPage as e:
        print(e)
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'list.html', context)


def article_edit_view(request, id):

    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if 'image' not in request.FILES:
            form.fields['image'].required = False
            image = False
        # print(request.POST)

        if form.is_valid():
            try:
                article.name = request.POST['name']
                article.description = request.POST['description']
                article.price = request.POST['price']

                if image:
                    article.image = request.FILES['image']

                category = Category.objects.get(id=request.POST['category'])
                article.category = category

                article.save()
                print(request.FILES)

                messages.success(request, 'Has been updated successfully')

                return redirect('polls:article-list')
            except Exception as e:
                print(e)
                message.error(request, 'An error has ocurred')

                return redirect('polls:article-edit', id=article.id)
            # print(request.POST)
    else:
        form = ArticleForm()

    categories = Category.objects.all()

    context = {
        'article': article,
        'categories': categories,
        'form': form
    }

    return render(request, 'edit.html', context)


def article_delete_view(request, id):

    article = get_object_or_404(Article, id=id)

    print(article)

    if request.method == 'POST':
        article.delete()

        messages.success(request, 'Has been deleted item')
        return redirect('polls:article-list')
    else:
        context = {'article': article}

    return render(request, 'delete.html', context)

#---------------------------------
#       CATEGORIES
#---------------------------------
def category_list_view(request):
    return render(request, 'polls/categories/list.html')


def category_create_view(request):


    if request.method == 'POST':
        form = CategoryModelForm(request.POST)

        print(request.POST)

        if form.is_valid():
            print(f'POST ------------>{request.POST}')
        else:
            print(form)

        
        #return redirect('polls:category-create')
    else:
        form = CategoryModelForm()

    context = {
        'form': form
    }

   


    return render(request, 'polls/categories/create.html', context)