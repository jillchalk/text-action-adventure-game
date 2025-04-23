import time
import tkinter as tk

x = "You are Trapped Forever"
y = "You have died"
a = "You Escaped!"
b = "You escaped."
c = "You Escaped!!!"
d = "Took The Longest Path to Freedom"


def main():
  global root
  root = tk.Tk()
  root.title("Escape The Dungeon")
  root.attributes('-fullscreen', False)

  root.geometry("800x400")

  title_label = tk.Label(root,
                         text="Welcome to Escape The Dungeon",
                         font=("Helvetica", 20))
  title_label.pack(pady=100)

  start_button = tk.Button(root, text="Start Game", command=start_game)
  start_button.pack()

  root.mainloop()


def clear_text(text_output):
  text_output.delete("1.0", tk.END)


#change delay back to 50/50 before you turn in.
def insert_with_delay(text_output, text, delay=50, newline_delay=50):
  lines = text.split('\n')
  for line in lines:
    line = line.strip()
    if line:
      for char in line:
        text_output.insert(tk.END, char)
        text_output.see(tk.END)  # Scroll to the bottom
        text_output.update()
        time.sleep(delay / 1000)
      text_output.insert(tk.END, '\n')
      text_output.see(tk.END)  # Scroll to the bottom
      text_output.update()
      time.sleep(newline_delay / 1000)  # Delay before moving


def destroy_all_buttons(root):
  for widget in root.winfo_children():
    if isinstance(widget, tk.Button):
      widget.destroy()


def restart_game():

  root.destroy()

  main()


def start_game():
  global root
  root.destroy()
  root = tk.Tk()
  root.title("Escape The Dungeon")
  root.attributes('-fullscreen', False)
  root.geometry("800x400")

  text_output = tk.Text(root, height=9.45, width=100, font=("Helvetica", 20))
  text_output.pack(anchor=tk.CENTER)

  initial_story = """
  You wake up in chains, trapped in a dungeon.
  As you look around, 
  you see an unknown man, a rusty saw to your left, 
  and a key on the far side of the room.
  With no hope of escape 
  unless one of you takes drastic action,
  the rusty saw gleams in the dim light.
  What will you do?"""
  insert_with_delay(text_output, initial_story)

  button_saw_off = tk.Button(root,
                             text="Saw Off Your Own Hand",
                             command=lambda: saw_off_own_hand(text_output))
  button_saw_off.pack()

  button_give_saw = tk.Button(
      root,
      text="Give the Saw to the Other Man",
      command=lambda: give_saw_to_other_man(text_output))
  button_give_saw.pack()

  button_wait_rescue = tk.Button(
      root,
      text="Wait to be Rescued",
      command=lambda: stay_trapped_forever(text_output))
  button_wait_rescue.pack()


#Choice 2 ^^^
def give_saw_to_other_man(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)

  text = """
  You extend an offer of sacrifice to the 
  other prisoner, giving them the saw and 
  allowing them to make the painful decision.
  The other man hesitates, overwhelmed by 
  the weight of your offer. Eventually, he accepts.
  You watch in silence as he saws 
  off his own hand.With the key in hand, 
  he unlocks his restraints and escapes, 
  leaving you behind to contemplate the price of freedom.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, x + "\n")  # Ending

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#Choice 3 ^^^
def stay_trapped_forever(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  You refuse to make any sacrifices and resign 
  yourselves to an eternity in the dungeon,
  choosing to endure the suffering rather than 
  inflict it upon yourselves or each other.
  Days turn into weeks, and weeks turn into 
  months as you languish in the darkness, 
  your hope dwindling with each passing moment.
  Eventually, you both succumb to despair, 
  resigned to your fate as eternal prisoners of the dungeon.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, x + "\n")  #ending

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#choice 1 ***
def saw_off_own_hand(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)

  text = """
You steel yourself for the agonizing pain
and use the saw to sever your own hand, 
sacrificing a part of yourself for the 
chance at freedom.With trembling hands 
and gritted teeth, you endure the excruciating pain 
as the saw bites through your flesh.
Bloodied and weakened, you grasp the 
key and unlock your restraints.
After freeing yourself from the chains, 
you look over at the other prisoner and must make a decision.
    """
  insert_with_delay(text_output, text)

  #buttons
  button_unlock_man = tk.Button(root,
                                text="Unlock the other man",
                                command=lambda: unlock_man(text_output))
  button_unlock_man.pack()

  button_leave_him = tk.Button(root,
                               text="Leave Him",
                               command=lambda: leave_him(text_output))
  button_leave_him.pack()


#yellow path ***
def unlock_man(
    text_output):  #come back and fix this later!! update: fixed somehow??
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
You decide to unlock the other man who is trapped
Despite your pain and exhaustion, 
you approach the other prisoner 
and use the key to unlock his restraints,
offering him the chance at freedom.
The other man, stunned by your selflessness, 
thanks you profusely as tears of gratitude 
streak down his face.
Together, you limp out of the dungeon. 
Despite the loss of your hand, 
you find solace in the knowledge that 
you chose compassion over self-preservation. 
After escaping your restraints, you and the 
other prisoner navigate the labyrinthine corridors 
of the dungeon until you come across a 
peculiar door with an arm-shaped hole.
Given that you sacrificed your own hand 
to obtain the key, the other prisoner offers to 
put his arm into the hole, reasoning that he 
has nothing left to lose.
What will you do?
"""
  insert_with_delay(text_output, text)

  #buttons
  button_allow_man = tk.Button(root,
                               text="Allow the Other Man to Put His Arm In",
                               command=lambda: allow_man(text_output))
  button_allow_man.pack()

  button_put_your_arm = tk.Button(root,
                                  text="Put Your Other Arm In the Hole",
                                  command=lambda: put_your_arm_in(text_output))
  button_put_your_arm.pack()

  button_turn_around = tk.Button(root,
                                 text="Turn Around and Find Another Way Out",
                                 command=lambda: turn_around(text_output))
  button_turn_around.pack()


#first ending on yellow path ^^^^^^
def allow_man(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)

  text = """
  With a solemn nod, the other man steps forward 
  and inserts his arm into the hole.
  Suddenly, the door swings open, revealing 
  a path to freedom!!! However...
  As the other man celebrates, a hidden mechanism triggers, 
  and spikes emerge from the walls, impaling him.
  Shocked and horrified, you realize you've escaped,
  but at the cost of the other man's life.
  """

  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, b)  # Ending

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#two possible endings for yellow ^^^^
def put_your_arm_in(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Faced with the uncertainty of what 
  lies beyond the door, you steel yourself 
  and offer your remaining arm as a sacrifice, 
  hoping it will lead to both yours and your 
  new companion's freedom.
  """
  insert_with_delay(text_output, text)

  import random

  def event_choice():
    if random.random() < 0.5:
      # Escape
      text = """
      With a mixture of fear and determination, 
      you insert your arm into the hole.
      The door creaks open, and you cautiously step through, 
      emerging into the blinding light of freedom.
      Though you've lost both hands, you've gained your liberty,
      a bittersweet victory as you contemplate
      the sacrifices made along the way.
      """

      insert_with_delay(text_output, text)
      clear_text(text_output)
      insert_with_delay(text_output, a)

    else:
      # Death
      text = """
        With a solemn nod, the other man steps forward
        and inserts his arm into the hole.
        Suddenly, the door swings open, 
        revealing a path to freedom!!! However...
        As the other man celebrates, a hidden mechanism triggers, 
        and spikes emerge from the walls, impaling him.
        Shocked and horrified, you realize you've escaped,
        but at the cost of the other man's life.
        """

      insert_with_delay(text_output, text)
      clear_text(text_output)
      insert_with_delay(text_output, y)

  event_choice()

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#yellow cont. 1    *****
def turn_around(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """"
  Uncertain of the risks posed by the door, 
  you and your companion decide to backtrack 
  and search for an alternative route to freedom. 
  After walking down the dark hallways of the dungeon, 
  you accidentally trigger a trap door 
  concealed within the floor. You and the other
  prisoner plummet into the darkness of the pit below.
  As you land with a thud, the faint sound of 
  slithering reaches your ears, indicating the 
  presence of a dangerous creature lurking in the shadows.
  What will you do?
  """
  insert_with_delay(text_output, text)

  #buttons
  button_fight = tk.Button(root,
                           text="Fight the Creature",
                           command=lambda: fight_creature(text_output))
  button_fight.pack()

  button_run = tk.Button(root,
                         text="Run Away",
                         command=lambda: run_away(text_output))
  button_run.pack()

  button_shove_man = tk.Button(root,
                               text="Sacrafice the Man",
                               command=lambda: shove_man(text_output))
  button_shove_man.pack()


#deaths for both yellow and blue path ^^^^
def run_away(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Frantically, you scramble to your feet,
  heart pounding with fear,
  and make a desperate attempt to flee. 
  However, the creature is faster, 
  its venomous fangs sinking into your 
  flesh before you can escape.
  As darkness engulfs your vision,
  you realize that your attempt to
  run has sealed your fate, 
  succumbing to the horrors of the dungeon's depths.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, y)  # Death

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


# yellow 3  *****
def fight_creature(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Despite the odds stacked against you, 
  you and the other prisoner quickly devise a plan
  to fend off the creature together, 
  pooling your resources and coordinating your efforts.
  With makeshift weapons in hand, 
  you and the other prisoner stand your ground 
  against the creature's relentless assault.
  Through sheer determination and teamwork,
  you manage to fend off the creature
  long enough to find a hidden passage leading to safety.
  Together, you climb out of the pit, 
  bruised and battered but alive,
  having triumphed over the perilous encounter 
  through cooperation and resilience.
  After fighting together against the creature 
  and finding a hidden passage 
  leading away from the pit,
  You and the other prisoner cautiously 
  venture deeper into the labyrinthine tunnels.
  The air grows colder, and the faint echo 
  of distant water reaches your ears,
  Hinting at the presence of an underground river.
  What will you do?
  """
  insert_with_delay(text_output, text)

  #buttons
  button_explore = tk.Button(root,
                             text="Explore the Tunnel System",
                             command=lambda: explore_tunnels(text_output))
  button_explore.pack()

  button_search = tk.Button(root,
                            text="Search for Clues",
                            command=lambda: search_for_clues(text_output))
  button_search.pack()

  button_rest = tk.Button(root,
                          text="Rest and Recover",
                          command=lambda: rest_and_recover(text_output))
  button_rest.pack()

  button_follow_river = tk.Button(root,
                                  text="Follow the River",
                                  command=lambda: follow_river(text_output))
  button_follow_river.pack()


# merges with blue path 2 ******
def shove_man(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Recognizing the urgency of the situation, 
  you make a split-second decision to
  sacrifice the other prisoner,
  hoping to use them as a distraction while 
  you make your escape.
  Without hesitation, you shove the other prisoner
  towards the creature, using them as a shield
  to buy yourself precious moments to 
  search for a escape route.
  As the creature pounces on its unsuspecting prey, 
  you manage spot a hidden passage and to scramble to safety.
  Haunted by the echoes of their screams as you
  flee into the darkness alone. 
  """
  insert_with_delay(text_output, text)

  clear_text(text_output)
  text = """
  You cautiously venture deeper into the 
  labyrinthine tunnels.
  The air grows colder, and the faint 
  echo of distant water reaches your ears,
  Hinting at the presence of an underground river.
  What will you do?
  """
  insert_with_delay(text_output, text)
  #buttons
  button_explore_blue = tk.Button(
      root,
      text="Explore the Tunnel System",
      command=lambda: explore_tunnels_blue(text_output))
  button_explore_blue.pack()

  button_search_blue = tk.Button(
      root,
      text="Search for Clues",
      command=lambda: search_for_clues_blue(text_output))
  button_search_blue.pack()

  button_rest_blue = tk.Button(root,
                               text="Rest and Recover",
                               command=lambda: rest_and_recover(text_output))
  button_rest_blue.pack()

  button_follow_river_blue = tk.Button(
      root,
      text="Follow the River",
      command=lambda: follow_river_blue(text_output))
  button_follow_river_blue.pack()


#yellow and blue merge 1
def explore_tunnels(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  You suggest exploring the tunnels further,
  hoping to find any signs of civilization
  or a way to the surface.
  As you and the other prisoner delve 
  deeper into the tunnels, you come across a narrow 
  passage that seems promising.
  However, as the man presses forward the
  ground trembles beneath you, 
  and with a deafening roar, 
  a cave-in seals off the tunnel
  ahead of you. You and the other prisoner
  are separated by tons of rubble, unable to reunite.
  You turn around and climb out of the 
  pit you had fallen into and continue 
  to search for a way out alone.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)

  text = """
  After turning around and walking for
  what seems like miles, 
  you find yourself standing at a crossroads 
  deep within the labyrinthine tunnels. 
  The flickering torchlight offers little solace 
  as you contemplate your next move, 
  knowing that every decision could mean the
  difference between escape and eternal confinement.
  """
  insert_with_delay(text_output, text)
  #buttons
  button_risk_dark_passage = tk.Button(
      root,
      text="Risk the Dark Passage",
      command=lambda: risk_dark_passage(text_output))
  button_risk_dark_passage.pack()

  button_navigate_flooded_corridor = tk.Button(
      root,
      text="Navigate the Flooded Corridor",
      command=lambda: navigate_flooded_corridor(text_output))
  button_navigate_flooded_corridor.pack()

  button_confront_ancient_obelisk = tk.Button(
      root,
      text="Confront the Ancient Obelisk",
      command=lambda: confront_ancient_obelisk(text_output))
  button_confront_ancient_obelisk.pack()


#first very good ending where you both escape ^^^^
def search_for_clues(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)

  text = """
  Recognizing the need for a plan, 
  you propose searching for any clues or markings 
  that might indicate the safest route out of the dungeon.
  With meticulous attention to detail,
  you and the other prisoner scour the tunnels
  for any signs of guidance.
  After hours of searching, 
  you discover a series of ancient runes 
  etched into the walls, pointing the way to a
  hidden passage. Following the markings, 
  you and the other prisoner find yourselves on 
  the outskirts of the dungeon, 
  free from its oppressive depths at last.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, a + "\n")  # Good Ending

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#Trapped ending ^^^^
def rest_and_recover(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Exhausted from the ordeal in the pit, 
  you suggest taking a moment to rest
  and recover your strength before 
  proceeding further into the tunnels.

  Finding a relatively safe alcove, 
  you and the other prisoner take 
  the opportunity to tend to your wounds.

  However, as you try to resume your journey, 
  you discover that the passage has 
  become blocked by a cave-in,  sealing you both
  within the labyrinthine depths of the dungeon.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, x + "\n")  # Ending

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#another death ending ^^^^
def follow_river(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Trusting your instincts, 
  you propose following the sound of the underground river, 
  believing it may lead to an exit or source of fresh water. 
  Braving the dark and winding tunnels,
  you and the other prisoner follow the sound of rushing water 
  deeper into the depths of the dungeon. 
  However, as you reach the river's edge, 
  you encounter a massive underground waterfall, 
  its sheer drop making escape impossible.
  Trapped between the churning waters and the impassable cliffs, 
  you realize with despair that your journey has come to a tragic end.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(tk.END, y + "\n")  # Death

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


# starts blue path ****
def leave_him(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
    Fearing further delay or complications, 
    you choose to leave the other prisoner 
    behind and make your escape alone. 
    Ignoring the other prisoner's pleas, 
    you hobble out of the dungeon, 
    leaving him behind to face his fate alone. 
    After escaping your restraints, 
    you navigate the labyrinthine corridors of the dungeon 
    until you come across a peculiar door with an arm-shaped hole.
    The weight of your previous sacrifice hangs heavy 
    in the air as you confront this new obstacle,
    and you find yourself alone, 
    facing the door.
    What do you do?
    """
  insert_with_delay(text_output, text)

  #buttons
  button_put_your_arm_solo = tk.Button(
      root,
      text="Put Your Other Arm In the Hole",
      command=lambda: put_your_arm_solo(text_output))
  button_put_your_arm_solo.pack()

  button_turn_around_solo = tk.Button(
      root,
      text="Turn Around and Find Another Way Out",
      command=lambda: turn_around_solo(text_output))
  button_turn_around_solo.pack()


#first endings on blue path  ^^^^^^^
def put_your_arm_solo(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Faced with the uncertainty of what 
  lies beyond the door, you steel yourself and 
  offer your remaining arm as a sacrifice,
  hoping it will lead to your freedom.
  """
  insert_with_delay(text_output, text)

  import random

  def event_choice():
    if random.random() < 0.5:
      # Escape
      text = """
       With a mixture of fear and determination,
       you insert your arm into the hole.
       The door creaks open, and you cautiously step through, 
       emerging into the blinding light of freedom.
       Though you've lost both hands, 
       you've gained your liberty, 
       a bittersweet victory as you contemplate 
       the sacrifices made along the way.
        """
      insert_with_delay(text_output, text)
      clear_text(text_output)
      insert_with_delay(text_output, a + "\n")

    else:
      # Death
      text = """
        "As you extend your arm into the hole, 
        a sharp pain shoots through your body.
        A hidden mechanism triggers, and spikes
        emerge from the walls, 
        impaling you. With your last breath, 
        you realize the cruel fate that awaited
        you, a grim reminder of the dangers lurking 
        in the depths of the dungeon.
        """
      insert_with_delay(text_output, text)
      clear_text(text_output)
      insert_with_delay(text_output, x + "\n")  # Death

  event_choice()
  destroy_all_buttons(root)

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#blue path cont. 1.   *****
def turn_around_solo(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  button_fight_creature_blue = tk.Button(
      root,
      text="Fight Creature",
      command=lambda: fight_creature_blue(text_output))
  text = """
    Uncertain of the risks posed by the door, 
    you decide to backtrack 
    and search for an alternative route to freedom.
    """
  insert_with_delay(text_output, text)

  text = """
  After triggering a trap door concealed within the floor, 
  you plummet into the darkness
  of the pit below. As you land with a thud, 
  the faint sound of slithering reaches your ears, 
  indicating the presence of a 
  dangerous creature lurking in the shadows.
  What will you do?
  """
  insert_with_delay(text_output, text)
  #buttons
  button_fight_creature_blue = tk.Button(
      root,
      text="Fight Creature",
      command=lambda: fight_creature_blue(text_output))
  button_fight_creature_blue.pack()

  button_run = tk.Button(root,
                         text="Run Away",
                         command=lambda: run_away(text_output))
  button_run.pack()


#blue choices merge with a yellow choice 2.1 ****
def fight_creature_blue(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  With makeshift weapons in hand, you stand your ground 
  against the creature's relentless assault.
  Through sheer determination you manage to fend off
  the creature long enough to find a 
  hidden passage leading to safety. You climb out of the pit, 
  bruised and battered but alive 
  and continue down the passage.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)

  text = """
  You cautiously venture deeper into the
  labyrinthine tunnels. The air grows colder, 
  and the faint echo of distant water reaches your ears,
  Hinting at the presence of an underground river.
  What will you do?
  """
  insert_with_delay(text_output, text)
  #buttons
  button_explore_blue = tk.Button(
      root,
      text="Explore the Tunnel System",
      command=lambda: explore_tunnels_blue(text_output))
  button_explore_blue.pack()

  button_search_blue = tk.Button(
      root,
      text="Search for Clues",
      command=lambda: search_for_clues_blue(text_output))
  button_search_blue.pack()

  button_rest_blue = tk.Button(root,
                               text="Rest and Recover",
                               command=lambda: rest_and_recover(text_output))
  button_rest_blue.pack()

  button_follow_river_blue = tk.Button(
      root,
      text="Follow the River",
      command=lambda: follow_river_blue(text_output))
  button_follow_river_blue.pack()


#merge blue and yellow 1.2    ***
def explore_tunnels_blue(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  You explore the tunnels further, hoping to find 
  any signs of civilization
  or a way to the surface.
  As you delve deeper into the tunnels, 
  you come across a narrow passage that seems promising.
  However, as you press forward the ground trembles beneath you, 
  and with a deafening roar, 
  a cave-in seals off the tunnel ahead of you.
  You turn around and climb out of the pit you
  had fallen into and continue 
  to search for a way out alone.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)

  text = """
  After turning around and walking for what 
  seems like miles, you find yourself standing 
  at a crossroads deep within the labyrinthine tunnels. 
  The flickering torchlight offers little
  solace as you contemplate your next move,
  knowing that every decision could 
  mean the difference between escape and eternal confinement.
  """
  insert_with_delay(text_output, text)
  #buttons
  button_risk_dark_passage = tk.Button(
      root,
      text="Risk the Dark Passage",
      command=lambda: risk_dark_passage(text_output))
  button_risk_dark_passage.pack()

  button_navigate_flooded_corridor = tk.Button(
      root,
      text="Navigate the Flooded Corridor",
      command=lambda: navigate_flooded_corridor(text_output))
  button_navigate_flooded_corridor.pack()

  button_confront_ancient_obelisk = tk.Button(
      root,
      text="Confront the Ancient Obelisk",
      command=lambda: confront_ancient_obelisk(text_output))
  button_confront_ancient_obelisk.pack()


#escape ending ^^^^
def search_for_clues_blue(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)

  text = """
  Recognizing the need for a plan, you search 
  for any clues or markings that might indicate the
  safest route out of the dungeon.
  With meticulous attention to detail, 
  you scour the tunnels for any signs of guidance.
  After hours of searching, 
  you discover a series of 
  ancient runes etched into the walls,
  pointing the way to a hidden passage.
  Following the markings, you find yourself on 
  the outskirts of the dungeon, 
  free from its oppressive depths at last.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, a + "\n")  # Good Ending

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#trapped forever ending ^^^^^
def rest_and_recover(text_output):  #trapped forever
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Exhausted from the ordeal in the pit,
  you take a moment to rest
  and recover your strength before 
  proceeding further into the tunnels.

  Finding a relatively safe alcove, you take 
  the opportunity to tend to your wounds.

  However, as you try to resume your journey, 
  you discover that the passage has become blocked by a cave-in, 
  sealing you within the labyrinthine depths of the dungeon.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, x + "\n")  # Ending

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#death ending ^^^^
def follow_river_blue(text_output):  #death
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Trusting your instincts, 
  you follow the sound of the underground river, 
  believing it may lead to an exit or source of fresh water. 
  Braving the dark and winding tunnels,
  you follow the sound of rushing water 
  deeper into the depths of the dungeon. 
  However, as you reach the river's edge, 
  you encounter a massive underground waterfall, 
  its sheer drop making escape impossible.
  Trapped between the churning waters and 
  the impassable cliffs, you realize with despair
  that your journey has come to a tragic end.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, y + "\n")  # Death

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#death ending
def risk_dark_passage(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  Ahead of you lies a narrow, dimly lit passage, 
  its depths shrouded in darkness. Despite the uncertainty, 
  you consider pressing forward, hoping that it may lead to an 
  alternate route out of the dungeon.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  text = """
  As you venture deeper into the darkness, the passage narrows, 
  and the air grows thick with the scent of decay. 
  Suddenly, you stumble upon a nest of vicious creatures 
  lurking in the shadows. With no means of escape, 
  you fight valiantly but ultimately succumb to the relentless
  onslaught, your life extinguished in the depths of the dungeon
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, y + "\n")

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#continuing on blue and yellow path      ****
def navigate_flooded_corridor(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  To your left, a corridor lies partially 
  submerged in icy water, its depths murky
  and foreboding. Despite the chilling waters, 
  you consider wading through in the hopes 
  of finding an undiscovered path to freedom.

  With each step, the icy water rises higher, sending shivers 
  down your spine as you navigate the flooded corridor. 
  Just as you begin to lose hope, you stumble upon a hidden passage 
  submerged beneath the surface. Taking a deep breath, 
  you plunge into the icy depths, emerging on the other side 
  into a previously unexplored chamber. With cautious 
  optimism, you continue your journey, determined to overcome 
  whatever challenges lie ahead. 
"""
  insert_with_delay(text_output, text)
  clear_text(text_output)
  text = """
  After navigating the flooded corridor,
  you find yourself standing in a previously unexplored chamber, 
  the echoes of your footsteps reverberating off the damp stone walls. 
  The torchlight casts long shadows, illuminating the 
  unknown depths that lie ahead. With determination in 
  your heart, you press onward, knowing that every decision
  could be crucial to your survival.
"""
  insert_with_delay(text_output, text)
  #buttons
  button_descend_abyss = tk.Button(
      root,
      text="Descend into the Abyss",
      command=lambda: descend_into_abyss(text_output))
  button_descend_abyss.pack()

  button_investigate_altar = tk.Button(
      root,
      text="Investigate the Mysterious Altar",
      command=lambda: investigate_mysterious_altar(text_output))
  button_investigate_altar.pack()


# death ending      ^^^^
def confront_ancient_obelisk(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
   To your right stands an ancient obelisk, 
   its surface adorned with cryptic symbols and intricate carvings.
   Despite the ominous aura surrounding it, 
   you consider investigating further, 
   believing that it may hold the key to your escape.
"""
  insert_with_delay(text_output, text)
  clear_text(text_output)
  text = """
   As you approach the obelisk, an otherworldly energy washes over you,
   filling you with an inexplicable sense of dread.
   With trembling hands, you decipher the symbols,
   unlocking a hidden chamber within the obelisk. 
   Inside, you uncover a forbidden artifact, its power
   pulsating with dark energy. Tempted by the promise of freedom, 
   you reach out to grasp the artifact, triggering a 
   catastrophic chain of events that seals your fate. 
   Your life fades away, consumed by the ancient power within 
   the depths of the dungeon.
   """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, y + "\n")

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


#final trapped forver ending ^^^^
def descend_into_abyss(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
 As you explore the chamber, 
 you notice a narrow opening in the floor, 
 leading to a dark abyss below. 
 Despite the ominous nature of 
 the descent, you consider descending into the abyss, 
 believing it may lead to an alternate
 route out of the dungeon.
With a deep breath, you steel yourself
for the descent and begin  to climb down 
into the darkness. The air grows colder 
with each step, and the echoes of your 
footsteps fade into the abyss below. 
Suddenly, you find yourself engulfed by darkness, 
the inky blackness swallowing you whole. 
With no way to climb back up, you realize with 
horror that you are trapped in the depths of the dungeon 
forever, lost to the darkness that surrounds you.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, x + "\n")
  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


  #final escape ending
def investigate_mysterious_altar(text_output):
  clear_text(text_output)
  destroy_all_buttons(root)
  text = """
  At the far end of the chamber, you spot a mysterious altar 
  adorned with ancient symbols and strange artifacts. Despite the 
  unsettling aura surrounding it, you consider investigating further, 
  believing that it may hold the key to your escape. As you 
  approach the altar, a sense of foreboding washes over you,
  but curiosity compels you to press on. With trembling hands,
  you examine the artifacts, deciphering the cryptic symbols etched 
  into their surface. Suddenly, you uncover a hidden compartment
  within the altar, revealing a small key adorned with intricate 
  engravings. With cautious optimism, you take the key and 
  continue your journey, unlocking a hidden passage that leads 
  you to freedom, emerging into the moonlit night, free from 
  the confines of the dungeon at last.
  """
  insert_with_delay(text_output, text)
  clear_text(text_output)
  insert_with_delay(text_output, d + "\n")

  restart_button = tk.Button(root, text="Restart Game", command=restart_game)
  restart_button.pack()


if __name__ == "__main__":
  main()
