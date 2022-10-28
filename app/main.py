import fire

from command.swallows import SwallowsCommand
from command.fighters import FightersCommand
from command.aggregating import AggregatingCommand


class Main(object):
    swallows = SwallowsCommand
    fighters = FightersCommand
    aggregating = AggregatingCommand


if __name__ == '__main__':
    fire.Fire(Main)
