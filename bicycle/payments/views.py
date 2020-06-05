import stripe 

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render 

stripe.api_key = settings.STRIPE_SECRET_KEY 

def index(request):
    return render(request,'index.html')


class HomePageView(TemplateView):
    template_name = 'Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): 
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')