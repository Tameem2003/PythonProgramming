import time
correct =0
print("Hello, welcome to quiz and true or false game.")
print("Totally there will be 3 rounds")
print("Each Round consists of 5 questions")
print("1st Round - Questions with clue")
print("2nd Round - Questions without clue")
print("3rd Round - True or False")
time.sleep(8)
name = input("What is your name?"   )
time.sleep(2)
print(name,",nice name")
time.sleep(2)
print("Lets begin!!")
print("1st Round:")

#1
time.sleep(2)
print("1.How many seconds are there in an hour?")
print("Clue :: There are 60 seconds in 1 minute")
print("and 60 minutes in an hour")
ans1 = int(input(">>>"))
one = 3600
if (ans1 == ques1):
	correct +=1
else:
	 correct +=0

#2	 
time.sleep(2)
print("2.How many days are there in leap year")
print("Clue :: 1 month will have 29 days in leap year.")
ans2= int(input(">>>"))
two = 366
if ans2 in two:
	correct +=1
else:
	correct +=0
	
#3	
time.sleep(2)
print("3.Who is the president of America?")
print("Do you watch the donald duck show :):)")
ans3 = input(">>> ")
three = "Donald Trump,donald trump"
if ans3 in three:
	correct +=1
else:
	correct +=0

#4	
time.sleep(2)
print("4.Which is the largest ocean?")
print("Its name starts from the letter P")
ans4 = input(">>>")
four = "Pacific Ocean,pacific ocean,pacific,Pacific"
if  ans4  in four:
	correct +=1
else: 
    correct +=0
  
 #5  
time.sleep(2)
print("5.What is the name of Bengaluru International Airport?")
print("It was named after a person who built Bengaluru")
ans5 = input("(type the name only) >>>")
five = "Kempegowda,kempegowda"
if ans5 in five:
	  correct +=1
else:
	   correct +=0
print("1st round is over",name,"lets move on 2nd round.")

#6
time.sleep(2)
print("6.Which is the capital of India.")
ans6 = input(">>>")
six = "New Delhi,new delhi ,newdelhi,New delhi"
if ans6 in six:
  	correct +=1
else:
  	correct +=0

#7
time.sleep(2)
print("7.The capital of China is?")
ans7 = input(">>>")
seven = "Beijing,beijing"
if ans7 in seven:
 	 correct +=1
else :
	  correct +=0

#8	  
time.sleep(2)
print("8.Which city is known as the                     silicon city.")
ans8 = input(">>>")
eight ="Bengaluru,bengaluru,banglore,Banglore,bangalore"
if ans8 in eight:
 	correct +=1
else:
	  correct +=0

#9
time.sleep(2)
print(" 9.Which is the biggest planet.")
ans9 = input("Your answer >>>")
nine = "Jupiter,jupiter"
if ans9 in nine:
  	correct +=1
else:
	  correct +=0
	  
#10
time.sleep(2)
print("10.What is the full form of CD")
ans10 = input(">>>")
ten ="Compact Disk,compact disk,Compact disk,compact disc,Compact disc,Compact Disc"
if ans10 in ten:
 	correct += 1
else:
	 correct +=0
time.sleep(3)
	
print("Ok",name,"lets move on to 3rd round.")
true = ["True","true","t"]
false = ["False","false","f"]

#11
time.sleep(2)
print("Type T/t or F/f for true or false")
print("11.Blue whale is a mammal.")
choice = input(">>>")
if choice in true:
	correct +=1
else :
	correct +=0
	
#12
time.sleep(2)
print("12.New Delhi is an union territory")
choice =input(">>>")
if choice in true:
     correct +=1
else:
	correct +=0

#13
time.sleep(2)
print("13.There are 22 spokes in Ashoka                  Chakra.")
choice = input(">>>")
if choice in false:
	correct +=1
else:
	correct +=0
	
#14
time.sleep(2)
print("14.Bill gates is the founder of                 Microsoft.")
choice = input(">>>")
if choice in true:
	correct +=1
else:
	correct +=0
	
#15
time.sleep(2)
print("15.Mango is the National fruit of India.")
choice = input(">>>")
if choice in true:
	correct +=1
else:
	 correct +=0
time.sleep(2)
if correct == 15:
  print("Wow Congrats",name,"You got",correct,"/15")
elif(correct <=15 , correct >=10):
	print("Not bad",name,"You got",correct,"/15")
else:
	print("Good luck next time,You got", correct,"/15")