from rest_framework import serializers
from ...models.TypeEvaluationModel import TypeEvaluationModel
from ...utils.clean_fields import clean_and_uppercase

class TypeEvaluationSerializer(serializers.ModelSerializer):
    class Meta():
        model = TypeEvaluationModel
        exclude = ('is_deleted',)
        read_only_fields = ('created_at', 'updated_at')

    def validate_code(self, value):
        return clean_and_uppercase(value)