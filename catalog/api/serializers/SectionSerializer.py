from rest_framework import serializers
from ...models import Section #import the section model
from ...utils import clean_fields#import the funciton to clean the code fields

#class main
class SectionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Section
        exclude = ('is_deleted',)
        read_only_fields = ('created_at', 'updated_at')

    def validate_code(self, value):
        return clean_fields.clean_and_uppercase(value)