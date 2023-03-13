from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions


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


class HelloViewset(viewsets.ViewSet):
    """TEST API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello Message"""
        a_viewset = ["Django", "Django Rest Framework", "Docker"]
        return Response({"message": "Hello", "A_viewset": a_viewset})

    def create(self, request):
        """Create a New Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!!"
            return Response({"message": message})
        else:
            return Response(
                serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle Getting an Object by it's ID"""
        return Response({"HTTP_method": "GET"})

    def update(self, request, pk=None):
        """Handle Updating an Object by it's ID"""
        return Response({"HTTP_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating a part of an Object"""
        return Response({"HTTP_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle Deleting an Object"""
        return Response({"HTTP_method": "DELETE"})


class ProfileViewset(viewsets.ModelViewSet):
    """Handles Creating andupdating Profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfiles.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "email"]
