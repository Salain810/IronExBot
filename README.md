# IronExBot

A Discord bot for tracking card inventory with an interactive embed interface. Players can add cards by reacting to the tracker and consume complete sets.

## Features

- Interactive card tracking with reaction buttons
- Persistent storage of card quantities
- Forum post creation with current inventory
- Complete set consumption tracking
- Auto-updating embed display

## Commands

### Card Tracking

- **`!setup`** - Create the card tracker embed
  - Creates an interactive card inventory in the current channel
  - Adds reaction buttons (1️⃣-7️⃣) for adding cards
  - Adds checkmark (✅) for consuming complete sets

- **`!status`** - Display current inventory
  - Shows quantities for all 7 card types
  - Displays total cards and available complete sets
  - Auto-deletes after 10 seconds

- **`!reset`** - Reset inventory to zero
  - Clears all card quantities
  - Updates the tracker embed automatically

### Forum Posts

- **`!forums`** - List all forum channels
  - Shows a numbered list of available forum channels
  - Use before creating a forum post

- **`!post <number>`** - Create a forum post
  - Creates a thread in the selected forum channel
  - Includes current card inventory embed
  - Example: `!post 1` creates post in forum #1

## How It Works

1. Run `!setup` to create the card tracker embed
2. React with number emojis (1️⃣-7️⃣) to add cards to inventory
3. When you have at least one of each card, react with ✅ to consume a complete set
4. The bot automatically updates the embed and tracks quantities
5. Data persists across bot restarts in `card_data.json`

## Setup

### For Wispbyte Hosting

See [WISPBYTE_SETUP.md](WISPBYTE_SETUP.md) for detailed hosting instructions.

**Quick Start:**
1. Upload `main.py` and `requirements.txt` to Wispbyte
2. Set environment variable `DISCORD_BOT_TOKEN` with your Discord bot token
3. Use the startup command from WISPBYTE_SETUP.md
4. Invite the bot to your Discord server

### For Local Development

1. Install dependencies:
   ```bash
   pip install discord.py>=2.3.0
   ```

2. Create `token.txt` with your Discord bot token

3. Run the bot:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.8+
- discord.py 2.3.0+

## Bot Permissions Required

The bot needs these Discord permissions:
- Read Messages/View Channels
- Send Messages
- Embed Links
- Add Reactions
- Manage Messages (to remove user reactions)
- Create Public Threads (for forum posts)

## File Structure

- `main.py` - Main bot code
- `card_data.json` - Persistent storage for card quantities (auto-created)
- `requirements.txt` - Python dependencies
- `token.txt` - Bot token for local development (gitignored)

## Security

Never commit your bot token to the repository. The bot supports multiple token loading methods:
- Environment variable `DISCORD_BOT_TOKEN` (recommended for hosting)
- Environment variable `BOT_TOKEN`
- `token.txt` file (for local development)
- `bot_token.txt` file (alternative)

All token files are gitignored by default.

## License

MIT