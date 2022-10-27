from django.urls import path

from mongo_db.views import all_entries, create_in_mongo


app_name = "mongo"

urlpatterns = [
    path("create_mongo/", create_in_mongo, name="create_mongo"),
    path("all_entries/", all_entries, name="all_entries"),
]