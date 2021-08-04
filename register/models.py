from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from django.conf import settings


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token,
                                 *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """

    print()
    print("QQQQQQQQQQQQQQQQQQQQ")
    print()

    subject = "Password Reset for {title}".format(title="Mapanare App")
    from_email = 'noreply@mapanare.es'
    to = [reset_password_token.user.email]

    text_content = "{}?token={}".format(reverse(
        'password_reset:reset-password-request'), reset_password_token.key)

    #url = settings.SITE_URL + "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    forgotten_url = settings.FRONT_URL + "/ForgottenPassword/"
    forgotten_url += reset_password_token.key

    html_content = render_to_string('register/forgotten_password_email.html',
                                    {'forgotten_url': forgotten_url})
    # plain_message = strip_tags(html_message)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()




    '''
    email_plaintext_message = "{}?token={}".format(reverse(
        'password_reset:reset-password-request'), reset_password_token.key)
    
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        # "noreply@mapanare.es",
        "mapanaredev@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
    '''

