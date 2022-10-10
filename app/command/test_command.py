from configs.database import db
from infrastructure.persistence.team import TeamPersistence
from usecase.test import TestUseCase
from presentation.test import TestPresentation


class TestCommand(object):
    def find_all(self):
        tp = TeamPersistence(db=db)
        tu = TestUseCase(tp=tp)
        tpre = TestPresentation(tu=tu)
        tpre.find()
