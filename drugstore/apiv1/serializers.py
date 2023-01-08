from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from main.models import Product, Category


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'descr', 'image', 'category')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')