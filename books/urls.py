from django.urls import path

from .views import AuthorDetail
from .views import AuthorList
from .views import BookDetail
from .views import BookCreate
from .views import BookList
from .views import BookReviewCreate
from .views import BookReviewDetail
from .views import BookReviewList
from .views import BookReviews
from .views import IndexView
from .views import LoanCreate
from .views import LoanDetail
from .views import LoanList
from .views import RegisterUser
from .views import UserLoans
from .views import UserDetail
from .views import BookLoanHistory

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('books/create/', BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/reviews/', BookReviews.as_view(), name='book_reviews'),
    path('books/<int:pk>/loan_history/', BookLoanHistory.as_view(), name='book_loan_history'),
    path('reviews/', BookReviewList.as_view(), name='book_review_list'),
    path('reviews/create/', BookReviewCreate.as_view(), name='book_review_create'),
    path('reviews/<int:pk>/', BookReviewDetail.as_view(), name='book_review'),
    path('loans/', LoanList.as_view(), name='loan_list'),
    path('loans/create/', LoanCreate.as_view(), name='loan_create'),
    path('loans/<int:pk>/', LoanDetail.as_view(), name='loan_detail'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('user/<int:pk>/loans/', UserLoans.as_view(), name='user_loans'),
    path('register/', RegisterUser.as_view(), name='register_user'),
]
