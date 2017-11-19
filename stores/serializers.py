from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
 
from stores.models import Store
from users.models import User
 
 
class StoreSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(format='hex_verbose')
    name = serializers.CharField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    products = serializers.JSONField()
 
    def create(self, validated_data):
        store = Store(
            name=validated_data.get('name', None)
        )
        store.owner = CurrentUserDefault()
        store.save()
        return store


    class Meta:
        model = Store
        fields = ('id', 'name',
                'owner', 'products')