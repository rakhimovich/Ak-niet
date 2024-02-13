from django.urls import path
from apps.users.views import SignUpView,UserUpdateView, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update-user/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
]