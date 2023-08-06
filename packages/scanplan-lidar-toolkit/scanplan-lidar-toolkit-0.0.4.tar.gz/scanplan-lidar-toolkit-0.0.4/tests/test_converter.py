import unittest
import laspy
from os.path import abspath, dirname

from ltk.io.converter import LIO


class TestingIO(unittest.TestCase):
    """ Testing Lidar IO methods """
    def setUp(self):
        # initial an instance
        self.lio = LIO()
        self.test_dir = dirname(abspath(__file__))
        self.lasfile = f"{self.test_dir}/data/las_small.las"
        self.lazfile = f"{self.test_dir}/data/las_small.laz"
        self.e57file = f"{self.test_dir}/data/las_small.e57"

    def tearDown(self):
        pass

    def test_las2numpy_f(self):
        points = self.lio.las2numpy(self.lasfile)
        self.assertEqual(len(points), 9089)

    def test_las2numpy_(self):
        lasdata = laspy.read(self.lasfile)
        points = self.lio.las2numpy(lasdata)
        self.assertEqual(len(points), 9089)

    def test_laz2numpy_f(self):
        points = self.lio.las2numpy(self.lazfile)
        self.assertEqual(len(points), 9089)

