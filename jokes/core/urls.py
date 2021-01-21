from django.urls import path
from .views import homepage, specific_joke, all_jokes, redirect_to_specific_joke, jokes_by_language, new_joke


urlpatterns = [
    path("", homepage),
    path("homepage/", homepage),
    path("i/want/to/see/jokes/", homepage),

    path("jokes/all/", all_jokes),
    path("joke/<int:joke_id>/", specific_joke, name="specific-joke"),
    path("joke/by-language/<slug:language>/", jokes_by_language),
    path("jokes/<int:joke_id>/", redirect_to_specific_joke),


    path("jokes/new/", new_joke)
]
