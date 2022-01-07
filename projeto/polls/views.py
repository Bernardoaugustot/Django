from django.views.generic import DetailView, ListView
from .models import polls
# view, genericas feitas por class.

class PostListView(ListView):
    model = polls

class PostDetailView(DetailView):
    model = polls