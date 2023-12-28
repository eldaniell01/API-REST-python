from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json
# Create your views here.

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get(self, request, id=0):
        if id>0:
            company = list(Company.objects.filter(id=id).values())
            if len(company)>0:
                comp = company[0]
                data={'message': 'completado', 'companies': comp}
            else:
                data={'message': 'no completado'}
                
        else: 
            companies = list(Company.objects.values())
            if len(companies)>0:
                data={'message': 'completado', 'companies': companies}
            else:
                data={'message': 'no completado'}
        return JsonResponse(data)
    
    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'], website=jd['website'], fundation=jd['fundation'])
        data={'message':'completado'}
        return JsonResponse(data)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        if id>0:
            company = list(Company.objects.filter(id=id).values())
            if len(company)>0:
                comp = Company.objects.get(id=id)
                comp.name=jd['name']
                comp.website=jd['website']
                comp.fundation=jd['fundation']
                comp.save()
                data={'message':'completado'}
            else:
                data={'message': 'no completado'}
        return JsonResponse(data)
    
    def delete(self, request, id):
        company = list(Company.objects.filter(id=id).values())
        if len(company)>0:
            Company.objects.filter(id=id).delete()
            data={'message':'completado'}
        else:
            data={'message': 'no completado'}
        return JsonResponse(data)