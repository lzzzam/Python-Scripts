print('''
  _______________________________
 /\                              \\
/++\    __________________________\\
\+++\   \ ************************/
 \+++\   \___________________ ***/
  \+++\   \             /+++/***/
   \+++\   \           /+++/***/
    \+++\   \         /+++/***/
     \+++\   \       /+++/***/
      \+++\   \     /+++/***/
       \+++\   \   /+++/***/
        \+++\   \ /+++/***/
         \+++\   /+++/***/
          \+++\ /+++/***/
           \+++++++/***/
            \+++++/***/
             \+++/***/
              \+/___/
''')

print("\n\nWELCOME TO THIS GAME\n\n")

answer = input("Do you go left or right? [L or R] ==> ")

if answer == 'L':
    answer = input("You arrive in a lake, you take the boat or swim? [B or S] ==> ")
    if answer == 'S':
        answer = input("You arrive in a Room with 3 doors, you choose Left, Center or Right? [L, C, R] ==> ")
        if answer == 'R':
            print("You WIN")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")

