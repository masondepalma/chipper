# This bot requires the 'message_content' intent.
import discord,logging,os
import utils.sendSMS as sendSMS

#discord bot initalization
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#logging setup. 
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)



config = {'channel':''}

@client.event
async def on_ready():
    #clear terminal and chipper again.
    os.system('clear')
    print('''
    ________  __________  ____  __________ 
  / ____/ / / /  _/ __ \/ __ \/ ____/ __ \
 / /   / /_/ // // /_/ / /_/ / __/ / /_/ /

/ /___/ __  // // ____/ ____/ /___/ _, _/ 
\____/_/ /_/___/_/   /_/   /_____/_/ |_|  
''')
    logging.info(f'We have logged in as {client.user} | Now monitoring for new tweets.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.channel.id) == config['channel']:
        logging.info('New tweet detected')
        chipCode = str(str(str(message.content).split("Text")[1]).split("to")[0]).strip()
        logging.info(f'Text Code found. -- {chipCode}')
        sendSMS.send(chipCode)
        logging.info('Attempt to send code to `888222` completed.')
        await message.channel.send('Sent code!')




#before run client. need to have CLI to start the bot. 
def startup():
    #Collect Token and Channel to monitor. 
    print('''
    ________  __________  ____  __________ 
  / ____/ / / /  _/ __ \/ __ \/ ____/ __ \
 / /   / /_/ // // /_/ / /_/ / __/ / /_/ /

/ /___/ __  // // ____/ ____/ /___/ _, _/ 
\____/_/ /_/___/_/   /_/   /_____/_/ |_|  
                                          

Welcome to CHIPPER bot. This is only meant to run on MAC machines. 
    ''')
    token = str(input('Enter discord bot token:'))
    channelID = str(input('Enter the ID of the discord channel to monitor:'))
    config['channel'] = channelID
    start = input('Click Enter to start monitoring.')
    startBot(token)

def startBot(token):
    client.run(f'{token}')


if __name__ == '__main__':
    startup()