from .models import ObjektasReview
from django import forms

class ObjektasReviewForm(forms.ModelForm):
    class Meta:
        model = ObjektasReview
        fields = ('content', 'objektas', 'reviewer',)
        widgets = {'objektas': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}