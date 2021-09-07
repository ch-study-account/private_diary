from django.shortcuts import render

from django.views import generic
# Create your views here.
from .froms import InquiryForm

def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name = "diary/index.html"

class InquiryView(generic.FormView):
    template_name = 'diary/inquiry.html'
    from_class = InquiryForm