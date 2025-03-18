class ButtonActions:

    @staticmethod
    def individualTreasureB(party_level):
        rh = Randomizer_Handler(self.programData)
        party_level = self.levelFrame.varLvl.get()
        outputText = ""
        if party_level <= 4:
            outputText = rh.indivTreasure(
                self.programData.individualTreasure.get("0-4")
            )
            self.textFrame.newOutput(outputText)
        elif party_level <= 10:
            outputText = rh.indivTreasure(
                self.programData.individualTreasure.get("5-10")
            )
            self.textFrame.newOutput(outputText)
        elif party_level <= 16:
            outputText = rh.indivTreasure(
                self.programData.individualTreasure.get("11-16")
            )
            self.textFrame.newOutput(outputText)
        elif party_level <= 20:
            outputText = rh.indivTreasure(
                self.programData.individualTreasure.get("17-20")
            )
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)
