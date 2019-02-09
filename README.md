# About 
Wrapper for [YouTube data API](https://developers.google.com/youtube/v3/)  
Currently only comments' extraction is implemented.

# Installation
From the parent directory run:  
`python setup.py install`

# How to use
1. Extract all comments from a YouTube video:  
```python
from yt_data.extractors import CommentsExtractor
from yt_data.utils import url_to_id

# Create extractor object
extractor = CommentsExtractor(api_key='YouTube_data_API_key',
                              include_replies=False)

# Extract id from the video url
yt_video_url = 'https://www.youtube.com/watch?v=aircAruvnKk'
video_id = url_to_id(yt_video_url)

# Extract up to n pages of comments (here 5)
# There are 100 comments per page                              
comments = extractor.extract(video_id, max_pages=5, verbose=True)
```

```diff
- Note: Single page corresponds to a single API request
```
Default daily quota for this API is 100000.
