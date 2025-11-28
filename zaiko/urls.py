from django.urls import path
from . import views

app_name = 'zaiko'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='index'),

    path('item/new/', 
         views.ItemCreateView.as_view(),
         name='item_create'),

    path('item/new/done/',
         views.ItemCreateDoneView.as_view(),
         name='item_create_done'),

    path('items/category/<str:category>/',
         views.CategoryItemListView.as_view(),
         name='item_category'),

    path('items/user/<int:user_id>/',
         views.UserItemListView.as_view(),
         name='user_items'),

    path('item/<int:pk>/',
         views.ItemDetailView.as_view(),
         name='item_detail'),

    path('mypage/',
         views.MyItemsView.as_view(),
         name='mypage'),

    path('item/<int:pk>/delete/',
         views.ItemDeleteView.as_view(),
         name='item_delete'),
    
    path('item/<int:pk>/edit/',
         views.ItemUpdateView.as_view(),
         name='item_edit'),
    
]
