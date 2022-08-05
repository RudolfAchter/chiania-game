# chiania-game
Game Engine for Chiania (i'll try)

- clone this repository

```bash
git clone https://github.com/RudolfAchter/chiania-game.git
```

- cd into root dir of this repo

```bash
cd chiania-game
```

- run test scripts fom root dir

```bash
python3 src/test_player.test.py
python3 src/test_movement.test.py
```

- world should be built out of json Data and python program just consumes data
- bring Data to [world.json](src/data/world.json) if you like
- Items will be made out of "Rules" added to NFTs

It's about blockchain. So it should be distributed.
So feel free to reuse this code

## What this is about
Basically i am replicating functionality from [Chia Inventory](https://discord.gg/vPCvmGmZ), trying to pack as much function in self explaining classes. I write test_scripts that should explain how the classes and functions should work. Should be designed to easily build bot functionality for discord (while i didn't already build a bot for discord, but want to test it for Chia Testnet).
There is basically one "innovation" right now. These are the randomized dungeons. It reads settings from /src/data/*.random_dungeon.json and creates a dungeon based on the settings defined there. If a player enters dungeon, it is created.

player sends commands to his "player" class and "player" moves character which is all defined in /src/chiania/player.py

planning to support other movement direction (for example "up" "do