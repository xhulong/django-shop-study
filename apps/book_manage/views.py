# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Author, Book, Borrower, BorrowedBook
# from .serializers import AuthorSerializer, BookSerializer, BorrowerSerializer, BorrowedBookSerializer
#
# class AuthorAPIView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         author = self.get_object(pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         author = self.get_object(pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return Author.objects.get(pk=pk)
#         except Author.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
# class BookAPIView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
# class BorrowerAPIView(APIView):
#     def get(self, request):
#         borrowers = Borrower.objects.all()
#         serializer = BorrowerSerializer(borrowers, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BorrowerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         borrower = self.get_object(pk)
#         serializer = BorrowerSerializer(borrower, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         borrower = self.get_object(pk)
#         borrower.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return Borrower.objects.get(pk=pk)
#         except Borrower.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
# class BorrowedBookAPIView(APIView):
#     def get(self, request):
#         borrowed_books = BorrowedBook.objects.all()
#         serializer = BorrowedBookSerializer(borrowed_books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BorrowedBookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         borrowed_book = self.get_object(pk)
#         serializer = BorrowedBookSerializer(borrowed_book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         borrowed_book = self.get_object(pk)
#         borrowed_book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return BorrowedBook.objects.get(pk=pk)
#         except BorrowedBook.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)