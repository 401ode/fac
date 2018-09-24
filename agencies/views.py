from django.shortcuts import render
from django.views.generic import ListView
from .models import FederalAgency, StateAgency, SubRecipient


class FederalAgencyListView(ListView):
    model = FederalAgency
    template_name = 'agencies/home.html'
    context_object_name = 'all_feds_list'
