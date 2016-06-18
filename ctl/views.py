from django.shortcuts import render
from django.utils import timezone
from .models import DataSample

# Create your views here.
def sample_list(request):
    datasamples = DataSample.objects.filter(sampled_date__lte=timezone.now()).order_by('sampled_date')

    return render(request, 'ctl/sample_list.html', {'datasamples': datasamples})




