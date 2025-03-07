import random  # For random outcomes

print("🏚️ You wake up in front of an old, abandoned mansion.")
print("⛈️ A storm rages behind you, and the door suddenly creaks open by itself...")

answer = input("Do you ENTER the house or RUN away? (enter/run) ").lower().strip()

if answer == "enter":
    print("\n🚪 You step inside. The door SLAMS shut behind you.")
    print("🕯️ Flickering candles light up a dusty hallway, with doors on both sides.")

    answer = input("Do you go LEFT or RIGHT? (left/right) ").lower().strip()

    if answer == "left":
        print("\n🖼️ You enter a dimly lit room full of old portraits.")
        print("👁️ The eyes in the paintings seem to FOLLOW you.")

        answer = input("Do you INSPECT a painting or KEEP WALKING? (inspect/walk) ").lower().strip()

        if answer == "inspect":
            if random.choice([True, False]):  # Random survival chance
                print("\n👀 The painting suddenly BLINKS. You hear whispers...")
                print("🚪 A hidden door opens behind the painting. You find an exit! YOU SURVIVED! 🎉")
            else:
                print("\n🩸 The painting's mouth OPENS and SCREAMS. The room goes dark... GAME OVER! 😱")

        else:
            print(
                "\n🚶‍♂️ You keep walking, but the floor COLLAPSES under you. You fall into a PIT OF SHADOWS. GAME OVER! 😵")

    elif answer == "right":
        print("\n🎵 A soft music box plays in the distance...")
        print("🛏️ A dusty old bed sits in the center of the room, covered in a white sheet.")

        answer = input("Do you LIFT the sheet or LEAVE the room? (lift/leave) ").lower().strip()

        if answer == "lift":
            if random.choice([True, False]):  # Random survival chance
                print("\n😨 Under the sheet is... NOTHING. But you hear breathing behind you...")
                print("🏃‍♂️ You RUN and find an open window! YOU ESCAPED! 🎉")
            else:
                print("\n👻 A corpse sits upright under the sheet. It GRABS YOUR ARM. GAME OVER! 😵")

        else:
            print("\n🚪 As you turn to leave, the door disappears. The walls close in. GAME OVER! 😱")

    else:
        print("\n😨 You hesitate... The shadows MOVE closer... GAME OVER!")

elif answer == "run":
    print("\n🌲 You sprint into the forest, but the trees seem to shift around you.")
    print("🌫️ A heavy fog rolls in, and you hear footsteps behind you...")

    answer = input("Do you HIDE or KEEP RUNNING? (hide/run) ").lower().strip()

    if answer == "hide":
        if random.choice([True, False]):  # Random survival chance
            print("\n🍂 You hide behind a tree. The footsteps stop. The fog lifts. You are SAFE. 🎉")
        else:
            print("\n👤 Something WHISPERS your name. Cold hands GRAB your shoulders... GAME OVER! 😨")

    else:
        print("\n🏃‍♂️ You keep running, but suddenly TRIP. A shadow looms over you... GAME OVER! 😱")

else:
    print("\n⏳ You freeze in fear... The shadows surround you... GAME OVER! 😈")
