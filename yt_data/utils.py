import urllib.parse as urlparse


def url_to_id(url: str)->str:
    """
    Extracts video_id from a YouTube video url
    :param url: YouTube video url
    :return: video_id
    """

    try:
        parsed = urlparse.urlparse(url)
        video_id = urlparse.parse_qs(parsed.query)['v']

        return video_id[0]
    except KeyError as err:
        print(err)

    except TypeError as err:
        print(err)

    except AttributeError as err:
        print(err)

    return None

