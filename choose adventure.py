EXTENSIONN
user_choice = None

story = """You are Ozan, a seventeen-year-old living in Toronto, Canada.

One night, your best friend Agam calls you in a panic.

"Ozan, come to the garage. Now. You have to see this."

You rush over and find a massive robot standing in the garage, its metal body still steaming from a hard landing.

"My name is Dart," the robot says. "I am a Guardian. My enemies are the Wreckers and they followed me to Earth, and I need help finding them before they find a way to open a portal home."

Dart explains that the Wreckers were last seen heading toward Italy.

He needs you and Agam to help him track them down.

A : Agree to travel with Dart to Italy right away.
OR
B : Ask Dart to explain more about the Wreckers before leaving.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """You and Agam grab your bags and climb into Dart, who transforms into a truck for the trip.

Within hours, you land in Rome, Italy.

The streets are very quiet, but Dart's sensors pick up energy waves near an old stone tower.

A : Head straight to the tower to investigate.
OR
B : Look for information from local people first.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """You and Agam walk toward the tower with Dart close behind.

Suddenly, a Wrecker scout leaps out, transforming from a black car into a sharp, fast robot.

A : Have Dart fight the scout while you and Agam stay back.
OR
B : Try to distract the scout so Dart can strike first.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            print("""Dart fights the scout quickly, landing a strong hit that sends it running.

The scout flees toward France, and Dart says the main Wreckers must be there too.

You, Agam, and Dart leave for Paris right away, following the trail to finish the mission.

In Paris, you track the Wreckers to the Eiffel Tower, where the final battle takes place.

With your help, Dart defeats the last Wrecker at the top of the tower, and the portal closes for good.

Ozan and Agam return home as heroes, with a story no one will ever believe.

THE END
""")
        else:
            print("""You and Agam throw rocks to distract the scout, giving Dart the chance to strike first.

The plan works, and Dart quickly disables the scout before it can call for backup.

Following its last signal, you all travel to Paris, where the wreckers start to gather at the eiffel tower.

You and Agam help Dart sneak past the guards, leading to a tense fight that happens at the center of the eiffel tower.

Dart wins, the portal is destroyed, and Ozan and Agam fly home with an unforgettable story.

THE END
""")

    else:
        story = """You ask around and learn from a shop owner that strange metal creatures were seen near the train station.

Dart says this matches the Wreckers' pattern of using train lines to travel quickly.

A : Follow the train tracks toward France immediately.
OR
B : Rest for the night and start fresh in the morning.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            print("""You, Agam, and Dart follow the tracks all night, finally catching up just outside Paris.

The Wreckers are already climbing the Eiffel Tower, trying to activate their portal device at the top.

Dart races up the tower, with you and Agam right behind, cheering him on.

After a hard fight, Dart smashes the device, and the Wreckers are defeated for good.

Ozan and Agam watch the sunrise over Paris, tired but proud of what they did.

THE END
""")
        else:
            print("""You all rest for the night, and Dart repairs some of his damage while you sleep.

In the morning, you follow the tracks and arrive in Paris just as the Wreckers reach the Eiffel Tower.

The fight is tougher this time, since the Wreckers had more time to prepare.

Still, Dart, Ozan, and Agam work together and manage to stop the portal just in time.

The three of them leave Paris exhausted but successful, already best friends with a robot for life.

THE END
""")

else:
    story = """Dart explains that the Wreckers are a group of robots who destroy planets for resources.

"If they succeed here," Dart says, "they will open a portal and bring many more of them to Earth."

With a clearer picture of the danger, you, Agam, and Dart head straight for Italy.

You land near Venice, where the canals make it hard to track the Wreckers since the sensors Dart uses arent as efficent.

A : Use a small boat to search the canals for signs of the Wreckers.
OR
B : Climb to a high rooftop to scan the city from above.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """You and Agam borrow a small boat and search the canals while Dart stays hidden nearby.

After an hour, you spot strange ripples near an old bridge, a sign of movement thats happening underwater.

A : Investigate the ripples directly.
OR
B : Call Dart over before getting any closer.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            print("""You lean closer to the water, and a Wrecker suddenly bursts out, soaking you both instantly.

Dart arrives just in time to fight it off before it can escape.

Following the Wrecker's retreat path, you all travel to Paris and track the rest of the group to the Eiffel Tower.

There, Dart leads the final fight, annd with your help you fight off the smaller wreckers, and end up winning the entire battle. 

Ozan and Agam head home with soaked shoes and an amazing story to tell.

THE END
""")
        else:
            print("""You wisely call Dart over first, and he arrives just as the Wrecker surfaces.

Dart handles the fight easily this time, catching the Wrecker off guard.

The trail leads to Paris, where the last Wreckers are gathering at the Eiffel Tower.

With careful planning, you help Dart take them down one by one until the tower is finally safe again.

Ozan and Agam return to Canada, proud of staying smart under pressure.

THE END
""")

    else:
        story = """You and Agam climb to a rooftop while Dart scans the city below.

From up high, you spot several Wreckers gathering near the train station, clearly preparing to leave.

A : Rush down to stop them before they leave the city.
OR
B : Let them go and follow them quietly instead.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            print("""You rush down just as the Wreckers board a train, forcing a fight right on the platform.

Dart fights hard, but a few Wreckers sadly escape and end up going towards the Eiffel tower.

You, Agam, and Dart chase them all the way to the Eiffel Tower, where the final battle takes place.

After a long fight, Dart finally crushes the portal device, and succeeds at preventing the Wreckers from expanding.

Ozan and Agam finally rest, knowing they helped save the world.

THE END
""")
        else:
            print("""You decide it is smarter to follow quietly instead of causing a scene.

The Wreckers lead you straight to Paris, giving Dart time to plan the perfect ambush.

At the Eiffel Tower, Dart strikes first, which surprises the Wreckers because they didnt expect Dart.

The fight ends quickly, and the portal device is destroyed before it can even activate.

Ozan and Agam watch the Eiffel Tower lights turn back on, safe and unharmed.

THE END
""")



