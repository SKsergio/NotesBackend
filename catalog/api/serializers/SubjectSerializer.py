from rest_framework import serializers
from ...models.SubjectsModel import SubjectModel
from ...utils.clean_fields import clean_and_uppercase

class SubjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = SubjectModel
        exclude = ('is_deleted',)
        read_only_fields = ('created_at','updated_at')

    def validate_code(self, value):
        return clean_and_uppercase(value)
    
