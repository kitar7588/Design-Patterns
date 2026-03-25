# The Challenge: The Infinite Spawner
Imagine you are developing an Open World RPG. Your game world needs to populate different regions with various entities: quiet villages need NPCs to give quests, while dark dungeons need Enemies to challenge the player.

## Your Task:

Implement a Character Factory system that decouples the logic of "spawning" from the specific "type" of character being created.

### 1. Define the Product: 
Create an interface or abstract class named Character.It should have a method introduce() and greeting()

### 2. Create Concrete Characters : 
Implement at least two classes: NPC , Enemy

### 3. The Factory Method:
Create an abstract class (or interface) called Character.
- It should have a spawn() method that calls create_charactor(), triggers their introduce() and greeting().