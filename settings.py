class Settings:
    def __init__(self):
        self.screenX = 850
        self.screenY = 650
        self.runningFlag = True
        self.menuFlag = True
        self.startedFlag = False
        self.inventoryFlag = False
        self.chunkSize = 50
        self.xChunks = self.screenX / self.chunkSize
        self.yChunks = self.screenY / self.chunkSize
        self.xMovement = 0
        self.yMovement = 0
        self.animateWalkLength = 7
        self.xToGo = 0
        self.yToGo = 0
        self.noOfAnimationSteps = 2
        self.xStep = self.chunkSize / self.noOfAnimationSteps
        self.yStep = self.chunkSize / self.noOfAnimationSteps