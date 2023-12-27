# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Activity, ActivityUser, ActivityBrowse
# from .serializers import ActivitySerializer, ActivityUserSerializer, ActivityBrowseSerializer
# # 查询活动列表，和提交活动
# @api_view(['GET', 'POST'])
# def activity_list(request):
#     if request.method == 'GET':
#         activities = Activity.objects.all()
#         serializer = ActivitySerializer(activities, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ActivitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 查询活动详情，修改活动，删除活动
# @api_view(['GET', 'PUT', 'DELETE'])
# def activity_detail(request, pk):
#     try:
#         activity = Activity.objects.get(pk=pk)
#     except Activity.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ActivitySerializer(activity)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ActivitySerializer(activity, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         activity.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # 查询参加活动的用户列表，和提交参加活动的用户
# @api_view(['GET', 'POST'])
# def activity_user_list(request):
#     if request.method == 'GET':
#         activity_users = ActivityUser.objects.all()
#         serializer = ActivityUserSerializer(activity_users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ActivityUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 查询参加活动的用户详情，修改参加活动的用户，删除参加活动的用户
# @api_view(['GET', 'PUT', 'DELETE'])
# def activity_user_detail(request, pk):
#     try:
#         activity_user = ActivityUser.objects.get(pk=pk)
#     except ActivityUser.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ActivityUserSerializer(activity_user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ActivityUserSerializer(activity_user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         activity_user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # 查询浏览活动的用户列表，和提交浏览活动的用户
# @api_view(['GET', 'POST'])
# def activity_browse_list(request):
#     if request.method == 'GET':
#         activity_browses = ActivityBrowse.objects.all()
#         serializer = ActivityBrowseSerializer(activity_browses, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ActivityBrowseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 查询浏览活动的用户详情，修改浏览活动的用户，删除浏览活动的用户
# @api_view(['GET', 'PUT', 'DELETE'])
# def activity_browse_detail(request, pk):
#     try:
#         activity_browse = ActivityBrowse.objects.get(pk=pk)
#     except ActivityBrowse.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ActivityBrowseSerializer(activity_browse)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ActivityBrowseSerializer(activity_browse, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         activity_browse.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
