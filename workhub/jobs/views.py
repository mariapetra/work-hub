from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Jobs
from .serializers import JobsSerializer
from django.http import Http404
from rest_framework import status


class JobsList(APIView):

    def get(self, request):
        # Perform the logic for creating a new job
        jobs = Jobs.objects.all()
        # self.perform_create(serializer)
        serializer = JobsSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class JobsDetail(APIView):

    def get_object(self, pk):
        try:
            return Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobsSerializer(jobs)
        return Response(serializer.data)

# {"company":"test",
# "description":"test",
# location":"test",
# hours":11,
# contract_type":"test",
# manager":"test",
# manager_email":"test@text.com",
# salary":123,
# notes":"test" }
