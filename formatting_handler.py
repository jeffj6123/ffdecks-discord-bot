from discord import embeds
import config


def format_deck(data):
    embed = embeds.Embed(title="Deck name", description=data['name'], color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value=data['creator'])
    embed.add_field(name="Archetype", value=data['archetype'])
    embed.add_field(name="views", value=data['views'])

    cards = ''
    for card in data['cards']:
        cards += card['card']['name'] + '(' + card['card']['serial_number'] + ') - ' + str(card['quantity']) + '\n'
    embed.add_field(name="cards", value=cards, inline=False)
    description = data['description']
    if len(description) == 0:
        description = 'No description'
    embed.add_field(name="description", value=description, inline=False)
    embed.add_field(name="comments", value=str(len(data['comments'])) + ' comments', inline=False)

    if data['tournament_info']:
        embed.add_field(name="played in", value=data['tournament_info']['name'])
        embed.add_field(name="played by", value=data['tournament_info']['player'])
        embed.add_field(name="placed", value=data['tournament_info']['rank'])

    return embed


def format_card(data):
    embed = embeds.Embed(title="Name", description=data['name'], color=0xeee657)
    embed.add_field(name="Cost", value=data['cost'])
    embed.add_field(name="Element", value=data['element'])
    if data['power']:
        embed.add_field(name="Power", value=data['power'])
    embed.add_field(name="EX-Burst", value=data['is_ex_burst'])
    embed.add_field(name="Multi-Playable", value=data['is_multi_playable'])
    embed.add_field(name="Category", value=data['category'])
    embed.add_field(name="Job", value=data['job'])

    embed.add_field(name="Ability Text", value=data['abilities'])
    embed.add_field(name="Rarity", value=data['rarity'])
    embed.add_field(name="Serial Number", value=data['serial_number'])

    embed.set_image(url=data['image'])
    return embed


def format_card_name_list(data):
    card_list = '\n'.join(data)
    embed = embeds.Embed(title="Search Results", description=card_list, color=0xeee657)
    return embed


def format_help_info():
    embed = embeds.Embed(title="ffdecks helper bot", description="A bot that can link cards and decks", color=0xeee657)

    embed.add_field(name=config.PREFIX + "card <serial number>", value="returns a card by serial number i.e --card -s 1-001",
                    inline=False)
    embed.add_field(name=config.PREFIX + "search <name>",
                    value="returns a list of card and their serial number i.e --search Auron would return Auron - 1-001 Auron - 1-002",
                    inline=False)
    embed.add_field(name=config.PREFIX + "deck <deck url>",
                    value="returns information about a deck on ffdecks i.e --getdeck https://ffdecks.com/deck/6443155092144128 ",
                    inline=False)
    return embed
