'''a program used to find the area of a triangle using Heron's formula'''
print("Enter the length of sides")
s1=int(input())
s2=int(input())
s3=int(input())
p=s1+s2+s3
print("The addition of {} {} {} gives perimeter of {}".format(s1,s2,s3,p))
s=p/2
pa=s*(s-s1)*(s-s2)*(s-s3)
print("pa is equal to {}".format(pa))
import math 
A=math.sqrt(pa)
print("The area is {}".format(A))