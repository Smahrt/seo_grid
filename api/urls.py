from django.urls import path
from . import views

urlpatterns = [
	path('campaign/', views.CampaignView.as_view(), name='campaign'),
	path('campaign/<int:pk>/', views.CampaignView.as_view(), name='campaign-user-id'),
]