from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Users HTTP Method as function(get, post, put, delete)',
            'Is similar to traditional Django View'
        ]
        return Response({'message': 'Hello!', 'an_api_view': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE'})
