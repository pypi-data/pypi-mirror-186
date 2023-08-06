``mpcd``
=======

----
Pure Python module to read and write point clouds stored in the [PCD file
format](http://pointclouds.org/documentation/tutorials/pcd_file_format.php),
used by the [Point Cloud Library](http://pointclouds.org/).
Folk from pypcd: https://github.com/dimatura/pypcd

```python
import mpcd
# also can read from file handles.
pc = mpcd.PointCloud.from_path('foo.pcd')
# pc.pc_data has the data as a structured array
# pc.fields, pc.count, etc have the metadata

# center the x field
pc.pc_data['x'] -= pc.pc_data['x'].mean()

# save as binary compressed
pc.save_pcd('bar.pcd', compression='binary_compressed')
```


I want to congratulate you / insult you
----------
My email is `mail@yuehao.wang`.

Copyright (C) 2023 Yuehao Wang
# mpcd
