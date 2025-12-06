# Wispbyte Setup Instructions for Card Tracker Bot

## Files to Upload

1. **main.py** - The bot code
2. **requirements.txt** - Dependencies (just contains: discord.py>=2.3.0)

## Startup Command

Copy and paste this into the Wispbyte command editor:

```bash
if [[ -d .git ]] && [[ "0" == "1" ]]; then git pull; fi; if [[ ! -z "" ]]; then pip install -U --prefix .local ; fi; if [[ -f /home/container/requirements.txt ]]; then pip install -U --prefix .local -r requirements.txt; fi; /usr/local/bin/python /home/container/main.py
```

## Environment Variables Setup

### Option 1: Wispbyte Environment Variables (Recommended)
1. Go to your bot's control panel in Wispbyte
2. Find "Environment Variables" or "Startup Variables" section
3. Add a new variable:
   - **Name:** `DISCORD_BOT_TOKEN`
   - **Value:** Your actual Discord bot token (starts with something like `MTIz...`)

### Option 2: Token File (If env vars don't work)
1. Create a file named `token.txt` in the same directory as main.py
2. Paste your Discord bot token in it (just the token, nothing else)
3. Upload this file to Wispbyte

The bot will automatically try both methods!

## Troubleshooting Token Issues

If the bot won't start, check the console output. It will tell you:
- ✓ Which method successfully loaded the token
- ❌ All the methods it tried if none worked

The bot tries these in order:
1. `DISCORD_BOT_TOKEN` environment variable
2. `BOT_TOKEN` environment variable  
3. `token.txt` file
4. `bot_token.txt` file

## After Starting

Once the bot is online in your Discord server, you can use these commands:

### Available Commands

- **`!setup`** - Create the card tracker embed with reaction buttons
  - The bot will create an interactive card inventory
  - React with 1️⃣-7️⃣ to add cards
  - React with ✅ to consume a complete set

- **`!status`** - Show current card quantities in chat
  - Displays all card counts
  - Shows total cards and complete sets available
  - Message auto-deletes after 10 seconds

- **`!reset`** - Reset all card quantities to 0
  - Clears the entire inventory
  - Updates the tracker embed automatically

- **`!forums`** - List all available forum channels in the server
  - Shows a numbered list of forums
  - Use this before creating a forum post

- **`!post <number>`** - Create a forum post with card inventory
  - First run `!forums` to see available forum channels
  - Then run `!post 1` (or the number you want)
  - Creates a thread in the selected forum with the current card inventory

## Notes

- The startup command installs discord.py automatically from requirements.txt
- Git auto-pull is disabled by default (the "0" == "1" part)
- To enable git auto-pull, change it to "1" == "1"
