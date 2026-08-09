# Evaluation — Dead Zone: Polymorphism

## Overview:

Dead Zone: Polymorphism was developed as a text-based RPG adventure game using Python and Object-Oriented Programming. The aim of the game is for the player to survive a zombie apocalypse, explore different locations, collect useful items, defeat or avoid zombies and reach the evacuation zone.

---

## Success Criteria:

| Success Criterion | Result | Evaluation |
|---|---|---|
| The game runs without crashing | Approved | The final version will be tested from start to finish. |
| The player can move between locations | Approved | Movement will be tested using valid and invalid inputs. |
| The player can collect items | Approved | Different locations will be searched to test item collection. |
| The player has an inventory | Approved | Items will be added, viewed and used through the inventory. |
| The player can use weapons | Approved| Weapons will be tested during combat. |
| The player can use healing items | Approved | Medkits and other consumables will be tested. |
| The game includes different zombie types | Approved | Normal, Fast and Tank Zombies will be tested. |
| The game demonstrates inheritance | Approved | The class structure will be checked to confirm inheritance is implemented. |
| The game demonstrates polymorphism | Approved | Different zombie types will be tested to confirm their behaviours differ. |
| The game has a win condition | Approved | The player will attempt to reach the evacuation zone. |
| The game has a lose condition | Approved | The game will be tested when the player's health reaches zero. |
| Invalid inputs are handled correctly | Approved | Invalid commands will be entered to check that the program does not crash. |

---

## OOP Evaluation:
The game will demonstrate several Object-Oriented Programming concepts.

### Classes and Objects:
The game uses classes to represent important parts of the game, such as the Player, Zombie, Item and Location. Objects can then be created from these classes during gameplay.

### Inheritance:
Inheritance is used so that related classes can share common attributes and methods. For example, different zombie types inherit from the Zombie class.

### Polymorphism:
Polymorphism is one of the main concepts demonstrated in the game. Different zombie classes can use the same method, such as `attack()`, while producing different behaviours.

### Encapsulation:
Encapsulation is used to keep related data and behaviours together inside classes. For example, the Player class manages information such as health, inventory and equipment.

### Abstraction:
Abstraction allows the player to interact with the game using simple commands without needing to understand the code behind each action.

---

## Improvements:

If the game were developed further, possible improvements could include:

- More locations
- More zombie types
- More weapons
- More items
- More complex combat
- Random events
- More possible endings
- A larger story
- Difficulty levels
- Save and load functionality

## Sequel Proposal - Dead Zone: Aftermath
A possible sequel to *Dead Zone: Polymorphism* could be called **Dead Zone: Aftermath**. The story could continue after the player escaped from the evacuation zone, revealing that the zombie outbreak has spread beyond the original city.

The sequel could introduce new locations, stronger zombie types, a larger map and possibly multiple endings.

> **“Escaping the city was only the beginning...”**

---

## Overall Evaluation:
The final game will be evaluated against the original success criteria to determine how successfully the project achieved its intended purpose.

