# pathfinder_character_sheet

## Setup

1. Export your character as an xml like this:
   ![Example Character Export](https://i.imgur.com/97OGYgb.png)
2. git pull to get latest version
3. cd to where the code lives
4. `python -m pathfinder_character_sheet.character_sheet <filepath to exported xml character sheet>`
5. Go to localhost:8080 and enjoy!
6. (Optional) If you have multiple characters you would like to bring up at once, you can pass in `port={port#}` to run multiple instances of the tool simultaneously
