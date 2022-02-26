import glob
import os

home_dir = '/home/alex/git/sketch_inpainting/'
files = glob.glob(f'{home_dir}tests/*')
for file in files:
    if not 'ans' in file and os.path.isfile(file):
        ans_file = '.'.join(file.split('.')[:-1]) + '_ans.' + file.split('.')[-1]
        print(f'/usr/bin/python3.8 {home_dir}src/cleaner.py {file} {ans_file}')
        os.system(f'/usr/bin/python3.8 {home_dir}src/cleaner.py {file} {ans_file}')
        print('done')
