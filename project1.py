#asking name 
name = input("Whats your name ?  ")
print("Hey," + name +" I am Iron man i will calculate your weight in future")

#asking age
age = input("What is your Age  ? ")
print("ohh great I thought you are 17")

#
# input()
#asking weight

weight = input("What is Your current weight  ? \n")
#if he i saying not weight
if weight == "0":
    print(" are u crazy " + name + " get out")

    exit()

#userweight = input()
#reciving input and giving output
print("Okay i am going to calculate your weight in 2028")
input()

print("I am going to calculate, your age is " + age  + " And your weight is " + weight + "kg")
input()

print("YES OR NO")

yes = input()

if yes == "no":
   print("so good bye")
   exit()

menu = "YES"
#options yes or no
print("You choosed," + menu +" nice Decition")
input()

result = int(weight)/int(age) + int(weight) + 11

print(result)

if  int(weight) < 100: 
    
 print("You are so faty. Try to do ome workout ")


exit()
print("goo its a Normal weight")

if weight == "0":
    print(" are u crazy " + name + "nigga")


