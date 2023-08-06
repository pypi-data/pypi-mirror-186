from mpcd.mpcd import PointCloud
from mpcd.visualizer import PointCloudVisualizer

import datetime
__version__ = datetime.datetime.now().strftime('%Y.%m.%d.%H%M')

__all__ = ['PointCloud', '__version__','PointCloudVisualizer']


if __name__ == "__main__":
    print(__version__)