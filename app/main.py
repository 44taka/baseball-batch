import fire

from command.yahoo import YahooCommand
from command.aggregating import AggregatingCommand


class Main(object):
    yahoo = YahooCommand
    aggregating = AggregatingCommand()


if __name__ == '__main__':
    fire.Fire(Main)
