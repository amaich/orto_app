from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.http import require_POST


from .models import Clients
from .forms import ClientsForm, VisitsForm


class ClientsListView(ListView):
    model = Clients
    template_name = 'clients/clients_list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Clients
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'


class ClientCreateView(CreateView):
    form_class = ClientsForm
    template_name = 'clients/client_create.html'
    success_url = reverse_lazy('clients:clients_list')


class ClientUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm
    template_name = 'clients/client_update.html'
    context_object_name = 'client'

    def get_success_url(self):
        return reverse('clients:client_detail', kwargs={'pk': self.object.id})


class ClientDeleteView(View):
    def get(self, request, pk):
        client_to_delete = get_object_or_404(Clients, pk=pk)
        client_to_delete.delete()
        return HttpResponseRedirect(reverse('clients:clients_list'))


class ClientSearchView(ListView):
    model = Clients
    template_name = 'clients/client_search.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Clients.objects.filter(fullname__icontains=self.request.GET.get('name'))

    def get_context_data(self, **kwargs):
        context = super(ClientSearchView, self).get_context_data(**kwargs)
        context['find_name'] = self.request.GET.get('name')
        return context


@require_POST
def visit_create(request, client_id):
    client = get_object_or_404(Clients,
                               id=client_id)

    visit = None
    form = ClientsForm(data=request.POST)
    if form.is_valid():
        visit = form.save(commit=False)
        visit.client = client
        visit.save()
    return render(request,
                  'clients/visit_create.html',
                  {'client': client, 'visit': visit, 'form': form})
