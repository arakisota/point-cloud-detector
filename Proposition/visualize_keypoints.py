import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib

def non_nms_harris3D(pcd, radius, max_nn,threshold):
    pcd.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius, max_nn=max_nn))
    pcd_tree = o3d.geometry.KDTreeFlann(pcd)
    harris = np.zeros(len(np.asarray(pcd.points)))
    is_active = np.zeros(len(np.asarray(pcd.points)), dtype=bool)

    # Compute Harris response
    for i in range( len(np.asarray(pcd.points)) ):
        [num_nn, inds, _] = pcd_tree.search_knn_vector_3d(pcd.points[i], max_nn)
        pcd_normals = pcd.select_by_index(inds)
        pcd_normals.points = pcd_normals.normals
        [_, covar] = pcd_normals.compute_mean_and_covariance()
        if np.trace(covar) != 0:
            harris[ i ] = np.linalg.det( covar ) / np.trace( covar )
        if (harris[ i ] > threshold):
            is_active[ i ] = True
    keypoints = pcd.select_by_index(np.where(is_active)[0])
    return keypoints, np.where(is_active)[0]

def non_nms_visualize_keypoints(pcd, method="harris3D", radius=0.03, max_nn=10, threshold=1e-5):
    pcd.paint_uniform_color([0.5, 0.5, 0.5])
    if method == "harris3D":
        keypoints, is_active = non_nms_harris3D(pcd, radius, max_nn, threshold)
    else:
        keypoints, finish = ISS(pcd, salient_radius=0.0, non_max_radius=0.0, gamma_21=0.975, gamma_32=0.975)
        zero=[]
    print(np.asarray(keypoints))
    #KD-treeの構築
    pcd_tree = o3d.geometry.KDTreeFlann(pcd)
    #pcd.colors[0] = [1, 0, 0]
    #print(np.asarray(pcd.points[0]))

    #原点の座標を追加
    #点群型データ作成
    pcd_2 = o3d.geometry.PointCloud()
    pcd_2.points.append([0, 0, 0])
    #o3d.visualization.draw_geometries([keypoints_to_spheres(pcd_2, radius = 0.1), keypoints_to_spheres(keypoints, radius = 0.01), pcd])
    #o3d.visualization.draw_geometries([keypoints_to_spheres(keypoints, radius = 0.01), pcd])
    #print(f"検出された特徴点の数 : {keypoints}")
    return keypoints, is_active