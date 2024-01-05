a = []
usr_op = 0
while(not usr_op == "5",):
  usr_op = input("""
  choice a operation, input by number
  1. add number
  2. delete a numer
  3. print list
  4. find anvger
  5. exit program
  """)
  if(usr_op == "1"):
    usr_input = input("input number for list")
    if(usr_input.isdigit()):
      a.append(int(usr_input))
    else:
      print("something went wrong")
  elif(usr_op == "2"):
    usr_input2 = input("remove a number by type it")
    if(usr_input2.isdigit()):
      if(not int(usr_input2) > len(a)):
        usr_input2 = int(usr_input2)
        a.pop(usr_input2)
      else: print("try again")
    else:
      print("try again")
  elif(usr_op == "3"):
    e = 0
    for x in a:
      print("index",e,":",x)
      e = e + 1
  elif(usr_op == "4"):
    avge = 0
    answer = 0.0
    for p in range(0,len(a)):
      if(not a[p] == 0):
        avge = avge + a[p]
      answer = avge / len(a)
    print(answer)
  elif(usr_op == "5"):
    exit()
  else:
    print("check your input")