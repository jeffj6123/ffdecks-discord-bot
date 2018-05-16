import discord
import formatting_handler as formatter
import config
from ffdeck_handler import FFDecks

ffdeck = FFDecks()
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith(config.PREFIX + 'card'):
        data = message.content.split(' ')
        data = [element for element in data if element != '']
        card = ffdeck.get_card_by_serial_number(data[1])
        if card is None:
            await client.send_message(message.channel, 'could not find card for {0}')
        else:
            embed = formatter.format_card(card)
            await client.send_message(message.channel, embed=embed)

    if message.content.startswith(config.PREFIX + 'search'):
        data = message.content.split(' ')
        data = [element for element in data if element != '']
        possible_cards = ffdeck.get_cards_by_name(data[1])
        embed = formatter.format_card_name_list(possible_cards)
        await client.send_message(message.channel, embed=embed)

    # stuff anyone has access to
    if message.content.startswith(config.PREFIX + 'deck'):
            data = message.content.split(' ')  # get last 16 digits
            data = ffdeck.get_deck_by_url(url=data[1])
            if data is None:
                await client.send_message(message.channel, 'could not find deck')
            else:
                embed = formatter.format_deck(data=data)
                await client.send_message(message.channel, embed=embed)

    if message.content.startswith(config.PREFIX + 'help'):
        embed = formatter.format_help_info()
        await client.send_message(message.channel, embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.TOKEN)
