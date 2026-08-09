# Dead Zone: Polymorphism — Project Journal

## Project Overview

Game Title: Dead Zone: Polymorphism
Programming Language: Python
Genre: Text-Based RPG / Adventure
Programming Paradigm: Object-Oriented Programming (OOP)

### Game Concept

Dead Zone: Polymorphism is a text-based RPG set during a zombie apocalypse. The player takes the role of a survivor trapped in an infected city. The main objective is to explore different locations, collect useful items, survive encounters with different types of zombies and eventually reach the evacuation zone.

The game will demonstrate important Object-Oriented Programming concepts including classes, objects, encapsulation, abstraction, inheritance and polymorphism.

⸻

## Journal Entry 1 — Project Beginning

Date: 14 May 2026

What I did

I began planning my Year 11 Software Engineering RPG project. After considering different possible themes, I decided to create a zombie apocalypse survival game.

I chose the name Dead Zone: Polymorphism because the game will use different types of zombies that can share common methods but behave differently. This will allow me to demonstrate polymorphism in my program.

I also identified some of the main features I want to include, such as exploring locations, collecting items, fighting zombies and reaching an evacuation zone.

Ideas Developed

The game will potentially include:

* A player character
* Different types of zombies
* Multiple locations
* Weapons
* Medical items
* An inventory
* Combat
* Health
* A final evacuation zone
* Win and lose conditions

OOP Concepts

I started identifying possible classes for the game:

* Character
* Player
* Zombie
* FastZombie
* TankZombie
* Item
* Weapon
* Location
* Game

I plan to use inheritance so that different zombie types can inherit common characteristics from the Zombie class. I also plan to use polymorphism so that different zombie types can have different behaviours while using the same methods.

Problems / Pitfalls

At this stage, I was unsure about how many features I should include. Adding too many features could make the project difficult to complete and test, while adding too few could make the game too simple.

I also needed to make sure that the game would demonstrate OOP concepts rather than simply being a normal Python program.

How I addressed this

I decided to focus on a smaller number of well-developed features rather than trying to make the game unnecessarily large. I will prioritise the OOP requirements and make sure each major concept has a clear purpose in the game.

Next Steps

* Complete the workbook activities
* Research Object-Oriented Programming
* Research Gregory Yob and Hunt the Wumpus
* Finalise the game’s requirements
* Begin designing the classes and game structure

⸻

## Journal Entry 2 — OOP Research

Date: 20 May 2026

What I did

I researched Object-Oriented Programming and how it can be used to develop computer games. I focused on how classes and objects can represent characters, items and locations within a game.

I also looked at the differences between procedural programming and object-oriented programming.

What I learned

I learned that OOP allows related data and behaviours to be organised together. This can make a game easier to develop, modify and maintain.

For example, instead of having separate variables and functions for every zombie, I can create a Zombie class and create multiple zombie objects from it.

Problems / Pitfalls

One difficulty was understanding the difference between a class and an object.

How I addressed this

I used the game as an example. The Zombie class is the blueprint, while individual zombies created from that class are objects.

Next Steps

* Continue completing the workbook
* Research Hunt the Wumpus
* Begin the game’s program specifications

⸻

## Journal Entry 3 — Hunt the Wumpus Research

Date: 29 May 2026

What I did

I researched Gregory Yob’s development of the original Hunt the Wumpus game. I looked at how the game was designed and how its gameplay involved exploring a connected environment, making decisions and dealing with hazards.

What I learned

The research helped me understand how a relatively simple text-based game can create an engaging experience through player choices, exploration and uncertainty.

I identified ideas from Hunt the Wumpus that could influence my game without directly copying it.

Ideas I could use

* Multiple connected locations
* Hidden dangers
* Player choices
* Items and resources
* Different possible outcomes
* Exploration

Problems / Pitfalls

I needed to make sure my game was an original adaptation rather than simply copying Hunt the Wumpus.

How I addressed this

I decided to change the setting, characters, gameplay and objectives. My game will focus on surviving a zombie apocalypse, collecting supplies and reaching an evacuation zone.

Next Steps

* Complete the game design
* Create the data dictionary
* Design the class diagram
* Create the structure chart

⸻

## Journal Entry 4 — Game Design

Date: 3 June 2026

What I did

I began designing the gameplay for Dead Zone: Polymorphism. I identified possible locations, characters and items that could be included in the game.

Locations

* Abandoned House
* Supermarket
* Hospital
* Police Station
* Evacuation Zone

Characters

* Player
* Normal Zombie
* Fast Zombie
* Tank Zombie
* Survivor/NPC

Items

* Medkit
* Food
* Weapon
* Evacuation Keycard

Problems / Pitfalls

I realised that every feature added to the game would increase the amount of code that needs to be tested. I therefore needed to avoid adding unnecessary features.

How I addressed this

I prioritised the features that contribute directly to the main objective and demonstrate OOP concepts.

Next Steps

* Complete the data dictionary
* Design the class diagram
* Create the structure chart
* Begin pseudocode

⸻

## Journal Entry 5 — Class Design

Date: 8 June 2026

What I did

I designed the initial class structure for the game.

The main inheritance structure is planned to be:

Character → Zombie → FastZombie / TankZombie

The player will also inherit from the Character class.

OOP Concepts

Inheritance: FastZombie and TankZombie will inherit common characteristics from Zombie.

Polymorphism: Different zombie classes will be able to use methods such as attack() but produce different behaviours.

Encapsulation: Important player information such as health and inventory will be managed through class methods.

Abstraction: The player will interact with the game through simple commands without needing to understand the code running behind them.

Problems / Pitfalls

I needed to make sure inheritance was being used for a genuine reason rather than simply including it because it was required for the assessment.

How I addressed this

I decided that all zombies should share basic characteristics such as health and attacks, while specialised zombies can modify their behaviour.

Next Steps

* Complete the class diagram
* Begin implementing the classes in Python
* Test each class individually

⸻

## Journal Entry 6 — Initial Programming

Date: 16 June 2026

What I did

I began implementing the classes in Python. I started with the base classes before creating the specialised zombie classes.

Problems / Pitfalls

During development, I encountered errors involving class inheritance, variables and methods.

How I addressed this

I tested individual sections of the program instead of trying to build everything at once. I used error messages and debugging to identify where problems were occurring.

Next Steps

* Complete the player class
* Complete the zombie classes
* Add items and locations
* Connect the classes through the main game loop

⸻

## Journal Entry 7 — Testing

Date: 20 June 2026

What I did

I began testing the game using different inputs and situations.

I tested:

* Valid commands
* Invalid commands
* Player movement
* Item collection
* Combat
* Inventory
* Health
* Zombie behaviour
* Win conditions
* Lose conditions

Problems / Pitfalls

Some unexpected inputs caused the program to behave incorrectly. This showed that testing normal gameplay alone was not enough.

How I addressed this

I added validation for user inputs and tested both expected and unexpected inputs.

Next Steps

* Complete unit testing
* Complete subsystem testing
* Complete system testing
* Document test results

⸻

## Journal Entry 8 — Final Evaluation

Date: 8 August 2026

What I did

I evaluated the completed game against the original success criteria.

What worked well

The final game successfully demonstrates OOP concepts and allows the player to explore locations, interact with objects and encounter different zombies.

Problems that remained

Some features could be improved, particularly the variety of gameplay and the number of possible player choices.

Improvements

If I developed a sequel, I could add:

* More locations
* More zombie types
* Random events
* A larger inventory system
* More endings
* A save/load system
* More NPC interactions
* Difficulty levels

Overall Evaluation

Dead Zone: Polymorphism successfully demonstrates how Object-Oriented Programming can be applied to the development of a text-based RPG. The project also helped me understand the importance of planning, testing, debugging and documenting software throughout the development process.

* NOTE - I was away overseas between 24 June to 28th July, hence the gap in Journal dates between entries 7 and 8.
