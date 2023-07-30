from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)  # Show 10 jobs per page.
    page_number = request.GET.get("page")
    jobs_page_obj = paginator.get_page(page_number)
    context = {
        'jobs':jobs_page_obj
    }
    return render(request, 'job/job_list.html', context)

def job_detail(request, id):
    job_detail = Job.objects.get(id = id)
    context = {
        'job' : job_detail
    }
    return render(request, 'job/job_detail.html', context)

