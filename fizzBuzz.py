# __ IMPORTED MODULES : ____________________________________________________
import keyboard
import random
import time
import os
#==============================================================================

# __ GLOBALS : _____________________________________________________________
ColorReset = cr = '\u001b[0m'
#==============================================================================

"""_________________________________________________________________________"""
# -- FUNCTIONS :   
"""‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""
# RETURNS the given string in a given color ('red', 'green', 'blue') fore/back
#   : by using Asci Esc Sequences, because they work on nearly every terminal
# _____________________________________________________________________________
def color_output (  stringToColor , color , foreground  ) :
  AsciEscSeq      = aec = '\u001b['
  ColorForeground = cf  = '38;2;'
  ColorBackground = cb  = '48;2;'
  coloredString   = CS  = aec
  Red   = r = '255;0;0'
  Green = g = '0;255;0'
  Blue  = b = '0;0;255'
  #
  if   foreground == True  : CS += cf
  else                     : CS += cb
  #
  if   color == 'red'  : CS += r
  elif color == 'green': CS += g
  elif color == 'blue' : CS += b
  #  could use another method here to decode a given string eg: 'x,y,z' [0-255]
  # USE WHITE__________________________________________________________________
  else                 : CS += '255;255;255'
  CS += 'm'
  CS += stringToColor + ColorReset
  #
  return CS

# PRINTS a single keystroke___________________________________________________
def on_press(key):
  #
  if   key == 'esc' : quit_program()
  else              : print('Key pressed:', key)

# QUITS THE PROGRAM RETURNS false______________________________________________
def quit_program():
  os.system('cls')
  print(' ' + color_output('[esc] ▻ Program stoped ', 'red', False))
  quit
  return False 

# RETURNS a user input_________________________________________________________
def get_input():
  return input("What do you want to do? ")

# PRINTS a prompt______________________________________________________________
def prompt(round_counter):
  # ___PLAYER_TURN__________________________________
  if round_counter % 2 == 0:  
   #
   key = player_round(round_counter)
   return key
  else:
   computer_round(round_counter)
   return

# PLAYS a player-rounnd, checks WIN / LOSE condition___________________________
def player_round(round_counter):
  print(  color_output(  'your turn    '      , 'green' , True  )  )
  print(  color_output(  '[w] - Fizz'         , 'green' , True  )  )
  print(  color_output(  '[a] - Buzz'         , 'green' , True  )  )
  print(  color_output(  '[s] - Fizz-Buzz'    , 'green' , True  )  )
  print(  color_output(  '[d] - print Number' , 'green' , True  )  )
  #
  key = keyboard.read_key()
  on_press(key)
  #
  player_choice = ''
  #
  if key == 'w':
    player_choice = 'Fizz'
    print(  f'{ color_output( player_choice , 'green' , False  ) }'  )
  if key == 'a':
    player_choice = 'Buzz'
    print(  f'{ color_output( player_choice , 'green' , False  ) }'  )
  if key == 's':
    player_choice = 'Fizz-Buzz'
    print(  f'{ color_output( player_choice , 'green' , False  ) }'  )
  if key == 'd':
    print(  f'{ color_output(  str(round_counter) , 'green' , False  ) }'  )
    player_choice = calculate_output(round_counter)
  #
  expected_output = calculate_output(round_counter)
  #
  if  expected_output == player_choice : return player_choice
  else : 
    print(  f'{ color_output(  ' FAIL ' , 'red' , True  ) }'  )
    time.sleep(1)
    print(  f'{ color_output(  'you lost the game' , 'red' , True  ) }'  )
    time.sleep(1)
    print(  f'{ color_output(  '.' , 'red' , True  ) }'  )
    time.sleep(1)
    print(  f'{ color_output(  '.' , 'red' , True  ) }'  )
    time.sleep(1)
    print(  f'{ color_output(  '.' , 'red' , True  ) }'  )
    #
    quit_program()
    return 'esc'

# PLAYS a computer-round_______________________________________________________
def computer_round(roundCounter):
  print(color_output('my turn' , 'blue' , True))
  time.sleep(1)
  output = calculate_output(roundCounter)
  print(color_output(output, 'blue', False))

# RETURNS the proper output for a given round__________________________________
def calculate_output(roundCounter):
  result = ''
  if   roundCounter % 3 == 0 and roundCounter % 5 == 0 : result = 'Fizz-Buzz'
  elif roundCounter % 3 == 0                           : result = 'Fizz'
  elif roundCounter % 5 == 0                           : result = 'Buzz'
  else : result = str(roundCounter)
  #
  return result

# PRINTS the menu, rolls a random Number to determin who starts the game_______
def print_menu(round_counter):
  menu_points = [color_output(' play ... [any key] ' , 'green' , True) , color_output(' exit ...   [esc]   ' , 'red' , True)]
  for i in (0,1):
    print(f'                {menu_points[i]}')
  #
  key = keyboard.read_key()
  key = on_press(key)
  #
  if key == 'esc':
    quit_program()
    return False
  else: 
    print(color_output('Who starts? . . . rolling', 'blue', True))
    key = keyboard.read_key()

    rnd = random.Random(1)

    if rnd == 0 :
      return True
    else :
      round_counter += 1
      return True

# PRINTS the games title_______________________________________________________
def print_header():
  os.system('cls')
  print(color_output(' ~ ~ ~ ~ ~ ~~~ Fizz, Buzz, Fizz- Buzz ~~~ ~ ~ ~ ~ ~ ' , 'green' , True))
  print()
#==============================================================================


"""_________________________________________________________________________"""
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
#  Main 'entry point' of the program                         [ main game-loop ]
#________________________________________________________________________  
"""‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""
def main(): 
  run_game = True
  round_counter = 1
  
  while(run_game):                      
   if round_counter == 1 : 
    print_header()
    run_game = print_menu(round_counter)

   if run_game == True:
    key = prompt(round_counter)
    if key == 'esc':
      run_game = False
    round_counter += 1
#______________________________________  


#____CALL_MAIN_PROGRAM_________________
if __name__ == '__main__':            # 
  main()                              #
  quit
#________________________________  
"""‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""

