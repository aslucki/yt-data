from yt_data.extractors import CommentsExtractor


def get_page():
    page = {'etag': '"XpPGQXPnxQJhLgs6enD_n8JR4Qk/0Syp9oVHmkRCldkzDvH_-0MOG64"',
            'items': [{'etag': '"XpPGQXPnxQJhLgs6enD_n8JR4Qk/eC2g02436Igtts87YYBBHIyVI4I"',
               'id': 'UgythqORP8n56FFbssh4AaABAg',
               'kind': 'youtube#commentThread',
               'snippet': {'canReply': True,
                'isPublic': True,
                'topLevelComment': {'etag': '"XpPGQXPnxQJhLgs6enD_n8JR4Qk/swsNB8vIgiSH23I7ueGdXjQ2odY"',
                 'id': 'UgythqORP8n56FFbssh4AaABAg',
                 'kind': 'youtube#comment',
                 'snippet': {'authorChannelId': {'value': 'UC72gthTZjfukN18l1MLynNg'},
                  'authorChannelUrl': 'http://www.youtube.com/channel/UC72gthTZjfukN18l1MLynNg',
                  'authorDisplayName': 'RAAGHAV SHARMA',
                  'authorProfileImageUrl': 'https://yt3.ggpht.com/-EipSR-rrpYc/AAAAAAAAAAI/AAAAAAAAAAA/jKqjxBfK0eQ/s28-c-k-no-mo-rj-c0xffffff/photo.jpg',
                  'canRate': True,
                  'likeCount': 1,
                  'publishedAt': '2019-01-31T17:31:56.000Z',
                  'textDisplay': 'where is double BAMM ?',
                  'textOriginal': 'where is double BAMM ?',
                  'updatedAt': '2019-01-31T17:31:56.000Z',
                  'videoId': 'yIYKR4sgzI8',
                  'viewerRating': 'none'}},
                'totalReplyCount': 1,
                'videoId': 'yIYKR4sgzI8'}},
              {'etag': '"XpPGQXPnxQJhLgs6enD_n8JR4Qk/a_Gmd9_ZmNXqUrNycXdfy_Zom_s"',
               'id': 'Ugx-s-Nchp27XG3zzCt4AaABAg',
               'kind': 'youtube#commentThread',
               'snippet': {'canReply': True,
                'isPublic': True,
                'topLevelComment': {'etag': '"XpPGQXPnxQJhLgs6enD_n8JR4Qk/nyIl_V7r9UBmfC1ktGqW0nSqNRQ"',
                 'id': 'Ugx-s-Nchp27XG3zzCt4AaABAg',
                 'kind': 'youtube#comment',
                 'snippet': {'authorChannelId': {'value': 'UCc-fe49old0O3bfuKvrkofw'},
                  'authorChannelUrl': 'http://www.youtube.com/channel/UCc-fe49old0O3bfuKvrkofw',
                  'authorDisplayName': 'Roshan Choudhary',
                  'authorProfileImageUrl': 'https://yt3.ggpht.com/--RkHWxKa-CE/AAAAAAAAAAI/AAAAAAAAAAA/ompNjSnFakg/s28-c-k-no-mo-rj-c0xffffff/photo.jpg',
                  'canRate': True,
                  'likeCount': 0,
                  'publishedAt': '2018-03-05T16:06:41.000Z',
                  'textDisplay': 'Hey Joshua.. ',
                  'textOriginal': 'Hey Joshua.. ',
                  'videoId': 'yIYKR4sgzI8',
                  'viewerRating': 'none'}},
                'totalReplyCount': 0,
                'videoId': 'yIYKR4sgzI8'}}],
            'kind': 'youtube#commentThreadListResponse',
            'pageInfo': {'resultsPerPage': 100, 'totalResults': 54}}

    return page


def test_extractor(requests_mock):
    requests_mock.get('http://test.com', json=get_page())
    extractor = CommentsExtractor('dummy_api_key')
    extractor._api_base_url = 'http://test.com'

    comments = extractor.extract('dummy_video_id')
    assert len(comments) == 2
    assert comments[0] == 'where is double BAMM ?'
    assert comments[1] == 'Hey Joshua.. '

