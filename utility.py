from discord import Embed


def error_embed(title: str = "", message: str = ""):
    return Embed(title=title, description=message, color=0xFC5165)


def default_embed(title: str = "", message: str = ""):
    return Embed(title=title, description=message, color=0xA68BD3)
