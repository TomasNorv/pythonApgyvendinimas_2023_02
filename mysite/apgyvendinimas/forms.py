from .models import ObjektasReview, Profilis
from django import forms
from django.contrib.auth.models import User
class ObjektasReviewForm(forms.ModelForm):
    class Meta:
        model = ObjektasReview
        fields = ('content', 'objektas', 'reviewer',)
        widgets = {'objektas': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}

class UserUpdateForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['foto']