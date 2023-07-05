import copy
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
import pandas as pd

def transforamte_pcd(pcd, what, heisin, query=0, angle_pi=3):

    if what == "r":
        #回転
        angle = np.pi/angle_pi
        R = o3d.geometry.get_rotation_matrix_from_yxz([angle, 0, 0])
        print("回転行列 R : ", np.round(R, 7))
        print("-"*100)
        pcd_r = copy.deepcopy(pcd).rotate(R, center=np.asarray(pcd.points)[query])
        #o3d.visualization.draw_geometries([pcd, pcd_r])
        pcd_trans = pcd_r
    elif what == "t":
        #並進
        t = heisin
        print("並進行列 T : ", t)
        print("-"*100)
        pcd_t = copy.deepcopy(pcd).translate(t)
        #o3d.visualization.draw_geometries([pcd, pcd_t])
        pcd_trans = pcd_t
    elif what == "rt":
        #回転と並進
        angle = np.pi/angle_pi
        R = o3d.geometry.get_rotation_matrix_from_yxz([angle, 0, 0])
        #t = [0.5, 0.7, 1]
        t = heisin
        RT = np.eye(4)
        RT[:3, :3] = R
        RT[:3, 3] = t
        print("回転・並進 RT : ", RT)
        print("-"*100)
        pcd_rt = copy.deepcopy(pcd).transform(RT)
        #o3d.visualization.draw_geometries([pcd, pcd_rt])
        pcd_trans = pcd_rt
    elif what == "s":
        #スケール
        pcd_s = copy.deepcopy(pcd)
        print("Scale")
        print("-"*100)
        pcd_s.scale(0.5, center=pcd_s.get_center())
        #o3d.visualization.draw_geometries([pcd, pcd_s])            
        pcd_trans = pcd_s

    return pcd, pcd_trans