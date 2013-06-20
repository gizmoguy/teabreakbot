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
    config.set("irc","chan","#teabreakbot")
    config.set("irc","nick","teabreakbot")

    config.add_section("twitter")
    config.set("twitter","enabled","false")
    config.set("twitter","screen_name","")
    config.set("twitter","consumer_key","")
    config.set("twitter","consumer_secret","")
    config.set("twitter","access_key","")
    config.set("twitter","access_secret","")

    config.add_section("log")
    config.set("log", "enabled","false")
    config.set("log", "path", "~/.teabreakbot.log")

    config.add_section("misc")
    config.set("misc","teabreaklength","600")

    config.read(filenames)
    return config

if __name__ == "__main__":
    config = read_config()
    print "Tweet teabreaks: %s" % config.get("twitter","enabled")
    print "Twitter Consumer Key: %s" % config.get("twitter","consumer_key")
    print "Twitter Consumer Secret: %s" % config.get("twitter","consumer_secret")
    print "Twitter Access Key: %s" % config.get("twitter","access_key")
    print "Twitter Access Secret: %s" % config.get("twitter","access_secret")
    if config.getboolean("log","enabled"):
        print "Logging to: %s" % config.get("log", "path")

# vim: set smartindent shiftwidth=4 tabstop=4 softtabstop=4 expandtab :
