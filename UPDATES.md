# UPDATES - Token Handling & Naming Standards

## What Changed

### 1. Renamed to Standard Bot Naming
- ✅ `card_tracker_bot.py` → `main.py` (industry standard)
- ✅ Updated all scripts and documentation

### 2. Fixed Token Loading (Multiple Fallback Methods)

The bot now tries **4 different methods** to get your token:

**Priority Order:**
1. `DISCORD_BOT_TOKEN` environment variable (Wispbyte default)
2. `BOT_TOKEN` environment variable (alternate)
3. `token.txt` file in bot directory
4. `bot_token.txt` file in bot directory

**Why this helps:**
- If Wispbyte's env vars don't work, the file method will
- You'll see exactly which method worked in the console
- Clear error messages if ALL methods fail

### 3. Better Error Messages

Old error:
```
⚠️ ERROR: No bot token found!
```

New error shows:
```
❌ ERROR: No bot token found!

Tried the following methods:
  1. DISCORD_BOT_TOKEN environment variable
  2. BOT_TOKEN environment variable
  3. token.txt file
  4. bot_token.txt file

For Wispbyte/hosting platforms:
  - Set DISCORD_BOT_TOKEN in the environment variables

For local development:
  - Create a file named 'token.txt' with your bot token
```

## For Wispbyte - Use This Startup Command

```bash
if [[ -d .git ]] && [[ "0" == "1" ]]; then git pull; fi; if [[ ! -z "" ]]; then pip install -U --prefix .local ; fi; if [[ -f /home/container/requirements.txt ]]; then pip install -U --prefix .local -r requirements.txt; fi; /usr/local/bin/python /home/container/main.py
```

## Setup Options for Token

### Option A: Environment Variable (Try This First)
In Wispbyte dashboard:
- Variable Name: `DISCORD_BOT_TOKEN`
- Variable Value: `your_actual_token_here`

### Option B: Token File (Backup Method)
1. Create file: `token.txt`
2. Contents: Just your bot token (nothing else)
3. Upload to Wispbyte with main.py

## Files You Need to Upload to Wispbyte

**Required:**
- `main.py` - The bot
- `requirements.txt` - Dependencies

**Optional (if env vars don't work):**
- `token.txt` - Your bot token

## What You'll See When It Starts

**Success:**
```
==================================================
Card Tracker Bot - Starting Up
==================================================
✓ Token loaded from DISCORD_BOT_TOKEN environment variable
==================================================
Starting bot...
==================================================
Card Tracker Bot is now online!
Ready to track cards!
```

**Failure:**
```
==================================================
❌ ERROR: No bot token found!
==================================================
[Shows all 4 methods it tried]
```

## Testing Locally

If you want to test on your own machine:

**Windows:**
```powershell
# Create token file
echo YOUR_TOKEN_HERE > token.txt

# Run bot
python main.py
```

**Linux/Mac:**
```bash
# Create token file
echo "YOUR_TOKEN_HERE" > token.txt

# Run bot
python3 main.py
```

The bot will find it automatically!
