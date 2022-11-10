print("Please enter number to check whether it is prime or not")
ip = input()

a = 2

while int(ip) % a != 0:
    a += 1

print("check " + str(a))

if str(a) == str(ip):
    print("Entered number " + ip + " is prime number")
