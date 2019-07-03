import  time
n=10000
zeta=0
i=1
pi_real=3.14159265359
t_start=time.time()
for i in range(i, n+1):
    zeta=zeta+1/i**2
    pi_approximate = (zeta*6)**(0.5)
    err=abs(pi_real - pi_approximate)/ pi_real
    t_stop = time.time()
print(zeta)
print(pi_real)
print(pi_approximate)
print(t_start)
print(t_stop)