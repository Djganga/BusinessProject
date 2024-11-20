from django.shortcuts import render

from api import serializers, models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

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
            return Response(serializer.data,status = status.HTTP_201_CREATED)


class ParticularProduct(APIView):
    def get_object(self,pk):
        try:
            itemm = models.Product.objects.get(id=pk)
            return itemm
        except models.Product.DoesNotExist:
            raise Http404
            # return Response({"Error Msg":f"No such item found with id of {pk}"})

    def get(self, request,pk, format=None):
        itemm = self.get_object(pk)
        serializer = serializers.ProductSerializer(itemm)
        return Response(serializer.data)

    def put(self,request,pk):
        itemm = self.get_object(pk)
        dataa = request.data
        dataa = self.getprice(dataa)
        serializer = serializers.ProductSerializer(itemm,data = dataa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"Error Msg":f"Update failed for this item : {pk}"})

    def delete(self, request,pk, format=None):
        itemm = self.get_object(pk)
        itemm.delete()
        return Response({"Msg":f"Item found with id of {pk} has been deleted."})

    ########## custoom methods ##########

    def getprice(self, recordd):
        if "discount" in recordd.keys():
            recordd["final_price"] = float(recordd["mrp"]) - (float(recordd["discount"])*float(recordd["mrp"])/100)
        else:
            recordd["final_price"] = recordd["mrp"]
            recordd["discount"] = string(float(0))
        return recordd
