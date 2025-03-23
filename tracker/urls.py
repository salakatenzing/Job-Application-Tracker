from django.urls import path
from .views import RegisterView
from .views import JobApplicationListCreateView, JobApplicationRetrieveUpdateDestroyView

urlpatterns = [
    path('applications/', JobApplicationListCreateView.as_view(), name='jobapplication-list-create'),
    path('applications/<int:pk>/', JobApplicationRetrieveUpdateDestroyView.as_view(), name='jobapplication-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]
