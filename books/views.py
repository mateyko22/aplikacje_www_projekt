from rest_framework.exceptions import NotFound
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from .models import Author
from .models import Book
from .models import BookReview
from .models import CustomUser
from .models import Loan
from .permissions import IsOwnerOrReadOnly
from .permissions import IsLibrarian
from .permissions import IsLibrarianOrReadOnly
from .permissions import IsOwnerOrLibrarian
from .serializers import AuthorSerializer
from .serializers import BookReviewSerializer
from .serializers import BookSerializer
from .serializers import CustomUserSerializer
from .serializers import LoanUpdateSerializer
from .serializers import LoanSerializer
from .serializers import RegisterSerializer

from datetime import datetime
from datetime import date


class IndexView(TemplateView):
    template_name = 'index.html'


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


# CRUD
class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]


class AuthorDetail(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarianOrReadOnly]
    authentication_classes = [BearerTokenAuthentication]


class BookList(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        author_param = self.request.query_params.get('author', None)
        if author_param:
            try:
                authors = Author.objects.filter(last_name__istartswith=author_param)
            except Author.DoesNotExist:
                return HttpResponse(f"Author not found.")

            queryset = Book.objects.filter(author__in=authors)
        else:
            queryset = Book.objects.all()

        return queryset


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarianOrReadOnly]
    authentication_classes = [BearerTokenAuthentication]


class BookCreate(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]
    authentication_classes = [BearerTokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(availability=True)


class BookReviewList(ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [AllowAny]


class BookReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [BearerTokenAuthentication]


class BookReviewCreate(CreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def perform_create(self, serializer):
        book_id = self.request.data.get('book', None)
        serializer.save(reader=self.request.user, book_id=book_id)


class LoanList(ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]


class LoanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanUpdateSerializer
    permission_classes = [IsLibrarianOrReadOnly]
    authentication_classes = [BearerTokenAuthentication]

    def perform_update(self, serializer):
        book_id = serializer.instance.book.id
        super().perform_update(serializer)
        if serializer.instance.returned:
            book = Book.objects.get(id=book_id)
            book.availability = True
            book.save()

            serializer.instance.return_date = date.today()
            serializer.instance.save()


class LoanCreate(CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def perform_create(self, serializer):
        book_id = self.request.data.get('book', None)
        if book_id:
            book = Book.objects.get(pk=book_id)
            if book.availability:
                serializer.save(reader=self.request.user)
                book.availability = False
                book.save()
            else:
                raise NotFound('Book is already booked.')
        else:
            raise NotFound('Book not found.')


class UserDetail(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrLibrarian]
    authentication_classes = [BearerTokenAuthentication]


class RegisterUser(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class BookReviews(ListAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        book = self.kwargs.get('pk')
        min_rating = self.request.query_params.get('min_rating', 1)
        max_rating = self.request.query_params.get('max_rating', 10)

        try:
            min_rating = int(min_rating)
            max_rating = int(max_rating)
            if not (1 <= min_rating <= 10) or not (1 <= max_rating <= 10) or min_rating > max_rating:
                raise ValueError("Invalid rating range.")
        except ValueError:
            raise ValueError("Invalid data.")

        return BookReview.objects.filter(book=book, rating__gte=min_rating, rating__lte=max_rating)


class UserLoans(ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrLibrarian]
    authentication_classes = [BearerTokenAuthentication]

    def get_queryset(self):
        user = self.kwargs.get('pk')
        year_param = self.request.query_params.get('year', datetime.now().year)

        try:
            year = int(year_param)
            if year < 1000 or year > 9999:
                raise ValueError("Invalid year.")
        except ValueError:
            raise ValueError("Invalid year.")

        queryset = Loan.objects.filter(reader=user)

        queryset = queryset.filter(
            borrow_date__year=year,
        )

        return queryset


class BookLoanHistory(ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def get_queryset(self):
        book = self.kwargs.get('pk')
        queryset = Loan.objects.filter(book=book).order_by('borrow_date')
        return queryset
