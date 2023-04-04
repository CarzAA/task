#
#Задача: рассчитать зависимости скорости сокращения численности противоположных 
#команд по формуле Риккати
import	numpy	as	np
import	scipy
from scipy import integrate
import	sympy
import	cv2
import	matplotlib as mpl
import	matplotlib.pyplot	as	plt
from	math import *

def Vx(s, n, k, t):
    dxdt = - k0 * n * s * exp(- k * (n - s)) *t
    return dxdt

def Vy(s, n, k, t):
    dydt =- k0 * n * s * exp(  k * (n - s))* t
    return dydt

#def V(s, n, k, t):
#    dxdt =n - k0 * n * Vy(s, n, k, t) * exp(- k * (n - Vy(s, n, k, t))) *t
#    dydt =s - k0 * Vx(s, n, k, t) * s * exp(  k * (Vx(s, n, k, t) - s))* t
#    return [dxdt,dydt]

t = np.linspace(0, 11, 500)
k0 = 0.02
x0 = 10					#начальное кол-во команды 1
#x0 = np.linspace(10, 0, 50)
y0 = [2, 4, 6, 8, 10]	#начальное кол-во команды 2
#y0 = np.linspace(2, 0, 50)
k1 = [0.1, 0.2, 0.05]	#{1/x0, 2/x0, 1/2*x0}

wx =x0 + Vx(y0[0], x0, k1[0], t)
wy =y0[0] + Vy(y0[0], x0, k1[0], t)

#w = V(y0[0], x0, k1[0], t)[:,0]
#print(wx,"\n", wy)
#print(w)

fig = plt.figure()#открытие области графика
fig, ax = plt.subplots()
ax.plot(t,Vx(y0[0], x0, k1[0], t), color="red")		#график
ax.plot(t,Vy(y0[0], x0, k1[0], t), color="blue")
ax.plot(t,wx, color="red")		#график
ax.plot(t,wy, color="blue")
#ax.plot(t,V(y0[0], x0, k1[0], t)[:,0], color="y")
#ax.plot(t,V(y0[0], x0, k1[0], t)[:,1], color="y")
#оформление графика
ax.set_ylabel("Vx, Vy")		#обозначение графика+его цвет
ax.set_xlabel("t")
#plt.xlim([0., 11.])
#plt.ylim([0., 10.])
plt.grid()
#fig.set_figwidth(10)
#fig.set_figheight(5)
plt.show()