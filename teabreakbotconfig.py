import ConfigParser
import os

def read_config():
    filenames = ['/etc/teabreakbot.cfg',
            os.path.expanduser('~/.teabreakbot.cfg'),
            'teabreakbot.cfg']

    config=ConfigParser.SafeConfigParser()

    config.add_section("irc")
    config.set("irc","host","localhost")
    config.set("irc","port","6667")

    config.add_section("twitter")
    config.set("twitter","enabled","false")
    config.set("twitter","consumer_key","")
    config.set("twitter","consumer_secret","")
    config.set("twitter","access_key","")
    config.set("twitter","access_secret","")

    config.read(filenames)
    return config

