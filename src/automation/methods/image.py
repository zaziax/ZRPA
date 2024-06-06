# import os
#
# import pyautogui as auto
#
# # 通过图像定位并点击
# def click_image(imgurl,button,nums):
#     try:
#         thisbutton = 'left'
#         if button == '右键':
#             thisbutton = 'right'
#         elif button == '滚轮':
#             thisbutton = 'middle'
#         imgurl = os.path.abspath(imgurl)
#         image_location = auto.locateOnScreen(imgurl,grayscale=True)
#         if image_location is not None:
#             # 获取图像中心坐标
#             image_center = auto.center(image_location)
#             # 点击图像中心
#             auto.click(image_center, button=thisbutton, clicks=int(nums),interval=0.3)
#             return True
#         else:
#             print("Image not found on the screen.")
#             return False
#     except Exception as e:
#         print("Error clicking image:", str(e))
#         return False

import os
import time
import pyautogui as auto


# 通过图像定位并点击，尝试最多10次，每次尝试间隔0.5秒，总共尝试5秒
def click_image(imgurl, button='left', nums=1):
    try:
        thisbutton = 'left'
        if button == '右键':
            thisbutton = 'right'
        elif button == '滚轮':
            thisbutton = 'middle'
        imgurl = os.path.abspath(imgurl)
        attempt_count = 0
        max_attempts = 10
        interval = 0.5  # 每次尝试之间的间隔时间，单位：秒
        total_time = interval * max_attempts  # 总共尝试的时间

        start_time = time.time()
        while time.time() - start_time < total_time:
            image_location = auto.locateOnScreen(imgurl, grayscale=True)
            if image_location is not None:
                # 获取图像中心坐标
                image_center = auto.center(image_location)
                # 点击图像中心
                auto.click(image_center, button=thisbutton, clicks=int(nums), interval=0.3)
                print("Image found and clicked.")
                return True

            attempt_count += 1
            if attempt_count < max_attempts:
                time.sleep(interval)  # 等待一段时间后再次尝试
            else:
                print("Exceeded maximum attempts. Image not found.")
                break  # 达到最大尝试次数后退出循环

        return False
    except Exception as e:
        print("Error clicking image:", str(e))
        return False



