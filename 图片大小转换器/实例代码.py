import time
from PIL import Image
img = Image.open(input("请输入文件的准确路径:"))
img_width = int(input('请输入转换后的长：'))
img_height = int(input('请输入转换后的宽：'))
img_resize1 = (img_width, img_height)
img_resize = img.resize(img_resize1)

img_name3 = input('请输入转换后文件的格式：')
img_name = input('请输入转换后文件的名字：')
img_name1 = input("请输入要存放的准确路径, 末尾的符号必须是”\“，如果没有就请加上:")
img_name2 = img_name1 + img_name+'.'+img_name3
print('保存的路径为：', img_name2)
img_save = img_resize.save(img_name2)
print('转换完成,程序将在5秒后自动关闭')
time.sleep(5)
exit()


