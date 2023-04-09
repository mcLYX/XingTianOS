import json,zlib,os
flist=[i for i in os.listdir() if '.mc' in i]#input('请输入文件名\n'))

try:os.mkdir('Melopy_Charts')
except:pass

def getbartime(beatlist):
    xiaojie=beatlist[0]
    bufen=beatlist[1]
    divide=beatlist[2]
    return ( xiaojie + (bufen * ( 1 / divide)) )

for f in flist:
    a=open(f,encoding='utf-8').read()
    b=json.loads(a)
    bpms=b['time']#[0]['bpm']
    bpmlistpos=0
    if len(b['time'])>1:
        print('警告：多bpm谱面，很可能出错:',f)
    try:
        if b['meta']['mode_ext']['column']!=4:
            print('不支持非4键谱面:',f)
            continue
    except:
        print('不支持此谱面:',f)
        continue

    offset1=0
    decode=[]
    try:
        if 'offset' in b['note'][-1]:
            offset1=b['note'][-1]['offset']
            offset=offset1
            if offset1>500:print('警告：过大的偏移量：',offset)
        for i in b['note']:
            bartime = getbartime(i['beat'])
            
            if bpmlistpos+1<len(bpms) and bartime>=getbartime(bpms[bpmlistpos+1]['beat']):
                psttime=0
                for j in range(bpmlistpos+1):
                    psttime+=1000*((getbartime(bpms[j+1]['beat'])-getbartime(bpms[j]['beat']))*(60/bpms[j]['bpm']))
                directtime=1000*(getbartime(bpms[bpmlistpos+1]['beat'])*(60/bpms[bpmlistpos+1]['bpm']))
                offset=offset1-(psttime-directtime)
                print(psttime,directtime)
                bpmlistpos+=1
            
            bpm=bpms[bpmlistpos]['bpm']
            jielen=(60/bpm)#*4
            notetime= 1000 * bartime * jielen - offset
            try:
                endxj=i['endbeat'][0]#小节
                endbf=i['endbeat'][1]
                endd=i['endbeat'][2]#结束小节
                endtime= 1000 * ( endxj * jielen + jielen * (endbf * ( 1 / endd)) ) - offset
                #endtime=' '+str(round(endtime))
            except:
                endtime=''
            column=i['column']
            decode.append((round(notetime), column)+((round(endtime),) if endtime else ()))# += str(round(notetime)) + ' ' + str(column) + endtime + '\n'
    except:
        pass
    
    #ChatGPT整挺好
    def sort_mixed_list(lst):
        lst.sort(key=lambda x: x[0] if isinstance(x, (tuple, list)) else x)
        return lst
    
    decode=sort_mixed_list(decode)
    
    outputstr=''
    for i in decode:
        if len(i)==3:
            outputstr+=str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n'
        else:
            outputstr+=str(i[0]) + ' ' + str(i[1]) + '\n'
            
    decode=outputstr
    
    try:
        TITLE=b['meta']['song']['title']
        VERSION=b['meta']['version']
        for char in "?_/\\*\"'<>|":
            TITLE=TITLE.replace(char, " ")
            VERSION=VERSION.replace(char, " ")
        TITLE=TITLE.strip()
        VERSION=VERSION.strip()
        os.mkdir('Melopy_Charts/'+TITLE)
        songid=input('发现新曲目:'+TITLE+',请输入歌曲在TF卡中的ID：')
        with open('Melopy_Charts/'+TITLE+'/songid.txt','w') as w:
            w.write(songid)
    except:
        pass

    with open('Melopy_Charts/'+TITLE+'/'+b['meta']['version']+'.mpc','wb') as w:
        w.write(zlib.compress(bytes(decode,encoding='ascii'),9))
    '''  
    with open('Melopy_Charts/'+b['meta']['song']['title']+'/'+b['meta']['version']+'.mpo','wb') as w:
        w.write(bytes(decode,encoding='ascii'))
    '''
    print('转换完成：'+f)
    
input('OK')
