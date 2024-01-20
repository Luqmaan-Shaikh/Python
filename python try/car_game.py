command=""
started = False
while True:
   command = input("> ").lower()
   if command == "start":
      if started:
         print("CAR IS ALREADY STARTED !!!!!!")
      else:
         started = True
         print("CAR STARTED ...... READY TO GOOOOO !!!!")
   elif command == "stop":
      if not started:
         print("CAR IS ALREADY STOPPED !!!")
      else:
         started = False
         print("CAR STOPPED ... ")
   elif command == "help":
      print("""
start - to start the car
stop - to stop the car
quit - to quit 
      """)
   elif command == "quit":
      break
   else:
      print("SORRY , I don't understand that")

      