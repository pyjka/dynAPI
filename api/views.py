from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#create custom API here

class CreateAPI(APIView):
    """
    Dynamically create simple API
    """

    def get(self, request):
        return Response({'response' : f'{request.method} methot now allowed'})

    def post(self, request):
        #test output
        return Response({'response': [{'result':'Hello, world!', 'method':f'{request.method}'}]})