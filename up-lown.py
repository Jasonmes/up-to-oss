# -*- coding: utf-8 -*-
import os
import oss2
import time

accessKeyId = "LTAIT6QWMPJndg3k"
accessKeySecret = "oCtePLNyMj9NL0GKpb9YNsEI69cvij"

endpoint = "http://oss-cn-hangzhou.aliyuncs.com"

bucket = "mozi-update"
# localDirectory = "/home/wwwroot/vmall3.mozi.top/uploads"   #改成本地路径
localDirectory = "/Users/jasonmes/个人/[乔丹经典比赛合辑].1998NBA.Playoffs.R1G3.Bulls@Nets.MJ38pts.avi"
prefix = "oss/uploads"


auth = oss2.Auth(accessKeyId, accessKeySecret)
bucket = oss2.Bucket(auth, endpoint, bucket)


# 遍历目录进行上传     
for fpathe, dirs, fs in os.walk(localDirectory):
    for f in fs:
        localFileName = os.path.join(fpathe, f)
        newObjectName = localFileName[len(localDirectory) + 1:]
        newObjectName = prefix +'/'+ newObjectName
        # 跳过已存在的文件
        # if bucket.object_exists(newObjectName):
        #     print('重复文件排除:'+newObjectName)
        #     continue
        oss2.resumable_upload(bucket,newObjectName,localFileName)
        print(newObjectName)
        print(localFileName)
