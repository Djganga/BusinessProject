from django.shortcuts import render

from api import serializers, models
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProductList(APIView):
    def get(self, request, format=None):
        itemss = models.Product.objects.all()
        serializer = serializers.ProductSerializer(itemss,many=True)
        return Response(serializer.data)

    def post(self,request):
        if "discount" in request.data.keys():
            request.data["final_price"] = float(request.data["mrp"]) - (float(request.data["discount"])*float(request.data["mrp"])/100)
        else:
            request.data["final_price"] = request.data["mrp"]
            request.data["discount"] = string(float(0))

        serializer = serializers.ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ParticularProduct(APIView):
    def get(self, request,pk, format=None):
        try:
            itemss = models.Product.objects.get(id=pk)
            serializer = serializers.ProductSerializer(itemss)
            return Response(serializer.data)
        except:
            return Response({"Error Msg":f"No such item found with id of {pk}"})

    def put(self,request,pk):
        return Response({"msg":"Yet to develop this."})

    def delete(self, request,pk, format=None):
        try:
            itemm = models.Product.objects.get(id=pk)
            itemm.delete()
            return Response({"Msg":f"Item found with id of {pk} has been deleted."})
        except:
            return Response({"Error Msg":f"No such item found with id of {pk}"})

def getprice(recordd):
    if "discount" in recordd.keys():
        recordd["final_price"] = float(recordd["mrp"]) - (float(recordd["discount"])*float(recordd["mrp"])/100)
    else:
        recordd["final_price"] = recordd["mrp"]
        recordd["discount"] = string(float(0))
    return recordd
