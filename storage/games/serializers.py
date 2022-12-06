from storage.games.models import Studio, Platform, Game
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['name']
        
class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['name']

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=data)
        except (TypeError, ValueError):
            self.fail('invalid')

class GameSerializer(serializers.ModelSerializer):
    studio = CreatableSlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Studio.objects.all()
    )
    platforms = CreatableSlugRelatedField(
        many=True,
        read_only=False,
        slug_field='name',
        queryset=Platform.objects.all()
    )

    class Meta:
        model = Game
        many = True
        fields = ['name','release_date','studio','ratings','platforms']