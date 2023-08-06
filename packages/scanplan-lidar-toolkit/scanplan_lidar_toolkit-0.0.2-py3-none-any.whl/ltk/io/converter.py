import logging
import laspy
from laspy import LasData
import numpy as np
import open3d as o3d

logger = logging.getLogger(__name__)


class LIO:
    """ Methods for lidar and pointcloud data conversion """

    def las2numpy(self, lasfile: str or LasData) -> np.ndarray:
        """
        convert las to numpy
        :param lasfile: las or laz file or lasdata
        :return: n*3 array
        """
        if isinstance(lasfile, str):
            lasdata = laspy.read(lasfile)
        elif isinstance(lasfile, LasData):
            lasdata = lasfile
        else:
            raise AttributeError("unknown data type!")

        points = np.vstack((lasdata.x, lasdata.y, lasdata.z)).T
        logger.info(points.shape)
        return points

    def las2pcd(self):
        pass

    def numpy2pcd(self):
        pass
