from .CsvSave import csv_save
from .Mongo import mongo_save
from .MySQL import sql_save
from .image_save import image_save, images_save


class DataSave:
    image_save = image_save
    images_save = images_save
    mongo_save = mongo_save
    sql_save = sql_save
    csv_save = csv_save


data_save = DataSave
