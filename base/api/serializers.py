#this is used because the data which is being dumped into api is not in json form so here converting the Room.objects.all() into the json form


from rest_framework.serializers import ModelSerializer
from base.models import Room 


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'