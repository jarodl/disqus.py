disqus.py
==============

A Python API for interacting with Disqus, a great community platform for
managing comments on your site.

## Usage

Init with your API key. To find out your key visit
[this page](http://disqus.com/api/get_my_key) while logged in to disqus.com.
    disqus = Disqus(secret_key)

Get a list of forums that user owns
    disqus.forum_list()

Get a list of posts on a forum
    disqus.forum_posts(forum_id=1)

Get a list of categories on a forum
    disqus.categories_list(forum_id=2)

Get a list of threads on a forum
    disqus.thread_list(forum_id=2)

Get a list of updated threads on a forum
    disqus.updated_threads(forum_id=1)

Get a list of posts on a thread
    disqus.thread_posts(thread_id=1)

Get a particular thread or create it if it doesn't exist
    disqus.thread_by_identifier(forum_id=1, identifier='my_thread',
                                title='My Killer Thread')
or
    disqus.thread_by_url(url='http://my.awesome/thread')

Update a thread
    disqus.update_thread(forum_id=1, thread_id=4)

Create a new post
    disqus.create_post(site_id=1, thread_id=4,
                       message='Dope API, yo!')

Moderate a post
    disqus.moderate_post(post_id=234, action='spam')
    disqus.moderate_post(post_id=123, action='approve')
    disqus.moderate_post(post_id=324, action='kill')

## Installation

`pip install disqus`

## Credit

[Tweepy](http://github.com/joshthecoder/tweepy) and
[The Twitter Python API](http://github.com/sixohsix/twitter) were a
great help for structure and ideas.
