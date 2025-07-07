from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Jacket
from .forms import JacketForm

class JacketListView(ListView):
    model = Jacket
    template_name = 'jackets/jacket_list.html'
    context_object_name = 'jackets'

class JacketDetailView(DetailView):
    model = Jacket
    template_name = 'jackets/jacket_detail.html'

class JacketCreateView(CreateView):
    model = Jacket
    form_class = JacketForm
    template_name = 'jackets/jacket_form.html'
    success_url = reverse_lazy('jacket_list')

class JacketUpdateView(UpdateView):
    model = Jacket
    form_class = JacketForm
    template_name = 'jackets/jacket_form.html'
    success_url = reverse_lazy('jacket_list')

class JacketDeleteView(DeleteView):
    model = Jacket
    template_name = 'jackets/jacket_confirm_delete.html'
    success_url = reverse_lazy('jacket_list')
