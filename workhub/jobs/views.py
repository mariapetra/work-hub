from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Jobs
from .serializers import JobsSerializer


class JobsList(APIView):

    def get(self, request):
        # Perform the logic for creating a new job
        jobs = Jobs.objects.all()
        # self.perform_create(serializer)
        serializer = JobsSerializer(jobs, many=True)
