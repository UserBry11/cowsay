from django.shortcuts import render

from cowsay.forms import MooForm
import subprocess

User_text = []


def Cow_Form(request):
    html = "homepage.html"

    if request.method == 'POST':
        form = MooForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            word = data['text']
            avatar = data['choice']

            User_text.append(word)
            while len(User_text) > 10:
                User_text.pop(0)

            with open('avatars.txt', 'w') as wf:
                subprocess.run(['cowthink',
                                '-f', f'{avatar}.cow',
                                f'{word}'], stdout=wf, text=True,)

            with open('avatars.txt') as f:
                cowthink = f.readlines()

                form = MooForm()

                return render(request, html, {
                        'form': form,
                        'cowthink': cowthink})

    form = MooForm()

    return render(request, html, {'form': form})


def history(request):
    saying = ""

    if len(User_text) == 0:
        saying = "You gotta make the cow speak. You have 0 sayings"

    return render(request, "history.html", {
        "history": User_text,
        "saying": saying
        })
