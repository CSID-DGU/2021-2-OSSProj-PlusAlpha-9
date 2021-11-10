import enum

class Images(enum.Enum):
    start = "./Image/StartImage.png"
    how_to_play = "./Image/howtoplay.png"

    character_car = "./Image/DesrtCar.png"
    char_battleship = "./Image/bgbattleship.png"
    char_speedship= "./Image/bgspeedship.png"
    char_medship = "./Image/medfrighter.png"

    # background_desert = "./Image/DESERT.jpeg"
    background_desert = "./Image/DESERT_modified_v3.jpg"
    background_antarctic = "./Image/Antarctic_modified_v1.jpg"
    enemy_scrophion = "./Image/Scorphion.png"
    enemy_cactus = "./Image/Catus.png"
    missile_missile2 = "./Image/MISSILE_2.png"
    item_powerup = "./Image/powerup.png"

class Sounds(enum.Enum):
    bgm_desert = "./Sound/ariant.mp3"
    bgm_rien = "./Sound/Rien.mp3"
    sfx_weapon1 = "./Sound/weapon-sound4.ogg"
    sfx_weapon2 = "./Sound/weapon-sound8.ogg"
    sfx_weapon3 = "./Sound/weapon-sound9.ogg"
    sfx_weapon4 = "./Sound/weapon-sound16.ogg"
    sfx_gameover = "./Sound/gameover.wav"
    sfx_monster1 = "./Sound/monster-sound7.ogg"
    sfx_penguin = "./Sound/penguin.mp3"
    sfx_present1 = "./Sound/present1.mp3"
    sfx_present2 = "./Sound/present2.mp3"
    sfx_present3 = "./Sound/present3.mp3"
    sfx_present4 = "./Sound/present4.mp3"
    sfx_hit = "./Sound/puck.mp3"

class Fonts(enum.Enum):
    font_default = "./Font/DXHanlgrumStd-Regular.otf"

class Color(enum.Enum):
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
