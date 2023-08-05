from helpers import functions


def get_followers(username:str):
    followers = functions.followers(username=username)
    return followers