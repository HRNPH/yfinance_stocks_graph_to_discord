import discord
from data_visualization import get_stock_price_history_and_plot_graph as get_Stock
from data_visualization import delete_graph_pic as del_pic
from data_visualization import save_pic
from readable_table import print_info
from readable_table import print_table

client = discord.Client()


@client.event
async def on_ready():
  print('ล๊อกอินในชื่อ{0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        lowercasemsg = message.content.lower()
        splitmsg = lowercasemsg.split(' ')

        if (('makima' in splitmsg[0]) or 'มากิมะ' in (splitmsg[0])):
            #main function

            if (len(splitmsg) > 1):
                if (splitmsg[1] == ('price') or splitmsg[1] == ('ราคา')):
                    try:
                        get_Stock(splitmsg[2], splitmsg[3], splitmsg[4])
                        await message.channel.send(
                          splitmsg[1]+splitmsg[2] + splitmsg[3]+splitmsg[4])
                        await message.channel.send(file=discord.File('image1.png'))

                    except ValueError:
                        message.channel.send('wrong input')
                        message.channel.send('asshole...')

              #bot run here
client.run('YourTokens')
