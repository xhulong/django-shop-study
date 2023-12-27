# #获取任务列表，提交任务
# @api_view(['GET', 'POST'])
# def task_list(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 查询任务详情，修改任务，删除任务
# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # 获取任务分类列表，提交任务分类
# @api_view(['GET', 'POST'])
# def delivery_task_list(request):
#     if request.method == 'GET':
#         delivery_tasks = DeliveryTask.objects.all()
#         serializer = DeliveryTaskSerializer(delivery_tasks, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = DeliveryTaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 查询任务分类详情，修改任务分类，删除任务分类
# @api_view(['GET', 'PUT', 'DELETE'])
# def delivery_task_detail(request, pk):
#     try:
#         delivery_task = DeliveryTask.objects.get(pk=pk)
#     except DeliveryTask.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = DeliveryTaskSerializer(delivery_task)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = DeliveryTaskSerializer(delivery_task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         delivery_task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # 获取任务分类列表，提交任务分类
# @api_view(['GET', 'POST'])
# def errand_task_list(request):
#     if request.method == 'GET':
#         errand_tasks = ErrandTask.objects.all()
#         serializer = ErrandTaskSerializer(errand_tasks, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ErrandTaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 查询任务分类详情，修改任务分类，删除任务分类
# @api_view(['GET', 'PUT', 'DELETE'])
# def errand_task_detail(request, pk):
#     try:
#         errand_task = ErrandTask.objects.get(pk=pk)
#     except ErrandTask.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ErrandTaskSerializer(errand_task)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ErrandTaskSerializer(errand_task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         errand_task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def task_user_list(request):
#     if request.method == 'GET':
#         task_users = TaskUser.objects.all()
#         serializer = TaskUserSerializer(task_users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TaskUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def task_user_detail(request, pk):
#     try:
#         task_user = TaskUser.objects.get(pk=pk)
#     except TaskUser.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TaskUserSerializer(task_user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TaskUserSerializer(task_user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         task_user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
