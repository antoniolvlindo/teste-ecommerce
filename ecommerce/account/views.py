from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render

from .forms import CreateUserForm
from .token import user_tokenizer_generate


def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')

    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)


# urls de verificação

def email_verification(request):
    pass


# urls de verificação enviado


def email_verification_sent(request):
    pass


# urls de verificação sucesso


def email_verification_success(request):
    pass


# urls de verificação falhou


def email_verification_fail(request):
    pass
