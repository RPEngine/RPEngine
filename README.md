# RPEngine Bot

A fully immersive Discord RP bot with world simulation, celestial tracking, character management, and AI-driven features. Built for Pathfinder 1e and custom worlds.

## Setup

1. Clone this repository
2. Copy `.env.example` to `.env` and fill in your:
   - DISCORD_TOKEN
   - GUILD_ID
   - BUMP_CHANNEL_ID
   - OPENAI_API_KEY
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```
   python main.py
   ```

## Deployment via Render

- Upload this repo to GitHub
- Connect it to [https://render.com](https://render.com)
- Add the environment variables from your `.env` file
