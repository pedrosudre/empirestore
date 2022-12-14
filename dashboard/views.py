from django.shortcuts import render
from orders.models import Order
from django.http import JsonResponse
from django.db.models import Sum
import datetime
type(datetime)


def dashboard(request):
    return render(request, "dashboard.html")


def retorna_total_vendido(request):
    total = Order.objects.all().aggregate(Sum('total'))['total__sum']
    if request.method == "GET":
        return JsonResponse({'total': total})


def relatorio_faturamento(request):
    x = Order.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.datetime.now().month + 1
    ano = datetime.datetime.now().year
    for i in range(1, 12): 
        mes -= 1
        
        y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)

