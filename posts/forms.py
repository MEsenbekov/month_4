from django import forms
from posts.models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == "python":
            raise forms.ValidationError("Такое название недопустимо")
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        image = cleaned_data.get('image')

        if title and content and title.lower() == content.lower():
            raise forms.ValidationError("Тайтл и контент должны различаться")

        return cleaned_data
