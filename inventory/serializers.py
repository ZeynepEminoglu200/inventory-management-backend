from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, StockLog, Item


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class StockLogSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StockLog
        fields = ['id', 'item', 'item_name', 'user', 'user_name', 'change_amount', 'timestamp']
        read_only_fields = ['user', 'timestamp']


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    stock_logs = StockLogSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'quantity',
            'category',
            'created_at',
            'updated_at',
            'stock_logs',
        ]

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value