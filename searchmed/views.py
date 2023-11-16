from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseForbidden
from .models import Med, Medcontraindication
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import ctypes

# Load the shared library
med_db_lib = ctypes.CDLL('./libs/med_db.so')

# Create your views here.
def home_view(request) :
	return render(request, 'searchmed/home.html', {})

def combine_view(request) :
    return render(request, 'searchmed/combine.html', {})

def age_view(request) :
    return render(request, 'searchmed/age.html', {})

def check_medicine(request):
    product_name = request.GET.get('product_name')
    if product_name:
        medicines = Med.objects.filter(product_name__icontains=product_name)
    else:
        medicines = Med.objects.none()
    medicines_list = medicines.values('id', 'product_name', 'compound_name', 'compound_code', 'product_code', 'company_name')
    return JsonResponse({'medicines': list(medicines_list)})

def check_contraindication(request):
    medA_id = request.GET.get('medA_id')
    medB_id = request.GET.get('medB_id')
    if medA_id and medB_id:
        results = Medcontraindication.objects.filter(
            Q(med_id_a=medA_id, med_id_b=medB_id) | Q(med_id_a=medB_id, med_id_b=medA_id)
        )
    else:
        results = Medcontraindication.objects.none()
    
    data = []
    for r in results:
        data.append({
            'contraindicated_info': r.contraindicated_info,
            'notification_no': r.notification_no,
            'notification_date': r.notification_date.strftime('%Y-%m-%d'),
            'detail_info': r.detail_info
        })

    return JsonResponse(data, safe=False)

@login_required
def addinfo_view(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")

    if request.method == 'GET':
        return render(request, 'searchmed/addinfo.html')

    elif request.method == 'POST':
        product_name = request.POST.get('product_name')
        compound_name = request.POST.get('compound_name')
        compound_code = request.POST.get('compound_code')
        product_code = request.POST.get('product_code')
        company_name = request.POST.get('company_name')

        med_db_lib.insert_into_med_db(product_name.encode('utf-8'), compound_name.encode('utf-8'), compound_code.encode('utf-8'), product_code.encode('utf-8'), company_name.encode('utf-8'))

        return redirect('searchmed:addinfo')
    
    else:
        return HttpResponse("Unsupported HTTP method.")


