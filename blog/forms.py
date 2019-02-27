from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="请写下你的评论", widget=forms.Textarea(attrs={'placeholder': '可使用markdown语法发表你的评论'}))
    class Meta:
        model = Comment
        fields = ('body',)
        

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '双击 Shift 启用搜索'}))    