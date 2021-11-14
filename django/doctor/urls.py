from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, PhysiciansTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("physicians-page/", PhysiciansTemplateView.as_view(), name="physicians"),
]
