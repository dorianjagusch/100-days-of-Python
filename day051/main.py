from internet_speed_twitter_bot import InternetSpeedTwitterBot, PROMISED_UP, PROMISED_DOWN

bot = InternetSpeedTwitterBot()
speeds = bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()
