from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, DeleteView, UpdateView,
)
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item
from .forms import ItemForm


class ItemListView(ListView):
    template_name = 'index.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 9
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(category__icontains=q) |
                Q(memo__icontains=q)
            )

        return qs


@method_decorator(login_required, name='dispatch')
class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('zaiko:item_create_done')

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return super().form_valid(form)


class ItemCreateDoneView(TemplateView):
    template_name = 'item_create_done.html'


class CategoryItemListView(ListView):
    template_name = 'index.html'
    context_object_name = 'items'
    paginate_by = 9

    def get_queryset(self):
        category_value = self.kwargs['category']
        return Item.objects.filter(
            category=category_value
        ).order_by('-created_at')


class UserItemListView(ListView):
    template_name = 'index.html'
    context_object_name = 'items'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Item.objects.filter(
            owner_id=user_id
        ).order_by('-created_at')


class ItemDetailView(DetailView):
    template_name = 'item_detail.html'
    model = Item
    context_object_name = 'item'


@method_decorator(login_required, name='dispatch')
class MyItemsView(ListView):
    template_name = 'mypage.html'
    context_object_name = 'items'
    paginate_by = 9

    def get_queryset(self):
        return Item.objects.filter(
            owner=self.request.user
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        ctx['total_items'] = qs.count()
        ctx['total_quantity'] = sum(i.quantity for i in qs)
        return ctx


@method_decorator(login_required, name='dispatch')
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('zaiko:mypage')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


@method_decorator(login_required, name='dispatch')
class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_edit.html'
    success_url = reverse_lazy('zaiko:mypage')

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)
