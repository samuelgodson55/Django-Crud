from django import forms
from .models import Post

class blogAppForm(forms):
    class Meta:
        models = Post
        fields = "__all__"
        