# Testing Strategies — Dead Zone: Polymorphism:

Testing will be used throughout the development of Dead Zone: Polymorphism to identify errors, verify that the game works as expected, and ensure that the final product meets the success criteria. Different types of testing will be used to test individual parts of the program as well as the complete game.

## Unit Testing:

Unit testing will be used to test individual classes and methods separately. This will help identify problems in specific parts of the program before they affect the rest of the game.

Examples of unit tests include:

- Testing the Player class
- Testing the Zombie class
- Testing player health
- Testing inventory methods
- Testing movement methods

### Example Unit Tests:

| Test | Input | Expected Result |
|---|---|---|
| Create player | Player name = "Alex" | Player is created with 100 health |
| Player attack | Attack zombie | Zombie health decreases |
| Player takes damage | Damage = 20 | Player health decreases by 20 |
| Use medkit | Use Medkit | Player health increases |
| Add item | Add Pistol | Pistol is added to inventory |
| Check health | Health = 0 | Player is no longer alive |

---

## Subsystem Testing:

Subsystem testing will test groups of related functions working together.

Examples include:

- Player + Inventory + Items
- Player + Zombie + Combat
- Player + Location + Movement
- Weapon + Combat + Zombie health

For example, when the player finds a weapon, the weapon should be added to the inventory, the player should be able to equip it and the weapon should affect the amount of damage dealt during combat.

---

## System Testing:

System testing will test the complete game as one system. This will make sure that all of the different parts of the game work together correctly.

The complete game will be tested from the beginning to the end, including:

1. Starting the game
2. Entering the player's name
3. Exploring locations
4. Searching for items
5. Collecting items
6. Fighting zombies
7. Using weapons and healing items
8. Finding the evacuation keycard
9. Entering the evacuation zone
10. Winning the game

---

## Black-Box Testing:

Black-box testing will focus on the inputs and outputs of the game without looking at how the internal code works.

For instance, a tester could enter an invalid menu option and check whether the game gives an appropriate error message rather than crashing.

| Test | Input | Expected Result |
|---|---|---|
| Valid menu option | `1` | Selected action is performed |
| Invalid menu option | `99` | Error message is displayed |
| Invalid text | `hello` | Program handles the input without crashing |
| Valid item | `Medkit` | Medkit is used |
| Invalid item | `Banana` | Invalid item message is displayed |

---

## White-Box Testing:

White-box testing will involve examining the internal code and logic of the program.

This will be used to check:

- If statements
- Loops
- Methods
- Class relationships
- Inheritance
- Polymorphism
- Combat calculations
- Win and lose conditions

For example, the different `attack()` methods in the zombie classes can be checked to make sure that each zombie type behaves differently.

---

## Grey-Box Testing:

Grey-box testing will combine knowledge of the game's internal structure with testing the game through normal user inputs.

For example, knowing that the evacuation zone requires a keycard allows the tester to specifically test what happens when:

1. The player does not have the keycard.
2. The player tries to enter the evacuation zone.
3. The player receives the keycard.
4. The player tries again.

The expected result is that the evacuation zone remains locked without the keycard and becomes accessible after the keycard is collected.

---

## Test Data

The game will use normal, invalid, boundary and extreme test data to make sure different types of inputs are handled correctly.

| Test Data Type | Example Input | Expected Result |
|---|---|---|
| Normal | `Alex` | Player is created |
| Normal | `1` | First menu option selected |
| Invalid | `abc` | Error message displayed |
| Invalid | `99` | Error message displayed |
| Boundary | Health = `0` | Player loses |
| Boundary | Health = `100` | Maximum health is maintained |
| Boundary | Damage = `0` | No health is lost |
| Empty | Empty player name | Program requests a valid name |
| Valid | `attack` | Player attacks zombie |
| Valid | `search` | Location is searched |
| Valid | `inventory` | Inventory is displayed |

---
