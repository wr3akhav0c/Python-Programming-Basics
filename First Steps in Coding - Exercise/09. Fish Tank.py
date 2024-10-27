length = int(input())
width = int(input())
height = int(input())
percentStuff = float(input())

vAquarium = length * width * height
vInL = vAquarium * 0.001
stuff = percentStuff / 100

print(vInL * (1-stuff))