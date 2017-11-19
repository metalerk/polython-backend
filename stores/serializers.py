from rest_framework import serializers
 
from stores.models import Store
from users.models import User
 
 
class StoreSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(format='hex_verbose')
    name = serializers.CharField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    products = serializers.JSONField()
 
    def create(self, validated_data):
        store = Store(
            name=validated_data.get('name', None)
        )
        store.owner = self.context['request'].user
        store.save()
        return store


    class Meta:
        model = Store
        fields = ('id', 'name',
                'owner', 'products')