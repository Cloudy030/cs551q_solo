from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Game

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    address = forms.CharField()

    # class Meta:cs551q_solo/games/__pycache__

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 
        'address', 'first_name', 'last_name', )

class GameForm (forms.ModelForm):
    name= forms.CharField(max_length=200)

    class Meta:
        model = Game
        fields = ('name',)

GAME_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 30)]

class BasketAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=GAME_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
