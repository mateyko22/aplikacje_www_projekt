from django.views.generic import TemplateView
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from .models import Author
from .models import Book
from .models import BookReview
from .models import CustomUser
from .models import Loan
from .serializers import AuthorSerializer
from .serializers import BookReviewSerializer
from .serializers import BookSerializer
from .serializers import CustomUserSerializer
from .serializers import LoanSerializer
from .serializers import RegisterSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


# CRUD
class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, TokenAuthentication]


class AuthorDetail(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, TokenAuthentication]


class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookEdit(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookReviewList(ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]


class BookReviewDetail(RetrieveAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]


class BookReviewCreate(CreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]


class BookReviewEdit(RetrieveUpdateDestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAdminUser]


class LoanList(ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]


class LoanDetail(ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]


class LoanCreate(CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAdminUser]


class LoanUpdate(UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAdminUser]


class BookReviews(ListAPIView):
    serializer_class = BookReviewSerializer

    def get_queryset(self):
        book = self.kwargs.get('pk')
        return BookReview.objects.filter(book=book)


class UserDetail(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, TokenAuthentication]


class RegisterUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserLoans(ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, TokenAuthentication]

    def get_queryset(self):
        user = self.kwargs.get('pk')
        return Loan.objects.filter(reader=user)
