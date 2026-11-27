# for i in range(1,4):
#     for j in range(1,4):
#         print("*",end="") 
#     print()  
# ***
# ***
# *** 


# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end="")
#     print()
# 111
# 222
# 333

# for i in range(1,5):
#     for j in range(1,5):  
#         print(j,end="")
#     print() 
# 1234
# 1234
# 1234
# 1234 

# for i in range(5,1,-1):
#     for j in range(5,1,-1):
#         print(i,end="")
#     print()
# 5555
# 4444
# 3333
# 2222                


# for i in range(5,1,-1):
#     for j in range(5,1,-1):
#         print(j,end="")
#     print()    
# 5432
# 5432
# 5432
# 5432   

# n=5
# k=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("{:2d} ".format(k),end="")
#         k+=1
#     print()
# 1  2  3  4  5 
#  6  7  8  9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 
# 21 22 23 24 25
         
# n=5
# k=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("{:2d} ".format(k),end="")
#         k+=2
#     print()    
# 1  3  5  7  9 
# 11 13 15 17 19 
# 21 23 25 27 29 
# 31 33 35 37 39 
# 41 43 45 47 49     

# n=5
# k=2
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("{:2d} ".format(k),end="")
#         k+=2
#     print()    
# 2  4  6  8 10 
# 12 14 16 18 20 
# 22 24 26 28 30 
# 32 34 36 38 40 
# 42 44 46 48 50 

# n=5
# k=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("{:2d} ".format(k),end="")
#         k+=5
#     print()    
# 5 10 15 20 25 
# 30 35 40 45 50 
# 55 60 65 70 75 
# 80 85 90 95 100 
# 105 110 115 120 125    

# n=3
# k=2
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("{:2d}  ".format(k),end="")
#         k*=2
#     print() 
# 2   4   8  
# 16  32  64  
# 128  256  512    

a=5
for i in range(1,a+1):
    print("* "*i)   

a=5
b=1
for i in range(1,b+1):
    for j in range(b-i):
        print("{:2d} ".format(b),end="")
        b+=1
    print()        

