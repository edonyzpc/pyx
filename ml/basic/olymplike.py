 #!/usr/bin/python
 #encoding: utf-8
 #        .---.         .-----------  
 #       /     \  __  /    ------    
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_            
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->   
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    / 
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /) 
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`  
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'    
 # ########################################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified: 2015-01-16 21:34
 # 
 # Filename: olymplike.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "py" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    
    格式: \033[显示方式;前景色;背景色m
    说明:
    前景色            背景色           颜色
    ---------------------------------------
    30                40              黑色
    31                41              红色
    32                42              绿色
    33                43              黃色
    34                44              蓝色
    35                45              紫红色
    36                46              青蓝色
    37                47              白色
    显示方式           意义
    -------------------------
    0                终端默认设置
    1                高亮显示
    4                使用下划线
    5                闪烁
    7                反白显示
    8                不可见
    
    例子：
    \033[1;31;40m   <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
    \033[0m         <!--采用终端默认设置，即取消颜色设置-->
    '''
    WARNING = '\033[0;37;41m'
    ENDC = '\033[0m'
    def disable(self):
        self.ENDC = ''
        self.WARNING = ''
 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
import math as m
 

f = open("olympics.txt",'r')
x = np.array([])
t = np.array([])
for line in f.readlines():
    tmp = line.split()
    x = np.append(x,float(tmp[0]))
    t = np.append(t,float(tmp[1]))
f.close()
T = np.matrix(t.reshape(t.size,1))
N = float(t.size)
logL = np.empty(9)

# rescale the x for numeric stability
x = x-x[0]
x = x/4.0
X = np.concatenate((np.array([np.ones(x.size)]),[x]),axis=0)
sigma2 = np.array(np.zeros(10))
sigma = np.array(np.zeros(10))

# degree of polynomial is 9
for i in range(9):
    Xm = np.matrix(X.T)
    sigma2[i] = (1/float(t.size))*(T.T*T-T.T*Xm*(Xm.T*Xm).I*Xm.T*T)
    w = (Xm.T*Xm).I*Xm.T*T
    sigma[i] = 1/N*(T.T*T-T.T*Xm*w)
    mu = np.array(Xm*w)
    logL[i] = np.sum(sp.random.multivariate_normal(mu,sig))
    X = np.concatenate((X,[x**(i+2)]),axis=0)

plt.plot(range(9),logL,'k-')
plt.show()
