from uwimg import *

# im = load_image("data/dog.jpg")
# for row in range(im.h):
#     for col in range(im.w):
#         rgb = get_pixel(im, col, row, 0) + get_pixel(im, col, row, 1) + get_pixel(im, col, row, 2)
#         set_pixel(im, col, row, 0, rgb/4)
#         set_pixel(im, col, row, 1, rgb/4)
#         set_pixel(im, col, row, 2, rgb/4)
#         # if (rgb < 1):
#         #     set_pixel(im, col, row, 0, 0)
#         #     set_pixel(im, col, row, 1, 0)
#         #     set_pixel(im, col, row, 2, 0)
#         # else:
#         #     set_pixel(im, col, row, 0, 1)
#         #     set_pixel(im, col, row, 1, 1)
#         #     set_pixel(im, col, row, 2, 1)
# save_image(im, "dog_test4")

# # 1. Getting and setting pixels
# im = load_image("data/dog.jpg")
# for row in range(im.h):
#     for col in range(im.w):
#         set_pixel(im, col, row, 0, 0)
# save_image(im, "dog_no_red_A")

# im = load_image("data/dog.jpg")
# for row in range(im.h):
#     for col in range(im.w):
#         set_pixel(im, col, row, 0, 0)
#         set_pixel(im, col, row, 1, 0)
# save_image(im, "dog_no_red_green_A")

# # 3. Grayscale image
# im = load_image("data/dog.jpg")
# graybar = rgb_to_grayscale(im)
# save_image(graybar, "graybar_A")

# # 4. Shift Image
# im = load_image("data/dog.jpg")
# shift_image(im, 0, .4)
# shift_image(im, 1, .4)
# shift_image(im, 2, .4)
# save_image(im, "overflow")

# # 5. Clamp Image
# clamp_image(im)
# save_image(im, "doglight_fixed")

# 6-7. Colorspace and saturation
im = load_image("data/dog.jpg")
rgb_to_hsv(im)
# shift_image(im, 1, .2)
scale_image(im, 1, 2)
clamp_image(im)
hsv_to_rgb(im)
save_image(im, "dog_scale_saturated_B")


