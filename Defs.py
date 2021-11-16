import enum
import math
from sys import version

class Images(enum.Enum):
    start = "./Image/StartImage.png"
    how_to_play = "./Image/howtoplay.png"

    character_car = "./Image/DesrtCar.png"
    char_battleship = "./Image/bgbattleship.png"
    char_speedship= "./Image/bgspeedship.png"
    char_medship = "./Image/medfrighter.png"

    # background_desert = "./Image/DESERT.jpeg"
    background_desert = "./Image/DESERT_modified_v3.jpg"
    background_antarctic = "./Image/Antarctic_modified_v2.jpg"
    enemy_scrophion = "./Image/scorphion1-1.png"
    enemy_cactus = "./Image/Catus.png"
    missile_missile2 = "./Image/MISSILE_2.png"
    weapon_target_missile = "./Image/Weapon/spaceMissiles_012.png"

    item_bomb = [
        "./Image/Items/Bomb/frame-1.png", 
        "./Image/Items/Bomb/frame-2.png", 
        "./Image/Items/Bomb/frame-3.png", 
        "./Image/Items/Bomb/frame-4.png", 
        "./Image/Items/Bomb/frame-5.png",
        "./Image/Items/Bomb/frame-1.png"
    ]
    item_coin = [
        "./Image/Items/Coin/frame-1.png", 
        "./Image/Items/Coin/frame-2.png", 
        "./Image/Items/Coin/frame-3.png", 
        "./Image/Items/Coin/frame-4.png", 
        "./Image/Items/Coin/frame-5.png",
        "./Image/Items/Coin/frame-1.png"
    ]
    item_health = [
        "./Image/Items/Health/frame-1.png", 
        "./Image/Items/Health/frame-2.png", 
        "./Image/Items/Health/frame-3.png", 
        "./Image/Items/Health/frame-4.png",
        "./Image/Items/Health/frame-1.png"
    ]
    item_powerup = [
        "./Image/Items/PowerUp/frame-1.png", 
        "./Image/Items/PowerUp/frame-2.png", 
        "./Image/Items/PowerUp/frame-3.png", 
        "./Image/Items/PowerUp/frame-4.png", 
        "./Image/Items/PowerUp/frame-5.png",
        "./Image/Items/PowerUp/frame-1.png"
    ]
    item_speedup = [
        "./Image/Items/SpeedUp/frame-1.png", 
        "./Image/Items/SpeedUp/frame-2.png", 
        "./Image/Items/SpeedUp/frame-3.png", 
        "./Image/Items/SpeedUp/frame-4.png", 
        "./Image/Items/SpeedUp/frame-5.png",
        "./Image/Items/SpeedUp/frame-1.png"
    ]

    anim_explosion = [
        "./Image/Effects/Bomb/frame-1.png", 
        "./Image/Effects/Bomb/frame-2.png", 
        "./Image/Effects/Bomb/frame-3.png", 
        "./Image/Effects/Bomb/frame-4.png", 
        "./Image/Effects/Bomb/frame-5.png", 
        "./Image/Effects/Bomb/frame-6.png", 
        "./Image/Effects/Bomb/frame-7.png", 
        "./Image/Effects/Bomb/frame-8.png", 
        "./Image/Effects/Bomb/frame-9.png",
        "./Image/Effects/Bomb/frame-10.png", 
        "./Image/Effects/Bomb/frame-11.png", 
        "./Image/Effects/Bomb/frame-12.png",
        "./Image/Effects/Bomb/frame-13.png", 
        "./Image/Effects/Bomb/frame-14.png", 
        "./Image/Effects/Bomb/frame-15.png"
    ]
    
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

class Misc(enum.Enum):
    org_size = {"x":0, "y":0}
    missile_volume = 0.1
    blinking_step = 0.05
    blinking_speed = 0.2

class Utils():
    @classmethod
    def clamp(cls, val, n_min, n_max):
        return max(n_min, min(val, n_max)) 

    @classmethod
    def get_distance(cls, a, b):
        return math.sqrt((b["x"] - a["x"])**2 + (b["y"] - a["y"])**2)
