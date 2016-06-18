from django.shortcuts import render

# Create your views here.
def sample_list(request):
    return render(request, 'ctl/sample_list.html', {})
