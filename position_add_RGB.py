from PIL import Image
import os
import pandas as pd 
import csv
from tqdm import trange

c = open("1m_label.csv", 'w+')
pre_folder = "./pre_label"

imlist = os.listdir(pre_folder)
imlist.sort()

for imagename in imlist:
	imurl = os.path.join(pre_folder,imagename)
	print(imurl)
	im = Image.open(imurl)
	rgb_im = im.convert('RGB')
	for w in trange(1460) # width = "1460":
		for h in range(630) # height = "630":
			r, g, b = rgb_im.getpixel((w, h))
			if  r==0 and g==0 and b==255 :
			 true_label=4
			elif r==150 and g==50 and b==20 :
			 true_label=0
			elif r==255 and g==255 and b==0 :
			 true_label=3
			elif r==0 and g==200 and b==255 :
			 true_label=1
			elif r==255 and g==0 and b==0 :
			 true_label=2
			elif r==20 and g==150 and b==150 :
			 true_label=5
			elif r==0 and g==0 and b==0 :
			 true_label=6
			elif r==255 and g==255 and b==255 :
			 true_label=7
			x=-34834.110001+1*w # x position in the .tfw file, mesh size = "1" 
			y=-142354.877014-1*h # y position in the .tfw file, mesh size = "1"
			print(w, h, x, y, true_label,r, g, b, file=c)

with open('1m_label.csv',newline='') as c:
    r = csv.reader(c)
    data = [line for line in r]
with open('1m_label.csv','w',newline='') as c:
    w = csv.writer(c)
    #w.writerow(['i','j','r','g','b','true_label'])
    w.writerow(['w', 'h', 'x', 'y', 'label', 'r', 'g', 'b'])
    w.writerows(data)

print('完成')
