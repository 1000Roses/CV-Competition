from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Cv, Section, SubSection, Content



class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields =  ('content', )

class SubSectionSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many = True)
    class Meta:
        model = SubSection
        fields = ['id', 'name', 'content']

class SectionSerializer(serializers.ModelSerializer):
    sub_section = SubSectionSerializer(many = True)
    class Meta:
        model = Section
        fields = ['id', 'name', 'column', 'sub_section']

class CvSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many = True)
    class Meta:
        model = Cv
        fields = ['id', 'name', 'section']
    
    def create(self, validated_data, cv = None):
        user = self.context.get("user")
        if not cv:
            cv = Cv.objects.create( name = validated_data.pop('name'), owner = user)

        for section in validated_data.get("section", None):
            if section['column'] not in ['right', 'left']:
                raise serializers.ValidationError({'error': 'column field invalid'})
            section_obj = Section.objects.create( 
                name = section['name'], 
                column = section['column'],
                cv = cv
            )

            for sub_section in section['sub_section']:
                sub_section_obj = SubSection.objects.create( name = sub_section['name'], section = section_obj)
                for content in sub_section.get('content', None):
                    content_obj = Content.objects.create(content = content['content'])
                    sub_section_obj.content.add(content_obj)
                
                sub_section_obj.save()
        
        return cv
    
    def update(self, instance, validated_data):

        instance.name = validated_data.pop("name", instance.name)


        # delete all manytomany content
        for section_obj in instance.section.all():
            for sub_section_obj in section_obj.sub_section.all():
                sub_section_obj.content.all().delete()
        
        # delete all foreign key
        instance.section.all().delete()

        instance = self.create(validated_data, cv = instance)
        instance.save()
        return instance
        
    




