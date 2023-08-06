from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json,shlex,mxpi
import traceback
import subprocess,threading,os 
import asyncio,platform
import signal
from io import BytesIO
import base64,time
from PIL import Image
from mss import mss
import pyscreenshot as ImageGrab
import numpy,platform
import serial
import traceback
from app.models import Mxpi_SArduino_out,Mxpi_SArduino_in

if (platform.system()=='Windows'):
    pass
else:
    import  fcntl

class remote_desktop_Thread (threading.Thread):
    def __init__(self, chat):
        threading.Thread.__init__(self)
        self.chat = chat
        self.read_stop=False

    def stop(self):
        pass
    def run(self):
        if platform.system()=='Windows':
            while 1:
                t1=time.time()
                img = self.capture_screenshot()
                bytesIO = BytesIO()
                img.save(bytesIO, format='PNG')
                binary_data = bytesIO.getvalue()
                base64_data = base64.b64encode(binary_data)
                self.chat.send(json.dumps({'msg':'windows_remote_desktop','data':base64_data.decode()}))
                t2=time.time()
        else:
            self.cmds('sudo bash  '+os.path.dirname(mxpi.__file__)+'/sh/VNC/start_vnc.sh '+os.path.dirname(mxpi.__file__) )
            self.chat.send(json.dumps({'msg':'Liunx_remote_desktop'}))

    def capture_screenshot(self):
        with mss() as sct:
            for i in range(100):
                monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)
                return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

    def cmds(self,cmd):
        os.system(cmd)
                
class RunThread (threading.Thread):
    def __init__(self, chat):
        threading.Thread.__init__(self)
        self.chat = chat
        self.read_stop=False
    def stop(self):
        if (platform.system()=='Windows'):
            p.terminate()
            self.read_stop=True
        else:
            self.read_stop=True
            os.killpg( p.pid,signal.SIGUSR1)
    def run(self):
        global p
        url=os.path.dirname(mxpi.__file__)
        url=url.replace('\\','/')
        if (platform.system()=='Windows'):
            shell_cmd ='python -u '+url+'/file/test.py'
        else:
            shell_cmd ='sudo python3 -u '+url+'/file/test.py'
        cmd = shlex.split(shell_cmd)
        try:
            if (platform.system()=='Windows'):
                p = subprocess.Popen(shell_cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                for i in iter(p.stdout.readline,'b'):
                    if not i:
                        break
                    if self.read_stop:
                        break
                    print(i.decode('gbk'), end='')
                    self.chat.send(json.dumps({'msg':'run_msg','data':i.decode('gbk')}))
                for i in iter(p.stderr.readline,'b'):
                    if not i:
                        break
                    if self.read_stop:
                        break
                    print(i.decode('gbk'), end='')
                    self.chat.send(json.dumps({'msg':'run_msg_err','data':i.decode('gbk')}))
                self.chat.send(json.dumps({'msg':'stop','data':'停止运行'}))
                p.stdout.close()
                print('运行结束')
            else:
                p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,close_fds=True, preexec_fn = os.setsid)
                fd = p.stdout.fileno()
                fl = fcntl.fcntl(fd, fcntl.F_GETFL)
                fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
                fd2 = p.stderr.fileno()
                fl2 = fcntl.fcntl(fd2, fcntl.F_GETFL)
                fcntl.fcntl(fd2, fcntl.F_SETFL, fl2 | os.O_NONBLOCK)
                while 1:
                    try:
                        line = p.stdout.readline()
                        err = p.stderr.readline()
                        if line.decode() == '' and  p.poll() is not None:
                            print(p.poll())
                            break
                        if line:
                            line = line.strip()
                            if len(line)>0:
                                self.chat.send(json.dumps({'msg':'run_msg','data':line.decode()}))
                                print(line.decode())
                        if err:
                            self.chat.send(json.dumps({'msg':'run_msg_err','data':err.decode()}))
                        if self.read_stop:
                            break
                    except Exception as e:
                        pass
                self.chat.send(json.dumps({'msg':'stop','data':'停止运行'}))
                print('运行结束')
        except Exception as e:
            print(str(e))
            self.chat.send(json.dumps({'msg':'run_err_msg','data':traceback.format_exc()}))
            self.chat.send(json.dumps({'msg':'stop','data':'停止运行'}))

class Pip_install_Thread (threading.Thread):
    def __init__(self, chat,name,url):
        threading.Thread.__init__(self)
        self.chat = chat
        self.read_stop=False
        self.name=name
        self.url=url
    def run(self):
        global p
        if(platform.uname().system=='Windows'):
            shell_cmd ='pip install '+self.name
        else:
            shell_cmd ='sudo pip3 install '+self.name+' -i https://pypi.tuna.tsinghua.edu.cn/simple'
        self.chat.send(json.dumps({'msg':'pip_msg','data':shell_cmd}))
        print(shell_cmd)
        cmd = shlex.split(shell_cmd)
        try:
            if (platform.system()=='Windows'):
                self.p = subprocess.Popen(shell_cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                for i in iter(self.p.stdout.readline,'b'):
                    if not i:
                        break
                    if self.read_stop:
                        break
                    print(i.decode('gbk'), end='')
                    self.chat.send(json.dumps({'msg':'pip_msg','data':i.decode('gbk')}))
                for i in iter(self.p.stderr.readline,'b'):
                    if not i:
                        break
                    if self.read_stop:
                        break
                    print(i.decode('gbk'), end='')
                    self.chat.send(json.dumps({'msg':'pip_msg_err','data':i.decode('gbk')}))
                self.chat.send(json.dumps({'msg':'pip_stop','data':'结束'}))
                self.p.stdout.close()
                print('结束')
            else:
                p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,close_fds=True, preexec_fn = os.setsid)
                fd = p.stdout.fileno()
                fl = fcntl.fcntl(fd, fcntl.F_GETFL)
                fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
                fd2 = p.stderr.fileno()
                fl2 = fcntl.fcntl(fd2, fcntl.F_GETFL)
                fcntl.fcntl(fd2, fcntl.F_SETFL, fl2 | os.O_NONBLOCK)
                while self.read_stop==False:
                    line = p.stdout.readline()
                    err = p.stderr.readline()
                    if line.decode() == '' and err.decode() == '' and p.poll() is not None:
                        break
                    if line:
                        line = line.strip()
                        self.chat.send(json.dumps({'msg':'pip_msg','data':line.decode()}))
                        print(line.decode())
                    if err:
                        err = err.strip()
                        self.chat.send(json.dumps({'msg':'pip_err_msg','data':err.decode()}))
                        print(err.decode())
                    if self.read_stop:
                        break
                self.chat.send(json.dumps({'msg':'pip_stop','data':'结束'}))
                print('结束')
        except Exception as e:
            self.chat.send(json.dumps({'msg':'pip_err_msg','data':traceback.format_exc()}))
            self.chat.send(json.dumps({'msg':'pip_stop','data':'结束'}))

class install_ku_Thread (threading.Thread):
    def __init__(self, chat,name,yuan,s):
        threading.Thread.__init__(self)
        self.chat = chat
        self.read_stop=False
        self.name=name
        self.yuan=yuan
        self.s=s
    def run(self):
        global p
        url=os.path.dirname(mxpi.__file__)
        url=url.replace('\\','/')
        if(platform.system()=='Windows'):
            shell_cmd ='pip install '+self.name+' -i '+ self.yuan
        elif (platform.uname().system=='Linux' and platform.uname().machine=='aarch64'):
            if self.s=='yuzhi':
                shell_cmd ='sudo bash '+url+'/install_ku/'+self.name+'.sh'
            else:
                shell_cmd ='sudo pip3 install '+self.name+' -i '+ self.yuan
        else:
            shell_cmd ='sudo pip3 install '+self.name+' -i '+ self.yuan
        self.chat.send(json.dumps({'msg':'pip_msg','data':shell_cmd}))
        print(shell_cmd)
        cmd = shlex.split(shell_cmd)
        try:
            if (platform.system()=='Windows'):
                self.p = subprocess.Popen(shell_cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                for i in iter(self.p.stdout.readline,'b'):
                    if not i:
                        break
                    if self.read_stop:
                        break
                    print(i.decode('gbk'), end='')
                    self.chat.send(json.dumps({'msg':'pip_msg','data':i.decode('gbk')}))
                for i in iter(self.p.stderr.readline,'b'):
                    if not i:
                        break
                    if self.read_stop:
                        break
                    print(i.decode('gbk'), end='')
                    self.chat.send(json.dumps({'msg':'pip_msg_err','data':i.decode('gbk')}))
                self.chat.send(json.dumps({'msg':'pip_stop','data':'结束'}))
                self.p.stdout.close()
                print('结束')
            else:
                p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,close_fds=True, preexec_fn = os.setsid)
                fd = p.stdout.fileno()
                fl = fcntl.fcntl(fd, fcntl.F_GETFL)
                fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
                fd2 = p.stderr.fileno()
                fl2 = fcntl.fcntl(fd2, fcntl.F_GETFL)
                fcntl.fcntl(fd2, fcntl.F_SETFL, fl2 | os.O_NONBLOCK)
                while self.read_stop==False:
                    line = p.stdout.readline()
                    err = p.stderr.readline()
                    if line.decode() == '' and err.decode() == '' and p.poll() is not None:
                        break
                    if line:
                        line = line.strip()
                        self.chat.send(json.dumps({'msg':'pip_msg','data':line.decode()}))
                        print(line.decode())
                    if err:
                        err = err.strip()
                        self.chat.send(json.dumps({'msg':'pip_err_msg','data':err.decode()}))
                        print(err.decode())
                    if self.read_stop:
                        break
                self.chat.send(json.dumps({'msg':'pip_stop','data':'结束'}))
                print('结束')
        except Exception as e:
            self.chat.send(json.dumps({'msg':'pip_err_msg','data':traceback.format_exc()}))
            self.chat.send(json.dumps({'msg':'pip_stop','data':'结束'}))

class COM_Thread (threading.Thread):
    def __init__(self,chat,com):
        threading.Thread.__init__(self)
        self.chat = chat
        self.stop=True
        self.opencom=False
        self.com=com
    def run(self):
        while self.stop:
            if self.opencom:
                data=self.read()
                datas=data.decode('gbk')
                print(datas)
                if len(datas)>0:
                    if 'MxPiSArduino-out' not in datas :
                        self.chat.send(json.dumps({'msg':'com_msg','rust':'connect_to_msg','data':'>> '+datas}))
                    if 'MxPiSArduino-in:' in datas:
                        all_in_data=Mxpi_SArduino_in.objects.all()
                        if len(all_in_data)>10:
                            all_in_data.last().delete()
                        s=Mxpi_SArduino_in()
                        s.data=datas.replace('MxPiSArduino-in:','')
                        s.save()
                    if 'MxPiSArduino-out' in datas:
                        first_data=Mxpi_SArduino_in.objects.all().first()
                        self.send_com(first_data.data.replace('\n',''),prin=False)
                self.ser.flush()
    def connect(self):
        try:
            self.ser = serial.Serial(port=self.com, baudrate=9600,timeout=0.5)
            if self.ser.is_open:
                self.opencom=True
                self.chat.send(json.dumps({'msg':'com_msg','rust':'connect_ok','data':self.com+'连接成功,波特率:9600'}))
            else:
                self.chat.send(json.dumps({'msg':'com_err_msg','data':self.com+'连接失败'}))
        except Exception:
            self.chat.send(json.dumps({'msg':'com_err_msg','data':self.com+'连接失败'}))

    def send_com(self,val,prin=True):
        if prin:
            print(val)
        self.ser.write(val.encode('gbk')+b'\n')
    
    def read(self):
        return self.ser.readline()

class ChatConsumer(WebsocketConsumer):
    # websocket建立连接时执行方法
    def connect(self):
        self.accept()
     
    # websocket断开时执行方法
    def disconnect(self, close_code):
        self.close()
     
    # 从websocket接收到消息时执行函数
    def receive(self, text_data):
        data=json.loads(text_data)
        if data['msg']=='run':
            self.sendRun=RunThread(self)
            self.sendRun.start()
            self.send(json.dumps({'msg':'run_msg','data':'开始运行'}))
            print('开始运行')

        elif data['msg']=='stop':
            self.sendRun.stop()
            self.sendRun.read_stop=True
            
        elif data['msg']=='pip_install':
            self.pip_install_Run=Pip_install_Thread(self,data['name'],data['pipyuan'])
            self.pip_install_Run.start()
            self.send(json.dumps({'msg':'pip_msg','data':'开始安装'}))
        
        elif data['msg']=='upclock':
            url=os.path.dirname(mxpi.__file__)
            f=open(url+'/file/mxpi.mxpi','w')
            f.write(data['code'])
            f.close()
        
        elif data['msg']=='remote_desktop':
            self.dk=remote_desktop_Thread(self)
            self.dk.start()

        elif data['msg']=='loadclock':
            try:
                url=os.path.dirname(mxpi.__file__)
                f=open(url+'/file/mxpi.mxpi','r')
                self.send(json.dumps({'msg':'load_msg','data':f.read()}))
                self.send(json.dumps({'msg':'run_msg','data':'读取缓存程序成功'}))
            except:
                self.send(json.dumps({'msg':'load_msg','data':''}))
                self.send(json.dumps({'msg':'run_msg','data':'读取缓存程序失败'}))
        elif data['msg']=='install_ku':
            yuan=[
                'https://pypi.tuna.tsinghua.edu.cn/simple',
                'https://mirrors.aliyun.com/pypi/simple/',
                'https://pypi.douban.com/simple/',
                'https://pypi.mirrors.ustc.edu.cn/simple/'

            ]
            yuan_id=data['pipyuan']
            s=data['s']
            self.ku=install_ku_Thread(self,data['name'],yuan[int(yuan_id)],s)
            self.ku.start()
            self.send(json.dumps({'msg':'pip_msg','data':'开始安装'}))
        
        elif data['msg']=='connect_com':
            self.ku=COM_Thread(self,data['com'])
            self.ku.start()
            self.ku.connect()

        elif data['msg']=='to_com_msg':
            self.ku.send_com(data['com'])
        
        elif data['msg']=='del_com':
            self.ku.stop=False
            self.send(json.dumps({'msg':'com_msg','rust':'connect_del','data':'断开连接'}))
            self.ku.ser.close()
            





