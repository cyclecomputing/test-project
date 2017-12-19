import unittest

class TestCluster(unittest.TestCase):
    def test_chef(self):
        # The chef cookbook writes a file to disk, make sure it's there and has the write content
        with open('/tmp/chef-text.txt', 'r') as f:
            self.assertEquals("This is a test written from chef!", f.read())

    def test_cluster_init(self):
        # The cluster init downloads a datafile (jetpack download) and then writes it's contents to a file
        # Make usre this is the case
        with open('/tmp/test.txt', 'r') as f:
            self.assertEquals("This is content in a data file!", f.read())
