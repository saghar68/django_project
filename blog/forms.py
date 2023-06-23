from django import forms
from .models import Post

class New_Post(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','text','status','about','author']
    


class Search_form(forms.Form):
    search=forms.CharField(max_length=20)
