from django.urls import path

from . import views, scraper

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('count', views.count, name='count'),
    path('show', scraper.show, name='show'),
    path('fetch', scraper.fetchTaipeiYouBikeAPIData, name='fatch'),
    path('fetchUbikeStopData', scraper.fetchUbikeStopDataFromAPI, name='fetchUbikeStopDataFromAPI'),
    path('fetchStopStatusData', scraper.fetchStopStatusDataFromAPI, name='fetchStopStatusDataFromAPI'),
    path('fetchAutoWeatherDataFromAPI', scraper.fetchAutoWeatherDataFromAPI, name='fetchAutoWeatherDataFromAPI'),
    path('fetchAutoWeatherStationFromAPI', scraper.fetchAutoWeatherStationFromAPI, name='fetchAutoWeatherStationFromAPI'),
    path('fetchAutoRainDataFromAPI', scraper.fetchAutoRainDataFromAPI, name='fetchAutoRainDataFromAPI'),
    path('fetchAutoRainStationFromAPI', scraper.fetchAutoRainStationFromAPI, name='fetchAutoRainStationFromAPI'),
    path('fetchBureauWeatherDataFromAPI', scraper.fetchBureauWeatherDataFromAPI, name='fetchBureauWeatherDataFromAPI'),
    path('fetchBureauWeatherStationFromAPI', scraper.fetchBureauWeatherStationFromAPI, name='fetchBureauWeatherStationFromAPI'),
    path('showData', scraper.showData, name='showData'),
]
