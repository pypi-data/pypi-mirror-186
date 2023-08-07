from ..orm.entity import Entity, Column

class SurveyShapeMapping(Entity):

  @staticmethod
  def _table():
    return "survey_shapes"

  def __init__(self, survey_id=None, shape_id=None):
    self.__survey_id = survey_id
    self.__shape_id = shape_id

  @property
  def survey_id(self):
    return self.__survey_id

  @survey_id.setter
  def survey_id(self, value):
    self.__survey_id = value

  @property
  def shape_id(self):
    return self.__shape_id

  @shape_id.setter
  def shape_id(self, value):
    self.__shape_id = value

  @classmethod
  def _columns(cls):
    return (
      Column("survey_id", cls.survey_id, id=True),
      Column("shape_id", cls.shape_id, id=True)
    )

