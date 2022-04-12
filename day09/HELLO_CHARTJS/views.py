from django.shortcuts import render
from HELLO_CHARTJS.daostock import DaoStock
from django.http.response import JsonResponse

def chartjs(request):
    return render(request, 'chartjs.html')


def axios_snames(request):
    ds = DaoStock()
    snames = ds.getSNames()
    prices = []
    
    for i in snames :
        prices.append(ds.getPrices(i['s_name']))
    
    myjson = {'snames' : snames,
              'prices' : prices}
    return JsonResponse(myjson)