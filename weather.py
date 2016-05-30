# -*- coding: utf-8 -*-
from tkinter import *
import sys, urllib, urllib.request, json

url = 'http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=ganyu'

req = urllib.request.Request(url)

req.add_header("apikey", "d3d2d8053c8a3352d487b0b6c2bca703")

resp = urllib.request.urlopen(req).read()

t=resp.decode('utf-8')
s=json.loads(t)

if s:
    print(s,end='\n')
print(s["retData"]["city"],end=' ')
print(s["retData"]['date'])
print(s["retData"]['weather'],end=' ')
print(s["retData"]['l_tmp']+'~'+s["retData"]['h_tmp'])

r=Tk()
r.title('LABEL TEST')

Label(r,fg='CornflowerBlue',bg='pink',width=100,height=2,text=s["retData"]["city"]).pack()
Label(r,fg='SlateBlue',bg='Gold1',width=100,height=2,text=s["retData"]['date']).pack()
Label(r,fg='MediumSlateBlue',bg='Yellow1',width=100,height=2,text=s["retData"]['weather']).pack()
Label(r,fg='LightSlateBlue',bg='Yellow2',width=100,height=2,text=[s["retData"]['l_tmp']+'~'+s["retData"]['h_tmp']]).pack()

#r.pack()
r.mainloop()
