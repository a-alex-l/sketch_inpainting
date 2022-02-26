import sys
import cv2
from run_sketch_simplification import run_sketch_simplification
from get_clear_background import get_clear_background
from merge_image_and_background import merge_image_and_background
from shadow_eraser import erase_shadow


def main():
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        in_file_name = sys.argv[1]
        out_file_name = sys.argv[2]
        raw_image = cv2.imread(in_file_name)
        image = erase_shadow(raw_image)
        wb_image = run_sketch_simplification(image)
        if len(sys.argv) == 4:
            cv2.imwrite(out_file_name, wb_image)
        else:
            clear_background = get_clear_background(image)
            merged_image = merge_image_and_background(wb_image, clear_background)
            cv2.imwrite(out_file_name, merged_image)

    else:
        print('Warning: Nothing was done!')
        print('Please, enter "python cleaner.py YOUR_INPUT_FILE_NAME YOUR_OUTPUT_FILE_NAME".')


if __name__ == '__main__':
    main()
