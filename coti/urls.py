from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from coti import views
app_name = 'coti'

urlpatterns = [
    path('colors/', views.TColorList.as_view(), name='colors'),
    path('installations/', views.TInstallationList.as_view(), name='installations'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
