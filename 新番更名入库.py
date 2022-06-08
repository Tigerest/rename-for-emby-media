import os
path = r'K:\新番' #rss文件夹

while True:
    for fname in os.listdir(path): #获取目录，遍历文件名
        if("Komi-san wa, Komyushou Desu." in fname):
            outputpath = r'K:\media\anime\古見さんは, コミュ症です' #输出路径
            fformat = fname[-3:]  #获取文件格式
            
            #获取集数
            ep = ""
            flag = False
            for i in fname:
                if i>="0" and i <="9":
                    flag = True
                    ep=ep + i
                if flag and (i<"0" or i >"9"):
                    break
            
            ep = str(int(ep)-12) #这季的古见是第二季但是我选的字幕组用了延续第一季的集数命名，故减去12集
            old_path = "%s/%s" % (path, fname)
            new_name = "古見さんは、コミュ症です。 - S02E%s - .%s" % (ep, fformat) #更名格式
            new_path = "%s/%s" % (outputpath, new_name)
            if(new_name not in os.listdir(outputpath)):
                os.renames(old_path, new_path)
        
        if("Summer Time Rendering" in fname):
            outputpath = r'K:\media\anime\サマータイムレンダ'
            fformat = fname[-3:]
            ep = ""
            flag = False
            for i in fname:
                if i>="0" and i <="9":
                    flag = True
                    ep=ep + i
                if flag and (i<"0" or i >"9"):
                    break
            old_path = "%s/%s" % (path, fname)
            new_name = "サマータイムレンダ - S01E%s - .%s" % (ep, fformat)
            new_path = "%s/%s" % (outputpath, new_name)
            if(new_name not in os.listdir(outputpath)):
                os.renames(old_path,new_path)
