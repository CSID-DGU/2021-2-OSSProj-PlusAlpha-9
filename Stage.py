from Defs import Images

class Stage:
    def __init__(self, stageInfo):
        self.chapter = stageInfo[0]
        self.stage = stageInfo[1]
        self.goal_score = stageInfo[2]
        self.background_image = stageInfo[3]
        self.background_music = stageInfo[4]
        self.is_boss_stage = stageInfo[5]
        self.is_unlocked = stageInfo[6]
        self.mob_image = stageInfo[7]
        self.boss_image = stageInfo[8]
        self.boss_bullet_image = stageInfo[9]

    