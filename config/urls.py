from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return redirect('/api/register/')  # Redirect to the registration page
                       
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]