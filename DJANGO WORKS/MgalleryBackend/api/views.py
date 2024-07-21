from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from api.models import Movie

from api.serializers import MovieSerializers



class MovieViewSetView(viewsets.ModelViewSet):

    serializer_class=MovieSerializers

    queryset=Movie.objects.all()

    model=Movie

    

