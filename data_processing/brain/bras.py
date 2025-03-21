from collections import Counter
import os
import PIL
import cv2
import tarfile
import numpy as np
import pydicom
import pandas as pd
from glob import glob
import nibabel as nib
from PIL import Image
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

path = '/home/jinan/Datasets/Medical-datasets/BraTS'

#print(os.listdir(path))
print(len(os.listdir(path)))

brats = '/home/jinan/Datasets/Medical-datasets/BraTS'

dir_list = os.listdir(brats)
id_all = []
for i in dir_list:
    id_all.append(i.split('_')[-1])
print('ALL:', len(id_all), ' id')
print(id_all)

train_id = ['00753', '00170', '01273', '00441', '00651', '01301', '01530', '00705', '01035', '00218', '01344', '01628', '01363', '01551', '01333', '01119', '00243', '01039', '00206', '00014', '01500', '01137', '01434', '00746', '00788', '00688', '00063', '01322', '00373', '00530', '00288', '01566', '01255', '01234', '01389', '00332', '01407', '01365', '00729', '00675', '01091', '00222', '01439', '01516', '01034', '00043', '00262', '00550', '00732', '01108', '00684', '01637', '01459', '01622', '00162', '00321', '00496', '00171', '00157', '01422', '01025', '01331', '00775', '00557', '01086', '00102', '01133', '01472', '00380', '01186', '01423', '01132', '01178', '00708', '00584', '00778', '00148', '01341', '01663', '01526', '01480', '00772', '00193', '00344', '01443', '01600', '01102', '00433', '01594', '01615', '01397', '01451', '00061', '01520', '01149', '01230', '00329', '01509', '01208', '01548', '00715', '00836', '01154', '01088', '00227', '00615', '01536', '00544', '00795', '00228', '00731', '00687', '01376', '01623', '01607', '00296', '00419', '00379', '00758', '01327', '01557', '00782', '01298', '00113', '01408', '00547', '00626', '00589', '00378', '01077', '01592', '01152', '00540', '01493', '00104', '00382', '01116', '01560', '01222', '01556', '01626', '00045', '00192', '00690', '01405', '00604', '01492', '01393', '01588', '01488', '01624', '01404', '00348', '01107', '00155', '00144', '01007', '00692', '01350', '00730', '01205', '01611', '00152', '01353', '01264', '01617', '01559', '01279', '01203', '00346', '01527', '00658', '01054', '01468', '00237', '00645', '01348', '00292', '00601', '01499', '00455', '00613', '00253', '01308', '01662', '01276', '01431', '00350', '00003', '01319', '00442', '01318', '01614', '00511', '00316', '00650', '00353', '01438', '00735', '01184', '01651', '00403', '01068', '01571', '00737', '01219', '00802', '00425', '00251', '00209', '00676', '01240', '01630', '00033', '00195', '00258', '01549', '01117', '01508', '00320', '01196', '01437', '01129', '00830', '00046', '01464', '01236', '01421', '01340', '00523', '01656', '00376', '00260', '00317', '00199', '01227', '00506', '01638', '00811', '01448', '00136', '01010', '00108', '01274', '00744', '00674', '01570', '00270', '00582', '01247', '01369', '01309', '00545', '00472', '00289', '00058', '01591', '01349', '01147', '01000', '00386', '00313', '01543', '01377', '00641', '01249', '00271', '01257', '01660', '00005', '01173', '00599', '01176', '01351', '01497', '00196', '00504', '01259', '01074', '00532', '00024', '01580', '01224', '01618', '01131', '01207', '01193', '00704', '01036', '01237', '00339', '01291', '01585', '01272', '01289', '00602', '00241', '01561', '00549', '01201', '01355', '00834', '00035', '00311', '00597', '00098', '00780', '01099', '00165', '00240', '01314', '00466', '00274', '00837', '01469', '01426', '00284', '00044', '00352', '01538', '00464', '00194', '00576', '01535', '00285', '01440', '01420', '00444', '01031', '00622', '01159', '01317', '01214', '01123', '00364', '00390', '00275', '01288', '00349', '01332', '01212', '00054', '00479', '00008', '00470', '01417', '00571', '00736', '01643', '00412', '00800', '01470', '01540', '01046', '01610', '00097', '01635', '01275', '01037', '01246', '01055', '00520', '00636', '01016', '01572', '00387', '00514', '00122', '01481', '00767', '00389', '01446', '00070', '01017', '01002', '01334', '01629', '00328', '01620', '01174', '01330', '01644', '00110', '01033', '00127', '01529', '01447', '01128', '00459', '01162', '00322', '01435', '00280', '01352', '01059', '01009', '00246', '01258', '01539', '00238', '01192', '00120', '01243', '00239', '00101', '01210', '00149', '00493', '00639', '01457', '00351', '01412', '00306', '01235', '00049', '00188', '00751', '01366', '00631', '00525', '00756', '00451', '01510', '00327']

valid_normal_id = ['01505', '00250', '00574', '01368', '00563', '01452', '00025', '01100', '01631', '01325', '00659', '01359', '00793', '01251', '01181', '00747', '01001', '00405', '00551', '01514', '01342', '01555', '01085', '01456', '01093', '01616', '00177', '01177', '01191', '00555', '00784', '00809', '01395', '01183', '00341', '00303', '00100', '01164', '01427']

test_normal_id = ['01328', '00485', '01287', '01589', '01586', '00453', '00649', '00495', '00642', '00457', '00291', '01244', '01398', '00618', '01028', '01248', '00570', '01453', '01027', '00652', '00166', '00537', '00020', '00078', '01103', '01127', '00750', '00305', '00777', '00478', '00488', '01221', '00254', '01545', '01052', '00026', '00723', '01115', '01474', '00118', '00596', '01356', '00085', '01487', '01394', '01118', '00542', '01135', '01649', '00283', '01187', '00806', '01082', '00728', '01146', '00139', '01081', '00624', '00431', '00805', '01364', '01048', '00066', '00204', '01305', '00594', '00072', '00598', '00554', '01441', '00249', '01056', '01390', '00146', '00621', '01030', '00219', '01277', '00018', '00516', '01372', '01550', '01166', '00011', '01020', '01014', '01062', '01023', '00383', '01075', '00524', '01579', '00000', '00556', '00331', '00186', '01109', '00021', '00656', '00839', '01383', '01097', '01112', '01011', '01381', '00796', '01083', '01122', '01599', '00231', '00421', '00230', '01268', '00314', '01563', '01150', '00491', '00210', '00628', '00682', '01652', '01165', '00578', '01534', '00056', '01382', '01501', '00831', '01245', '01604', '01577', '00694', '01043', '00089', '01361', '00273', '00768', '01442', '00269', '00140', '01295', '00580', '01518', '01106', '01271', '00261', '01450', '01336', '00356', '01263', '01008', '01633', '01161', '01057', '00612', '00646', '00799', '01460', '00593', '00500', '01094', '00028']

abnormal_id = list(set(id_all)-set(train_id)-set(valid_normal_id)-set(test_normal_id))
#print(len(abnormal_id))

valid_abnormal_id = abnormal_id[:11]
#print(len(valid_abnormal_id))

test_abnormal_id = list(set(abnormal_id)-set(valid_abnormal_id))
#print(len(test_abnormal_id))


# !!! FOR TRAIN DATA: 7,500 samples (424 id)
root = '/home/jinan/Datasets/Medical-datasets/Brain/train/'
good = []
Ungood = []

for img_id in train_id:
    isgood = 'good'
    if img_id == "Store":
        continue
    flair = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_flair.nii.gz'
    seg = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_seg.nii.gz'
    
    flair = nib.load(flair).get_fdata()
    seg = nib.load(seg).get_fdata()

    assert flair.shape[-1] == 155
    assert seg.shape[-1] == 155

    for j in range(60, 100):
        img_path = os.path.join(root, isgood, str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if np.max(seg[:, :, j]) >= 1:
            continue
        good.append(img_path)
        plt.imsave(img_path, flair[:, :, j], cmap="bone")

print(good)
print(len(good))


path = '/home/jinan/Datasets/Medical-datasets/Brain/train/good/'

dir_list = os.listdir(path)
print('train (normal): ', len(dir_list), ' 424 id')


# !!! FOR VALID NORMAL DATA: 39 samples (39 id)
root = '/home/jinan/Datasets/Medical-datasets/Brain/valid/'
good = []
Ungood = []


for img_id in valid_normal_id:
    isgood = 'good'
    if img_id == "Store":
        continue
    flair = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_flair.nii.gz'
    seg = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_seg.nii.gz'
    
    flair = nib.load(flair).get_fdata()
    seg = nib.load(seg).get_fdata()

    assert flair.shape[-1] == 155
    assert seg.shape[-1] == 155

    for j in range(60, 100):
        img_path = os.path.join(root, isgood, 'img', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'img')) == False:
            os.mkdir(os.path.join(root, isgood, 'img'))
        label_path = os.path.join(root, isgood, 'label', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'label')) == False:
            os.mkdir(os.path.join(root, isgood, 'label'))
        if np.max(seg[:, :, j]) >= 1:
            continue
        good.append(img_path)
        Ungood.append(label_path)
        plt.imsave(img_path, flair[:, :, j], cmap="bone")
        plt.imsave(label_path, seg[:, :, j], cmap="bone")

path = '/home/jinan/Datasets/Medical-datasets/Brain/valid/good/img/'
label_path = '/home/jinan/Datasets/Medical-datasets/Brain/valid/good/label/'
assert os.listdir(path) == os.listdir(label_path)
dir_list = os.listdir(path)

print('valid (normal): ', len(dir_list), ' 39 id')


# !!! FOR VALID ABNORMAL DATA: 44 samples (11 id)
root = '/home/jinan/Datasets/Medical-datasets/Brain/valid/'
good = []
Ungood = []


for img_id in valid_abnormal_id:
    isgood = 'Ungood'
    if img_id == "Store":
        continue
    flair = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_flair.nii.gz'
    seg = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_seg.nii.gz'
    
    flair = nib.load(flair).get_fdata()
    seg = nib.load(seg).get_fdata()

    assert flair.shape[-1] == 155
    assert seg.shape[-1] == 155

    for j in range(60, 100, 10):
        img_path = os.path.join(root, isgood, 'img', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'img')) == False:
            os.mkdir(os.path.join(root, isgood, 'img'))
        label_path = os.path.join(root, isgood, 'label', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'label')) == False:
            os.mkdir(os.path.join(root, isgood, 'label'))
        # if np.max(seg[:, :, j]) >= 1:
        #     continue
        good.append(img_path)
        Ungood.append(label_path)
        plt.imsave(img_path, flair[:, :, j], cmap="bone")
        plt.imsave(label_path, seg[:, :, j], cmap="bone")

path = '/home/jinan/Datasets/Medical-datasets/Brain/valid/Ungood/img/'
label_path = '/home/jinan/Datasets/Medical-datasets/Brain/valid/Ungood/label/'
assert os.listdir(path) == os.listdir(label_path)
dir_list = os.listdir(path)

print('valid (abnormal): ', len(dir_list), ' 11 id')


# !!! FOR TEST NORMAL DATA: 640 samples (162 id)
root = '/home/jinan/Datasets/Medical-datasets/Brain/test/'
good = []
Ungood = []


for img_id in test_normal_id:
    isgood = 'good'
    if img_id == "Store":
        continue
    flair = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_flair.nii.gz'
    seg = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_seg.nii.gz'
    
    flair = nib.load(flair).get_fdata()
    seg = nib.load(seg).get_fdata()

    assert flair.shape[-1] == 155
    assert seg.shape[-1] == 155

    for j in range(60, 100):
        img_path = os.path.join(root, isgood, 'img', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'img')) == False:
            os.mkdir(os.path.join(root, isgood, 'img'))
        label_path = os.path.join(root, isgood, 'label', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'label')) == False:
            os.mkdir(os.path.join(root, isgood, 'label'))
        if np.max(seg[:, :, j]) >= 1:
            continue
        good.append(img_path)
        Ungood.append(label_path)
        plt.imsave(img_path, flair[:, :, j], cmap="bone")
        plt.imsave(label_path, seg[:, :, j], cmap="bone")

print(len(good))
print(good[0])
print(len(Ungood))
print(Ungood[0])

path = '/home/jinan/Datasets/Medical-datasets/Brain/test/good/img/'
label_path = '/home/jinan/Datasets/Medical-datasets/Brain/test/good/label/'
assert os.listdir(path) == os.listdir(label_path)
dir_list = os.listdir(path)

print('test (normal): ', len(dir_list), ' 162 id')


for i in range(len(dir_list)):
    dir_list[i] = dir_list[i].split('_')[0]
print(len(list(set(dir_list))))
df = pd.DataFrame(dict(Counter(dir_list)).items(), columns=['id', 'num_of_normal']).reset_index(drop=True)
df= df.sort_values(by='num_of_normal', ascending=False)
print(df[:424]['id'].tolist())
print(df[424:586]['id'].tolist())
print(df[586:]['id'].tolist())
print(len(df[:424]['id'].tolist()), len(df[424:586]['id'].tolist()), len(df[586:]['id'].tolist()))

df.to_csv('brain.csv', index=False)


# !!! FOR VALID ABNORMAL DATA:  samples (615 id)
root = '/home/jinan/Datasets/Medical-datasets/Brain/test/'
good = []
Ungood = []


for img_id in test_abnormal_id:
    isgood = 'Ungood'
    if img_id == "Store":
        continue
    flair = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_flair.nii.gz'
    seg = f'/home/jinan/Datasets/Medical-datasets/BraTS/BraTS2021_{img_id}/BraTS2021_{img_id}_seg.nii.gz'
    
    flair = nib.load(flair).get_fdata()
    seg = nib.load(seg).get_fdata()

    assert flair.shape[-1] == 155
    assert seg.shape[-1] == 155

    for j in range(60, 100, 8):
        img_path = os.path.join(root, isgood, 'img', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'img')) == False:
            os.mkdir(os.path.join(root, isgood, 'img'))
        label_path = os.path.join(root, isgood, 'label', str(img_id) + '_' + str(j) + '.png')
        if os.path.exists(os.path.join(root, isgood)) == False:
            os.mkdir(os.path.join(root, isgood))
        if os.path.exists(os.path.join(root, isgood, 'label')) == False:
            os.mkdir(os.path.join(root, isgood, 'label'))
        # if np.max(seg[:, :, j]) >= 1:
        #     continue
        good.append(img_path)
        Ungood.append(label_path)
        plt.imsave(img_path, flair[:, :, j], cmap="bone")
        plt.imsave(label_path, seg[:, :, j], cmap="bone")


path = '/home/jinan/Datasets/Medical-datasets/Brain/test/Ungood/img/'
label_path = '/home/jinan/Datasets/Medical-datasets/Brain/test/Ungood/label/'
assert os.listdir(path) == os.listdir(label_path)
dir_list = os.listdir(path)

print('test (abnormal): ', len(dir_list), ' 615 id')