import unittest
from models.project import Project


class TestProjectModel(unittest.TestCase):

    def setUp(self):
        self.data_file = 'c:/bench/pmgr/data/projects.xls'

    def test_get(self):
        prjs = Project.get(self.data_file)
        pass