from django.shortcuts import render
from .models import med_list
# Create your views here.
def home_view(request) :
	return render(request, 'searchmed/home.html', {})

def combine_view(request) :
    context={
         "meds_list": med_list.objects.all()
    }

    if request.method == "POST":
        drug_a = request.POST.get('drug_a')
        drug_b = request.POST.get('drug_b')
        drug_a = med_list.objects.filter(product_name = drug_a)
        drug_b = med_list.objects.filter(product_name = drug_b)
        # import pdb; pdb.set_trace()
        is_contraindicated = drug_a.first().contraindicated.all().filter(product_name = drug_b.first())

        if(len(is_contraindicated) > 0):
            context["is_contraindicated"] = "True"
        else:
            context["is_contraindicated"] = "False"
        # print(drug_a)
        # print(drug_b)

    return render(request, 'searchmed/combine.html', context)

def age_view(request) :
    return render(request, 'searchmed/age.html', {})