import fire

# from command.yahoo import YahooCommand
# from command.aggregating import AggregatingCommand
from command.npb import NpbCommand


class Main(object):
    npb = NpbCommand


if __name__ == '__main__':
    fire.Fire(Main)
