import discord
from discord.ext import commands
import json
import os

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Storage for card quantities and message ID
DATA_FILE = 'card_data.json'

def load_data():
    """Load card quantities and message ID from file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'quantities': [0, 0, 0, 0, 0, 0, 0],
        'message_id': None,
        'channel_id': None
    }

def save_data(data):
    """Save card quantities and message ID to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Load initial data
data = load_data()

def create_embed():
    """Create the card inventory embed"""
    embed = discord.Embed(
        title="🎴 Card Inventory",
        color=0x00ff00,
        description="React with 1️⃣-7️⃣ to add cards\nReact with ✅ to consume a set"
    )
    
    # Create the table
    cards = "\n".join([f"**{i+1}**" for i in range(7)])
    quantities = "\n".join([str(q) for q in data['quantities']])
    
    embed.add_field(name="Cards", value=cards, inline=True)
    embed.add_field(name="Quantity", value=quantities, inline=True)
    
    return embed

@bot.event
async def on_ready():
    """Called when bot is ready"""
    print(f'{bot.user} is now online!')
    print('Ready to track cards!')

@bot.command(name='setup')
async def setup_tracker(ctx):
    """Create the card tracker embed"""
    embed = create_embed()
    message = await ctx.send(embed=embed)
    
    # Add reaction buttons
    reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '✅']
    for reaction in reactions:
        await message.add_reaction(reaction)
    
    # Save message info
    data['message_id'] = message.id
    data['channel_id'] = ctx.channel.id
    save_data(data)
    
    await ctx.send("Card tracker setup complete! React to track cards.", delete_after=5)

@bot.command(name='reset')
async def reset_cards(ctx):
    """Reset all card quantities to 0"""
    data['quantities'] = [0, 0, 0, 0, 0, 0, 0]
    save_data(data)
    
    if data['message_id'] and data['channel_id']:
        channel = bot.get_channel(data['channel_id'])
        try:
            message = await channel.fetch_message(data['message_id'])
            await message.edit(embed=create_embed())
            await ctx.send("Card quantities reset to 0!", delete_after=5)
        except:
            await ctx.send("Couldn't find the tracker message. Use !setup to create a new one.")
    else:
        await ctx.send("No tracker found. Use !setup to create one.")

@bot.event
async def on_reaction_add(reaction, user):
    """Handle reactions being added"""
    # Ignore bot's own reactions
    if user.bot:
        return
    
    # Only process reactions on the tracker message
    if reaction.message.id != data['message_id']:
        return
    
    # Map emoji to card index
    emoji_map = {
        '1️⃣': 0, '2️⃣': 1, '3️⃣': 2, '4️⃣': 3,
        '5️⃣': 4, '6️⃣': 5, '7️⃣': 6
    }
    
    # Handle number reactions (add cards)
    if str(reaction.emoji) in emoji_map:
        card_index = emoji_map[str(reaction.emoji)]
        data['quantities'][card_index] += 1
        save_data(data)
        
        # Update the embed
        await reaction.message.edit(embed=create_embed())
        
        # Remove the user's reaction
        await reaction.remove(user)
    
    # Handle checkmark (consume set)
    elif str(reaction.emoji) == '✅':
        # Check if we have at least one of each card
        if all(q > 0 for q in data['quantities']):
            # Consume one of each
            data['quantities'] = [q - 1 for q in data['quantities']]
            save_data(data)
            
            # Update the embed
            await reaction.message.edit(embed=create_embed())
            
            # Send confirmation
            await reaction.message.channel.send(f"{user.mention} consumed a complete set! 🎉", delete_after=5)
        else:
            # Not enough cards
            await reaction.message.channel.send(
                f"{user.mention} You need at least one of each card to consume a set!",
                delete_after=5
            )
        
        # Remove the user's reaction
        await reaction.remove(user)

@bot.command(name='status')
async def show_status(ctx):
    """Show current card quantities in chat"""
    status = "**Current Card Inventory:**\n"
    for i, qty in enumerate(data['quantities'], 1):
        status += f"Card {i}: {qty}\n"
    
    total = sum(data['quantities'])
    complete_sets = min(data['quantities']) if data['quantities'] else 0
    
    status += f"\nTotal cards: {total}"
    status += f"\nComplete sets available: {complete_sets}"
    
    await ctx.send(status, delete_after=10)

# Run the bot
if __name__ == '__main__':
    print("=" * 50)
    print("Card Tracker Bot - Starting Up")
    print("=" * 50)
    
    # Try multiple methods to get the token
    token = None
    
    # Method 1: Environment variable (works on most hosting platforms)
    token = os.getenv('DISCORD_BOT_TOKEN')
    if token:
        print("✓ Token loaded from DISCORD_BOT_TOKEN environment variable")
    
    # Method 2: Try common alternative env var names
    if not token:
        token = os.getenv('BOT_TOKEN')
        if token:
            print("✓ Token loaded from BOT_TOKEN environment variable")
    
    # Method 3: Try loading from token.txt file
    if not token and os.path.exists('token.txt'):
        try:
            with open('token.txt', 'r') as f:
                token = f.read().strip()
            if token:
                print("✓ Token loaded from token.txt file")
        except Exception as e:
            print(f"⚠️  Could not read token.txt: {e}")
    
    # Method 4: Try loading from bot_token.txt file
    if not token and os.path.exists('bot_token.txt'):
        try:
            with open('bot_token.txt', 'r') as f:
                token = f.read().strip()
            if token:
                print("✓ Token loaded from bot_token.txt file")
        except Exception as e:
            print(f"⚠️  Could not read bot_token.txt: {e}")
    
    # Final check
    if not token:
        print("\n" + "=" * 50)
        print("❌ ERROR: No bot token found!")
        print("=" * 50)
        print("\nTried the following methods:")
        print("  1. DISCORD_BOT_TOKEN environment variable")
        print("  2. BOT_TOKEN environment variable")
        print("  3. token.txt file")
        print("  4. bot_token.txt file")
        print("\nFor Wispbyte/hosting platforms:")
        print("  - Set DISCORD_BOT_TOKEN in the environment variables")
        print("\nFor local development:")
        print("  - Create a file named 'token.txt' with your bot token")
        print("  - OR set environment variable: export DISCORD_BOT_TOKEN='your_token'")
        print("=" * 50)
        exit(1)
    
    print("=" * 50)
    print("Starting bot...")
    print("=" * 50)
    
    try:
        bot.run(token)
    except Exception as e:
        print(f"\n❌ Bot crashed: {e}")
        exit(1)
