from rest_framework import generics, permissions, filters, serializers
from .serializers import RegisterSerializer, ItemSerializer, CategorySerializer, StockLogSerializer
from .models import Item, Category, StockLog
from .models import Profile
from .serializers import ProfileSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]


class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Item.objects.filter(owner=self.request.user)

        category_id = self.request.query_params.get('category')
        low_stock = self.request.query_params.get('low_stock')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if low_stock == 'true':
            queryset = queryset.filter(quantity__lt=5)

        return queryset

    def perform_create(self, serializer):
        item = serializer.save(owner=self.request.user)

        StockLog.objects.create(
            item=item,
            user=self.request.user,
            change_amount=item.quantity
        )


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        old_item = self.get_object()
        old_quantity = old_item.quantity

        updated_item = serializer.save()
        new_quantity = updated_item.quantity

        if new_quantity < 0:
            raise serializers.ValidationError("Stock cannot be negative.")

        change_amount = new_quantity - old_quantity

        if change_amount != 0:
            StockLog.objects.create(
                item=updated_item,
                user=self.request.user,
                change_amount=change_amount
            )


class StockLogListView(generics.ListAPIView):
    serializer_class = StockLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StockLog.objects.filter(user=self.request.user).order_by('-timestamp')