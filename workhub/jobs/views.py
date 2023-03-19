from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Jobs
from .serializers import JobsSerializer, JobsDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly


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
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class JobsDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                          ]

    def get_object(self, pk):
        try:
            jobs = Jobs.objects.get(pk=pk)
            self.check_object_permissions(self.request, jobs)
            return jobs
        except Jobs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobsSerializer(jobs)
        return Response(serializer.data)

    def put(self, request, pk):
        jobs = self.get_object(pk)
        data = request.data
        serializer = JobsDetailSerializer(
            instance=jobs,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
