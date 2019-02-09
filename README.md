# About 
Wrapper for [YouTube data API](https://developers.google.com/youtube/v3/)  
Currently only comments' extraction is implemented.

# Installation
From the parent directory run:  
`python setup.py install`

# How to use
## 1. Extract comments from a YouTube video:  
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
# There are 100 (or all if less than 100) comments per page                              
comments = extractor.extract(video_id, max_pages=5, verbose=True)
```
Sample ouput:
```python
>>> comments
["Dont forget to turn off adblocker for this channel. I will gladly sit through all the ads for this guy's hard work",
 'Great Video. Many thanks and best artificialneuralnetwork.app',
 'People disliking should be asked to submit a mandatory public comment explaining their actions',
 '11:19',
 'What software did you use for creating the video?',
 
 ...
 
 'This explains artificial neural networks with such great detail that even my 12 year old brain can make perfect sense of them.',
 'Hail you sir!🙇🙇🙇',
 '1 thumb up for "squishification"',
 'How does this relate to our senses? Because you used your senses to comprehend our senses. Strange looping inhere but i will accept challenges of course ¯\\_(ツ)_/¯',
 'physical action programs']
```

### Notes: 
```diff
- Single page corresponds to a single API request.
- Default daily quota for this API is 10000.
```
