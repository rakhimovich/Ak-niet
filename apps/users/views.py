from django.views.generic import CreateView, UpdateView, DetailView
from apps.users.forms import UserForm, UserUpdateForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = '/user/2'
    template_name = 'update_user.html'


class UserDetailView(DetailView):
    model = User
    pk_url_kwarg = 'pk'
    template_name = 'user_detail.html'
    
