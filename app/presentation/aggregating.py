import datetime

from domain.usecase.aggregating import IAggregatingUseCase


class AggregatingPresentation(object):

    def __init__(self, agu: IAggregatingUseCase):
        self._agu = agu

    def run(self, date: datetime.date) -> int:
        self._agu.aggregate(date)
        return 0
