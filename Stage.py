class Stage:
    def __init__(self, stageInfo):
        self.goalScore = stageInfo[0]
        self.backgroundImage = stageInfo[1]
        self.backgroundMusic = stageInfo[2]
        self.isBossStage = stageInfo[3]
        self.isUnlocked = stageInfo[4]

    