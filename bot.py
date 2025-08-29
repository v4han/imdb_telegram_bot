from telebot import TeleBot, types
import parser
from dotenv import load_dotenv
import os


load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = TeleBot(token=TOKEN)


MOVIE_MAP = {}


@bot.message_handler(commands=['start'])
def run_bot(message):
    """Handles the /start command and shows main menu."""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton("🎬 Movies", callback_data="movies"))
    keyboard.row(types.InlineKeyboardButton("📺 TV Shows", callback_data="tv"))

    bot.send_message(
        message.chat.id,
        "Welcome! Choose between two options",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    """Handles all callback queries from inline buttons."""
    global MOVIE_MAP

    # Movies menu
    if call.data == "movies":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton("🔥 Most Popular Now", callback_data="movies_popular"))
        keyboard.row(types.InlineKeyboardButton("🏆 Most Popular All Time", callback_data="movies_all_time"))
        keyboard.row(types.InlineKeyboardButton("⬅️ Back", callback_data="main_menu"))

        bot.send_message(call.message.chat.id, "Choose a Movies option:", reply_markup=keyboard)

    elif call.data == "movies_popular":
        MOVIE_MAP.clear()
        movies = parser.movies_most_popular()
        keyboard = types.InlineKeyboardMarkup()

        for i, movie in enumerate(movies):
            MOVIE_MAP[str(i)] = movie.split(". ", 1)[1] if ". " in movie else movie
            keyboard.row(
                types.InlineKeyboardButton(MOVIE_MAP[str(i)], callback_data=f"movie|{i}|popular_now")
            )

        keyboard.row(types.InlineKeyboardButton("⬅️ Back", callback_data="movies"))
        bot.send_message(call.message.chat.id, "🔥 Most Popular Movies Now:", reply_markup=keyboard)

    elif call.data == "movies_all_time":
        MOVIE_MAP.clear()
        movies = parser.most_popular_movies_of_all_time()
        keyboard = types.InlineKeyboardMarkup()

        for i, movie in enumerate(movies):
            MOVIE_MAP[str(i)] = movie.split(". ", 1)[1] if ". " in movie else movie
            keyboard.row(
                types.InlineKeyboardButton(MOVIE_MAP[str(i)], callback_data=f"movie|{i}|all_time")
            )

        keyboard.row(types.InlineKeyboardButton("⬅️ Back", callback_data="movies"))
        bot.send_message(call.message.chat.id, "🏆 Most Popular Movies of All Time:", reply_markup=keyboard)

    elif call.data.startswith("movie|"):
        _, index, list_type = call.data.split("|")

        if list_type == "popular_now":
            url = "https://www.imdb.com/chart/moviemeter/?ref_=chttvtp_nv_menu"
            previous_callback = "movies"
        else:
            url = "https://www.imdb.com/chart/top/?ref_=chttp_nv_menu"
            previous_callback = "movies"

        description = parser.get_movie_description(int(index), url)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("⬅️ Back", callback_data=previous_callback))

        bot.send_message(call.message.chat.id, description, reply_markup=keyboard)

    # TV Shows menu
    elif call.data == "tv":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton("🔥 Most Popular Now", callback_data="tv_popular"))
        keyboard.row(types.InlineKeyboardButton("🏆 Most Popular All Time", callback_data="tv_all_time"))
        keyboard.row(types.InlineKeyboardButton("⬅️ Back", callback_data="main_menu"))

        bot.send_message(call.message.chat.id, "Choose a TV Shows option:", reply_markup=keyboard)

    elif call.data == "tv_popular":
        MOVIE_MAP.clear()
        shows = parser.tv_shows_most_popular()
        keyboard = types.InlineKeyboardMarkup()

        for i, show in enumerate(shows):
            MOVIE_MAP[str(i)] = show.split(". ", 1)[1] if ". " in show else show
            keyboard.row(
                types.InlineKeyboardButton(MOVIE_MAP[str(i)], callback_data=f"tv|{i}|popular_now")
            )

        keyboard.row(types.InlineKeyboardButton("⬅️ Back", callback_data="tv"))
        bot.send_message(call.message.chat.id, "🔥 Most Popular TV Shows Now:", reply_markup=keyboard)

    elif call.data == "tv_all_time":
        MOVIE_MAP.clear()
        shows = parser.tv_shows_most_popular_all_time()
        keyboard = types.InlineKeyboardMarkup()

        for i, show in enumerate(shows):
            MOVIE_MAP[str(i)] = show.split(". ", 1)[1] if ". " in show else show
            keyboard.row(
                types.InlineKeyboardButton(MOVIE_MAP[str(i)], callback_data=f"tv|{i}|all_time")
            )

        keyboard.row(types.InlineKeyboardButton("⬅️ Back", callback_data="tv"))
        bot.send_message(call.message.chat.id, "🏆 Most Popular TV Shows All Time:", reply_markup=keyboard)

    elif call.data.startswith("tv|"):
        _, index, list_type = call.data.split("|")

        if list_type == "popular_now":
            url = "https://www.imdb.com/chart/tvmeter/?ref_=chttvtp_nv_menu"
            previous_callback = "tv"
        else:
            url = "https://www.imdb.com/chart/toptv/?ref_=chtmvm_nv_menu"
            previous_callback = "tv"

        description = parser.get_tv_description(int(index), url)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("⬅️ Back", callback_data=previous_callback))

        bot.send_message(call.message.chat.id, description, reply_markup=keyboard)

    # Back to main menu
    elif call.data == "main_menu":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton("🎬 Movies", callback_data="movies"))
        keyboard.row(types.InlineKeyboardButton("📺 TV Shows", callback_data="tv"))

        bot.send_message(
            call.message.chat.id,
            "Welcome! WatchWise finds the top 10 most watched movies and TV shows relevant right now and the best overall lists, updated by IMDb.",
            reply_markup=keyboard
        )


bot.polling()
