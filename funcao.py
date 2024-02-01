#funções do bot
from discord_webhook import DiscordWebhook, DiscordEmbed

def discord_webhook123(bot):
    webhook = DiscordWebhook(url= bot["webhook_url"])
    embed = DiscordEmbed(title= bot["title_msg"], description= bot["msg"], color= bot["color"])
    embed.set_author(name= bot["name_author"], icon_url= bot["author_icon"])
    embed.set_footer(text= bot["footer"])
    embed.set_timestamp()
    embed.set_thumbnail(url= bot["thumb"])
    webhook.add_embed(embed)
    response = webhook.execute()
