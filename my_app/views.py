from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Foo
from .serializers import FooSerializer

class StatusUpdateView(APIView):
    def get(self, request):
       
        foo = Foo.objects.first()
         
        return Response(FooSerializer(foo).data, status=status.HTTP_200_OK)
    
    def put(self, request):
        foo=Foo.objects.first()
        serializer = FooSerializer(foo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
