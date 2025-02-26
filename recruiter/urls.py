from django.urls import path
from . import views

urlpatterns = [
    path('candidates/', views.CandidateListView.as_view(), name='candidate-list'),
    path('candidate_create/', views.CandidateCreateView.as_view(), name='candidate-create'),
    path('candidate_update/<int:id>/', views.CandidateUpdateView.as_view(), name='candidate-update'),
    path('candidate_delete/<int:id>/', views.CandidateDeleteView.as_view(), name='candidate-delete'),
]

