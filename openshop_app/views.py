from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        # Kriteria 5: Search by name
        name_query = request.query_params.get('name')
        
        # Filter produk yang belum dihapus untuk list view
        products = Product.objects.filter(is_delete=False)
        
        if name_query:
            products = products.filter(name__icontains=name_query)
            
        serializer = ProductSerializer(products, many=True, context={'request': request})
        # Kriteria 2 & 5: Response dibungkus dalam key "products"
        return Response({"products": serializer.data})

    def post(self, request):
        # Kriteria 1: Create product
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, pk):
        # Kriteria 4: Produk berstatus terhapus masih dapat diakses via ID
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        # Kriteria 4: Soft delete
        product.is_delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)