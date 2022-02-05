import sys
import cv2
from run_sketch_simplification import run_sketch_simplification
from get_clear_background import get_clear_background
from finalize_wb_image import finalize_wb_image
from merge_image_and_background import merge_image_and_background


def main():
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        in_file_name = sys.argv[1]
        out_file_name = sys.argv[2]
        image = cv2.imread(in_file_name)
        wb_simplified = run_sketch_simplification(image)
        wb_image = finalize_wb_image(wb_simplified)
        if len(sys.argv) == 4:
            cv2.imwrite(out_file_name, wb_image)
        else:
            clear_background = get_clear_background(image, wb_simplified)
            merged_image = merge_image_and_background(wb_image, clear_background)
            cv2.imwrite(out_file_name, merged_image)

    else:
        print('Warning: Nothing was done!')
        print('Please, enter "python cleaner.py YOUR_INPUT_FILE_NAME YOUR_OUTPUT_FILE_NAME".')


if __name__ == '__main__':
    main()
