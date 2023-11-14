import stripe
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.


class StripePaymentView(TemplateView):
    template_name = './payment/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency='usd',
                source=token,
                description='Example charge',
            )
            # Handle successful charge and redirect to success page
            return HttpResponseRedirect(reverse('payment_success'))
        except stripe.error.StripeError as e:
            # Handle Stripe errors here, e.g., log the error
            return HttpResponseRedirect(reverse('payment_error'))



class PaymentErrorView(TemplateView):
    template_name = './payment/payment_error.html'

class PaymentSuccessView(TemplateView):
    template_name = './payment/payment_success.html'