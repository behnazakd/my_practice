n=10000
pi_real =3.14159265359
zeta=0
i= 1
err = 0.000001
while True :
    zeta= zeta + 1/i**2
    pi_approximate = (zeta*6)**0.5
    if (abs(pi_approximate - pi_real) / pi_real < err):
        break
    i=i+1
print(pi_real)
print(pi_approximate)
print(i)