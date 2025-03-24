# これはDiscordボットの一般的なコマンドを含むCogです。
# ここでは、ボットのレイテンシを確認するためのpingコマンドを実装しています。
import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="ボットのレスポンスを確認します")
    async def ping(self, interaction: discord.Interaction):
        """ボットのレイテンシ（応答速度）を表示します。"""
        latency = self.bot.latency * 1000
        await interaction.response.send_message(f"Pong! レイテンシ: {latency:.2f} ms")

async def setup(bot):
    await bot.add_cog(General(bot))