from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response
from .models import Cv
from .serializers import CvSerializer

class CvViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == "update":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def list(self, request):
        cvs = Cv.objects.all()
        serializers = CvSerializer(cvs, many = True)
        return Response(serializers.data)

    def retrieve(self, request, pk= None):
        try:
            cv = Cv.objects.get(id = pk)
        except:
            return Response({'error': 'cv is not exist'})
        serializers = CvSerializer(cv)
        return Response(serializers.data)
    
    def create(self, request):
        user = request.user
        data = request.data

        serializer = CvSerializer(data = data, context = { "user": user })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("create successfully")
        return Response({ "error": "invalid field" })
    
    def update(self, request, pk = None):
        user = request.user
        data = request.data

        try:
            cv = Cv.objects.get(id = pk)
        except:
            return Response({ 'error': 'cv is not exist' })
        
        if not user.is_superuser:
            if cv.owner.id != user.id:  
                return Response({ 'error': 'must be author' })

        serializer = CvSerializer(cv, data = data, context = { "user": user })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("update successfully")
        return Response({ "error": "invalid field" })