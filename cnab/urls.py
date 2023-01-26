from django.urls import path
from .views import UploadCnabView

urlpatterns = [
    path("cnab/", UploadCnabView.as_view(), name="cnab"),
]
