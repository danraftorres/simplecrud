from django import forms
from polls.models import Article, Category


class ArticleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
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


class CategoryModelForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) #'id': 'name'
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def is_valid(self):
        result = super().is_valid()
        # loop on *all* fields if key '__all__' found else only on errors:
        print(f'self.erros---->{self.errors}')
        print(f'self.fields--->{self.fields}')
        for field in self.errors: #(self.fields if '__all__' in self.errors else self.errors):
            print(field)
            attrs = self.fields[field].widget.attrs
            print(f'attttrs  ---->{attrs}')
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result
        print(f'is valid--------->{result}')
    
    class Meta:
        model = Category
    #     fields = ('name', 'description')

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'})
        # }

