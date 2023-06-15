from django.urls import path

from .views import IndexView, LogoutView, CreateAccountView

app_name = 'login'

urlpatterns = [
   path('', IndexView.as_view(), name="login"),
   path('logout/', LogoutView.as_view(), name="logout"),
   path('create/', CreateAccountView.as_view(), name="create"),
]
