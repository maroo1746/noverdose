from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseForbidden
from .models import Med, Medcontraindication, UserMedication
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import ctypes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import numpy as np

# Load the shared library
med_db_lib = ctypes.CDLL('./libs/med_db.so')

# Create your views here.
def home_view(request) :
	return render(request, 'searchmed/home.html', {})

def combine_view(request) :
    return render(request, 'searchmed/combine.html', {})

def add_med_user_view(request) :
    return render(request, 'searchmed/add_med_user.html', {})

def add_med_user(request) :
    return render(request, 'searchmed/add_med_user.html', {})

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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 선택적: 회원가입 후 자동 로그인
            return redirect('searchmed:home')  # 회원가입 후 이동할 페이지
    else:
        form = UserCreationForm()

    return render(request, 'searchmed/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'searchmed/login.html'

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('searchmed:addinfo')
        return reverse_lazy('searchmed:home')

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
    
@login_required
def user_med_view(request):
    # 로그인 여부 확인 (옵션)
    if not request.user.is_authenticated:
        return redirect('searchmed:login')

    return render(request, 'searchmed/user_med.html')


def add_medicine(request):
    if request.method == 'POST':
        med_id =request.POST.get('med_id')
        med = Med.objects.get(id=med_id)

        medication_exists = UserMedication.objects.filter(
            user=request.user, 
            med=med
        ).exists()

        if medication_exists:
            return JsonResponse({
                'status': 'error', 
                'message': '이미 추가된 약품입니다. You have already added this medication.'
            }, status=400)

        UserMedication.objects.create(user=request.user, med=med)
        return JsonResponse({'status': 'success', 'message': 'Medication added successfully.'})
    
    # POST 요청이 아닌 경우 오류 메시지를 담은 JsonResponse를 반환합니다.
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)  
    

@login_required
def get_user_medications(request):
    user_medications = UserMedication.objects.filter(user=request.user).select_related('med')
    medications_list = [
        {
            'product_name': user_med.med.product_name,
            'compound_name': user_med.med.compound_name,
            'compound_code': user_med.med.compound_code,
            'product_code': user_med.med.product_code,
            'company_name': user_med.med.company_name,
            
        }
        for user_med in user_medications
    ]
    return JsonResponse({'medications': medications_list})

@login_required
def get_user_contraindications(request):
    user_medications = UserMedication.objects.filter(user=request.user).select_related('med')
    med_id_list = [
        {'id': user_med.med.id,
         'product_name': user_med.med.product_name,
        }
        for user_med in user_medications
    ]

    data = []
    for i in range(0, len(med_id_list)) :
        if (i < len(med_id_list) -1):
            for j in range (i+1, len(med_id_list)):
                medA_id = med_id_list[i]['id']
                medB_id = med_id_list[j]['id']
                results = Medcontraindication.objects.filter(
                    Q(med_id_a=medA_id, med_id_b=medB_id) | Q(med_id_a=medB_id, med_id_b=medA_id)
                    )
        
                for r in results:
                    data.append({
                        'med_a': med_id_list[i]['product_name'],
                        'med_b': med_id_list[j]['product_name'],
                        'contraindicated_info': r.contraindicated_info,
                        'notification_no': r.notification_no,
                        'notification_date': r.notification_date.strftime('%Y-%m-%d'),
                        'detail_info': r.detail_info
                    })

    return JsonResponse(data, safe=False)                 
                

