from django.shortcuts import render
from rest_framework import viewsets
from .serislizers import MovieSerializer
from .models import Moviedata


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer



# Create your views here.
