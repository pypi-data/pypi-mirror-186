NF_VIDEO_PLAYER_LINK='http://213.108.4.28/video/player/'



def create_player_link(to_nftv_id) -> str:
    """returns an url of a web player
    
    Arguments:
        to_nftv_id: str| int
            video to get a player for
            a 13 digid video id of Nanofootball video server
            ex. 1669983631719
            """
    return f'{NF_VIDEO_PLAYER_LINK}{to_nftv_id}'