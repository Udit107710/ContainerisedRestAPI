from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from sklearn.externals import joblib
import numpy as np
import pandas as pd
from sklearn import datasets
from .models import Results
from .serializers import ResultSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
import os
import json
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = dir_path + '/iris_svm_model.pkl'


class Predict(APIView):
    permission_classes= (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    def post(self, request, format=None):
        serializer = ResultSerializer(data=request.POST)
        if serializer.is_valid():
            petal_length = serializer.validated_data['petal_length']
            petal_width = serializer.validated_data['petal_width']
            sepal_length = serializer.validated_data['sepal_length']
            sepal_width = serializer.validated_data['sepal_width'] 
            
            iris = datasets.load_iris()
            target = iris.target_names
            
            val = np.array([petal_length, petal_width,sepal_length,sepal_width])
            model = joblib.load(file_name)
            y_pred = model.predict(val.reshape(1,-1))
            prediction = target[y_pred[0]]
            
            serializer.save(prediction=prediction,owner= request.user)
            
            json_1 = json.loads(json.dumps(serializer.validated_data))
            json_1['prediction'] = prediction
            
            return Response(json_1, status=status.HTTP_201_CREATED)
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)



class UserList(generics.ListAPIView):
    permission_classes= (permissions.IsAuthenticatedOrReadOnly,)
    queryset= User.objects.all()
    serializer_class= UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer

