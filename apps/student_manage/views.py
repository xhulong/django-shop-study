# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Student, Department, Major
# from .serializers import StudentSerializer, DepartmentSerializer, MajorSerializer
# from rest_framework import status
#
# class StudentAPIView(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404
#
# class DepartmentAPIView(APIView):
#     def get(self, request):
#         departments = Department.objects.all()
#         serializer = DepartmentSerializer(departments, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = DepartmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         department = self.get_object(pk)
#         serializer = DepartmentSerializer(department, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         department = self.get_object(pk)
#         department.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return Department.objects.get(pk=pk)
#         except Department.DoesNotExist:
#             raise Http404
# class MajorAPIView(APIView):
#     def get(self, request):
#         majors = Major.objects.all()
#         serializer = MajorSerializer(majors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = MajorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         major = self.get_object(pk)
#         serializer = MajorSerializer(major, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         major = self.get_object(pk)
#         major.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return Major.objects.get(pk=pk)
#         except Major.DoesNotExist:
#             raise Http404