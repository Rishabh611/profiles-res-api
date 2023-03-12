from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """API VIEW"""
    def get(self, request, format = None):
        """Returns  a list of  APIVIEW features"""
        an_view = [
            'apple','mango','orange','black'
        ]

        return Response({
            'message':"hello",
            'an_view': an_view
        })