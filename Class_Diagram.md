# Class Diagram

## Description for Class Diagram
The class diagram highlights the main classes that will be used in Dead Zone: Polymorphism and how they are connected. It includes the attributes and methods of each class and shows relationships such as inheritance between the different characters, zombies and items. The diagram helps plan how the game will be structured using OOP concepts and will be used as a guide when developing the Python code.

                         ┌────────────────────────┐
                         │       Character        │
                         ├────────────────────────┤
                         │ - name: string         │
                         │ - health: int          │
                         │ - damage: int          │
                         ├────────────────────────┤
                         │ + attack()             │
                         │ + takeDamage()         │
                         │ + isAlive()            │
                         └───────────┬────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
                    ▼                                 ▼
        ┌─────────────────────┐          ┌─────────────────────┐
        │       Player        │          │       Zombie        │
        ├─────────────────────┤          ├─────────────────────┤
        │ - inventory: list   │          │ - zombieType: str   │
        │ - location: string  │          │ - damage: int       │
        │ - weapon: Weapon    │          ├─────────────────────┤
        ├─────────────────────┤          │ + attack()          │
        │ + move()            │          │ + takeDamage()      │
        │ + search()          │          └──────────┬──────────┘
        │ + useItem()         │                     │
        │ + attack()          │              ┌──────┼──────┐
        └─────────────────────┘              │      │      │
                                             ▼      ▼      ▼
                                      ┌──────────┐ ┌──────────┐
                                      │  Normal  │ │   Fast   │
                                      │  Zombie  │ │  Zombie  │
                                      └──────────┘ └──────────┘
                                                   
                                             ┌──────────┐
                                             │   Tank   │
                                             │  Zombie  │
                                             └──────────┘
        ┌─────────────────────┐
        │        Item         │
        ├─────────────────────┤
        │ - name: string      │
        │ - description: str  │
        ├─────────────────────┤
        │ + use()             │
        └──────────┬──────────┘
                   │
             ┌─────┴─────┐
             ▼           ▼
      ┌────────────┐ ┌─────────────┐
      │   Weapon   │ │  Consumable │
      ├────────────┤ ├─────────────┤
      │ - damage   │ │ - healing   │
      ├────────────┤ ├─────────────┤
      │ + use()    │ │ + use()     │
      └────────────┘ └─────────────┘
                
                    │
                    
        ┌─────────────────────────┐
        │        Location         │
        ├─────────────────────────┤
        │ - name: string          │
        │ - description: string   │
        │ - items: list           │
        │ - zombies: list         │
        ├─────────────────────────┤
        │ + enter()               │
        │ + search()              │
        │ + addItem()             │
        └─────────────────────────┘
              
                    │
                    
        ┌─────────────────────────┐
        │          Game           │
        ├─────────────────────────┤
        │ - player: Player        │
        │ - locations: list       │
        │ - gameOver: boolean     │
        ├─────────────────────────┤
        │ + start()               │
        │ + gameLoop()            │
        │ + checkWin()            │
        │ + gameOver()            │
        └─────────────────────────

Class Diagram created using the help of Textik and Miro to be made in Github format.
