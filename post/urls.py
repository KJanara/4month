from django.urls import path
from post import views



urlpatterns = [
    # path('hello/', views.hello_view),
    # path('current_date/', views.current_date_view),
    # path('goodbye/', views.goodbye_view),
    path('', views.main_view),
    path('products/', views.products_view),
    path('category/', views.category_view),
    path('category/create/', views.category_create),
    path('products/create/', views.product_create),
    path('products/<int:p_id>/', views.product_detail_view),
    path('products/', views.review_create),
    path('review/', views.review_view)

]
