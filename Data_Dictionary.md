# Data Dictionary:

## Description for Data Dictionary:
The data dictionary provides an overview of the main data and variables that will be used in Dead Zone: Polymorphism. It explains what each variable is used for, the type of data it stores, an example of the information it could contain, and any validation rules that need to be followed. This will make it easier to understand how information such as the player’s health, inventory, location, and more.

| Variable | Data Type | Format for Display | Size for Display | Description | Example | Validation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `playerName` | String | XXXXXXXXXX | 1–20 | Name chosen by the player | `Matej` | Must be 1–20 characters |
| `health` | Integer | NNN | 1–3 | Current health of the player | `75` | Must be between 0 and 100 |
| `maxHealth` | Integer | NNN | 1–3 | Maximum health of the player | `100` | Must be greater than 0 |
| `damage` | Integer | NN | 1–2 | Amount of damage dealt during combat | `25` | Must be 0 or greater |
| `inventory` | List | N/A | N/A | Stores items currently carried by the player | `[Medkit, Pistol]` | Items must be valid game items |
| `currentLocation` | String | XXXXXXXXXXXXX | Variable | The location where the player currently is | `Hospital` | Must be a valid location |
| `weapon` | Object | N/A | N/A | Weapon currently equipped by the player | `Pistol` | Must be a valid Weapon object |
| `zombieName` | String | XXXXXXXXXX | Variable | Name of the zombie encountered | `Fast Zombie` | Must be a valid zombie |
| `zombieHealth` | Integer | NNN | 1–3 | Current health of a zombie | `40` | Cannot be less than 0 |
| `zombieDamage` | Integer | NN | 1–2 | Amount of damage a zombie can cause | `15` | Must be 0 or greater |
| `zombieType` | String | XXXXXXXXXX | Variable | Identifies the type of zombie | `Tank` | Must be a valid zombie type |
| `itemName` | String | XXXXXXXXXXXXX | Variable | Name of an item found in the game | `Medkit` | Must be a valid item |
| `itemType` | String | XXXXXXXXXX | Variable | Identifies the category of an item | `Weapon` | Must be a valid item type |
| `weaponDamage` | Integer | NN | 1–2 | Amount of damage caused by a weapon | `30` | Must be between 1 and 100 |
| `healingAmount` | Integer | NN | 1–2 | Amount of health restored by a consumable | `25` | Must be greater than 0 |
| `locationName` | String | XXXXXXXXXXXXX | Variable | Name of a location in the game | `Hospital` | Must be a valid location |
| `locationDescription` | String | XXXXXXXXXXXXX | Variable | Description displayed when entering a location | `An abandoned hospital` | Cannot be empty |
| `hasKeycard` | Boolean | X | 1 | Determines whether the player has the evacuation keycard | `True` | Must be True or False |
| `gameOver` | Boolean | X | 1 | Determines whether the game has ended | `False` | Must be True or False |
| `gameWon` | Boolean | X | 1 | Determines whether the player has successfully escaped | `True` | Must be True or False |
| `playerChoice` | String | XXXXXXXXXX | Variable | Command entered by the player | `attack` | Must be a valid command |
| `enemyType` | String | XXXXXXXXXX | Variable | Type of enemy currently being encountered | `Fast Zombie` | Must be a valid enemy type |
