import math
first_coefficient = float(input("enter Equation coefficients plz :\n"))
second_coefficient = float(input())
third_coefficient = float(input())
delta = (second_coefficient * second_coefficient)-(4*first_coefficient*third_coefficient)
if delta <0 :
    print("The equation doesn't have an answer")
elif delta == 0 :
    answer = print((-second_coefficient)/(2*first_coefficient))
else:
    answer_1 = print((-second_coefficient)+ (math.sqrt(delta)/2*first_coefficient))
    answer_2 = print((-second_coefficient)- (math.sqrt(delta)/2*first_coefficient))