import random

print("🌆 Welcome to Desi Dungeon: The Chai Quest 🌆")
name = input("Enter your name, brave explorer: ")

print("\nNamaste, " + name + "! You are in a dark underground station.")
print("Find the legendary Cutting Chai and escape... or be lost forever.\n")

health = 100
inventory = []
enemies = ["Bhoot Baba", "Annoying TC", "Wi-Fi Ghost", "Lost Passenger"]
items = ["Chai Token", "Power Bank", "Maggi", "Aadhaar Card"]

while health > 0:
    print("\n📍 What do you want to do?")
    print("1. Explore area")
    print("2. Check inventory")
    print("3. Exit game")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        if random.randint(0, 1) == 0:
            enemy = random.choice(enemies)
            print("\n⚠️ You encountered " + enemy + "!")
            action = input("Do you want to [fight] or [run]? ").strip().lower()
            
            if action == "fight":
                if random.randint(0, 1) == 1:
                    print("You defeated " + enemy + " using your desi logic! 🧠")
                else:
                    damage = random.randint(10, 30)
                    health -= damage
                    print(enemy + " hit you! You lost", damage, "health. ❤️ =", health)
            else:
                print("You ran away safely... but they might return 👻")
        
        else:
            item = random.choice(items)
            print("\n🔍 You found a " + item + "!")
            inventory.append(item)

            if "Chai Token" in inventory:
                print("\n🎉 You found the Chai Token! The chaiwala appears out of nowhere!")
                print("☕ You sip the Cutting Chai. You've won. Life is complete.\n")
                break

    elif choice == "2":
        print("\n🧳 Inventory:", inventory)
        print("❤️ Health:", health)

    elif choice == "3":
        print("\n👋 Thanks for playing! Jai Hind!")
        break

    else:
        print("Invalid choice. Try again.")

if health <= 0:
    print("\n💀 You fainted in the desi dungeon. Game over.")