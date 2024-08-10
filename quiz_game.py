print("welcome to my computer quiz!!!!")
playing = input("do you want to play?")
if playing.lower()!= "yes":
    quit()

print("okay lets play!!")
score=0

answer=input("what does cpu stand for?")
if answer.lower() == "central processing unit":
    print("correct")
    score=score+1
else:
    print("not correct")

answer=input("what does gpu stand for?")
if answer.lower() == "graphics processing unit":
    print("correct")
    score = score + 1
else:
    print("not correct")

answer=input("what does psu stand for?")
if answer.lower() == "power supply":
    print("correct")
    score = score + 1
else:
    print("not correct")

answer=input("what does RAM stand for?")
if answer.lower() == "random access memory":
    print("correct")
    score = score + 1
else:
    print("not correct")


print(f"your score is : {score}")
if score==4:
    print("wow!!!! hurrayyyyyy:) highest score")
elif score==2 or score==3:
    print("very good!!!!")
else:
    print("can be done better")