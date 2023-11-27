from django.contrib import admin
from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.hello_view),
    # path('current_date/', views.current_date_view),
    # path('goodbye/', views.goodbye_view),
    path('', views.main_view),
    path('products/', views.products_view),
    path('category/', views.category_view),
    path('products/<int:p_id>/', views.product_detail_view),
    path('review/', views.review_view)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
