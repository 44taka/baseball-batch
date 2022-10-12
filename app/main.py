import fire

from command.swallows import SwallowsCommand
from command.fighters import FightersCommand


class Main(object):
    swallows = SwallowsCommand
    fighters = FightersCommand


if __name__ == '__main__':
    fire.Fire(Main)
