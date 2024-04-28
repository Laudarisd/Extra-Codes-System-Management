import cv2, os
path = './saved_images/'
imgs = sorted(os.listdir(path))
print(imgs)

save_dir = './cropped/'

for item in imgs:
    file_name = save_dir + item + '_'
    img = cv2.imread(path + item)
    section_1 = img[0:800, 100:400]
    cv2.imwrite(save_dir + item + '_1', section_1)
    section_2 = img[150:700, 400:550]
    cv2.imwrite(save_dir + item + '_2', section_2)
    section_3 = img[200:650, 550:690]
    cv2.imwrite(save_dir + item + '_3', section_3)
    section_4 = img[200:600, 690:780]
    cv2.imwrite(save_dir + item + '_4', section_4)
    section_5 = img[200:600, 780:840]
    cv2.imwrite(save_dir + item + '_5', section_5)
    section_6 = img[200:550, 840:880]
    cv2.imwrite(save_dir + item + '_6', section_6)
    section_7 = img[200:500, 880:910]
    cv2.imwrite(save_dir + item + '_7', section_7)
    section_8 = img[200:500, 910:935]
    cv2.imwrite(save_dir + item + '_8', section_8)
    

