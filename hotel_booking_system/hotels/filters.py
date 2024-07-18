from rest_framework import viewsets, filters
from django.db.models import Q

class MultiFieldSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_fields = request.query_params.get('search', '')
        if not search_fields:
            return queryset

        search_terms = search_fields.split()
        query = Q()
        for term in search_terms:
            query |= Q(name__icontains=term) | Q(address__icontains=term) | Q(city__icontains=term)
        
        return queryset.filter(query)
            
