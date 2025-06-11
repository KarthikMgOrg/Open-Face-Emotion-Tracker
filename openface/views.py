from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import json
from feature_extractor.run_feature_extraction import launch_feature_extraction

# Create your views here.


class ProcessVideoView(APIView):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        url = json.loads(request.body)['url']
        launch_feature_extraction(url)
        return Response({"status": "Started Feature Extraction"}, status=HTTP_200_OK)
    

class GetResultsView(APIView):

    def get(self, request, *args, **kwargs):
        pass