from Defs import Images

class Stage:
    def __init__(self, stageInfo):
        self.chapter = stageInfo[0]
        self.stage = stageInfo[1]
        self.goalScore = stageInfo[2]
        self.backgroundImage = stageInfo[3]
        self.backgroundMusic = stageInfo[4]
        self.isBossStage = stageInfo[5]
        self.isUnlocked = stageInfo[6]
        self.mobImage = stageInfo[7]

    