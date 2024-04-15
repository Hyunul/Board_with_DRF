from django import forms

class BoardForm(forms.Form): #내가 만든 앱 이름은 articles니까 ArticleForm으로 만들었음
    title = forms.CharField(max_length=15)
    content = forms.CharField(widget=forms.Textarea)