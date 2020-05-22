from django import forms
from polls.models import Article, Category


class ArticleForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(required=False)
    price = forms.DecimalField()
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())


    # name = forms.CharField()
    # description = forms.CharField()
    # price = forms.DecimalField()
    # image = forms.ImageField()
    # category = forms.ChoiceField()
    #category = forms.ModelChoiceField(queryset=Category.objects.all())

    # def __init__(self, *args, **kwargs):
    #     super(ArticleForm, self).__init__(*args, **kwargs)
    #     self.fields['category'].queryset = Category.objects.all()


# class ArticleModelForm(forms.ModelForm):
#     # categoryx = forms.ModelChoiceField(Category.objects)
#     def __init__(self, *args, **kwargs):
#         super(ArticleModelForm, self).__init__(*args, **kwargs)
#         self.fields['category'].queryset = Category.objects.all()[:1]

#     class Meta:
#         model = Article
#         fields = ('name', 'description', 'price', 'image', 'category')


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.CharField()


# class CategoryModelForm(forms.ModelForm):
#     namex = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'id': 'name'}))

#     class Meta:
#         model = Category
#         fields = ('name', 'description')
        # exclude = ['name']

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        # }
