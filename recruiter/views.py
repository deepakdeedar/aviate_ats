from django.db.models import Count, Q
from rest_framework import pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView
import re

from .models import Candidate
from .serializers import CandidateSerializer

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CandidateListView(APIView, StandardResultsSetPagination):
    def get(self, request):
        query = request.query_params.get('q', '').strip()
        query = re.sub(r'[^a-zA-Z0-9\s]', '', query)
        query = re.sub(r'\s+', ' ', query)

        if query:
            words = query.split()
            filters = Q()
            for word in words:
                filters |= Q(name__icontains=word)

            candidates = Candidate.objects.filter(filters)
            candidates = candidates.annotate(
                relevance=Count('name', filter=filters)
            ).order_by('-relevance')
        else:
            candidates = Candidate.objects.all()

        results = self.paginate_queryset(candidates, request, view=self)
        serializer = CandidateSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
class CandidateCreateView(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CandidateUpdateView(APIView):
    def put(self, request, id):
        try:
            candidate = Candidate.objects.get(pk=id)
        except Candidate.DoesNotExist:
            return Response({"error": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CandidateSerializer(candidate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CandidateDeleteView(APIView):
    def delete(self, request, id):
        try:
            candidate = Candidate.objects.get(pk=id)
            candidate.delete()
            return Response({"msg": "Candidate deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Candidate.DoesNotExist:
            return Response({"error": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)