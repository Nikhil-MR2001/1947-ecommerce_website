from django.urls import path
from . import views

app_name = 'payment'



urlpatterns = [
    path('payment/', views.StripePaymentView.as_view(), name='stripe_payment'),
    path('payment/success/', views.PaymentSuccessView.as_view(), name='payment_success'),
    path('payment/error/', views.PaymentErrorView.as_view(), name='payment_error'),
]