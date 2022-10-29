import fire

from command.swallows import SwallowsCommand
from command.fighters import FightersCommand
from command.yahoo import YahooCommand
from command.aggregating import AggregatingCommand


class Main(object):
    swallows = SwallowsCommand
    fighters = FightersCommand
    yahoo = YahooCommand
    aggregating = AggregatingCommand


if __name__ == '__main__':
    fire.Fire(Main)
