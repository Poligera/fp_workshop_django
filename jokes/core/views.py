from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Joke, Language, ToldJoke
from .forms import JokeForm


# MVC
# Models Views Controllers
# Django
# MVC Models == models.py
# MVC Views == templates/
# MVC Controllers = views.py

# TODO:
# [x] New Joke Form
# [x] User Creation Form
# Login
# Logout
# Login required
# request.user

# If time, new model to be interacted with button
# Tests
# Extensions

def homepage(request):
    return HttpResponse("Welcome to our jokes page")


def all_jokes(request):
    template_dictionary = {
        'jokes': Joke.objects.all()
    }
    return render(request, "core/all_jokes.html", template_dictionary)


@csrf_exempt
def specific_joke(request, joke_id):
    if Joke.objects.filter(id=joke_id).exists():
        joke = Joke.objects.get(id=joke_id)
        context = {
            'joke': joke
        }

        if request.method == 'POST':
            print("Received POST")            
            payload = json.loads(request.body)
            if request.user.is_authenticated:
                if "tell_joke" in payload:
                    ToldJoke.objects.create(
                        user=request.user,
                        joke=joke
                    )
                    return HttpResponse("Thanks for telling this joke")

        if request.user.is_authenticated:
            if ToldJoke.objects.filter(
                user=request.user,
                joke=joke
            ).exists():
                context['already_told_joke'] = True


        return render(request, "core/specific_joke.html", context)

    else:
        return HttpResponse("Sorry, no joke with that ID exists")


def jokes_by_language(request, language):
    capitalised_language = language.capitalize()
    if not Language.objects.filter(name=capitalised_language).exists():
        return HttpResponse("Sorry, no language with that name exists")
    language = Language.objects.get(name=capitalised_language)
    jokes = Joke.objects.filter(language=language)
    values_dictionary = {
        'language': language,
        'jokes': jokes
    }
    return render(request, "core/jokes_by_language.html", values_dictionary)


def redirect_to_specific_joke(request, joke_id):
    return redirect('specific-joke', joke_id=joke_id)


@login_required
def new_joke(request):

    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            new_joke = form.save()
            return redirect('specific-joke', joke_id=new_joke.id)
        else:
            # Give the user a helpful error message
            print(form.errors)
    else:
        form = JokeForm()
    
    context = {
        'form': form
    }

    return render(request, "core/new_joke.html", context)
