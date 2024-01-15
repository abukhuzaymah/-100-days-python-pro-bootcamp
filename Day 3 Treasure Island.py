print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You have encountered two different paths, would you like to go left or right?")
x = input()
y = x.lower()
if y == "left":
    print("""After twisting and turning down the pass, you encountered a slow moving river, would you like to swim or wait to see if the coast is clear?""")
    s = input()
    z = s.lower()
    if z == 'swim':
        print("""You have been attacked by a massive trout! GAME OVER!
               _
                 )_ `.
                )_ `. \
               )_ `. `|
              )_ `.` /
             )_ `.` ` \
             )_.- ` `  \
              )_.-` `   \
               )_.-`\ /\ \
                )_.-| \O  \
                    |  \   \
          _        /   /    \        _
         ) `-._   / /O\  /O\ \   _.-` (
        )      `-/  `-'  `-'  \-`      (
        )     _.-|    __      |-._     (
         )_.-`   \ .-'  `-._  /   `-._(
                  \ `-.__.--`/
                   `-._  _.-"
                       ``""")
    else:
        print("""You waited to see the coast is clear and observed a duck landing on the slow moving river, only for it to be engulfed by a giant troat! You've found a boat hidden in the bushes on the river bank, still operational! You slowly push the boat into the river and quietly hop on, thankfully the troat is not big enough to engulf the boat. You have safely made it to the other side of the river. And you come across many different coloured trap doors. Which door do you pick?""")
        c = input()
        c = c.lower()
        if c == 'red':
            print("""You have been burnt by fire! GAME OVER! 
                 (  .      )
                   )           (              )
                         .  '   .   '  .  '  .
                (    , )       (.   )  (   ',    )
                 .' ) ( . )    ,  ( ,     )   ( .
              ). , ( .   (  ) ( , ')  .' (  ,    )
              (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
              jgs^^^^^^^^^^^""")
        elif c == 'blue':
            print("""You have been eaten by beasts! GAME OVER!
                /\\
                                  ( ;`~v/~~~ ;._
                             ,/'"/^) ' < o\  '".~'\\\--,
                           ,/",/W  u '`. ~  >,._..,   )')
                          ,/'  w  ,U^v  ;//^)/')/^\;~)')
                       ,/"'/   W` ^v  W |;         )/'
                     ;''  |  v' v`" W }  \
                    "    .'\    v  `v/^W,) '\)\.)\/)
                             `\   ,/,)'   ''')/^"-;'
                                  \
                                   '". _
                                        \ """)
        elif c == 'yellow':
            print(r"""You win! Enjoy your prize
                                              _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||
                           _.-:'_.-::::::'  ||
                         .'`-.-:::::::'     ||
                        /.'`;|:::::::'      ||_
                       ||   ||::::::'     _.;._'-._
                      ||   ||:::::'  _.-!oo @.!-._'-.
                      \'.  ||:::::.-!()oo @!()@.-'_.|
                       '.'-;|:.-'.&$@.& ()$%-'o.'\U||
                          `>'-.!@%()@'@_%-'_.-o _.|'||
                           ||-._'-.@.-'_.-' _.-o  |'||
                           ||=[ '-._.-\U/.-'    o |'||
                           || '-.]=|| |'|      o  |'||
                           ||      || |'|        _| ';
                           ||      || |'|    _.-'_.-'
                           |'-._   || |'|_.-'_.-'
                            '-._'-.|| |' `_.-'
                                '-.||_/.-'
                   """
            )
        else:
            print("GAME OVER")
else:
  print("You have fallen into a hole. GAME OVER")
