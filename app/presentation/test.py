from domain.usecase.test import ITestUseCase


class TestPresentation(object):
    def __init__(self, tu: ITestUseCase):
        self._tu = tu

    def find(self):
        result = self._tu.find_all()
        return result
