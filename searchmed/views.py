from django.shortcuts import render
from django.http import JsonResponse
from .models import Med

# Create your views here.
def home(request) :
	return render(request, 'searchmed/home.html', {})

def combine(request) :
    return render(request, 'searchmed/combine.html', {})

def age(request) :
    return render(request, 'searchmed/age.html', {})

def check_medicine(request):
    product_name = request.GET.get('product_name')
    medicines = Med.objects.filter(product_name__icontains=product_name)  # 수정된 부분
    medicines_list = medicines.values('id', 'product_name', 'compound_name', 'compound_code', 'product_code', 'company_name')
    return JsonResponse({'medicines': list(medicines_list)}) #이 코드는 medicines라는 키로 의약품 리스트를 JSON 형태로 반환하게 됩니다. 따라서 프론트엔드에서 이 데이터를 받을 때, data.medicines로 접근하면 해당 의약품 리스트를 가져올 수 있습니다.