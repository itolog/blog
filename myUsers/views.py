from django.shortcuts import render, redirect

from .forms import userFormReg
from django.contrib import messages
# Create your views here.

def regUser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = userFormReg(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            username = form.cleaned_data.get("username")
            # pass1 = form.cleaned_data.get("pass1")
            # pass2 = form.cleaned_data.get("pass2")
            # redirect to a new URL:

            form.save()
            messages.success(request, f'пользователь {username} добавлен')
            return redirect('home')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = userFormReg()
    return render(request, 'myUsers/reg.html', {'form': form, 'title': 'Регистрация'})