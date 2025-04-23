from rest_framework import serializers
from ...models import Classrooms #import the section model
from ...utils import clean_fields#import the funciton to clean the code fields

#class main
class ClassRoomSerizlizer(serializers.ModelSerializer):
    class Meta():
        model = Classrooms
        exclude = ('is_deleted',)
        read_only_fields = ('created_at', 'updated_at')

    def validate_code(self, value):
        return clean_fields.clean_and_uppercase(value)