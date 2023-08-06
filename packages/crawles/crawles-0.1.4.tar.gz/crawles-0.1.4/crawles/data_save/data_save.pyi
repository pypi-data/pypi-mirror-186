from .CsvSave import csv_save
from .image_save import image_save
from .image_save import images_save
from .Mongo import mongo_save
from .MySQL import sql_save

from .CsvSave import CsvSave
from .Mongo import Mongo
from .MySQL import SqlSave
from typing import Text, Union, Iterable, Optional
from CsvSave import CsvSave
from typing import Text, Optional, List




class DataSave:
    def image_save(self, image_url: Text,
                   image_path: Union[Text, bytes],
                   astrict: Optional = 100):
        pass

    def images_save(self, image_iteration: Iterable[Iterable[Text, Text]],
                    astrict: Optional = 100): pass


    mongo_save = Mongo()
    sql_save = SqlSave()

    def csv_save(self,filename, mode='r+',
                 encoding='gbk',
                 newline='',
                 **kwargs) -> CsvSave: pass


data_save = DataSave