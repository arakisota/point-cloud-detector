import copy
from transform_pcd import transforamte_pcd
from visualize_keypoints import non_nms_visualize_keypoints

def set_theory1(pcd, radius=0.03, max_nn=10, threshold=1e-5):
    base_pcd = copy.deepcopy(pcd)
    what = "t"
    method = "harris3D"
    #原点:[0,0,0]
    k_n0, is_n0 = non_nms_visualize_keypoints(pcd, method, radius, max_nn, threshold)
    #原点:[0,0,1]
    heisin = [0, 0, -1]
    pcd, pcd_t_n1 = transforamte_pcd(cube, what, heisin)
    k_n1, is_n1 = non_nms_visualize_keypoints(pcd_t_n1, method, radius, max_nn, threshold)
    #原点:[0,1,0]
    heisin = [0, -1, 0]
    pcd, pcd_t_n2 = transforamte_pcd(cube, what, heisin)
    k_n2, is_n2 = non_nms_visualize_keypoints(pcd_t_n2, method, radius, max_nn, threshold)
    #原点:[0,1,1]
    heisin = [0, -1, -1]
    pcd, pcd_t_n3 = transforamte_pcd(cube, what, heisin)
    k_n3, is_n3 = non_nms_visualize_keypoints(pcd_t_n3, method, radius, max_nn, threshold)
    #原点:[1,0,0]
    heisin = [-1, 0, 0]
    pcd, pcd_t_n4 = transforamte_pcd(cube, what, heisin)
    k_n4, is_n4 = non_nms_visualize_keypoints(pcd_t_n4, method, radius, max_nn, threshold)
    #原点:[1,0,1]
    heisin = [-1, 0, -1]
    pcd, pcd_t_n5 = transforamte_pcd(cube, what, heisin)
    k_n5, is_n5 = non_nms_visualize_keypoints(pcd_t_n5, method, radius, max_nn, threshold)
    #原点:[1,1,0]
    heisin = [-1, -1, 0]
    pcd, pcd_t_n6 = transforamte_pcd(cube, what, heisin)
    k_n6, is_n6 = non_nms_visualize_keypoints(pcd_t_n6, method, radius, max_nn, threshold)
    #原点:[1,1,1]
    heisin = [-1, -1, -1]
    pcd, pcd_t_n7 = transforamte_pcd(cube, what, heisin)
    k_n7, is_n7 = non_nms_visualize_keypoints(pcd_t_n7, method, radius, max_nn, threshold)
    #点を立方体の中心に持ってくる
    heisin = [-0.5, -0.5, -0.5]
    pcd, pcd_t_n8 = transforamte_pcd(cube, what, heisin)
    k_n8, is_n8 = non_nms_visualize_keypoints(pcd_t_n8, method, radius, max_nn, threshold)

    #原点:[0,0,0]
    method = "harris3D"
    k_n01, is_n01 = non_nms_visualize_keypoints(k_n0, method, radius, max_nn, threshold)
    #原点:[0,0,1]
    method = "harris3D"
    k_n11, is_n11 = non_nms_visualize_keypoints(k_n1, method, radius, max_nn, threshold)
    #原点:[0,1,0]
    method = "harris3D"
    k_n21, is_n21 = non_nms_visualize_keypoints(k_n2, method, radius, max_nn, threshold)
    #原点:[0,1,1]
    method = "harris3D"
    k_n31, is_n31 = non_nms_visualize_keypoints(k_n3, method, radius, max_nn, threshold)
    #原点:[1,0,0]
    method = "harris3D"
    k_n41, is_n41 = non_nms_visualize_keypoints(k_n4, method, radius, max_nn, threshold)
    #原点:[1,0,1]
    method = "harris3D"
    k_n51, is_n51 = non_nms_visualize_keypoints(k_n5, method, radius, max_nn, threshold)
    #原点:[1,1,0]
    method = "harris3D"
    k_n61, is_n61 = non_nms_visualize_keypoints(k_n6, method, radius, max_nn, threshold)
    #原点:[1,1,1]
    method = "harris3D"
    k_n71, is_n71 = non_nms_visualize_keypoints(k_n7, method, radius, max_nn, threshold)
    #点を立方体の中心に持ってくる
    method = "harris3D"
    k_n81, is_n81 = non_nms_visualize_keypoints(k_n8, method, radius, max_nn, threshold)

    set_keys_plus_n2 = list(sorted(set(correct_idx(is_n0, is_n01)) | set(correct_idx(is_n1, is_n11)) | set(correct_idx(is_n2, is_n21)) | set(correct_idx(is_n3, is_n31)) | set(correct_idx(is_n4, is_n41)) | set(correct_idx(is_n5, is_n51)) | set(correct_idx(is_n6, is_n61)) | set(correct_idx(is_n7, is_n71)) | set(correct_idx(is_n8, is_n81))))
    pcd_set_plus2 = base_pcd.select_by_index(set_keys_plus_n2)

    return pcd_set_plus2

#和集合ver, パターン②
def set_theory2(pcd, radius=0.03, max_nn=10, threshold=1e-3):
    base_pcd = copy.deepcopy(pcd)
    what = "t"
    method = "harris3D"
    #原点:[0,0,0]
    k_n0, is_n0 = non_nms_visualize_keypoints(pcd, method, radius, max_nn, threshold)
    #原点:[0,0,1]
    heisin = [0, 0, -1]
    pcd, pcd_t_n1 = transforamte_pcd(cube, what, heisin)
    k_n1, is_n1 = non_nms_visualize_keypoints(pcd_t_n1, method, radius, max_nn, threshold)
    #原点:[0,1,0]
    heisin = [0, -1, 0]
    pcd, pcd_t_n2 = transforamte_pcd(cube, what, heisin)
    k_n2, is_n2 = non_nms_visualize_keypoints(pcd_t_n2, method, radius, max_nn, threshold)
    #原点:[0,1,1]
    heisin = [0, -1, -1]
    pcd, pcd_t_n3 = transforamte_pcd(cube, what, heisin)
    k_n3, is_n3 = non_nms_visualize_keypoints(pcd_t_n3, method, radius, max_nn, threshold)
    #原点:[1,0,0]
    heisin = [-1, 0, 0]
    pcd, pcd_t_n4 = transforamte_pcd(cube, what, heisin)
    k_n4, is_n4 = non_nms_visualize_keypoints(pcd_t_n4, method, radius, max_nn, threshold)
    #原点:[1,0,1]
    heisin = [-1, 0, -1]
    pcd, pcd_t_n5 = transforamte_pcd(cube, what, heisin)
    k_n5, is_n5 = non_nms_visualize_keypoints(pcd_t_n5, method, radius, max_nn, threshold)
    #原点:[1,1,0]
    heisin = [-1, -1, 0]
    pcd, pcd_t_n6 = transforamte_pcd(cube, what, heisin)
    k_n6, is_n6 = non_nms_visualize_keypoints(pcd_t_n6, method, radius, max_nn, threshold)
    #原点:[1,1,1]
    heisin = [-1, -1, -1]
    pcd, pcd_t_n7 = transforamte_pcd(cube, what, heisin)
    k_n7, is_n7 = non_nms_visualize_keypoints(pcd_t_n7, method, radius, max_nn, threshold)
    #点を立方体の中心に持ってくる
    heisin = [-0.5, -0.5, -0.5]
    pcd, pcd_t_n8 = transforamte_pcd(cube, what, heisin)
    k_n8, is_n8 = non_nms_visualize_keypoints(pcd_t_n8, method, radius, max_nn, threshold)

    set_keys_plus_n1 = list(sorted(set(is_n0) | set(is_n1) | set(is_n2) | set(is_n3) | set(is_n4) | set(is_n5) | set(is_n6) | set(is_n7) | set(is_n8)))
    pcd_set1 = pcd.select_by_index(set_keys_plus_n1)
    
    max_nn=5
    
    #原点:[0,0,0]
    k_n01, is_n01 = non_nms_visualize_keypoints(pcd_set1, method, radius, max_nn, threshold)
    #原点:[0,0,1]
    heisin = [0, 0, -1]
    pcd2, pcd_t_n11 = transforamte_pcd(pcd_set1, what, heisin)
    k_n11, is_n11 = non_nms_visualize_keypoints(pcd_t_n11, method, radius, max_nn, threshold)
    #原点:[0,1,0]
    heisin = [0, -1, 0]
    pcd2, pcd_t_n21 = transforamte_pcd(pcd_set1, what, heisin)
    k_n21, is_n21 = non_nms_visualize_keypoints(pcd_t_n21, method, radius, max_nn, threshold)
    #原点:[0,1,1]
    heisin = [0, -1, -1]
    pcd2, pcd_t_n31 = transforamte_pcd(pcd_set1, what, heisin)
    k_n31, is_n31 = non_nms_visualize_keypoints(pcd_t_n31, method, radius, max_nn, threshold)
    #原点:[1,0,0]
    heisin = [-1, 0, 0]
    pcd2, pcd_t_n41 = transforamte_pcd(pcd_set1, what, heisin)
    k_n41, is_n41 = non_nms_visualize_keypoints(pcd_t_n41, method, radius, max_nn, threshold)
    #原点:[1,0,1]
    heisin = [-1, 0, -1]
    pcd2, pcd_t_n51 = transforamte_pcd(pcd_set1, what, heisin)
    k_n51, is_n51 = non_nms_visualize_keypoints(pcd_t_n51, method, radius, max_nn, threshold)
    #原点:[1,1,0]
    heisin = [-1, -1, 0]
    pcd2, pcd_t_n61 = transforamte_pcd(pcd_set1, what, heisin)
    k_n61, is_n61 = non_nms_visualize_keypoints(pcd_t_n61, method, radius, max_nn, threshold)
    #原点:[1,1,1]
    heisin = [-1, -1, -1]
    pcd2, pcd_t_n71 = transforamte_pcd(pcd_set1, what, heisin)
    k_n71, is_n71 = non_nms_visualize_keypoints(pcd_t_n71, method, radius, max_nn, threshold)
    #点を立方体の中心に持ってくる
    heisin = [-0.5, -0.5, -0.5]
    pcd2, pcd_t_n81 = transforamte_pcd(pcd_set1, what, heisin)
    k_n81, is_n81 = non_nms_visualize_keypoints(pcd_t_n81, method, radius, max_nn, threshold)
    
    set_keys_plus_n2 = list(sorted(set(correct_idx(set_keys_plus_n1, is_n01)) | set(correct_idx(set_keys_plus_n1, is_n11)) | set(correct_idx(set_keys_plus_n1, is_n21)) | set(correct_idx(set_keys_plus_n1, is_n31)) | 
                          set(correct_idx(set_keys_plus_n1, is_n41)) | set(correct_idx(set_keys_plus_n1, is_n51)) | set(correct_idx(set_keys_plus_n1, is_n61)) | set(correct_idx(set_keys_plus_n1, is_n71)) | set(correct_idx(set_keys_plus_n1, is_n81))))
    pcd_set_plus2 = base_pcd.select_by_index(set_keys_plus_n2)

    return pcd_set_plus2

#和集合ver, パターン③
def set_theory3(pcd, radius=0.03, max_nn=10, threshold=1e-5):
    base_pcd = copy.deepcopy(pcd)
    what = "t"
    method = "harris3D"
    #原点:[0,0,0]
    k_n0, is_n0 = non_nms_visualize_keypoints(pcd, method, radius, max_nn, threshold)
    #原点:[0,0,1]
    heisin = [0, 0, -1]
    pcd, pcd_t_n1 = transforamte_pcd(cube, what, heisin)
    k_n1, is_n1 = non_nms_visualize_keypoints(pcd_t_n1, method, radius, max_nn, threshold)
    #原点:[0,1,0]
    heisin = [0, -1, 0]
    pcd, pcd_t_n2 = transforamte_pcd(cube, what, heisin)
    k_n2, is_n2 = non_nms_visualize_keypoints(pcd_t_n2, method, radius, max_nn, threshold)
    #原点:[0,1,1]
    heisin = [0, -1, -1]
    pcd, pcd_t_n3 = transforamte_pcd(cube, what, heisin)
    k_n3, is_n3 = non_nms_visualize_keypoints(pcd_t_n3, method, radius, max_nn, threshold)
    #原点:[1,0,0]
    heisin = [-1, 0, 0]
    pcd, pcd_t_n4 = transforamte_pcd(cube, what, heisin)
    k_n4, is_n4 = non_nms_visualize_keypoints(pcd_t_n4, method, radius, max_nn, threshold)
    #原点:[1,0,1]
    heisin = [-1, 0, -1]
    pcd, pcd_t_n5 = transforamte_pcd(cube, what, heisin)
    k_n5, is_n5 = non_nms_visualize_keypoints(pcd_t_n5, method, radius, max_nn, threshold)
    #原点:[1,1,0]
    heisin = [-1, -1, 0]
    pcd, pcd_t_n6 = transforamte_pcd(cube, what, heisin)
    k_n6, is_n6 = non_nms_visualize_keypoints(pcd_t_n6, method, radius, max_nn, threshold)
    #原点:[1,1,1]
    heisin = [-1, -1, -1]
    pcd, pcd_t_n7 = transforamte_pcd(cube, what, heisin)
    k_n7, is_n7 = non_nms_visualize_keypoints(pcd_t_n7, method, radius, max_nn, threshold)
    #点を立方体の中心に持ってくる
    heisin = [-0.5, -0.5, -0.5]
    pcd, pcd_t_n8 = transforamte_pcd(cube, what, heisin)
    k_n8, is_n8 = non_nms_visualize_keypoints(pcd_t_n8, method, radius, max_nn, threshold)

    set_keys_plus_n1 = list(sorted(set(is_n0) & set(is_n1) & set(is_n2) & set(is_n3) & set(is_n4) & set(is_n5) & set(is_n6) & set(is_n7) & set(is_n8)))
    pcd_set1 = pcd.select_by_index(set_keys_plus_n1)
    
    max_nn = 5
    #原点:[0,0,0]
    k_n01, is_n01 = non_nms_visualize_keypoints(pcd_set1, method, radius, max_nn, threshold)
    #原点:[0,0,1]
    heisin = [0, 0, -1]
    pcd2, pcd_t_n11 = transforamte_pcd(pcd_set1, what, heisin)
    k_n11, is_n11 = non_nms_visualize_keypoints(pcd_t_n11, method, radius, max_nn, threshold)
    #原点:[0,1,0]
    heisin = [0, -1, 0]
    pcd2, pcd_t_n21 = transforamte_pcd(pcd_set1, what, heisin)
    k_n21, is_n21 = non_nms_visualize_keypoints(pcd_t_n21, method, radius, max_nn, threshold)
    #原点:[0,1,1]
    heisin = [0, -1, -1]
    pcd2, pcd_t_n31 = transforamte_pcd(pcd_set1, what, heisin)
    k_n31, is_n31 = non_nms_visualize_keypoints(pcd_t_n31, method, radius, max_nn, threshold)
    #原点:[1,0,0]
    heisin = [-1, 0, 0]
    pcd2, pcd_t_n41 = transforamte_pcd(pcd_set1, what, heisin)
    k_n41, is_n41 = non_nms_visualize_keypoints(pcd_t_n41, method, radius, max_nn, threshold)
    #原点:[1,0,1]
    heisin = [-1, 0, -1]
    pcd2, pcd_t_n51 = transforamte_pcd(pcd_set1, what, heisin)
    k_n51, is_n51 = non_nms_visualize_keypoints(pcd_t_n51, method, radius, max_nn, threshold)
    #原点:[1,1,0]
    heisin = [-1, -1, 0]
    pcd2, pcd_t_n61 = transforamte_pcd(pcd_set1, what, heisin)
    k_n61, is_n61 = non_nms_visualize_keypoints(pcd_t_n61, method, radius, max_nn, threshold)
    #原点:[1,1,1]
    heisin = [-1, -1, -1]
    pcd2, pcd_t_n71 = transforamte_pcd(pcd_set1, what, heisin)
    k_n71, is_n71 = non_nms_visualize_keypoints(pcd_t_n71, method, radius, max_nn, threshold)
    #点を立方体の中心に持ってくる
    heisin = [-0.5, -0.5, -0.5]
    pcd2, pcd_t_n81 = transforamte_pcd(pcd_set1, what, heisin)
    k_n81, is_n81 = non_nms_visualize_keypoints(pcd_t_n81, method, radius, max_nn, threshold)
    
    set_keys_plus_n2 = list(sorted(set(correct_idx(set_keys_plus_n1, is_n01)) | set(correct_idx(set_keys_plus_n1, is_n11)) | set(correct_idx(set_keys_plus_n1, is_n21)) | set(correct_idx(set_keys_plus_n1, is_n31)) | 
                          set(correct_idx(set_keys_plus_n1, is_n41)) | set(correct_idx(set_keys_plus_n1, is_n51)) | set(correct_idx(set_keys_plus_n1, is_n61)) | set(correct_idx(set_keys_plus_n1, is_n71)) | set(correct_idx(set_keys_plus_n1, is_n81))))
    pcd_set_plus2 = base_pcd.select_by_index(set_keys_plus_n2)

    return pcd_set_plus2