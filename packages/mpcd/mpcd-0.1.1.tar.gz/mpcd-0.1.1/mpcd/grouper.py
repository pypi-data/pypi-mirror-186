from pathlib import Path
import numpy as np
import subprocess
from tqdm import tqdm
import sys
import os
import shutil



def get_namelist(folder):
    res = []
    for i in folder.iterdir():
        if i.name == ".DS_Store":
            continue
        ts = i.stem
        if len(str(ts)) >= 13:
            ts = round(int(ts) / 1000)
            path_new = i.with_name(str(ts) + i.suffix)
            i.rename(path_new)
        res.append(ts)
    return np.array(sorted(res), dtype=int)


def find_closest(timestamp, timestamp_list):
    closest = [timestamp]
    for i in timestamp_list:
        absolute_val_array = np.abs(i - timestamp)
        smallest_difference_index = absolute_val_array.argmin()
        closest_element = i[smallest_difference_index]
        if abs(closest_element - timestamp) < 50000:
            closest.append(closest_element)
        else:
            return None
    return closest


def group(path,output_dir):
    sensor_dir = Path(path)
    reference_sensor = "front_center_radar"
    radars = [
        "front_left_radar",
        "front_right_radar",
        "rear_right_radar",
        "rear_left_radar",
    ]
    cameras = ["front_left_cam", "front_right_cam", "front_wide_cam"]
    lidars = ["top_lidar"]
    sensors = [reference_sensor] + radars + cameras + lidars
    name_list = {}
    for sensor in sensors:
        name_list[sensor] = get_namelist(sensor_dir / sensor)

    subprocess.Popen(f"rm -rf {output_dir}", shell=True)
    subprocess.Popen(f"mkdir -p {output_dir}", shell=True)
    
    for i in tqdm(name_list[reference_sensor]):
        res = find_closest(i, [name_list[i] for i in sensors if i != reference_sensor])
        if res is not None:
            for count, sensor in enumerate(sensors):
                Path(f'{output_dir}/{res[0]}/{sensor}/').mkdir(parents=True, exist_ok=True)
                subprocess.Popen(f'cp {sensor_dir}/{sensor}/{res[count]}.* {output_dir}/{res[0]}/{sensor}/', shell=True)

# def merge_pcd(output_path):
#     from MB_extr_mat import extr_mat
#     vis = PointCloudVisualizer()
#     cur = Path(output_path)


#     reference_sensor = "front_center_radar"
#     radars = [
#         "front_left_radar",
#         "front_right_radar",
#         "rear_right_radar",
#         "rear_left_radar",
#     ]
#     radars_5 = [reference_sensor] + radars
#     cameras = ["front_left_cam", "front_right_cam", "front_wide_cam"]
#     lidars = ["top_lidar"]

#     sensor_dict = {}
#     sensors = [reference_sensor] + radars + lidars
#     for timestamp_dir in cur.iterdir():
#         if timestamp_dir.is_dir() and timestamp_dir.name.isdigit():
#             sensor_dict[timestamp_dir.name] = {"radar": {},"lidar": {}}
#             for radar in radars_5:
#                 radar_pcd = list((timestamp_dir / radar).iterdir())
#                 assert len(radar_pcd) == 1
#                 sensor_dict[timestamp_dir.name]["radar"][radar] = radar_pcd[0]
#             lidar_pcd = list((timestamp_dir / lidars[0]).iterdir())
#             assert len(lidar_pcd) == 1
#             sensor_dict[timestamp_dir.name]["lidar"][lidars[0]] = lidar_pcd[0]

#     for time_stamp, sensor_paths in tqdm(sensor_dict.items()):
#         pc_list = []
#         for radar, radar_path in sensor_paths['radar'].items():
#             if radar != 'front_center_radar':
#                 pc_list.append(PointCloud.from_path(radar_path).coor_trans(extr_mat[radar]))

#         concat_radar = PointCloud.pc_concat(pc_list)
#         concat_radar.save_pcd(f"{output_path}/{time_stamp}_concat_radar.pcd")

#         lidar_pc = PointCloud.from_path(sensor_paths['lidar']['top_lidar'])
#         #lidar_pc=lidar_pc.coor_trans(extr_mat['top_lidar'])
#         lidar_pc.save_pcd(f"{output_path}/{time_stamp}_lidar.pcd")

#         v = vis.draw_pc_overlay(((lidar_pc,'gray',0),(concat_radar,'red',1)))
#         print(v.shape)
#         from IPython import embed; embed(colors='neutral')


# def pcd2png():
#     path=Path('concat')
#     for i in path.iterdir():
#         if i.is_file() and i.suffix == '.pcd':
#             PointCloud.from_path(str(i)).draw_pcloud(color='gray',r=1,save=True,show=False, save_path=str(i.with_suffix('.png')))


if __name__ == "__main__":
    group('raw_data','output')
    #merge_pcd('output')
    #pcd2png()
