from rest_framework import serializers
from django.urls import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'sku', 'description', 'shop', 'location', 
            'price', 'discount', 'category', 'stock', 'is_available', 
            'picture', 'is_delete', '_links'
        ]
        extra_kwargs = {
            'is_delete': {'read_only': True}
        }

    def get__links(self, obj):
        request = self.context.get('request')
        if request is None:
            return []
        
        # Menggunakan reverse untuk mendapatkan URL endpoint
        list_url = request.build_absolute_uri(reverse('product-list')).replace('127.0.0.1', 'localhost')
        detail_url = request.build_absolute_uri(reverse('product-detail', args=[obj.id])).replace('127.0.0.1', 'localhost')
        
        return [
            {
                "rel": "self",
                "href": list_url,
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]