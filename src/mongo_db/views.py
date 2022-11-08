from django.http import HttpResponse
from faker import Faker

from mongo_db.models import Blog, Entry


def create_in_mongo(request):
    faker = Faker()
    saved = Entry(
        blogs=[Blog(name=faker.word(), text=faker.paragraph(nb_sentences=5))], headline="some random category"
    ).save()

    return HttpResponse(f"Done: {saved}")


def all_entries(request):
    blogs_timestamps = list(Entry.objects.values_list("timestamp"))

    print(blogs_timestamps)

    return HttpResponse("|".join([timestamp.strftime("%m-%d-%Y %H:%M:%S") for timestamp in blogs_timestamps]))
