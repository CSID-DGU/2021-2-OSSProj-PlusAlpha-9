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

    icon_caution = "./Image/Caution.jpg"
    icon_award = "./Image/Award.jpg"

    stage_clear = "./Image/Stageclear_v1.jpg"
    chapter_clear_oasis = "./Image/ChapterClear_Oasis.jpg"
    chapter_clear_ice = "./Image/ChapterClear_Ice.jpg"
    chapter_clear_space = "./Image/ChapterClear_Space.jpg"
    chapter_cleared = "./Image/ClearedChapter.jpg"
    gameover = "./Image/Gameover_v2.jpg"

    F5S1_locked = "./Image/CharacterLocked_F5S1.jpg"
    F5S4_locked = "./Image/CharacterLocked_F5S4.jpg"
    Tank_locked = "./Image/CharacterLocked_Tank.jpg"
    stage_locked = "./Image/StageLocked_v1.jpg"

    info_infi_1 = "./Image/Info_infi_1.png"
    info_infi_2 = "./Image/Info_infi_2.png"
    info_infi_3 = "./Image/Info_infi_3.png"
    info_infi_4 = "./Image/Info_infi_4.png"
    info_infi_5 = "./Image/Info_infi_5.png"
    info_stage_1 = "./Image/Info_stage_1.png"
    info_stage_2 = "./Image/Info_stage_2.png"
    info_stage_3 = "./Image/Info_stage_3.png"
    info_stage_4 = "./Image/Info_stage_4.png"
    info_stage_5 = "./Image/Info_stage_5.png"
    info_stage_6 = "./Image/Info_stage_6.png"
    info_items = "./Image/Info_items.png"
    info_controls = "./Image/Info_controls.jpg"

class Scales(enum.Enum):
    large = (2, 2)
    default = (1, 1)
    small = (.6, .6)
    tiny = (.3, .3)
    

class Color(enum.Enum):
    RED = (200,60,50)
    BLUE = (0,60,200)
    GREEN = (50,200,50)
    YELLOW = (255,255,0)
    WHITE = (255,255,255)
    TRANSPARENT = (255,255,255,128)
    GRAY = (220,220,220)
    BLACK = (0,0,0)

class Menus(enum.Enum):
    margin_10 = 10
    margin_20 = 20
    margin_40 = 40
    margin_50 = 50
    margin_100 = 100
    margin_200 = 200
    ranking_search_result_margin = (0,20)

    fontsize_50 = 50
    fontsize_30 = 30
    fontsize_25 = 25
    fontsize_default = 20

    ID_maxchar = 20
    table_padding = 10


class Default(enum.Enum):
    game = {
        "size": {
            "x":0, 
            "y":0
            }
    }
    sound = {
        "sfx":{
            "volume":0.2
        }
    }
    font = "./Font/DXHanlgrumStd-Regular.otf"
    boss = {
        "size": {
            "x":250, 
            "y":250
        },
        "velocity": [
            6,
            8,
            12
        ],
        "gun_size": 10,
        "bullet_size": {
            "x":20, 
            "y":20
        },
        "health": 12000,
        "firing_speed": [
            25, 
            20, 
            15
        ],
        "grace_timers": [
            120,
            90, 
            65
        ],
        "grace_time": 30
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
            "speed_inc":1
            },
        "max_stats":{
            "power":500,
            "fire_rate":0.3,
            "mobility":25
        }
    }
    item = {
        "duration":10.0,
        "size":{
            "x":50, 
            "y":50
        },
        "sound": "./Sound/Item/speedup.wav",
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
            ],
            "sound": "./Sound/Weapon/explosion.wav"
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
            ],
            "sound": "./Sound/destroyed.wav"
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
        "open_source": {
            "IMAGES":{
                "MillionthVector CC BY 4.0": "http://millionthvector.blogspot.com/p/free-sprites.html",
                "You're Perfect Studio CC0 1.0":"https://opengameart.org/content/space-shoter-crosshairs",
                "bevouliin.com CC0 1.0":"https://opengameart.org/content/shining-coin-shining-health-shining-power-up-sprite-sheets",
                "Felis Chaus CC0 1.0":"https://opengameart.org/content/fire-explosion",
                "9KeyStudio CC0 1.0":"https://opengameart.org/content/pixel-art-explosion-animation",
                "Icons made by Freepik":'https://www.freepik.com',
                "Flaticon":"https://www.flaticon.com/"
            },
            "SOUNDS":{
                "MATRIXXX_ CC0 1.0": "https://freesound.org/people/MATRIXXX_/sounds/441373/",
                "simoneyoh3998 CC0 1.0": "https://freesound.org/people/simoneyoh3998/sounds/500673/",
                "jalastram CC BY 3.0": "https://freesound.org/people/jalastram/sounds/317769/",
                "befig CC BY 3.0": "https://freesound.org/people/befig/sounds/455530/",
                "Royalty Free Music from Bensound":"www.bensound.com"
            },
            "BASE CODE":{
                "CSID-DGU/2021-1-OSSPC-MUHIRYO-4":"https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4.git",
                "TimurKhayrullin/Ultimate-Antivirus":"https://github.com/TimurKhayrullin/Ultimate-Antivirus"
            }
        }
    }

class Utils():
    @classmethod
    def clamp(cls, val, n_min, n_max):
        return max(n_min, min(val, n_max)) 

    @classmethod
    def get_distance(cls, a, b):
        return math.sqrt((b["x"] - a["x"])**2 + (b["y"] - a["y"])**2)
