# Wispbyte Setup Instructions for Card Tracker Bot

## Setup Method 1: Git Auto-Pull (Recommended)

This method allows Wispbyte to automatically pull updates from GitHub on every restart.

### Step 1: Create GitHub Personal Access Token

Since this is a private repository, you need a GitHub token:

1. Go to GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name like "Wispbyte IronExBot"
4. Select scopes: Check `repo` (full control of private repositories)
5. Click "Generate token"
6. **COPY THE TOKEN** - you won't see it again!

### Step 2: Set Environment Variables

In your Wispbyte control panel, set these environment variables:

- **`AUTO_UPDATE`** = `1` (enables git auto-clone and auto-pull)
- **`GH_TOKEN`** = `your_github_personal_access_token` (the token you just created)
- **`PY_FILE`** = `main.py`
- **`REQUIREMENTS_FILE`** = `requirements.txt`
- **`DISCORD_BOT_TOKEN`** = `your_discord_bot_token_here`

### Step 3: Startup Command

**Option A: With GitHub Token (for private repos)**

Use this startup command if you've set the `GH_TOKEN` variable:

```bash
if [[ "${AUTO_UPDATE}" == "1" ]]; then if [[ ! -d .git ]] && [[ ! -z "${GH_TOKEN}" ]]; then rm -rf * .[^.]* 2>/dev/null; git clone https://${GH_TOKEN}@github.com/Salain810/IronExBot.git .; elif [[ -d .git ]]; then git pull; fi; fi; if [[ ! -z "${PY_PACKAGES}" ]]; then pip install -U --prefix .local ${PY_PACKAGES}; fi; if [[ -f /home/container/${REQUIREMENTS_FILE} ]]; then pip install -U --prefix .local -r ${REQUIREMENTS_FILE}; fi; /usr/local/bin/python /home/container/${PY_FILE}
```

**Option B: Public Repo (if you make the repo public)**

If you make the repository public, you don't need the token:

```bash
if [[ "${AUTO_UPDATE}" == "1" ]]; then if [[ ! -d .git ]]; then rm -rf * .[^.]* 2>/dev/null; git clone https://github.com/Salain810/IronExBot.git .; elif [[ -d .git ]]; then git pull; fi; fi; if [[ ! -z "${PY_PACKAGES}" ]]; then pip install -U --prefix .local ${PY_PACKAGES}; fi; REQFILE=${REQUIREMENTS_FILE:-requirements.txt}; if [[ -f /home/container/$REQFILE ]]; then pip install -U --prefix .local -r $REQFILE; fi; PYFILE=${PY_FILE:-main.py}; /usr/local/bin/python /home/container/$PYFILE
```

**How it works:**
- On first start (no `.git` folder): Clears the directory and clones the repository
- On subsequent starts (`.git` exists): Runs `git pull` to get latest updates
- Installs dependencies from `requirements.txt`
- Starts the bot

**Troubleshooting:**
- If git asks for a password, the `GH_TOKEN` is not set or empty
- Check that you've created the `GH_TOKEN` environment variable in Wispbyte (not just in the startup command)
- Verify there are no extra spaces in the token value
- Alternative: Make the repository public and use Option B

---

## Setup Method 2: Manual File Upload

If you prefer not to use git auto-pull:

### Files to Upload

1. **main.py** - The bot code
2. **requirements.txt** - Dependencies (just contains: discord.py>=2.3.0)

### Startup Command

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
