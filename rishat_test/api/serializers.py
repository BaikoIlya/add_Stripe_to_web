from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'

    def get_price(self, obj):
        return "{0:.2f}".format(obj.price / 100)
