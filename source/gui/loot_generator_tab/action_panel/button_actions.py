from source.gui.loot_generator_tab.output_panel.index import OutputPanel


class ButtonActions:

    @staticmethod
    def individual_loot(party_level: int, output_panel: OutputPanel) -> None:
        rh = Randomizer_Handler(self.programData)
        if party_level <= 4:
            data = self.programData.individualTreasure.get("0-4")
        elif party_level <= 10:
            data = self.programData.individualTreasure.get("5-10")
        elif party_level <= 16:
            data = self.programData.individualTreasure.get("11-16")
        elif party_level <= 20:
            data = self.programData.individualTreasure.get("17-20")
        else:
            output_panel.newOutput("Error!")
            return
        output_panel.newOutput(rh.indivTreasure(data))

    @staticmethod
    def horde_loot(party_level: int, output_panel: OutputPanel) -> None:
        rh = Randomizer_Handler(self.programData)
        if party_level <= 4:
            data_coins = self.programData.hordeTreasureCoins.get("0-4")
            data_items = self.programData.hordeTreasureItems.get("0-4")
        elif party_level <= 10:
            data_coins = self.programData.hordeTreasureCoins.get("5-10")
            data_items = self.programData.hordeTreasureItems.get("5-10")
        elif party_level <= 16:
            data_coins = self.programData.hordeTreasureCoins.get("11-16")
            data_items = self.programData.hordeTreasureItems.get("11-16")
        elif party_level <= 20:
            data_coins = self.programData.hordeTreasureCoins.get("17-20")
            data_items = self.programData.hordeTreasureItems.get("17-20")
        else:
            output_panel.newOutput("Error!")
            return
        output_panel.newOutput(
            rh.hordeTreasure(data_coins, data_items, self.programData)
        )

    def weaponDropB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <= 4:
            outputText = rh.aswDrop("0-4")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = rh.aswDrop("5-10")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = rh.aswDrop("11-16")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = rh.aswDrop("17-20")
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)

    def runeB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        outputText = ""
        if currentLvl <= 4:
            outputText = rh.rollEnchant("0-4")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 10:
            outputText = rh.rollEnchant("5-10")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 16:
            outputText = rh.rollEnchant("11-16")
            self.textFrame.newOutput(outputText)
        elif currentLvl <= 20:
            outputText = rh.rollEnchant("17-20")
            self.textFrame.newOutput(outputText)
        else:
            outputText = "Error!"
            self.textFrame.newOutput(outputText)

    def artgemB(self):
        rh = Randomizer_Handler(self.programData)
        currentLvl = self.levelFrame.varLvl.get()
        if currentLvl <= 4:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("0-4")))
        elif currentLvl <= 10:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("5-10")))
        elif currentLvl <= 16:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("11-16")))
        elif currentLvl <= 20:
            self.textFrame.newOutput(rh.rollartgem(self.programData.aglt.get("17-20")))
        else:
            self.textFrame.newOutput("Error!")

    def rollItemB(self):
        rh = Randomizer_Handler(self.programData)
        sel = []
        outputText = ""
        for i in range(len(self.itemTypeFrame.varState)):
            if self.itemTypeFrame.varState[i].get():
                sel.append(self.programData.itemTypeList[i])
            # selection = str(self.itemTypeFrame.templist[i]) + " ~ State Bool:\t" + str(self.itemTypeFrame.varState[i].get()) + '\n'
            # self.textFrame.newOutput(selection)
        r = random.choice(sel)
        choice = r[2] + "_" + self.rarityFrame.varRty.get()

        if self.programData.asw.get(choice) != None:
            self.textFrame.newOutput(rh.getasw(self.programData.asw.get(choice)) + "\n")
        elif self.programData.rrsww.get(choice) != None:
            self.textFrame.newOutput(
                rh.getrrsww(self.programData.rrsww.get(choice)) + "\n"
            )
        elif self.programData.potion.get(choice) != None:
            self.textFrame.newOutput(
                rh.getPotion(self.programData.potion.get(choice)) + "\n"
            )
        elif self.programData.enchantments.get(choice) != None:
            self.textFrame.newOutput(
                rh.gete(self.programData.enchantments.get(choice)) + "\n"
            )
        elif "Scroll" in choice != None:
            temp = "Spell_"
            sl = 0
            if choice[-1] == "C":
                sl = random.choice((0, 1))
            elif choice[-1] == "U":
                sl = random.choice((2, 3))
            elif choice[-1] == "R":
                sl = random.choice((4, 5))
            elif choice[-1] == "V":
                sl = random.choice((6, 7, 8))
            elif choice[-1] == "L":
                sl = 9
            choice = "SPELL_" + str(sl)
            self.textFrame.newOutput(
                rh.getScroll(self.programData.spell.get(choice)) + "\n"
            )
