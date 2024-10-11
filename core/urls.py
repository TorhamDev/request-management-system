from django.contrib import admin
from django.urls import path
from providers.views import ProvidersView, RequestsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("provider/", ProvidersView.as_view()),
    path("request/", RequestsView.as_view()),
]
