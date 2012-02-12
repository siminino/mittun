from django.views.generic import CreateView

from events.forms import BootstrapForm
from events.models import Event


class BootstrapView(CreateView):

    model = Event
    form_class = BootstrapForm
    template_name = 'event_form.html'
    success_url = '/'
