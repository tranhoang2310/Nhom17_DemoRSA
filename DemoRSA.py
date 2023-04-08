import random
import math
from random import randrange
import time
import binascii

##############################################
#Hàm kiểm tra nguyên tố bằng Rabin Miller
#Chạy thuật toán Rabin Miller kiểm tra 30 lần
def HamRabinMiller(n, k=30):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True    

##############################################
MangSoNguyenTo =   [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,
                        173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,
                        359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,
                        569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,
                        769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

##############################################
#Hàm tạo số nguyên tố lớn theo độ dài n Bit   
def TaoSoNgauNhien(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
 
#Tạo Số Nguyên Lớn Ngẫu Nhiên và Kiểm tra nguyên tố với Sàng Eratosthenes (Sieve of Eratosthenes)  
def KiemTraNguyenToEratosthenes(n):
    while True:
        # Tạo Số Ngẫu Nhiên n Bit
        pc = TaoSoNgauNhien(n)
 
        # Sàng Eratosthenes (Sieve of Eratosthenes)
        for divisor in MangSoNguyenTo:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            return pc

def TaoSoNguyenTo(n):
  while True:
        SoNguyenTo = KiemTraNguyenToEratosthenes(n)
        if not HamRabinMiller(SoNguyenTo):
            continue
        else:
            return SoNguyenTo
  return 0;

##############################################
#Hàm tìm Ước Chung Lớn nhất của a và b
def TimUCLN(a,b):
  if b==0:
    return a
  return TimUCLN(b,a%b);

##############################################
#Hàm EuClide mở rộng  
def HamEuclideMoRong(a, b):
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx

##############################################
#Hàm Sinh Khoá theo Size
def HamSinhKhoa(n):
  #Tạo số nguyên tố p
  while(True):
    p=TaoSoNguyenTo(n);
    if(p!=0):
      break
  print("Số Nguyên Tố p với size ",n," Bit là:",p);

  #Tạo số nguyên tố q
  while(True):
    q=TaoSoNguyenTo(n);
    if(q!=p and q!=0):
      break
  print("Số Nguyên Tố q với size ",n," Bit là:",q);

  #N = p*q
  n=p*q;
  phi=(p-1)*(q-1);

  #Chọn e cố định = 2150134321 (Là Số Nguyên Tố)
  e=2150134321;

  #Tính d=e^-1 trong phi(n)
  d=HamEuclideMoRong(e,phi);

  return (n,e),(n,d)

##############################################
#Mã hoá
def HamMaHoa(KhoaCongKhai,m):
  n,key=KhoaCongKhai
  return pow(m,key,n)

##############################################
#Giải mã
def HamGiaiMa(KhoaCongKhai,c):
  n,key=KhoaCongKhai
  return pow(c,key,n)

##############################################
#Main function của Demo Code => Quy trình là: Nhập Size để tạo Key
print("============================================================:")
print("============================================================:")
print("")

n =int(input("Xin Mời Nhập size (Bit) "))

print("")
print("Tạo số nguyên tố ngẫu nhiên")
KhoaCongKhai,KhoaBiMat= HamSinhKhoa(n);
print("")

n,e=KhoaCongKhai
print("Cặp Khoá Công Khai là (",n ,", ",e,")") 
print("")

n,d= KhoaBiMat
print("Cặp Khoá Bí Mật là (", n,", ",d,")") 

print("")
m=input("Nhập Thông Điệp Cần Mã Hoá: ")
m=int(binascii.hexlify(m.encode()),16)
c=HamMaHoa(KhoaCongKhai,m);
print("")
print("Thông Điệp Sau Khi Đã Mã Hoá Thành Công: ",hex(c));

print("")
m=HamGiaiMa(KhoaBiMat,c);


print ("Kết Quả Sau Khi Giải Mã Thông Điệp: "+bytearray.fromhex(hex(m).split('x')[-1]).decode())
print("")
print("============================================================:")
print("============================================================:")