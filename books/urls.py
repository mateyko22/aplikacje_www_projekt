from django.urls import path

from .views import AuthorDetail
from .views import AuthorList
from .views import BookDetail
from .views import BookEdit
from .views import BookList
from .views import BookReviewCreate
from .views import BookReviewDetail
from .views import BookReviewEdit
from .views import BookReviewList
from .views import BookReviews
from .views import IndexView
from .views import LoanCreate
from .views import LoanDetail
from .views import LoanList
from .views import LoanUpdate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('books/<int:pk>/edit', BookEdit.as_view(), name='book_edit'),
    path('books/<int:pk>/reviews', BookReviews.as_view(), name='book_reviews'),
    path('reviews/', BookReviewList.as_view(), name='book_review_list'),
    path('reviews/create', BookReviewCreate.as_view(), name='book_review_create'),
    path('reviews/<int:pk>/', BookReviewDetail.as_view(), name='book_review'),
    path('reviews/<int:pk>/edit', BookReviewEdit.as_view(), name='book_review_edit'),
    path('loans/', LoanList.as_view(), name='loan_list'),
    path('loans/create', LoanCreate.as_view(), name='loan_create'),
    path('loans/<int:pk>/', LoanDetail.as_view(), name='loan_detail'),
    path('loans/<int:pk>/edit', LoanUpdate.as_view(), name='loan_detail'),
]
