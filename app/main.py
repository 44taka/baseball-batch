import fire

from command.npb import NpbCommand


class Main(object):
    npb = NpbCommand


if __name__ == '__main__':
    fire.Fire(Main)
