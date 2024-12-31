# from pathlib import Path
import os
import shutil
import pandas as pd
import collections
import numpy as np

# change the metadata path
meta_data = pd.read_csv('C:\\Users\\32470\\Downloads\\Musicnet\\musicnet\\musicnet_metadata.csv')
idx = []

for i in meta_data["composer"]:
    # print(os.path.join(path2+i))
    # shutil.move(os.path.join(path2+format(i)), os.path.join(o_path+format(j)))
    idx.append(i)
    # print(i)


def classes_folder(path1, idx):
    if not os.path.exists(path1+"train_classes\\"):
        os.mkdir(path1+"train_classes\\")
    o_path = path1+"train_classes\\"

    # CREATES FOLDER BASED ON CLASSES
    for x, y in collections.Counter(idx).items():
        if y > 1:
            # print(x)
            if not os.path.exists(o_path+x):
                os.mkdir(o_path+x)


def move_folders(meta_data, path1, path2):
    o_path = path1+"train_classes\\"
    for i, j in zip(meta_data["id"], meta_data["composer"]):
        try:
            # print(os.path.join(path2+str(i)))
            shutil.move(os.path.join(path2+format(i)), os.path.join(o_path+format(j)))
        except:
            pass


Path1 = "C:\\Users\\32470\\Downloads\\Musicnet\\Spectograms_fft\\"
Path2 = "C:\\Users\\32470\\Downloads\\Musicnet\\Spectograms_fft\\Schubert\\"

classes_folder(Path1, idx)
move_folders(meta_data, Path1, Path2)


# RENAMES THE FILENAMES IN EACH RECORDING FOLDER (required for old code)
# p = "C:\\Users\\32470\\Downloads\\Musicnet\\Spectograms_cpu\\Schubert\\"
# # # path3 = "C:\\Users\\32470\\Downloads\\Musicnet\\CQT\\train_classes\\"
# for x in os.listdir(p):
#     # print(x)
#     for y in os.listdir(p+x+'\\'):
#         os.rename(os.path.join(p+ x + '\\' + y), os.path.join(p + x + '\\' +x+'_'+y))
        # print(y)
#         for z in os.listdir(o_path+x+'\\'+y):
#             print(z)
#             os.rename(os.path.join(o_path+x+'\\'+y+'\\'+z), os.path.join(o_path+x+'\\'+y+'\\'+y+'_'+z))


















# # def main(data_path, out_path, train_ratio):
#     #1
#     # dir_paths = [child for child in Path(data_path).iterdir() if child.is_dir()]
#
#     # for i, dir_path in enumerate(dir_paths):
#     #     #2
#     #     files = list(dir_path.iterdir())
#     #     train_len = int(len(files) * (1 - train_ratio))
#     #
#     #     #3
#     #     out_dir = Path(out_path).joinpath(dir_path.name)
#     #     if not out_dir.exists():
#     #         out_dir.mkdir(parents=True)
#     #
#     #     #4
#     #     for file_ in files[:train_len]:
#     #         file_.replace(out_dir.joinpath(file_.name))
# #
# # if __name__ == '__main__':
# #     main('data', 'test', 0.8)
#
#
# data_path= 'C:\\Users\\32470\\Downloads\\Musicnet\\Spectograms_fft_scipy_30swindow\\Test_set\\'
# out_path = "C:\\Users\\32470\\Downloads\\Musicnet\\Spectograms_fft_scipy_30swindow\\Test_set_new\\"
# # for x in os.listdir(path_to_test_data):
# #     for y in os.listdir(path_to_test_data+'\\'+x):
# #         # print(y)
# #         y.rename(x+'_'+y)
# dir_paths = [child for child in Path(data_path).iterdir() if child.is_dir()]
#
# for i, dir_path in enumerate(dir_paths):
#     #2
#     files = list(dir_path.iterdir())
#     # print(files)
#     for file_ in files:
#         # print(file_)
#         a = str(file_).split('\\')[-1]
#         b = str(file_).split('\\')[7]
#         # print(b + '_' + a)
#         # print(b)
#         new_name = b + '_' + a
#         os.rename(str(file_), os.path.join(out_path, new_name))
        # shutil.move(str(file_), out_path+b+'_'+a)

        # dest_dir = "tmp\\2"
        # new_name = "bar.txt"
        # current_file_name = "tmp\\1\\foo.txt"
        # os.rename(current_file_name, os.path.join(dest_dir, new_name))