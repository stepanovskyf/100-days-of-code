import webbrowser
import time

print("Welcome to your journey")
print("Your mission is to find your way to bratislava from ljubljana")
start = input("Do you wish to start? y/n ")
start = start.lower()
if (start == "y"):
    print("You start here:\n")
    time.sleep(3)
    webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/4/46/Ljubljana_%28296%29_%283896834569%29.jpg')
    print("So you have started...\n You go at the speed of 50km/h towards Highway")
    highway1 = input("Do you wish to \na Go on the highway\nb Continue to Vrhnika\n")
    highway1 = highway1.lower()
    if (highway1 == "a"):
        print("You have decided to continue on your journey to Bratislava")
        print("You are now cruising along the highway along Ljubljana\nYou suddenly come to a fork...")
        fork1 = input("Do you \na Wish to turn on the fork in the direction of Maribor\nb Wish to turn in direction of Ljubjlana-jug?\n")
        fork1 = fork1.lower()
        if (fork1 == "a"):
            print("You have chosen to cruise along the highway along Celje and Maribor and you are continuing your journey")
            time.sleep(1)
            print("5...")
            time.sleep(1)
            print("4...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("You have arrived at the border crossing between Austria and Slovenia...")
            time.sleep(3)
            webbrowser.open('https://www.euractiv.com/wp-content/uploads/sites/2/2022/05/shutterstock_1760388668-800x450.jpg')
            border1 = input("Border police asks you for your ID.\nYou \na Show the ID\nb Are a criminal and afraid to show your ID as it would expose you are on the run from the police\n")
            border1 = border1.lower()
            if (border1 == "a"):
                print("You have shown you are not a criminal and are now on the way again cruising the Austrian highway")
                time.sleep(1)
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                print("You have come to Graz")
                time.sleep(3)
                webbrowser.open('https://thumbs.dreamstime.com/b/graz-road-sign-against-clear-blue-sky-147111625.jpg')
                fork2 = input("Do you\na Use the exit to the direction of Vienna\nb Use the exit into Graz\n")
                fork2 = fork2.lower()
                if (fork2 == "a"):
                    print("You are now on the way to Vienna")
                    time.sleep(1)
                    print("3...")
                    time.sleep(1)
                    print("2...")
                    time.sleep(1)
                    print("1...")
                    time.sleep(1)
                    while True:
                        fork3 = input("You have come to Vienna\nWill you\na Continue to Bratislava\nb Get a coffee and go to Bratislava later\nc Go back to Slovenia \n")
                        fork3 = fork3.lower()
                        if (fork3 == "a"):
                            print("You are now on the way to Bratislava")
                            print("You have chosen to go to Bratislava now...\nYou continue on the highway...")
                            time.sleep(1)
                            print("3...")
                            time.sleep(1)
                            print("2...")
                            time.sleep(1)
                            print("1...")
                            time.sleep(1)
                            print("You are almost there...\nYou have been stopped at the border of Slovakia tho...")
                            border2 = input("Do you\na Show your ID\nb Decide it's not worth it and return home\n")
                            if(border2 == "a"):
                                print("You have shown your ID and are travelling to Bratislava now...")
                                print("You have come to Bratislava")

                            else:
                                print("You have decided to go home now")
                                break
                        elif (fork3 == "c"):
                            print("You went home.")
                            break
                        else:
                            print("You got some nice coffee and now you can choose what to do again")
                            time.sleep(3)


                else:
                    print("You got lost in Graz")
            else:
                print("You did not show your ID and have been charged and are now in prison")
        else:
            print("You have decided to come home and wasted your precious fuel")
    else:
        print("You are now on your way home to Ljubljana")
else:
    print("Goodbye")
