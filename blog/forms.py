from django import forms
from blog.models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'vs_or_not', 'side_1', 'side_2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']