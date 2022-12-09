import discord
from discord.ext import commands
from config import config

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user} запущен и готов к работе!')


@bot.event
async def on_message(message):
    # если сообщение от бота - игнорируем
    if message.author.bot:
        return
    # проверяем, является ли сообщение командой
    await bot.process_commands(message)


@bot.command(name='join', aliases=['summon'])  # создаю команду подключения к голосовому
async def _join(ctx, *,
                channel: discord.VoiceChannel = None):  # TAKING ARGUMENT CHANNEL SO People CAN MAKE THE BOT JOIN A VOICE CHANNEL THAT THEY ARE NOT IN
    """Подключение к голосовому чату."""

    destination = channel if channel else ctx.author.voice.channel  # CHOOSING THE DESTINATION, MIGHT BE THE REQUESTED ONE, BUT IF NOT THEN WE PICK AUTHORS VOICE CHANNEL

    if ctx.voice_client:  # проверка того, проигрывает ли бот что-то
        await ctx.voice_state.voice.move_to(
            destination)  # если бот проигрывает что-то направляем его
        return

    await destination.connect()  # CONNECTING TO DESTINATION
    await ctx.send(f"Подключен к голосовому каналу: {destination.name} ({destination.id}).")


@bot.command(aliases=['test', 'тест', 'тестовая_команда', 'test_command'])
async def test_(ctx):
    # список свойств и методов контекста можно найти в документации по запросу context
    await ctx.send('Успешный тест!')


@bot.command()
async def join_voice(self, ctx):
    channel = ctx.author.voice.channel
    print(channel.id)
    await channel.connect()


@bot.command()
async def get_values(ctx, number: int, boolean: bool, member: discord.Member):
    print(f'number = {number}, type = {type(number)}')
    print(f'boolean = {boolean}, type = {type(boolean)}')
    print(f'member = {member}, type = {type(member)}')


@bot.command()
async def get_text(ctx, first_word, second_word, *, other_text):
    print(f'Первое слово: {first_word}, длина: {len(first_word)}')
    print(f'Второе слово: {second_word}, длина: {len(second_word)}')
    print(f'Остальной текст: {other_text}, длина: {len(other_text)}')


bot.run(config['token'])
