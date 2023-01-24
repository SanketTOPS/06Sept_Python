from django.shortcuts import render
from .serializers import userSerializers
from .models import userinfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getalldata(request):
    if request.method=='GET':
        stdata=userinfo.objects.all()
        dtserial=userSerializers(stdata,many=True)
        return Response(dtserial.data)

@api_view(['GET'])
def getstid(request,id):
    try:
        stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    dtserial=userSerializers(stid)
    return Response(dtserial.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def savestdata(request):
    if request.method=='POST':
        stdata=userSerializers(data=request.data)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deletestid(request,id):
    try:
        stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    userinfo.delete(stid)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
def updatedata(request,id):
    try:
        stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        stserial=userSerializers(data=request.data,instance=stid)
        if stserial.is_valid():
            stserial.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

