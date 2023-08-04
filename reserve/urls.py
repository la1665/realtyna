from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'reserve'

urlpatterns = [
    path('check/<int:y>/<int:m>/<int:d>/', views.AvailableRoomsAPIView.as_view()),
    path('<int:res_id>', views.ReservationAPIView.as_view()),
    path('', views.AddReservationAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
