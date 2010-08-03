import urllib2

from exceptions import Exception

from disqus.disqus_globals import POST_ACTIONS
from disqus.auth import NoAuth

class DisqusError(Exception):
    """
    Base Exception thrown by the Disqus object when there is an error
    interacting with the API.
    """
    pass

class DisqusHTTPError(DisqusError):
    """
    Exception thrown by the Disqus object when there is an HTTP error
    interacting with disqus.com
    """
    def __init__(self, e, uri, format, uriparts):
        self.e = e
        self.uri = uri
        self.format = format
        self.uriparts = uriparts

    def __str__(self):
        return (
            "Disqus sent status %i for URL: %s.%s using parameters: "
            "(%s)\ndetails: %s" %(
                self.e.code, self.uri, self.format, self.uriparts,
                self.e.fp.read()))

class DisqusCall(self):
    pass

class Disqus(self):
    """
    The Disqus API class.

    Accessing members of this class returns RESTful data from the Disqus API.
    The data is returned as python objects (lists and dicts).

    You can find more about the Disqus API here:

    http://docs.disqus.com/developers

    Examples:
    ---------

    disqus = Disqus(auth=Auth(secret_key))

    # Get a list of sites that user owns
    disqus.sites.all()

    # Get a list of comments on a site
    disqus.sites.comments(site=site_id)

    # Get a list of categories on a site
    disqus.sites.categories(site=site_id)

    # Get a list of threads on a site
    disqus.sites.threads(site=site_id)

    # Get a particular thread
    disqus.sites.thread(site=site_id, thread=thread_id)

    # Create a new post
    disqus.sites.thread.post.new(site=site_id, thread=thread_id,
                                 message='Dope API, yo!')

    # Delete a post
    disqus.sites.thread.post.delete(post=post_id)

    # Mark a post as spam
    disqus.sites.thread.post.mark_spam(post=post_id)

    # Approve a post
    disqus.sites.thread.post.approve(post=post_id)

    Using the data returned:
    ------------------------

    All API calls are returned in decoded JSON. This is converted into python
    objects.

    x = disqus.sites.all()

    # The first site
    x[0]

    # The description of the first site
    x[0]['description']

    # The shortname of the first site
    x[0]['shortname']

    """
    def __init__(self, domain="disqus.com", auth=None, api_version='1.1'):
        """
        Creates a new Disqus API connector.

        Pass an Auth object initialized with your Disqus API key. To get your
        Disqus API key visit http://disqus.com/api/get_my_key while logged in.
        """
        if not auth:
            auth = NoAuth()

        uriparts = (str(api_version),)

        DisqusCall.__init__(
            self, auth=auth, domain=domain, uriparts=uriparts)


__all__ = ["Disqus", "DisqusError", "DisqusHTTPError"]
