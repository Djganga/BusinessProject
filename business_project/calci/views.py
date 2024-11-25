from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from calci import models, serializers
from datetime import datetime, date, timedelta
# Create your views here.

# def get_balance(dictt):
#     ''' Not working, Need to check'''
#     dictt["balance_amount"] = str(float(dictt["bill_amount"]) - float(dictt["received_amount"]))
#     print(dictt["balance_amount"])
#     return dictt

@api_view(["GET","POST"])
def bill_info(request):
    if request.method == "GET":
        items = models.Ledger.objects.all()
        serializer = serializers.LedgerSerializer(items, many = True)
        return Response(serializer.data)
    if request.method == "POST":
        request.data["balance_amount"] = str(float(request.data["bill_amount"]) - float(request.data["received_amount"]))
        serializer = serializers.LedgerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

@api_view(["GET","PUT","DELETE"])
def particular_bill_info(request,pk):
    # print(datetime.now())
    try:
        itemm = models.Ledger.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.LedgerSerializer(itemm)
        return Response(serializer.data)
    if request.method == "PUT":
        request.data["balance_amount"] = str(float(request.data["bill_amount"]) - float(request.data["received_amount"]))
        # request.data['updated_date_time'] = str(datetime.now)
        serializer = serializers.LedgerSerializer(itemm, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        itemm.delete()
        return Response({"message":"Record deleted successfully."})

@api_view(['GET'])
def particular_day_transactions(request,pk):
    datee = str(date.today() + timedelta(days=int(pk)))
    # print("select * from calci_Ledger where created_date_time like '{}%'".format(datee))
    recordss = models.Ledger.objects.raw("select * from calci_Ledger where created_date_time like '{}%'".format(datee))
    serializer = serializers.LedgerSerializer(recordss,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def particular_day_collections(request,pk):
    datee = str(date.today() + timedelta(days=int(pk)))
    # print("select * from calci_Ledger where created_date_time like '{}%'".format(datee))
    recordss = models.Ledger.objects.raw("select * from calci_Ledger where created_date_time like '{}%'".format(datee))
    serializer = serializers.LedgerSerializer(recordss,many = True)
    dictt = {"date":datee,"total_bill_amount":0,"total_received_amount":0,"total_balance_amount":0}
    for record in serializer.data:
        dictt["total_bill_amount"] = dictt["total_bill_amount"] + float(record['bill_amount'])
        dictt["total_received_amount"] = dictt["total_received_amount"] + float(record['received_amount'])
        dictt["total_balance_amount"] = dictt["total_balance_amount"] + float(record['balance_amount'])
    return Response({'collections':dictt})
