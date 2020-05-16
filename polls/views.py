from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Category, Article
from django.contrib import messages

# Create your views here.
def article_new(request):

    if request.method == 'POST':
        try:

            category = Category.objects.get(id=request.POST['category_id'])

            article = Article(name=request.POST['name'], 
                            description=request.POST['description'],
                            quantity=request.POST['quantity'], 
                            image=request.FILES['image'], 
                            category=category)

       
            article.save()

            messages.success(request, 'Has been saved successfully')
        except Exception as e:
            print(e)
            messages.error(request, 'An error has occurred')

        return redirect('polls:article-new')
        #return HttpResponseRedirect(reverse('polls:article-new'))
    else:
        categories = Category.objects.all()

        context = {
            'categories': categories
        }

        return render(request, 'polls/article/create.html', context)


def article_list(request):

    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'polls/article/list.html', context)
