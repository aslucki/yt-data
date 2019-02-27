from yt_data.utils import url_to_id


def get_urls():
    urls = ['https://www.youtube.com/watch?v=Q1PglMRgHdw',
            'https://www.youtube.com/watch?v=WTrNsAsjEmY',
            'https://www.youtube.com/watch?v=QK5Ut9E8yb0',
            'https://www.youtube.com/watch?v=y8GveGhOSC0&t=367s']

    return urls


def get_ids():
    ids = [
        'Q1PglMRgHdw',
        'WTrNsAsjEmY',
        'QK5Ut9E8yb0',
        'y8GveGhOSC0'
    ]

    return ids


def test_valid():
    urls = get_urls()
    ids = get_ids()

    for url, id in zip(urls, ids):
        assert url_to_id(url) == id


def test_wrong_url():
    url = 'https://www.youtube.com/watch=Q1PglMRgHdw'

    assert url_to_id(url) is None


def test_wrong_type():
    url = 1203

    assert 3 == 4
