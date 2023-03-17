from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # fazendo email ser obrigatorio
        self.fields['email'].required = True


# Validação do email

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Esse email é invalido.')

        if len(email) >= 350:
            raise forms.ValidationError("Seu email e muito longo.")

        return email
