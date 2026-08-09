"""Dead Zone: Polymorphism.

A text-based zombie survival RPG designed for a Year 11 Software Engineering
assessment. The game demonstrates key OOP ideas such as classes, inheritance,
encapsulation, and polymorphism while remaining simple enough for a classroom
project.

The game can be run directly from Python or integrated into a web application by
using the Game class and its command-processing methods.
"""

from __future__ import annotations

import argparse
import json
import os
import random
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Dict, List, Optional
from urllib.parse import urlparse


class InvalidCommandError(ValueError):
    """Raised when a user enters a command that is not valid in the current state."""


@dataclass
class Item:
    """Base class for all world items, including weapons and healing objects.

    This demonstrates abstraction: the player only needs to interact with an item
    using simple methods such as use() or equip(), without caring about the item
    details.
    """

    name: str
    description: str
    item_type: str = "loot"
    heal_amount: int = 0
    damage: int = 0

    def __str__(self) -> str:
        return self.name


class Weapon(Item):
    """A weapon item that increases the player's damage output in combat."""

    def __init__(self, name: str, description: str, damage: int):
        super().__init__(name=name, description=description, item_type="weapon", damage=damage)


class HealingItem(Item):
    """A consumable item that restores health when used."""

    def __init__(self, name: str, description: str, heal_amount: int):
        super().__init__(name=name, description=description,
                         item_type="healing", heal_amount=heal_amount)


class Zombie:
    """Base zombie class.

    Different zombie subclasses override the same attack behaviour to demonstrate
    polymorphism: they share a common interface but behave differently.
    """

    def __init__(self, name: str, health: int, damage: int, zombie_type: str, description: str):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.zombie_type = zombie_type
        self.description = description

    def attack(self, target):
        """Main enemy action. The target is typically the Player object."""
        return target.take_damage(self.damage)

    def take_damage(self, amount: int) -> int:
        self.health -= amount
        return self.health

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name} ({self.zombie_type})"


class FastZombie(Zombie):
    """A quicker zombie that deals moderate damage but has lower health."""

    def __init__(self, name: str = "Runner"):
        super().__init__(
            name=name,
            health=18,
            damage=7,
            zombie_type="Fast Zombie",
            description="It moves extremely quickly and lunges at you without warning.",
        )

    def attack(self, target):
        extra = random.randint(0, 3)
        return target.take_damage(self.damage + extra)


class TankZombie(Zombie):
    """A slow but powerful zombie that deals high damage."""

    def __init__(self, name: str = "Brute"):
        super().__init__(
            name=name,
            health=28,
            damage=12,
            zombie_type="Tank Zombie",
            description="A massive undead creature that can crush a survivor in one hit.",
        )


class Player:
    """Represents the player character.

    Encapsulation keeps the player's state protected behind methods such as
    take_damage(), heal(), add_item(), and equip_weapon().
    """

    def __init__(self, name: str):
        self.name = name.strip()
        self.max_health = 100
        self.health = self.max_health
        self.inventory: List[Item] = []
        self.equipped_weapon: Optional[Weapon] = None
        self.location = None
        self.has_keycard = False

    def take_damage(self, amount: int) -> int:
        self.health = max(0, self.health - amount)
        return self.health

    def heal(self, amount: int) -> int:
        self.health = min(self.max_health, self.health + amount)
        return self.health

    def add_item(self, item: Item) -> None:
        self.inventory.append(item)

    def remove_item(self, item_name: str) -> Optional[Item]:
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                return item
        return None

    def has_item(self, item_name: str) -> bool:
        return any(item.name.lower() == item_name.lower() for item in self.inventory)

    def equip_weapon(self, weapon_name: str) -> str:
        weapon = self.find_item(weapon_name, item_type="weapon")
        if weapon is None:
            return "You do not have that weapon."

        self.equipped_weapon = weapon
        return f"You equip the {weapon.name}."

    def find_item(self, item_name: str, item_type: Optional[str] = None) -> Optional[Item]:
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item_type is None or item.item_type == item_type:
                    return item
        return None

    def use_item(self, item_name: str) -> str:
        item = self.find_item(item_name)
        if item is None:
            return "You do not have that item."

        if item.item_type == "healing":
            self.heal(item.heal_amount)
            self.inventory.remove(item)
            return f"You use the {item.name} and recover {item.heal_amount} health."

        if item.name.lower() == "evacuation keycard":
            self.has_keycard = True
            return "You study the Evacuation Keycard. It unlocks the evacuation route."

        return f"The {item.name} is not useful right now."

    def inventory_summary(self) -> str:
        if not self.inventory:
            return "Your inventory is empty."

        names = [item.name for item in self.inventory]
        return "Inventory: " + ", ".join(names)

    def attack_damage(self) -> int:
        if self.equipped_weapon is not None:
            return self.equipped_weapon.damage
        return 6


class Location:
    """A location that the player can move between and search for supplies."""

    def __init__(self, name: str, description: str, exits: Optional[Dict[str, str]] = None):
        self.name = name
        self.description = description
        self.exits = exits or {}
        self.items: List[Item] = []
        self.searched = False
        self.zombie: Optional[Zombie] = None
        self.locked_to_keycard = False

    def search(self) -> str:
        """Search the location for loot and possible threats."""
        if self.searched:
            return f"You have already searched {self.name}. There may be nothing left to find."

        self.searched = True
        loot_found = []

        if self.items:
            loot_found.extend([item.name for item in self.items])
            result = f"You search the area and find: {', '.join(loot_found)}."
        else:
            result = "You search carefully but find nothing useful."

        if self.zombie is not None:
            result += f" A {self.zombie.name} blocks your path!"

        return result

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> Optional[Item]:
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        return None

    def __str__(self) -> str:
        return self.name


class Game:
    """Main controller for the game.

    The Game object manages the player, world map, battle flow, and state checks.
    It is structured to be used either as a console game or integrated with a web
    interface that calls process_command().
    """

    def __init__(self):
        self.player = None
        self.locations: Dict[str, Location] = {}
        self.current_location: Optional[str] = None
        self.game_over = False
        self.victory = False
        self.story_intro = (
            "The city is in chaos. The dead walk the streets, and you are one of the last survivors. "
            "Find the Evacuation Keycard, gather supplies, survive the infected, and escape to the Evacuation Zone."
        )
        self.setup_world()

    def setup_world(self) -> None:
        """Create all locations, items, weapons, and zombie events."""
        abandoned_house = Location(
            "Abandoned House",
            "An old house covered in ash. Broken furniture and torn curtains still remain.",
            {"east": "Supermarket", "south": "Hospital"},
        )
        supermarket = Location(
            "Supermarket",
            "Shelves are smashed and the freezer doors hang open. It smells of rot and metal.",
            {"west": "Abandoned House", "east": "Police Station"},
        )
        hospital = Location(
            "Hospital",
            "The emergency wing is silent except for the echo of your footsteps.",
            {"north": "Abandoned House", "east": "Evacuation Zone"},
        )
        police_station = Location(
            "Police Station",
            "The station is filled with broken glass, riot gear, and old evidence boxes.",
            {"west": "Supermarket", "east": "Evacuation Zone"},
        )
        evacuation_zone = Location(
            "Evacuation Zone",
            "A fenced extraction point with bright floodlights and a single locked access gate.",
            {"west": "Hospital", "south": "Police Station"},
        )
        evacuation_zone.locked_to_keycard = True

        abandoned_house.add_item(
            Weapon("Baseball Bat", "A heavy bat that can smash a zombie skull.", 10))
        abandoned_house.add_item(HealingItem(
            "Bandage", "A basic field dressing to stop bleeding.", 12))
        abandoned_house.zombie = FastZombie("Scratcher")

        supermarket.add_item(
            Weapon("Kitchen Knife", "A sharp kitchen blade for close combat.", 12))
        supermarket.add_item(HealingItem(
            "Energy Drink", "A sugary drink that restores a small amount of health.", 8))
        supermarket.zombie = FastZombie("Shambler")

        hospital.add_item(HealingItem(
            "Medkit", "A proper emergency kit with bandages and antiseptic.", 20))
        hospital.add_item(
            Weapon("Pistol", "A sidearm that packs a solid punch.", 18))
        hospital.add_item(Item(
            "Evacuation Keycard", "A secured card that opens the evacuation gate.", "keycard"))
        hospital.zombie = TankZombie("Medic")

        police_station.add_item(
            Weapon("Police Baton", "A sturdy baton used for crowd control.", 15))
        police_station.add_item(HealingItem(
            "Painkiller", "Medicines that reduce pain and restore health.", 14))
        police_station.zombie = TankZombie("Officer")

        self.locations = {
            "Abandoned House": abandoned_house,
            "Supermarket": supermarket,
            "Hospital": hospital,
            "Police Station": police_station,
            "Evacuation Zone": evacuation_zone,
        }

    def create_player(self, player_name: str) -> Player:
        """Create the game player and start them in the Abandoned House."""
        player = Player(player_name)
        starting_location = self.locations["Abandoned House"]
        player.location = starting_location
        player.add_item(
            Weapon("Rusty Pipe", "A dented pipe used as a basic melee weapon.", 8))
        player.add_item(HealingItem(
            "Bandage", "A simple dressing for minor injuries.", 12))
        self.player = player
        self.current_location = "Abandoned House"
        return player

    def current_description(self) -> str:
        if self.player is None:
            return "No active player."

        location = self.player.location
        description = [
            f"\nLocation: {location.name}",
            f"{location.description}",
            f"Exits: {', '.join(location.exits.keys()) if location.exits else 'None'}",
            f"Health: {self.player.health}/{self.player.max_health}",
            f"Weapon: {self.player.equipped_weapon.name if self.player.equipped_weapon else 'Unarmed'}",
            f"Inventory: {self.player.inventory_summary()}",
        ]
        return "\n".join(description)

    def show_help(self) -> str:
        return (
            "Commands:\n"
            "- help: show this information\n"
            "- look: describe your current location\n"
            "- inventory: show your items\n"
            "- search: search the area for items and enemies\n"
            "- move <direction>: travel to another location (north, south, east, west)\n"
            "- attack: fight the zombie in your current area\n"
            "- run: try to escape from combat\n"
            "- use <item>: use a healing item or keycard\n"
            "- equip <weapon>: equip a weapon from your inventory\n"
            "- stats: show player health and equipped weapon\n"
            "- quit: exit the game"
        )

    def get_location_items(self) -> List[str]:
        return [item.name for item in self.player.location.items]

    def fight_zombie(self) -> str:
        """Handle one combat round against the current location zombie."""
        location = self.player.location
        if location.zombie is None:
            return "There is no zombie here to fight."

        if not location.zombie.is_alive():
            return "The zombie is already defeated."

        player_damage = self.player.attack_damage()
        zombie_damage = location.zombie.damage

        # Round 1: player attacks
        location.zombie.take_damage(player_damage)
        result = f"You attack the {location.zombie.name} for {player_damage} damage."

        if not location.zombie.is_alive():
            location.zombie = None
            result += "\nThe zombie collapses to the ground."
            self.player.location.searched = True
            return result

        # Round 2: zombie attacks
        self.player.take_damage(zombie_damage)
        result += f"\nThe {location.zombie.name} hits you for {zombie_damage} damage."
        if self.player.health <= 0:
            self.game_over = True
            result += "\nYou fall in battle. The dead zone wins."
        return result

    def run_from_zombie(self) -> str:
        """Attempt to escape from an active zombie encounter."""
        location = self.player.location
        if location.zombie is None:
            return "There is no need to run."

        chance = random.randint(1, 100)
        if chance <= 60:
            location.zombie = None
            return "You escape the zombie and move away from the danger."

        damage = random.randint(4, 9)
        self.player.take_damage(damage)
        if self.player.health <= 0:
            self.game_over = True
            return f"You try to run but the zombie catches you. You take {damage} damage and collapse."

        return f"You fail to escape and take {damage} damage before getting away."

    def take_item_from_location(self, item_name: str) -> str:
        location = self.player.location
        found = location.remove_item(item_name)
        if found is None:
            return "You cannot find that item here."

        self.player.add_item(found)
        return f"You take the {found.name}."

    def validate_name(self, player_name: str) -> str:
        cleaned = player_name.strip()
        if not cleaned:
            raise InvalidCommandError("Player name cannot be blank.")
        if len(cleaned) < 2:
            raise InvalidCommandError(
                "Player name must be at least 2 characters long.")
        if any(character.isdigit() for character in cleaned):
            raise InvalidCommandError("Player name cannot contain numbers.")
        return cleaned

    def process_command(self, command: str) -> str:
        """Handle a player command and return the narrative text for the game loop."""
        if self.game_over or self.victory:
            return "The game has ended. Start a new run to play again."

        command_text = command.strip()
        if not command_text:
            return "Please enter a command. Type 'help' for instructions."

        parts = command_text.split()
        verb = parts[0].lower()

        if verb in {"help", "?"}:
            return self.show_help()

        if verb in {"look", "status"}:
            return self.current_description()

        if verb in {"inventory", "inv"}:
            return self.player.inventory_summary()

        if verb == "stats":
            return (
                f"Name: {self.player.name}\n"
                f"Health: {self.player.health}/{self.player.max_health}\n"
                f"Weapon: {self.player.equipped_weapon.name if self.player.equipped_weapon else 'Unarmed'}\n"
                f"Keycard: {'Yes' if self.player.has_keycard else 'No'}"
            )

        if verb in {"move", "go"}:
            if len(parts) < 2:
                return "You must specify a direction such as north, south, east, or west."
            direction = parts[1].lower()
            if direction not in {"north", "south", "east", "west"}:
                return "Invalid direction. Use north, south, east, or west."

            current = self.player.location
            target_name = current.exits.get(direction)
            if target_name is None:
                return "You cannot move in that direction from here."

            if target_name == "Evacuation Zone" and not self.player.has_keycard:
                return "The gate is locked. You need the Evacuation Keycard before entering the Evacuation Zone."

            self.player.location = self.locations[target_name]
            self.current_location = target_name
            if self.player.location.zombie is not None:
                return (
                    f"You arrive at {target_name}. {self.player.location.description}\n"
                    f"A {self.player.location.zombie.name} is waiting here! Type 'attack' or 'run'."
                )
            return f"You move to {target_name}. {self.player.location.description}"

        if verb == "search":
            location = self.player.location
            if location.zombie is not None and location.zombie.is_alive():
                return (
                    f"You search around the area but the {location.zombie.name} is blocking your path! "
                    "You must fight or run."
                )

            if location.searched:
                return f"You search {location.name} again, but there is nothing else to find."

            found_items = [item.name for item in location.items]
            if found_items:
                output = [
                    f"You search {location.name} and find: {', '.join(found_items)}. "]
                for item in list(location.items):
                    output.append(f"Type 'take {item.name}' to pick it up.")
                return "\n".join(output)

            if location.name == "Hospital":
                return "You search the hospital and find a hidden locker. The Evacuation Keycard was kept inside."

            return f"You search {location.name} and find nothing useful."

        if verb in {"attack", "fight"}:
            if self.player.location.zombie is None:
                return "There is no zombie here to attack."
            return self.fight_zombie()

        if verb == "run":
            if self.player.location.zombie is None:
                return "There is nowhere to run from here."
            result = self.run_from_zombie()
            if self.player.health <= 0:
                self.game_over = True
            return result

        if verb == "take":
            if len(parts) < 2:
                return "Specify which item you want to take. Example: take medkit"
            item_name = " ".join(parts[1:]).strip()
            if not item_name:
                return "You must specify an item name."
            location_item = self.player.location.remove_item(item_name)
            if location_item is None:
                # Support a case where the item is not directly on the ground but found by search
                if self.player.location.name == "Hospital" and item_name.lower() == "evacuation keycard":
                    self.player.add_item(Item(
                        "Evacuation Keycard", "A secured card that opens the evacuation gate.", "keycard"))
                    self.player.has_keycard = True
                    return "You take the Evacuation Keycard from the locker."
                return f"There is no {item_name} here to take."
            self.player.add_item(location_item)
            if location_item.name.lower() == "evacuation keycard":
                self.player.has_keycard = True
            return f"You take the {location_item.name}."

        if verb == "equip":
            if len(parts) < 2:
                return "Specify the weapon to equip. Example: equip pistol"
            weapon_name = " ".join(parts[1:]).strip()
            if not weapon_name:
                return "Weapon name cannot be blank."
            return self.player.equip_weapon(weapon_name)

        if verb == "use":
            if len(parts) < 2:
                return "Specify which item to use. Example: use medkit"
            item_name = " ".join(parts[1:]).strip()
            if not item_name:
                return "Item name cannot be blank."
            return self.player.use_item(item_name)

        if verb == "quit":
            self.game_over = True
            return "You leave the dead zone behind. The city still burns, but you have chosen to walk away."

        if verb == "clear" and self.player.location.name == "Evacuation Zone":
            if self.player.has_keycard:
                self.victory = True
                return "You swipe the Evacuation Keycard and the extraction gate opens. Survivors are rescued. YOU WIN!"
            return "The gate remains locked without the Evacuation Keycard."

        return "Invalid command. Type 'help' for a list of commands."

    def check_victory_condition(self) -> None:
        """Determine whether the player has reached the victory state."""
        if self.player is None:
            return

        if self.player.location.name == "Evacuation Zone" and self.player.has_keycard:
            self.victory = True

    def get_web_state(self) -> dict:
        """Return the current game state in a format suitable for a web UI."""
        if self.player is None:
            return {
                "started": False,
                "player_name": "",
                "location": "",
                "health": 0,
                "max_health": 100,
                "weapon": "Unarmed",
                "inventory": [],
                "keycard": False,
                "game_over": False,
                "victory": False,
                "intro": self.story_intro,
            }

        return {
            "started": True,
            "player_name": self.player.name,
            "location": self.player.location.name,
            "health": self.player.health,
            "max_health": self.player.max_health,
            "weapon": self.player.equipped_weapon.name if self.player.equipped_weapon else "Unarmed",
            "inventory": [item.name for item in self.player.inventory],
            "keycard": self.player.has_keycard,
            "game_over": self.game_over,
            "victory": self.victory,
            "intro": self.story_intro,
            "description": self.current_description(),
        }

    def start_new_game(self, player_name: str) -> dict:
        """Begin a new run and return the initial web state."""
        self.game_over = False
        self.victory = False
        cleaned_name = self.validate_name(player_name)
        self.create_player(cleaned_name)
        return self.get_web_state()

    def play(self) -> None:
        """Run the main console game loop."""
        print("Welcome to Dead Zone: Polymorphism")
        print(self.story_intro)

        while True:
            try:
                player_name = input("Enter your name: ").strip()
                if not player_name:
                    raise InvalidCommandError("Player name cannot be blank.")
                self.create_player(player_name)
                break
            except InvalidCommandError as error:
                print(f"Invalid input: {error}")

        print(
            f"\nWelcome, {self.player.name}! You wake up in the {self.player.location.name}.")
        print(self.show_help())

        while not self.game_over and not self.victory:
            print(self.current_description())
            command = input("\nWhat do you do? ")
            response = self.process_command(command)
            print(response)

            if self.player.health <= 0:
                self.game_over = True
                print("Game over. You were overwhelmed by the zombie horde.")
                break

            self.check_victory_condition()
            if self.victory:
                print(
                    "\nCongratulations! You reached the Evacuation Zone with the Keycard and escaped the dead zone.")
                break

        print("\nThanks for playing Dead Zone: Polymorphism.")


def run_web_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Serve the game through a lightweight browser UI using the Python standard library."""
    game = Game()

    def get_index() -> str:
        file_path = os.path.join(os.path.dirname(__file__), "index.html")
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    class GameHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_path = urlparse(self.path)
            if parsed_path.path == "/":
                content = get_index().encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

            if parsed_path.path == "/api/state":
                payload = json.dumps(game.get_web_state()).encode("utf-8")
                self.send_response(200)
                self.send_header(
                    "Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
                return

            self.send_error(404, "Not found")

        def do_POST(self):
            parsed_path = urlparse(self.path)
            if parsed_path.path == "/api/start":
                length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(length).decode("utf-8")
                data = json.loads(body or "{}")
                name = str(data.get("player_name", "")).strip()

                try:
                    state = game.start_new_game(name)
                    message = f"Welcome, {state['player_name']}! You wake up in the {state['location']}."
                    response = {"success": True,
                                "message": message, "state": state}
                except InvalidCommandError as error:
                    response = {"success": False, "message": str(
                        error), "state": game.get_web_state()}

                payload = json.dumps(response).encode("utf-8")
                self.send_response(200)
                self.send_header(
                    "Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
                return

            if parsed_path.path == "/api/command":
                length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(length).decode("utf-8")
                data = json.loads(body or "{}")
                command = str(data.get("command", "")).strip()

                if game.player is None:
                    response = {
                        "success": False, "message": "Start a new game first.", "state": game.get_web_state()}
                else:
                    result = game.process_command(command)
                    if game.player is not None and game.player.health <= 0:
                        game.game_over = True
                    if game.player is not None and game.player.location.name == "Evacuation Zone" and game.player.has_keycard:
                        game.check_victory_condition()
                    response = {"success": True, "message": result,
                                "state": game.get_web_state()}

                payload = json.dumps(response).encode("utf-8")
                self.send_response(200)
                self.send_header(
                    "Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
                return

            self.send_error(404, "Not found")

        def log_message(self, format, *args):
            return

    server = ThreadingHTTPServer((host, port), GameHandler)
    print(f"Dead Zone server running at http://{host}:{port}")
    print("Press Ctrl+C to stop the server.")
    server.serve_forever()


def main() -> None:
    """Entry point for the console version of the game."""
    parser = argparse.ArgumentParser(description="Dead Zone: Polymorphism")
    parser.add_argument("--web", action="store_true",
                        help="Run the game in the browser.")
    parser.add_argument("--host", default="127.0.0.1",
                        help="Host for the web server.")
    parser.add_argument("--port", type=int, default=8000,
                        help="Port for the web server.")
    args = parser.parse_args()

    if args.web:
        run_web_server(host=args.host, port=args.port)
        return

    game = Game()
    game.play()


if __name__ == "__main__":
    main()
