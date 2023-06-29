from .models import UserComment, TipComments
from django import forms


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('body',)


class TipCommentForm(forms.ModelForm):
    class Meta:
        model = TipComments
        fields = ('body',)
