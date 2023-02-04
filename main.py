import discord
import random

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connected as {client.user}')

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
    if message.author == client.user:
        return
    if channel == "general":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "what is love?" or user_message.lower() == "what is love":
            await message.channel.send(f"""Love can be thought of as a combination of biological, psychological, and social factors that influence our feelings, thoughts,
and behaviors towards others. At the biological level, love is associated with changes in the brain, such as increased activity in regions that are associated 
with reward and pleasure, and increased release of neurotransmitters 
such as dopamine, oxytocin, and serotonin. These changes can influence our feelings of euphoria, attachment, and bonding towards others.
From a psychological perspective, love can involve feelings of attachment, intimacy, and commitment, as well as various behaviors and cognitions, 
such as a desire to be close to the loved one, 
protect and care for them, and prioritize their needs and well-being over one\'s own. 
Finally, love is also a socially constructed concept that is influenced by cultural and societal norms, beliefs, and expectations. 
The way love is experienced and expressed can vary greatly 
across individuals and cultures, and is shaped by factors such as gender, ethnicity, religion, and social and historical context.""")
        elif user_message.lower() == "what are feelings?" or user_message.lower() == "what are feelings":
            await message.channel.send(f"""Feelings are complex physiological and psychological experiences that arise from the interplay of several factors, 
including cognitive processes, cultural and social influences, and neural and hormonal activity.
In the brain, feelings are associated with specific patterns of neural activity, which are triggered by specific stimuli and 
can result in the release of hormones and neurotransmitters, such as dopamine, 
serotonin, and oxytocin, that influence our emotional and physiological responses. For example, a stimulus that elicits a 
positive feeling may cause the release of dopamine, a neurotransmitter associated with pleasure and reward, while a stimulus 
that elicits a negative feeling may cause the release of cortisol, a hormone associated with stress and anxiety.
Overall, feelings are thought to be a result of the integration of multiple neural and physiological systems, which work
together to produce our subjective emotional experiences. Understanding the underlying mechanisms of feelings and emotions 
continues to be an active area of research in psychology, neuroscience, and biology.""")
        elif user_message.lower() == "pizza":
            await message.channel.send(f'PAUSEEEE, PLZ WAIT 4 HOURS, PIZZA 4 FORMAGGI WITH CHAMPIGNONES')
TOKEN = 'ENTER YOUR TOKEN'
client.run(TOKEN)