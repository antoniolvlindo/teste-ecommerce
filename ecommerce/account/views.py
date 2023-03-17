from django.shortcuts import redirect, render

from .forms import CreateUserForm


def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')

    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)


def email_verification(request):
    pass


def email_verification_sent(request):
    pass


def email_verification_success(request):
    pass


def email_verification_fail(request):
    pass
