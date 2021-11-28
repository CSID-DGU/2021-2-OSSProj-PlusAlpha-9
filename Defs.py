import enum
import math
from sys import version

class Images(enum.Enum):
    start = "./Image/StartImage.png"
    how_to_play = "./Image/howtoplay.png"
    about = "./Image/AboutPage.jpg"
    background_desert = "./Image/DESERT_modified_v3.jpg"
    background_antarctic = "./Image/Antarctic_modified_v2.jpg"
    enemy_scrophion = "./Image/scorphion1-1.png"
    enemy_cactus = "./Image/Catus.png"
    missile_missile2 = "./Image/MISSILE_2.png"
    weapon_target_missile = "./Image/Weapon/spaceMissiles_012.png"
    
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

class Color(enum.Enum):
    RED = (200,60,50)
    BLUE = (0,60,200)
    GREEN = (50,200,50)
    YELLOW = (255,255,0)
    WHITE = (255,255,255)
    TRANSPARENT = (255,255,255,128)
    GRAY = (220,220,220)
    BLACK = (0,0,0)

class Default(enum.Enum):
    game = {
        "size": {
            "x":0, 
            "y":0
            }
    }
    font = "./Font/DXHanlgrumStd-Regular.otf"
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
            "volume":0.1,
            "speed_inc":1
            }
    }
    item = {
        "duration":10.0,
        "size":{
            "x":50, 
            "y":50
        },
        "velocity":5,
        "speedup":{
            "spawn_rate": 0.004,
            "frames":[
                "./Image/Items/SpeedUp/frame-1.png", 
                "./Image/Items/SpeedUp/frame-2.png", 
                "./Image/Items/SpeedUp/frame-3.png", 
                "./Image/Items/SpeedUp/frame-4.png", 
                "./Image/Items/SpeedUp/frame-5.png",
                "./Image/Items/SpeedUp/frame-1.png"
            ]
        },
        "powerup":{
            "spawn_rate": 0.004,
            "duration":10.0,
            "frames":[
                "./Image/Items/PowerUp/frame-1.png", 
                "./Image/Items/PowerUp/frame-2.png", 
                "./Image/Items/PowerUp/frame-3.png", 
                "./Image/Items/PowerUp/frame-4.png", 
                "./Image/Items/PowerUp/frame-5.png",
                "./Image/Items/PowerUp/frame-1.png"
            ]
        },
        "bomb":{
            "spawn_rate": 0.004,
            "interval":1.0,
            "power":1000,
            "frames":[
                "./Image/Items/Bomb/frame-1.png", 
                "./Image/Items/Bomb/frame-2.png", 
                "./Image/Items/Bomb/frame-3.png", 
                "./Image/Items/Bomb/frame-4.png", 
                "./Image/Items/Bomb/frame-5.png",
                "./Image/Items/Bomb/frame-1.png"
            ]
        },
        "health":{
            "spawn_rate": 0.002,
            "frames":[
                "./Image/Items/Health/frame-1.png", 
                "./Image/Items/Health/frame-2.png", 
                "./Image/Items/Health/frame-3.png", 
                "./Image/Items/Health/frame-4.png",
                "./Image/Items/Health/frame-1.png"
            ]
        },
        "coin":{
            "spawn_rate": 0.002,
            "frames":[
                "./Image/Items/Coin/frame-1.png", 
                "./Image/Items/Coin/frame-2.png", 
                "./Image/Items/Coin/frame-3.png", 
                "./Image/Items/Coin/frame-4.png", 
                "./Image/Items/Coin/frame-5.png",
                "./Image/Items/Coin/frame-1.png"
            ]
        }
    }
    effect = {
        "speed": 0.4,
        "velocity": 5,
        "bomb":{
            "duration": 7.0,
            "size":{
                "x": 500,
                "y": 500
            },
            "frames": [
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
        },
        "boom":{
            "duration": 4.0,
            "size":{
                "x": 150,
                "y": 150
            },
            "frames":[
                "./Image/Effects/Boom/frame-1.png", 
                "./Image/Effects/Boom/frame-2.png", 
                "./Image/Effects/Boom/frame-3.png", 
                "./Image/Effects/Boom/frame-4.png", 
                "./Image/Effects/Boom/frame-5.png", 
                "./Image/Effects/Boom/frame-6.png", 
            ]
        },
        "crosshair":{
            "image": "./Image/Effects/Crosshair.png",
            "size": {
                "x": 120,
                "y": 120
            },
            "velocity": 5
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
    about = {
        "authors": [
            "Jibmin Jung",
            "Heesu Ju", 
            "Seyeong Lee",
        ],
        "sprites": [
            "MillionthVector"
        ]
    }

class Utils():
    @classmethod
    def clamp(cls, val, n_min, n_max):
        return max(n_min, min(val, n_max)) 

    @classmethod
    def get_distance(cls, a, b):
        return math.sqrt((b["x"] - a["x"])**2 + (b["y"] - a["y"])**2)
