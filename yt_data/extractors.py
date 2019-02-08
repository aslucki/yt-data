import requests


class CommentsExtractor:

    def __init__(self, api_key, include_replies=False):
        self._api_key = api_key
        self._api_base_url = \
            'https://www.googleapis.com/youtube/v3/commentThreads'
        self._include_replies = include_replies

    def _get_query_params(self, video_id, page_token):
        part = 'snippet'
        if self._include_replies:
            part = 'snippet%2Creplies'

        params = {'part': part, 'videoId': video_id,
                  'maxResults': 100, 'pageToken': page_token,
                  'key': self._api_key}

        return params

    def _retrieve_page(self, video_id, page_token=None):
        params = self._get_query_params(video_id, page_token)

        api_response =\
            requests.get(self._api_base_url,
                         params=params)
        if api_response.status_code == 200:
            return api_response.json()

        return None

    @staticmethod
    def _extract_comment(response_item):
        try:
            comment = response_item['snippet']['topLevelComment']\
                                   ['snippet']['textOriginal']
            return comment
        except KeyError as err:
            print(err)

        return None

    def _process_single_page(self, api_response):
        try:
            items = api_response['items']
            comments = list(map(lambda item:
                                self._extract_comment(item), items))
            return comments
        except KeyError as err:
            print(err)

        return None

    def extract(self, video_id, max_pages=1000, verbose=False):

        comments = []
        page_cnt = 0
        while True:

            if page_cnt >= max_pages:
                break

            try:
                page_token = page['nextPageToken']
            except NameError:
                page_token = None
            except KeyError:
                break

            page = self._retrieve_page(video_id, page_token=page_token)
            page_comments = self._process_single_page(page)

            if page_comments:
                comments.extend(page_comments)
            page_cnt += 1

            if verbose:
                message = 'Processed the page no. {}.\n' \
                          'Extracted {} comments.'.format(page_cnt,
                                                          len(comments))
                print(message)

        return comments


