from django.shortcuts import render
from .forms import UserProfileAddForm


def UserProfileAddView(request):
    form = UserProfileAddForm()
    return render(request, 'profiles/add_form.html', {'form': form})


def UserProfile(request):
    form = UserProfileAddForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            form.save()
        else:
            msg = 'Error validating the form'

    return render(request, "profiles.html", {"form": form, "msg": msg})

