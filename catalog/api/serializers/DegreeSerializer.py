from rest_framework import serializers
from ...models import DegreesModel
from ...utils import clean_fields

class DegreeSeializer(serializers.ModelSerializer):
    class Meta():
        model = DegreesModel
        exclude = ('is_deleted',)
        read_only_fields = ('created_at', 'updated_at')

    def validate_code(self, value):
        return clean_fields.clean_and_uppercase(value)