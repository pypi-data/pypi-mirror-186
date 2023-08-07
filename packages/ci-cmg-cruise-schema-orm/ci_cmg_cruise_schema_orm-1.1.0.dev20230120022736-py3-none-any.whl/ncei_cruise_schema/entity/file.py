from ..orm.entity import Entity, Column
from ..orm.column_consts import DATE_PLACEHOLDER, date_select_name


class File(Entity):

  @staticmethod
  def _table():
    return "files"

  def __init__(
        self,
        id=None,
        dataset_id=None,
        name=None,
        raw_size=None,
        publish=None,
        collection_date=None,
        publish_date=None,
        version_id=None,
        type_id=None,
        format_id=None,
        archive_date=None,
        last_update=None,
        temp_id=None,
        gzip_size=None
    ):
      self.__id = id
      self.__dataset_id = dataset_id
      self.__name = name
      self.__raw_size = raw_size
      self.__publish = publish
      self.__collection_date = collection_date
      self.__publish_date = publish_date
      self.__version_id = version_id
      self.__type_id = type_id
      self.__format_id = format_id
      self.__archive_date = archive_date
      self.__last_update = last_update
      self.__temp_id = temp_id
      self.__gzip_size = gzip_size


  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, value):
    self.__id = value

  @property
  def dataset_id(self):
    return self.__dataset_id

  @dataset_id.setter
  def dataset_id(self, value):
    self.__dataset_id = value

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  @property
  def raw_size(self):
    return self.__raw_size

  @raw_size.setter
  def raw_size(self, value):
    self.__raw_size = value

  @property
  def publish(self):
    return self.__publish

  @publish.setter
  def publish(self, value):
    self.__publish = value

  @property
  def collection_date(self):
    return self.__collection_date

  @collection_date.setter
  def collection_date(self, value):
    self.__collection_date = value

  @property
  def publish_date(self):
    return self.__publish_date

  @publish_date.setter
  def publish_date(self, value):
    self.__publish_date = value

  @property
  def version_id(self):
    return self.__version_id

  @version_id.setter
  def version_id(self, value):
    self.__version_id = value

  @property
  def type_id(self):
    return self.__type_id

  @type_id.setter
  def type_id(self, value):
    self.__type_id = value

  @property
  def format_id(self):
    return self.__format_id

  @format_id.setter
  def format_id(self, value):
    self.__format_id = value

  @property
  def archive_date(self):
    return self.__archive_date

  @archive_date.setter
  def archive_date(self, value):
    self.__archive_date = value

  @property
  def last_update(self):
    return self.__last_update

  @last_update.setter
  def last_update(self, value):
    self.__last_update = value

  @property
  def temp_id(self):
    return self.__temp_id

  @temp_id.setter
  def temp_id(self, value):
    self.__temp_id = value

  @property
  def gzip_size(self):
    return self.__gzip_size

  @gzip_size.setter
  def gzip_size(self, value):
    self.__gzip_size = value

  @classmethod
  def _columns(cls):
    return (
      Column("file_id", cls.id, id=True, sequence="files_seq"),
      Column("dataset_id", cls.dataset_id),
      Column("file_name", cls.name),
      Column("raw_size", cls.raw_size),
      Column("publish", cls.publish),
      Column("collection_date", cls.collection_date, placeholder=DATE_PLACEHOLDER, select_name_func=date_select_name),
      Column("publish_date", cls.publish_date, placeholder=DATE_PLACEHOLDER, select_name_func=date_select_name),
      Column("version_id", cls.version_id),
      Column("type_id", cls.type_id),
      Column("format_id", cls.format_id),
      Column("archive_date", cls.archive_date, placeholder=DATE_PLACEHOLDER, select_name_func=date_select_name),
      Column("last_update", cls.last_update, placeholder=DATE_PLACEHOLDER, select_name_func=date_select_name),
      Column("temp_id", cls.temp_id),
      Column("gzip_size", cls.gzip_size)
    )
