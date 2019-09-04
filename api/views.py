from rest_framework.views import APIView
from rest_framework.response import Response
from service.creation import create_fields
#create custom API here

class CreateAPI(APIView):
    """
    Dynamically create simple API
    """

    def get(self, request):
        return Response({'response' : f'{request.method} methot now allowed'})

    def post(self, request):
        if request.method ==  'POST':
            tmp_var = request.body
            fields = create_fields(tmp_var)
            return Response({'result':fields})
        return Response({'response': [{'result':'Hello, world!', 'method':f'{request.method}'}]})