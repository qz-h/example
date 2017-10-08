#coding:utf-8
import json
import os
f = open('../scene_train_annotations_20170904.json', 'r')

jsonData = json.load(f)

for item in jsonData:
    folderName = item['label_id']
    sourceFile = '../scene_train_images_20170904/%s'%(item['image_id'])
    targetFile= './%s/%s'%(folderName,item['image_id'])
    if (os.path.exists(folderName)):
        pass
    else:
        os.mkdir(folderName)
    open(targetFile, "wb").write(open(sourceFile, "rb").read())
f.close()
