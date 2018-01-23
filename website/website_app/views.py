from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'launchsite_app/index.html')

def workers(request):
    return render(request, 'launchsite_app/workers.html')


def contact(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ContactForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            to_email = form.cleaned_data['contact_to']
            name = form.cleaned_data['contact_name']
            from_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']

            subject = "Message from {}".format(name)

            send_mail(
                subject,
                content,
                from_email,
                [to_email],
                fail_silently=False,
            )

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contact_success'))


    # If this is a GET (or any other method) create the default form.
    else:
        form = ContactForm()

    #Also catches the 'form is invalid' case
    return render(request, 'launchsite_app/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'launchsite_app/contact_success.html')

