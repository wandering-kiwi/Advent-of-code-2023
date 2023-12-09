t=60947882 
#  both t and l from my puzzle input so i dont have to find the numbers in the code, cos i cant be bothered
# i realise i can do this in one line but i want to be able to change the numbers for t and l without making a faff
l=475213810151650
a = (t + (t**2 - 4*l)**0.5)/2
b = (t - (t**2 - 4*l)**0.5)/2
print(int(a-int(b)))