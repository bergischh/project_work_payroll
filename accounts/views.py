from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signup_view(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect setelah berhasil signup
    template_name = 'registration/signup.html'  # Template bawaan dari Django
