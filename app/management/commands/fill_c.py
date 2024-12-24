import json
from django.core.management import BaseCommand
from app.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories_list = []
        with open('app/fixtures/category.json', encoding='utf-8') as f:
            categories = json.load(f)

        for category_item in categories:
            categories_list.append(category_item["fields"])

        print(categories_list)

        for category_item in categories_list:
            Category.objects.create(**category_item)
