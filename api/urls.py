from django.urls import path
from api.views import CreateAPI

urlpatterns = [
    path('hello/', CreateAPI.as_view())
]