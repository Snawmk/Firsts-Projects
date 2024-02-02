#!/bin/env python3
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests

def lambda_handler(event, context):
    def discord_webhook(bot):
        webhook = DiscordWebhook(url= bot["webhook_url"])
        embed = DiscordEmbed(title= bot["title_msg"], description= bot["msg"], color= bot["color"])
        embed.set_author(name= bot["name_author"], icon_url= bot["author_icon"])
        embed.set_footer(text= bot["footer"])
        embed.set_timestamp()
        embed.set_thumbnail(url= bot["thumb"])
        webhook.add_embed(embed)
        response = webhook.execute()
    
    
    # Declaração da API TripAdvisor
    dataIda = '2024-07-07'
    dataVolta = '2024-07-27'
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"
    querystring = {"sourceAirportCode":"GRU","destinationAirportCode":"NRT","date":dataIda,"itineraryType":"ROUND_TRIP","sortOrder":"PRICE","numAdults":"1","numSeniors":"0","classOfService":"ECONOMY","returnDate": dataVolta,"pageNumber":"1","currencyCode":"BRL"}
    headers = {
    	"X-RapidAPI-Key": "dc64b340f6msh70817691e115e37p1cf4eejsn8cf17ca24f09",
    	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    
    voos_resp = response.json()
    
    voo_mais_barato = {
        'companhia': voos_resp["data"]["flights"][0]["purchaseLinks"][0]["providerId"],
        'preco': voos_resp["data"]["flights"][0]["purchaseLinks"][0]["totalPrice"],
        'imgUrl': voos_resp["data"]["flights"][0]["purchaseLinks"][0]['partnerSuppliedProvider']['logoUrl']
    }
    
    precoFormatado = f'R$ {voo_mais_barato["preco"]}'
    
    # Declaração dos parâmetros do Bot
    bot = {
        'webhook_url':'https://discord.com/api/webhooks/1202644291776675990/Iq3_O4wCQELY6SB7nW2ACo-DDY5tpRtbcEo47TUwIJFW6QjO8aoa45Ga_Ujs3UhjT8qJ',
        'title_msg':f'Radar de preço de passagem aérea Brasil pro Japão\nIda: {dataIda}| Volta: {dataVolta}',
        'msg':f'Companhia: {voo_mais_barato["companhia"]}\nPreço: {precoFormatado}',
        'color':'0000000',
        'name_author':'Sr. voos - Atualizações',
        'author_icon':'https://cdn-icons-png.freepik.com/512/7893/7893979.png',
        'thumb':voo_mais_barato['imgUrl'],
        'footer':'Sr. Voos'}
    
    
    # Chama a função para mandar a mensagem no bot
    discord_webhook(bot)