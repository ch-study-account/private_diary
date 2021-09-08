import logging
from django.urls import reverse_lazy
# from django.contrib import messages

from django.shortcuts import render

from django.views import generic
# Create your views here.
from .froms import InquiryForm

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name = "diary/index.html"

class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        # messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

