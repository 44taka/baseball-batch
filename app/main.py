import fire

from command.test_command import TestCommand
from command.swallows import SwallowsCommand


class Main(object):
    test = TestCommand
    swallows = SwallowsCommand


if __name__ == '__main__':
    fire.Fire(Main)
