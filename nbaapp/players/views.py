from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters, permissions
from .models import Player
from .serializers import PlayerSerializer
import datetime

# Create your views here.
class PlayerView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer
    permission_classes = [permissions.AllowAny]

    # old way
    #queryset = Player.objects.all()
    # if 'search' in request.query_params:
    #     filter_backends = [filters.SearchFilter]
    #     search_fields = ['^last_name', '^college']
    # else:
    #     filter_backends = [DjangoFilterBackend]
    #     filterset_fields = ['start_year', 'end_year', 'height', 'weight']

    def get_queryset(self):
        queryset = Player.objects.all()

        search_phrase_college = self.request.query_params.get('search_college', None)
        search_phrase_name = self.request.query_params.get('search_name', None)
        if search_phrase_name or search_phrase_college:
            if search_phrase_name:
                if search_phrase_college:
                    queryset = queryset.filter(last_name__startswith=search_phrase_name, college__startswith=search_phrase_college)
                else:
                    queryset = queryset.filter(last_name__startswith=search_phrase_name)
            else:
                queryset = queryset.filter(college__startswith=search_phrase_college)
        #else:
        from_weight = self.request.query_params.get('from_weight', None)
        to_weight = self.request.query_params.get('to_weight', None)

        if from_weight:
            if to_weight:
                queryset = queryset.filter(weight__gte=from_weight, weight__lte=to_weight)
            else:
                queryset = queryset.filter(weight__gte=from_weight, weight__lte=350)
        else:
            if to_weight:
                queryset = queryset.filter(weight__gte=150, weight__lte=to_weight)

        from_height = self.request.query_params.get('from_height', None)
        to_height = self.request.query_params.get('to_height', None)

        if from_height:
            if to_height:
                queryset = queryset.filter(height__gte=from_height, height__lte=to_height)
            else:
                queryset = queryset.filter(height__gte=from_height, height__lte=100)
        else:
            if to_height:
                queryset = queryset.filter(height__gte=50, height__lte=to_height)

        start_year = self.request.query_params.get('start_year', None)
        end_year = self.request.query_params.get('end_year', None)

        if start_year:
            if end_year:
                queryset = queryset.filter(start_year__gte=start_year, end_year__lte=end_year)
            else:
                queryset = queryset.filter(start_year__gte=start_year, end_year__lte=2019)
        else:
            if end_year:
                queryset = queryset.filter(start_year__gte=1930, end_year__lte=end_year)

        from_age = self.request.query_params.get('from_age', None)
        to_age = self.request.query_params.get('to_age', None)

        if from_age:
            if to_age:
                from_date = datetime.datetime.now() - datetime.timedelta(days=int(to_age)*365)
                to_date = datetime.datetime.now() - datetime.timedelta(days=int(from_age)*365)
                queryset = queryset.filter(birthday__gte=from_date, birthday__lte=to_date)
            else:
                from_date = datetime.datetime.now() - datetime.timedelta(days=70*365)
                to_date = datetime.datetime.now() - datetime.timedelta(days=int(from_age)*365)
                queryset = queryset.filter(birthday__gte=from_date, birthday__lte=to_date)
        else:
            if to_age:
                from_date = datetime.datetime.now() - datetime.timedelta(days=int(to_age)*365)
                to_date = datetime.datetime.now() - datetime.timedelta(days=18*365)
                queryset = queryset.filter(birthday__gte=from_date, birthday__lte=to_date)

        return queryset.order_by('last_name')