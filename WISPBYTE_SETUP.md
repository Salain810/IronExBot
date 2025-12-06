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

Once the bot is online in your Discord server:
1. Type `!setup` in any channel
2. The bot will create the card tracker embed
3. Click reactions to add/remove cards

## Notes

- The startup command installs discord.py automatically from requirements.txt
- Git auto-pull is disabled by default (the "0" == "1" part)
- To enable git auto-pull, change it to "1" == "1"
