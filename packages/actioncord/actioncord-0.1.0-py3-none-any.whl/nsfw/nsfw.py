import requests
import json

# I was basically getting bored and so I created this API wrapper. 
# I don't take any guarentee of it working in the future. Since the 
# endpoints change over time. Care to cope with it. You can fork the 
# project and DIY it according to what API endpoints say. Thank You !




# Declaring a base url for scrapping !
BASE_URL="https://purrbot.site/api"

# Declaring a common returned-but-not-working API response.  
GLOBAL_ERROR_RESP= str("API didn't repond correctly, might be a problem with the server side. Kindly try again later.")


# Declaring a common request API response.  

GLOBAL_ERROR_RESP= str("API didn't repond correctly, might be a problem with the server side. Kindly try again later.")

"""
    Example with Hikari and LightBulb as command handlers given below!
    A wrapper library developed by:
    [@halfstackpgr](https://www.github.com/halfstackpgr)
    This is an API wrapper which uses endpoints of [Purr Bot](https://purrbot.site)
    to wrap up some GIFs and other images that contain SFW and NSFW materials. 

    This class from the wrapper is specifically only for "SFW" that is "Safe For Work".

    SFW Sub-Functions Given as Below:
    ----------------------------------------------------------------------------------------
    Usage: 
    ```python
    blushGifUrl=str(actiondiscord.nsfw.blush())
    ```
    ----------------------------------------------------------------------------------------
    ```json
    1. anal= /img/nsfw/anal/gif Returns a randomly selected Anal-Sex Gif
    2. blowjob= /img/nsfw/blowjob/gif Returns a randomly selected blowjob Gif.
    3. cumshot= /img/nsfw/cum/gif Returns a randomly selected cumming Gif.
    4. fuck= /img/nsfw/fuck/gif Returns a randomly selected Sex Gif.
    5. neko= /img/nsfw/neko/gif Returns a randomly selected NSFW Neko (Cat Girl) Gif or Image.
    6. lickpussy= /img/nsfw/pussylick/gif Returns a randomly selected pussy licking Gif.
    7. solosex= /img/nsfw/solo/gif Returns a randomly selected Gif of a female masturbating.
    8. female3some= /img/nsfw/threesome_fff/gif Returns a randomly selected Threesome Gif (Females only).
    9. twoFoneMthreesome= /img/nsfw/threesome_ffm/gif Returns a randomly selected Threesome Gif (2 Females, 1 Male).
    10. oneFtwoMthreesome= /img/nsfw/threesome_mmf/gif Returns a randomly selected Threesome Gif (1 Female, 2 Males).
    11. yaoi= /img/nsfw/yaoi/gif Returns a randomly selected Yaoi (Gay Hentai) Gif.
    12. yuri= /img/nsfw/yuri/gif Returns a randomly selected Yuri (Lesbian Hentai) Gif.
    ```
    ---------------------------------------------------------------------
    ___________________________________________________________________________________________________
    ```python
    # Importing Libs
    import lightbulb
    import hikari 
    import actioncord
    #Setting Up a bot instance.
    bot=hikari.GatewayBot(tokken="...")
    # Making a hug command.
    @bot.command
    @lightbulb.option('reason', "Reason to Fuck ", type=str,modifier=lightbulb.OptionModifier.CONSUME_REST, required=False, default=f"please dont leave me.. keep holding...")
    @lightbulb.option('user', "User to Fuck ", type=hikari.Member)
    @lightbulb.command("fuck", "Hugs the mentioned user.")
    @lightbulb.implements(lightbulb.SlashSubCommand, lightbulb.PrefixSubCommand)
    async def huganime(ctx):
        author_member = ctx.get_guild().get_member(ctx.author)
        nickname_of_author = author_member.display_name
        if isinstance(ctx, lightbulb.PrefixContext):
            await ctx.event.message.delete()
        anacEmbed=hikari.Embed(title=None, description=f"{ctx.options.reason}", timestamp=datetime.datetime.now().astimezone())
        # Use it this way:
        anacEmbed.set_image(str(actioncord.nsfw.fuck()))
        # Easy ?
        webhook = await ctx.app.rest.create_webhook(channel=ctx.channel_id, name=nickname_of_author)
        await webhook.execute(content=f"{ctx.options.user.mention}", embed=anacEmbed,avatar_url=ctx.author.avatar_url, user_mentions=True, role_mentions=True, mentions_everyone=True)
        await ctx.app.rest.delete_webhook(webhook=webhook)
    bot.run()
    ___________________________________________________________________________________________________
    ```

"""

def anal() -> None:
    """
    /img/nsfw/anal/gif
    Returns a randomly selected Anal-Sex Gif
    """
    url=BASE_URL+"/img/nsfw/anal/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else:
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def blowjob() -> None:
    """
    /img/nsfw/blowjob/gif
    Returns a randomly selected blowjob Gif.
    """
    url=BASE_URL+"/img/nsfw/blowjob/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def cumshot() -> None:
    """
    /img/nsfw/cum/gif
    Returns a randomly selected cumming Gif.
    """
    url=BASE_URL+"/img/nsfw/cum/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def fuck() -> None:
    """
    /img/nsfw/fuck/gif
    Returns a randomly selected Sex Gif.
    """
    url=BASE_URL+"/img/nsfw/fuck/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def  neko() -> None:
    """
    /img/nsfw/neko/gif
    Returns a randomly selected NSFW Neko (Cat Girl) Gif
    """
    url=BASE_URL+"/img/nsfw/neko/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def lickpussy() -> None:
    """
    /img/nsfw/pussylick/gif
    Returns a randomly selected pussy licking Gif.
    """
    url=BASE_URL+"/img/nsfw/pussylick/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
                print(GLOBAL_ERROR_RESP)
                return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def solosex() -> None:
    """
    /img/nsfw/solo/gif
    Returns a randomly selected Gif of a female masturbating.
    """
    url=BASE_URL+"/img/nsfw/solo/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def FemaleThreeSome() -> None:
    """
    /img/nsfw/threesome_fff/gif
    Returns a randomly selected Threesome Gif (Females only).
    """
    url=BASE_URL+"/img/nsfw/threesome_fff/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def twoFoneMthreesome() -> None:
    """
    /img/nsfw/threesome_ffm/gif
    Returns a randomly selected Threesome Gif (2 Females, 1 Male).
    """
    url=BASE_URL+"/img/nsfw/threesome_ffm/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def oneFtwoMthreesome() -> None:
    """
    /img/nsfw/threesome_mmf/gif
    Returns a randomly selected Threesome Gif (1 Female, 2 Males).
    """
    url=BASE_URL+"/img/nsfw/threesome_mmf/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP
def lesbianSex() -> None:
        """
        /img/nsfw/yuri/gif
        Returns a randomly selected Yuri (Lesbian Hentai) Gif.
        """
        url=BASE_URL+"/img/nsfw/yuri/gif"
        responseRaw=requests.get(url=url)
        response=responseRaw.json()
        if responseRaw.status_code==200:
            if str(response["error"])== "False":
                return str(response["link"])  
            else: 
                print(GLOBAL_ERROR_RESP)
                return GLOBAL_ERROR_RESP
        else:
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
def gaySex() -> None:
    """
    /img/nsfw/yaoi/gif
    Returns a randomly selected Yaoi (Gay Hentai) Gif.
    """
    url=BASE_URL+"/img/nsfw/yaoi/gif"
    responseRaw=requests.get(url=url)
    response=responseRaw.json()
    if responseRaw.status_code==200:
        if str(response["error"])== "False":
            return str(response["link"])  
        else: 
            print(GLOBAL_ERROR_RESP)
            return GLOBAL_ERROR_RESP
    else:
        print(GLOBAL_ERROR_RESP)
        return GLOBAL_ERROR_RESP