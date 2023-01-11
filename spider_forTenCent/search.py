from urllib import parse
import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser
import re

class APP:
    def __init__(self,width=500,height=300):
        self.w=width
        self.h=height
        self.title='bonesdl在线模式'
        self.root=tk.Tk(className=self.title)
        
        #控件
        self.url = tk.StringVar()
        
        #video sourse
        self.v=tk.IntVar()
        self.v.set(1)
        
        frame_1=tk.Frame(self.root)
        frame_2=tk.Frame(self.root)
        frame_3=tk.Frame(self.root)
        
        #menu
        menu=tk.Menu(self.root)
        self.root.config(menu=menu)
        moviemenu=tk.Menu(menu,tearoff=0)
        menu.add_casecade(label='链接',menu=moviemenu)
        
        #web sourse
        moviemenu.add_command(label='搜狐视频',command=lambda:webbrowser.open('http://v.qq.com/'))
        moviemenu.add_command(label='芒果视频',command=lambda:webbrowser.open('http://tv.sohu.com/'))
        moviemenu.add_command(label='芒果TV',command=lambda:webbrowser.open('http://www.mgtv.com/'))
        moviemenu.add_command(label='爱奇艺',command=lambda:webbrowser.open('http://ww.iqiyi.com'))
        moviemenu.add_command(label='哔哩哔哩',command=lambda:webbrowser.open('http://www.bilibili.com'))     
        moviemenu.add_command(label='优酷视频',command=lambda:webbrowser.open('http://www.youku.com'))
        moviemenu.add_command(label='乐视视频',command=lambda:webbrowser.open('http://www.le.com/'))
        moviemenu.add_command(label='土豆视频',command=lambda:webbrowser.open('http://tudou.com/'))
        moviemenu.add_command(label='Acfun',command=lambda:webbrowser.open('http://www.acfun.tv/'))
        
        group=tk.label(frame_1,text='请选择解码方式：',padx=10,pady=10)
        tb1=tk.Radiobutton(frame_1,text="方式一",variable=self.v,value=1,width=10,height=3)
        tb2=tk.Radiobutton(frame_1,text="方式一",variable=self.v,value=2,width=10,height=3)
        tb3=tk.Radiobutton(frame_1,text="方式一",variable=self.v,value=3,width=10,height=3)
        label1=tk.Label(frame_2,text="请输入链接")
        entry=tk.Entry(frame_2,textvariable=self.url,highlightcolor='Fuchsia',highlightthickness=1,width=35)
        label2=tk.Label(frame_2,text="")
        play=tk.Button(frame_2,text="播放",font=('楷体',12),fg='Purple',width=2,height=1,command=self.video_play)
        label3=tk.Label(frame_2,text="")
        label_explain=tk.Label(frame_3,fg='red',font=('楷体',18),text="此工具作者：hip，隶属于home工作室 QQ：3202638964")
        label_warning=tk.Label(frame_3,fg='black',font=('楷体',16),text="\n\n")
        
        #布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group.grid(row=0,column=0)
        tb1.grid(row=0,column=1)
        tb2.grid(row=0,column=2)
        tb3.grid(row=0,column=3)
        label1.grid(row=0,column=0)
        entry.grid(row=0,column=1)
        label2.grid(row=0,column=2)
        play.grid(row=0,column=3,ipadx=10,ipady=10)
        label3.grid(row=0,column=4)
        label_explain.grid(row=1,column=0)
        label_warning.grid(row=2,column=0)
        
    #函数部分
        
    """
    1,video play
    """
    def video_play(self):
        #port_1='https://jx.618g.com/?url='    
        port_1='https://quanmingjiexi.com/?url='
        port_2='https://www.wmxz.wang/video.php?url='
        port_3='https://ckmov.vip/api.php?url='
        if re.match(r'https?:/{2}\w/+$',self.url.get()):    
            ip=self.url.get()
            ip=parse.quote_plus(ip)
            webbrowser.open(port_1+self.url.get())
        elif self.v.get()==2:
            ip=self.url.get()
            ip=parse.quote_plus(ip)
            get_url='http://www.wmxz.wang/video.php?url=%s'%ip
            webbrowser.open(get_url)
        elif self.v.get()==3:
           ip=self.url.get()
           ip=parse.quote_plus(ip)
           get_url='https://ckmov.vip/api.php?url=%s'%ip
           webbrowser.open(get_url)
        else:
            msgbox.showerror(title='错误',message='视频链接无法解析!')
    def center(self):
        ws=self.root.winfo_screenwidth()     
        hs=self.root.winfo_screenheight()       
        x=int((ws/2)-(self.w/2))
        y=int((hs/2)-(self.h/2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w,self.h,x,y))
        
    def loop(self)
       self.root.resizable(False,False)
       self.center()
       self.root.mainloop()
       
if __name__=="__main__":
    app=APP()
    app.loop()        
        