from .models import Comment
from django import forms
from allauth.account.forms import SignupForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        pass
    pass

