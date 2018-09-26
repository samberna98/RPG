#  File: RPG.py
#  Description:
#  Student's Name: Samuel Bernasconi
#  Date Created: 9-17-17
#  Date Last Modified:9-16-17

class Weapon: # weapon class 
    damage = 0 
    weapontype = ""

    def __init__(self, weapon): # creates object and establishes weapontype and sets damage equal to the type of weapons attack strength
        if weapon == "dagger":
            self.damage = 4
            self.weapontype = weapon
        elif weapon == "axe":
            self.damage = 6
            self.weapontype = weapon
        elif weapon == "staff":
            self.damage = 6
            self.weapontype = weapon
        elif weapon == "sword":
            self.damage = 10
            self.weapontype = weapon
        else:
            damage = 1
            weapontype = "none"

class Armor: 
    armorclass = 0
    armortype = ""
    
    def __init__(self, armor): # creates object and establishes armortype and sets Armor Class equal to the armor type's strength
        if armor == "plate":
            self.armorclass = 2
            self.armortype = "plate"
        elif armor == "chain":
            self.armorclass = 5
            self.armortype = "chain"
        elif armor == "leather":
            self.armorclass = 8
            self.armortype = "leather"
        else:
            self.armorclass = 10
            self.armortype = "none"


class RPGCharacter:

    name = ""
    health = 0
    spellP = 0
    weapon = ""
    weaponStrength = 1
    armor = "none"
    armorClass = 10
    
    def __str__(self): # prints RPGCharacters Statistics
        return ('\n' + self.name +
                "\n\tCurrent Health: " + str(self.health) +
                "\n\tCurrent Spell Points: " + str(self.spellP) +
                "\n\tWielding: " + self.weapon +
                "\n\tWearing: " + self.armor +
                "\n\tArmor Class: " + str(self.armorClass)+
                '\n')
                
        
    def unwield(self): # sets weapon to "none" and prints 
        self.weapon = "none"
        print(self.name + " is no longer wielding anything.")
        
    def fight(self, other): # deducts the attacked RPGCharacter's health by the attackers weapon strength and prints the changes then checks to see if the character has been defeated
        print(self.name + " attacks " + other.name + " with a(n) " + self.weapon)
        other.health -= self.weaponStrength
        print(self.name + " does " + str(self.weaponStrength) + " damage to " + other.name)
        print(other.name + " is now down to " + str(other.health) + " health")
        other.checkForDefeat()

    def checkForDefeat(self): # checks wether health is still above zero
        if self.health <= 0:
            print(self.name + " has been defeated!")
    
class Fighter(RPGCharacter):

    maxHealth = 40

    def __init__(self, charname): # creates Fighter object and sets health, name and spell points
        self.name = charname
        self.health = 40
        self.spellP = 0
        
    def wield(self, Weapon): # sets the RPGCharacters damage to the value of the Weapon object's attack strength and names its weapon
        self.weapon = Weapon.weapontype
        self.weaponStrength = Weapon.damage
        print(self.name + " is now wielding a(n) " + self.weapon)

    def putOnArmor(self, Armor): # sets the RPGCharacters armor to the armortype of the Armor object and sets the armorClass to the armor's armortype
        self.armor = Armor.armortype
        self.armorClass = Armor.armorclass
        print(self.name + " is now wearing " + self.armor)
        
    def takeOffArmor(self): # sets the RPGcharacters armor to "none" and resets the armor class 
        self.armor = "none"
        self.armorClass = 10
        print(self.name + " is no longer wearing anything")
        

class Wizard(RPGCharacter):

    maxHealth = 16
    
    def __init__(self, charname): # creates Wizard object with a name and sets health and spell points sepcified for that character
        self.name = charname
        self.health = 16
        self.spellP = 20

    def wield(self, Weapon): # establishes whether the Weapon is allowed for the character, if it is, it sets the RPGCharacters weapon and attacking strength
        if Weapon.weapontype == "axe" or Weapon.weapontype == "sword":
            print("Weapon not allowed for this character class")
        else:
            self.weapon = Weapon.weapontype
            self.weaponStrength = Weapon.damage
        print(self.name + " is now wielding a(n) " + Weapon.weapontype)

    def putOnArmor(self, Armor): # armor never allowed for wizard so it prints this 
        print("Armor not allowed for this character class")

    def castSpell(self, spellName, other): # takes the spell name and target 
        if spellName == "Fireball": # if spell name "Fireball" the appopriate amount of damage is done to target and spell point are deducted if there are sufficient
            if self.spellP >= 3:
                self.spellP -= 3
                other.health -= 5
                print(self.name + " casts " + spellName + " at " + other.name )
                print(self.name + " does 5 damage to " + other.name)
                print(other.name + " is now down to " + str(other.health) + " health")
            else:
                print("Insufficient spell points.")
                
        elif spellName == "Lightning Bolt": # if spell name "Lightning Bolt" the appopriate amount of damage is done to target and spell point are deducted if there are sufficient
            if self.spellP >= 10:
                self.spellP -= 10
                other.health -= 10
                print(self.name + " casts " + spellName + " at " + other.name)
                print(self.name + " does 10 damage to " + other.name)
                print(other.name + " is now down to " + str(other.health) + " health")
            else:
                print("Insufficient spell points.")
                
        elif spellName == "Heal": # if spell name "Heal" the appopriate amount of health added to target and spell point are deducted if there are sufficient, checks if maxhealth would be exceeded and only adds appropriate amount 
            if self.spellP >= 6:               
                if other.health + 6 >= other.maxHealth: 
                    self.spellP -= 6
                    other.health += 6
                    print(self.name + " casts " + spellName + " at " + other.name)
                    print(self.name + " heals " + other.name + " for 6 health points.")
                    print(other.name + " is now at " + str(other.health) + " health")
                else:
                    x = other.maxHealth - other.health
                    other.health = other.maxHealth
                    print(self.name + " casts " + spellName + " at " + other.name)
                    print(self.name + " heals " + other.name + " for " + str(x) + " health points")
                    print(other.name + " is now at " + str(other.health) + " health")
                        
        else:  # if the spell name is wrong, error message is printed
            print("Unknown spell name. Spell failed")
            
        

def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)

main()
    
















