class Config(object):
    # Server configuration
    SERVER = 'irc.gamesurge.net'
    PORT = 6667
    SSL = False
    TIMEOUT = 3000
    DEBUG = True

    NICK = 'DiznatchIsAFoolBot'
    REALNAME = 'https://github.com/buttscicles/RedditBot'
    CHANNELS = ['#pveseneca']

    ADMINS = ['*!*mattman00@mattman00000.user.gamesurge']

    REJOIN_KICKERS = ['SpamServ']

    # Plugin specific configs

    # This needs to a valid SQLAlchemy connection string
    # Find one for your preferred db + driver here:
    # http://docs.sqlalchemy.org/en/rel_0_7/core/engines.html
    TELL_DB = 'sqlite:///{0}.{1}.db'.format(NICK, SERVER)

    REDDIT_BLACKLIST = []
    TWITTER_BLACKLIST = []
    COUNTDOWN_CHANNELS = ['#countdown']
    SNOOP_CHANNEL = ''

    TWITTER_UNSHORTEN_LIMIT = 45
    TWITTER_CONSUMER_KEY = ''
    TWITTER_CONSUMER_SECRET = ''
    TWITTER_ACCESS_KEY = ''
    TWITTER_ACCESS_SECRET = ''

    LASTFM_API_KEY = ''
    MCBOUNCER_KEY = ''
    WOLFRAMALPHA_KEY = 'JW9THU-PRPUQ839L4'
    GOOGLESEARCH_KEY = ''

    MINECRAFT_USER = ''
    MINECRAFT_PASSWORD = ''
    MINECRAFT_SHOW_SERVER_VER = False
    MINECRAFT_SERVER_LIST = [
        ('c.nerd.nu', 25565, ['c', 'creative']),
        ('p.nerd.nu', 25565, ['p', 'pve']),
        ('s.nerd.nu', 25565, ['s', 'survival', 'pvp']),
        ('chaos.nerd.nu', 25565, ['x', 'chaos']),
        ('event.nerd.nu', 25565, ['e', 'event', 'ctf']),
        ('mumble.nerd.nu', 6162, ['m', 'mumble', 'voice']),
        ('mc.senecan.net', 25599, ['sps', 'seneca', 'senecaplanningserver', 'seneca planning server'])
    ]

    ENABLED_SERVERS = 'c,p,s,sps'

    BITLY_KEY = ''
    BITLY_USER = ''
