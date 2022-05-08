import math


def f_act(x):
    return 1/(1+math.exp(-x))



def neural_net_ex6(age, weight,height):
    output = 0
    hidden1 = (-0.46122 * age) + (0.97314 * weight) + (-0.39203 * height) + 1*0.80109
    hidden1act = f_act(hidden1)
    hidden2 = (0.78548 * age) + (2.10584 * weight) + (-0.57847 * height) + (1*0.43529)
    hidden2act = f_act(hidden2)
    output = (-0.81546 * hidden1act) + (1.03775 * hidden2act) - 1*0.2368
    return output




print("Output: ",neural_net_ex6(23,75,176))