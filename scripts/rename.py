import os

if __name__ == '__main__':
    jpg_name = 1
    root_dir = r'../data/raw'
    dir_walk = os.walk(root_dir)
    for path, dir_list, file_list in dir_walk:
        for file in file_list:
            os.rename(root_dir + '/' + file, f'{root_dir}/{jpg_name}.jpg')
            jpg_name += 1
