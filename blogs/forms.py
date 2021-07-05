from django import forms
from django.forms import widgets
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'author', 'category', 'image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.ImageField(),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
