from urllib.parse import urlparse


class Util(object):

    @staticmethod
    def parse_url_path(url: str, i: int) -> str:
        parsed = urlparse(url=url)
        return parsed.path.split('/')[i]
