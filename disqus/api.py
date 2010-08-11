import urllib2
import urllib

def _usingPy26():
    import sys
    return sys.hexversion > 0x20600f0

if _usingPy26():
    import json
else:
    import simplejson as json

from exceptions import Exception

from disqus.disqus_globals import POST_ACTIONS

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
    def __init__(self, e, uri, arg_string):
        self.e = e
        self.uri = uri
        self.arg_string = arg_string

    def __str__(self):
        return (
            "Disqus sent status %i for URL: %s using parameters: "
            "(%s)\ndetails: %s" %(
                self.e.code, self.uri, self.arg_string,
                self.e.fp.read()))

class DisqusCall(object):
    def __init__(self, api_key=None, partner_key=None,
                 domain='disqus.com', api_version='1.1',
                 method=''):
        self.api_key = api_key
        self.partner_key = partner_key
        self.domain = domain
        self.method = method
        self.api_version = api_version

    def __getattr__(self, k, **kwargs):
        try:
            return object.__getattr__(self, k)
        except AttributeError:
            return DisqusCall(api_key=self.api_key,
                              partner_key=self.partner_key,
                              domain=self.domain, api_version=self.api_version,
                              method=k)

    def __call__(self, **kwargs):
            # format the arguments
            kwargs['api_version'] = self.api_version
            if self.api_key:
                kwargs['user_api_key'] = self.api_key
            if self.partner_key:
                kwargs['partner_api_key'] = self.partner_key
            arg_string = urllib.urlencode(kwargs)

            # Get request type
            if self.method in POST_ACTIONS:
                request_type = "POST"
                body = arg_string
                uri = "http://%s/api/%s/" % (self.domain, self.method)
            else:
                request_type = "GET"
                body = None
                uri = "http://%s/api/%s/?%s" % (self.domain, 'get_' + \
                                                self.method, \
                                                arg_string)

            req = urllib2.Request(uri, body, {})
            try:
                handle = urllib2.urlopen(req)
                res = json.loads(handle.read())
                return res['message']
            except urllib2.HTTPError, e:
                if (e.code == 304):
                    return []
                else:
                    raise DisqusHTTPError(e, uri, arg_string)

class Disqus(DisqusCall):
    """
    The Disqus API class.

    Accessing members of this class returns RESTful data from the Disqus API.
    The data is then converted to python objects (lists and dicts).

    You can find more about the Disqus API here:

    http://docs.disqus.com/developers

    Examples:
    ---------

    # Init with your API key. To find out your key visit
    # http://disqus.com/api/get_my_key while logged in to disqus.com.
    disqus = Disqus(secret_key)

    # Get a list of forums that user owns
    disqus.forum_list()

    # Get a list of posts on a forum
    disqus.forum_posts(forum_id=1)

    # Get a list of categories on a forum
    disqus.categories_list(forum_id=2)

    # Get a list of threads on a forum
    disqus.thread_list(forum_id=2)

    # Get a list of updated threads on a forum
    disqus.updated_threads(forum_id=1)

    # Get a list of posts on a thread
    disqus.thread_posts(thread_id=1)

    # Get a particular thread or create it if it doesn't exist
    disqus.thread_by_identifier(forum_id=1, identifier='my_thread',
                                title='My Killer Thread')
    # or
    disqus.thread_by_url(url='http://my.awesome/thread')

    # Update a thread
    disqus.update_thread(forum_id=1, thread_id=4)

    # Create a new post
    disqus.create_post(site_id=1, thread_id=4,
                       message='Dope API, yo!')

    # Moderate a post
    disqus.moderate_post(post_id=234, action='spam')
    disqus.moderate_post(post_id=123, action='approve')
    disqus.moderate_post(post_id=324, action='kill')

    Using the data returned:
    ------------------------

    All API calls are returned in decoded JSON. This is converted into python
    objects.

    x = disqus.forum_list()

    # The first forum
    x[0]

    # The description of the first forum
    x[0]['description']

    # The shortname of the first forum
    x[0]['shortname']

    """
    def __init__(self, api_key=None, partner_key=None, domain="disqus.com",
                 api_version='1.1'):
        """
        Creates a new Disqus API connector.

        Pass an Auth object initialized with your Disqus API key. To get your
        Disqus API key visit http://disqus.com/api/get_my_key while logged in.
        """
        DisqusCall.__init__(self, api_key=api_key, partner_key=partner_key,
                            domain=domain, api_version=api_version)
