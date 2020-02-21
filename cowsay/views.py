from django.shortcuts import render
from cowsay.models import History
from cowsay.forms import MooForm
import subprocess


def Cow_Form(request):
    html = "homepage.html"

    if request.method == 'POST':
        form = MooForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            word = data['text']
            avatar = data['choice']

            History.objects.create(
                text=word
            )

            with open('avatars.txt', 'w') as wf:
                subprocess.run(['cowthink',
                                '-f', f'{avatar}.cow',
                                f'{word}'], stdout=wf, text=True,)

            with open('avatars.txt') as f:
                cowthink = f.readlines()

                form = MooForm()

                return render(request, html, {
                        'form': form,
                        'cowthink': cowthink
                        })

    form = MooForm()

    return render(request, html, {'form': form})


def history(request):

    moose = History.objects.order_by("-date")[:10]
    print(type(moose))

    return render(request, "history.html", {"moose": moose})
