import enum
import math
from sys import version

class Images(enum.Enum):
    start = "./Image/StartImage.png"
    how_to_play = "./Image/howtoplay.png"
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

    effect_crossair = "./Image/Effects/Crosshair.png"
    
class Sounds(enum.Enum):
    bgm_desert = "./Sound/ariant.wav"
    bgm_rien = "./Sound/Rien.wav"
    sfx_weapon1 = "./Sound/weapon-sound4.wav"
    sfx_weapon2 = "./Sound/weapon-sound8.wav"
    sfx_weapon3 = "./Sound/weapon-sound9.wav"
    sfx_weapon4 = "./Sound/weapon-sound16.wav"
    sfx_gameover = "./Sound/gameover.wav"
    sfx_monster1 = "./Sound/monster-sound7.wav"
    sfx_penguin = "./Sound/penguin.wav"
    sfx_present1 = "./Sound/present1.wav"
    sfx_present2 = "./Sound/present2.wav"
    sfx_present3 = "./Sound/present3.wav"
    sfx_present4 = "./Sound/present4.wav"
    sfx_hit = "./Sound/puck.wav"

class Fonts(enum.Enum):
    font_default = "./Font/DXHanlgrumStd-Regular.otf"

class Color(enum.Enum):
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)

class Default(enum.Enum):
    game = {
        "size": {
            "x":0, 
            "y":0
            }
    }
    character = {
        "size": {
            "x":100, 
            "y":100
            },
        "invincible_period": 4.0,
        "missile":{
            "min":1,
            "max":4,
            "speed":20,
            "volume":0.1
            },
    }
    item = {
        "duration":10.0,
        "size":{
            "x":50, 
            "y":50
        },
        "speed":5,
        "speedup":{
            "spawn_rate": 0.004
        },
        "powerup":{
            "spawn_rate": 0.004,
            "duration":10.0
            },
        "bomb":{
            "spawn_rate": 0.004,
            "interval":1.0,
            "size":{
                "x":500, 
                "y":500
            },
            "power":1000
        },
        "health":{
            "spawn_rate": 0.002
        },
        "coin":{
            "spawn_rate": 0.002
        }
    }
    animation = {
        "blink":{
            "speed":0.05,
            "frame":0.2,
            "duration":4.0
        },
        "interval":10.0,
        "speed":0.5
    }

class Utils():
    @classmethod
    def clamp(cls, val, n_min, n_max):
        return max(n_min, min(val, n_max)) 

    @classmethod
    def get_distance(cls, a, b):
        return math.sqrt((b["x"] - a["x"])**2 + (b["y"] - a["y"])**2)
