import unittest
from disqus import *

"""Configuration"""
# Must supply a Disqus API key for tests
secret_key = ''
# A partner key is only required by some API calls
partner_key = ''

"""Unit Tests"""

class DisqusAPITests(unittest.TestCase):

    def setUp(self):
        self.partner = Disqus(partner_key=partner_key)
        self.api = Disqus(api_key=secret_key)
        self.forum_id = self.api.forum_list()[0]['id']
        self.forum_api_key = self.api.forum_api_key(forum_id=self.forum_id)
        self.thread_id = self.api.thread_list(forum_id=self.forum_id)[0]['id']
        self.post_id = self.api.forum_posts(forum_id=self.forum_id)[0]['id']

    def testForumList(self):
        self.api.forum_list()

    def testPostsOnForum(self):
        self.api.forum_posts(forum_id=self.forum_id)

    def testCategoryList(self):
        self.api.categories_list(forum_id=self.forum_id)

    def testUpdatedThreads(self):
        self.api.updated_threads(forum_id=self.forum_id,
                                 since='2009-03-30T15:41')

    def testThreadByIdentifier(self):
        """
        Warning, this will create a new thread if it does not exist.
        """
        self.api.thread_by_identifier(forum_api_key=self.forum_api_key,
                                      identifier='my_thread',
                                      title='My Thread')
    # def testThreadByUrl(self):
        # self.api.thread_by_url(url="http://my.test/thread/")

    def testUpdateThread(self):
        self.api.update_thread(forum_id=self.forum_id, thread_id=self.thread_id,
                               forum_api_key=self.forum_api_key)

    def testCreatePost(self):
        self.api.create_post(thread_id=self.thread_id,
                             message='Testing Disqus Python Lib',
                             author_name='Disqus',
                             author_email='test@disqus.com',
                             forum_api_key=self.forum_api_key)

    def testModeratePost(self):
        self.api.moderate_post(post_id=self.post_id, action='approve')

    def testPartnerRecentForums(self):
        self.partner.recent_forums_comments()

    def testPartnerUserComments(self):
        self.partner.user_comments(username='jarodluebbert', forum_id='276227')

    def testPartnerUserInfo(self):
        self.partner.user_info(username='jarodluebbert')

    def testPartnerMostCommented(self):
        self.partner.most_commented_threads(forum_id='276227')

if __name__ == '__main__':
    unittest.main()
