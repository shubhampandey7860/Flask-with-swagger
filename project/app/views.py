from django.shortcuts import render,redirect
from django.conf import settings
import os


# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import YourModel
from .serializers import YourModelSerializer
from rest_framework import status
from rest_framework.views import APIView

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer



@api_view(['GET', 'POST'])
def your_model_list(request):
    if request.method == 'GET':
        your_models = YourModel.objects.all()
        serializer = YourModelSerializer(your_models, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def your_model_detail(request, pk):
    try:
        your_model = YourModel.objects.get(pk=pk)
    except YourModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = YourModelSerializer(your_model)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = YourModelSerializer(your_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        your_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


class YourModelAPIView(APIView):
    """
    A view for handling YourModel instances.
    """

    def get(self, request, pk=None):
        """
        Retrieve a list of YourModel instances or a specific instance.
        """
        if pk is not None:
            try:
                your_model = YourModel.objects.get(pk=pk)
                serializer = YourModelSerializer(your_model)
                return Response(serializer.data)
            except YourModel.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            your_models = YourModel.objects.all()
            serializer = YourModelSerializer(your_models, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Create a new YourModel instance.
        """
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update a YourModel instance.
        """
        try:
            your_model = YourModel.objects.get(pk=pk)
        except YourModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = YourModelSerializer(your_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a YourModel instance.
        """
        try:
            your_model = YourModel.objects.get(pk=pk)
        except YourModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        your_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
    



def file_upload(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['file']
        # Handle the uploaded file
        handle_uploaded_file(uploaded_file)
        # Redirect to a success page
        return redirect('success_url')
    return render(request, 'template.html')

def handle_uploaded_file(uploaded_file):
    # Define the directory where uploaded files will be saved
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    # Create the directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    # Write the uploaded file to the filesystem
    with open(os.path.join(upload_dir, uploaded_file.name), 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk) 

def success_view(request):
    return render(request, 'success.html')               
