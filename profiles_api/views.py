from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView(APIView):
    """API VIEW"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns  a list of  APIVIEW features"""
        an_view = ["apple", "mango", "orange", "black"]

        return Response({"message": "hello", "an_view": an_view})

    def post(self, request):
        """Create a hello message in our Name"""
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({"method": "put"})

    def patch(self, Request, pk=None):
        """Handles partial update of object"""
        return Response({"method": "patch"})

    def delete(self, Request, pk=None):
        """delete a object"""
        return Response({"method": "delete"})
