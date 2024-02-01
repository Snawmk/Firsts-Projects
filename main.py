#!/bin/env python3
from funcao import discord_webhook123


# Declaração dos parâmetros do Bot
bot = {
    'webhook_url':'https://discord.com/api/webhooks/1202644291776675990/Iq3_O4wCQELY6SB7nW2ACo-DDY5tpRtbcEo47TUwIJFW6QjO8aoa45Ga_Ujs3UhjT8qJ',
    'title_msg':'Radar de preço de passagem aérea',
    'msg':'Segue o valor da passagem',
    'color':'0000000',
    'name_author':'Sr. voos - Atualizações',
    'author_icon':'https://cdn-icons-png.freepik.com/512/7893/7893979.png',
    'thumb':'',
    'footer':'Sr. Voos'}
# Chama a função para mandar a mensagem no bot
discord_webhook(bot)