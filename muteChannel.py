import requests
import time

token = "CHANGE THIS" #Your account token. Guide Here https://www.youtube.com/watch?v=YEgFvgg7ZPI&ab_channel=GaugingGadgets
ServerID = "CHANGE THIS" #Channel's Id you want to mute. Guide Here https://www.youtube.com/watch?v=NLWtSHWKbAI&ab_channel=GaugingGadgetsGaugingGadgetsVerified

minutes = 20 # Change this to the minutes that the server will stay muted
minutes = minutes * 60 #This turns the previous varible to minutes by multiplying by 60.

def muteChannel(token, ServerID):
    '''
    This method sends a patch request do discord to mute notifications from a server.
    :param token: Your account authorization token
    :param ServerID: The Id of the server you want to mute.
    :return: The response of the request.
    '''
    url = "https://discord.com:443/api/v9/users/@me/guilds/" + ServerID + "/settings"
    headers = {"Connection": "close", "Authorization": token, "Accept-Language": "en-US",
                     "sec-ch-ua-mobile": "?0",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                     "Content-Type": "application/json", "Accept": "*/*", "Origin": "https://discord.com",
                     "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
                     "Accept-Encoding": "gzip, deflate"}
    json = {"muted": True}
    r1 = requests.patch(url, headers=headers, json=json)
    print(r1)

def unmuteChannel(token, ServerID):
    '''
    This method sends a patch request do discord to unmute notifications from a server.
    :param token: Your account authorization token
    :param ServerID: The Id of the server you want to mute.
    :return: The response of the request.
    '''
    url = "https://discord.com:443/api/v9/users/@me/guilds/" + ServerID + "/settings"
    headers = {"Connection": "close", "Authorization": token, "Accept-Language": "en-US",
                     "sec-ch-ua-mobile": "?0",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                     "Content-Type": "application/json", "Accept": "*/*", "Origin": "https://discord.com",
                     "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
                     "Accept-Encoding": "gzip, deflate"}
    json = {"muted": False}
    r2 = requests.patch(url, headers=headers, json=json)
    print(r2)

def main(token, ServerID, minutes):
    '''
    This method runs the muteChannel method and waits the minutes amount until it unmutes the channel again by running unmuteChannel
    :param token: Your account authorization token
    :param ServerID: The Id of the server you want to mute.
    :param minutes: Amount of time as integer that server will be muted.
    '''
    muteChannel(token, ServerID)
    time.sleep(minutes)
    unmuteChannel(token, ServerID)

main(token, ServerID, minutes)