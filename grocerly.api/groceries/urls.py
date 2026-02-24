from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [path("grocery/", views.GroceryView.as_view(), name="grocery")]

urlpatterns = format_suffix_patterns(urlpatterns)
