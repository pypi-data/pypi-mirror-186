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
class sfw:
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
    blushGifUrl=str(actiondiscord.sfw.blush())
    ```
    ----------------------------------------------------------------------------------------
    ```json
    1. welcomebgimage= Returns a randomly selected Welcome Background Image.
    2. bite=  Returns a randomly selected Bite Gif.
    3. blush= Returns a randomly selected Blush Gif.
    4. comfy= Returns a randomly selected Comfy Gif.
    5. cry= Returns a randomly selected Cry Gif.
    6. cuddle= Returns a randomly selected Cuddle Gif.
    7. dance= Returns a randomly selected Dance Gif.
    8. eevee= Returns a randomly selected Eevee Gif.
    9. feed= Returns a randomly selected Feeding Gif.
    10 fluff= Returns a randomly selected Blush Gif.
    11 holo= Returns a randomly selected Image of Holo from 'Spice and Wolf'
    12 hug= Returns a randomly selected hugging Gif.
    13 welcomeicon= Returns a randomly selected Welcome Icon.
    14 kiss= Returns a randomly selected kissing Gif.
    15 kitsune= Returns a randomly selected Kitsune (Fox Girl) Image.
    16 lick= Returns a randomly selected licking Gif
    17 neko= Returns a randomly selected Neko (Cat Girl) Gif or Image.
    18 okami= Returns a randomly selected Okami (Wolf Girl) Image.
    19 pat= Returns a randomly selected patting Gif.
    20 poke= Returns a randomly selected poking Gif.
    21 senko= Returns a randomly selected Image of Senko-San.
    22 shiro= Returns a randomly selected Image of Shiro.
    23 slap= Returns a randomly selected slapping Gif.
    24 smile= Returns a randomly selected smiling Gif.
    25 tail= Returns a randomly selected tail wagging Gif.
    26 tickle= Returns a randomly selected tickling Gif.
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
    @lightbulb.option('reason', "Reason to Hug ", type=str,modifier=lightbulb.OptionModifier.CONSUME_REST, required=False, default=f"please dont leave me.. keep holding...")
    @lightbulb.option('user', "User to Hug ", type=hikari.Member)
    @lightbulb.command("hug", "Hugs the mentioned user.")
    @lightbulb.implements(lightbulb.SlashSubCommand, lightbulb.PrefixSubCommand)
    async def huganime(ctx):
        author_member = ctx.get_guild().get_member(ctx.author)
        nickname_of_author = author_member.display_name
        if isinstance(ctx, lightbulb.PrefixContext):
            await ctx.event.message.delete()
        anacEmbed=hikari.Embed(title=None, description=f"{ctx.options.reason}", timestamp=datetime.datetime.now().astimezone())
        # Use it this way:
        anacEmbed.set_image(str(actioncord.sfw.blush()))
        # Easy ?
        webhook = await ctx.app.rest.create_webhook(channel=ctx.channel_id, name=nickname_of_author)
        await webhook.execute(content=f"{ctx.options.user.mention}", embed=anacEmbed,avatar_url=ctx.author.avatar_url, user_mentions=True, role_mentions=True, mentions_everyone=True)
        await ctx.app.rest.delete_webhook(webhook=webhook)
    bot.run()
    ___________________________________________________________________________________________________
    ```

    """
    def welcomebgimage() -> None:
        """
        /img/sfw/background/img
        Returns a randomly selected Welcome Background Image.
        """
        url=BASE_URL+"/img/sfw/background/img"
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
    def bite() -> None:
        """
        /img/sfw/bite/gif
        Returns a randomly selected Bite Gif.
        """
        url=BASE_URL+"/img/sfw/bite/gif"
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
    def blush() -> None:
        """
        /img/sfw/blush/gif
        Returns a randomly selected Blush Gif.
        """
        url=BASE_URL+"/img/sfw/blush/gif"
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
    def comfy() -> None:
        """
        /img/sfw/comfy/gif
        Returns a randomly selected Comfy Gif.
        """
        url=BASE_URL+"/img/sfw/comfy/gif"
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
    def cry() -> None:
        """
        /img/sfw/cry/gif
        Returns a randomly selected Cry Gif.
        """
        url=BASE_URL+"/img/sfw/cry/gif"
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
    def cuddle() -> None:
        """
        /img/sfw/cuddle/gif
        Returns a randomly selected Cuddle Gif.
        """
        url=BASE_URL+"/img/sfw/cuddle/gif"
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
    def dance() -> None:
        """
        /img/sfw/dance/gif
        Returns a randomly selected Dance Gif.
        """
        url=BASE_URL+"/img/sfw/dance/gif"
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
    def eevee() -> None:
        """
        /img/sfw/eevee/gif
        Returns a randomly selected Eevee Gif.
        """
        url=BASE_URL+"/img/sfw/eevee/gif"
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
    def feed() -> None:
        """
        /img/sfw/feed/gif
        Returns a randomly selected Feeding Gif.
        """
        url=BASE_URL+"/img/sfw/feed/gif"
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
    def fluff() -> None:
        """
        /img/sfw/fluff/gif
        Returns a randomly selected Fluff Gif.
        """
        url=BASE_URL+"/img/sfw/fluff/gif"
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
    def hug() -> None:
        """
        /img/sfw/hug/gif
        Returns a randomly selected Hug Gif.
        """
        url=BASE_URL+"/img/sfw/hug/gif"
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
    def kiss() -> None:
        """
        /img/sfw/kiss/gif
        Returns a randomly selected Kiss Gif.
        """
        url=BASE_URL+"/img/sfw/kiss/gif"
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
    def kitsune() -> None:
        """
        /img/sfw/kitsune/img
        Returns a randomly selected Kitsune Gif.
        """
        url=BASE_URL+"/img/sfw/kitsune/img"
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
    def neko() -> None:
        """
        /img/sfw/neko/gif
        Returns a randomly selected Neko Gif.
        """
        url=BASE_URL+"/img/sfw/neko/gif"
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

    def okami() -> None:
        """
        /img/sfw/okami/img
        Returns a randomly selected Okami Image.
        """
        url=BASE_URL+"/img/sfw/okami/img"
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
    def pat() -> None:
        """
        /img/sfw/pat/gif
        Returns a randomly selected Patting Gif.
        """
        url=BASE_URL+"/img/sfw/pat/gif"
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
    def poke() -> None:
        """
        /img/sfw/poke/gif
        Returns a randomly selected Poking Gif.
        """
        url=BASE_URL+"/img/sfw/poke/gif"
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
    def senko() -> None:
        """
        /img/sfw/senko/img
        Returns a randomly selected senko Image.
        """
        url=BASE_URL+"/img/sfw/senko/img"
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
    def shiro() -> None:
        """
        /img/sfw/shiro/img
        Returns a randomly selected shiro Gif.
        """
        url=BASE_URL+"/img/sfw/shiro/img"
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
    def slap() -> None:
        """
        /img/sfw/slap/gif
        Returns a randomly selected slap Gif.
        """
        url=BASE_URL+"/img/sfw/slap/gifs"
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
    def smile() -> None:
        """
        /img/sfw/smile/gif
        Returns a randomly selected smiling Gif.
        """
        url=BASE_URL+"/img/sfw/smile/gif"
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
    def tail() -> None:
        """
        /img/sfw/tail/gif
        Returns a randomly selected tailing Gif.
        """
        url=BASE_URL+"/img/sfw/tail/gif"
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
    def tail() -> None:
        """
        /img/sfw/tickle/gif
        Returns a randomly selected Tickling Gif.
        """
        url=BASE_URL+"/img/sfw/tickle/gif"
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