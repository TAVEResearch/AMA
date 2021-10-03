from django import forms
from blog.models import Question, Top10, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'vs_or_not', 'side_1', 'side_2']

# class Top10Form(forms.ModelForm):
#     class Meta:
#         model = Top10
#         fields = ['question', 'grade', 'rank']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
