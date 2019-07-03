n=10000
zeta=0
i=1
pi_real=3.14159265359
for i in range(i, n+1):
    zeta=zeta+1/i**2
    pi_approximate = (zeta*6)**(0.5)
    err=abs(pi_real - pi_approximate)/ pi_real
print(zeta)
print(pi_real)
print(pi_approximate)
print(err)