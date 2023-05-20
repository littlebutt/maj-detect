import os


if __name__ == '__main__':
    root_dir = r'../data/raw_labels'
    dir_walk = os.walk(root_dir)
    for path, dir_list, file_list in dir_walk:
        for file in file_list:
            if '.xml.' not in file:
                continue
            new_file = '.'.join(file.split('.xml.'))
            os.rename(root_dir + '/' + file, root_dir + '/' + new_file)