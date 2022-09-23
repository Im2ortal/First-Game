class Heroes:

  def __init__(self, name, hero_class, level):
    self.name = name
    self.hero_class = hero_class
    self.level = level
    self.exp = 0
    self.exp_needed = (level / 0.07) ** 2
    self.health = (level * 0.3) ** 2
    self.isDead = False
    self.equipped_weapon = []

  def __repr__(self):
    description = "{name} is a {hero_class}, level {level}. To level up {name} needs {exp} experience.".format(name = self.name, hero_class = self.hero_class, level = self.level, 
    exp = self.exp_needed)
    return description
  
  def death(self):
    self.isDead = True
    # A killed out hero can't have any health. This is a safety precaution. death() should only be called if heath was set to 0, but if somehow the hero had health left, it gets set to 0.
    if self.health != 0:
      self.health = 0
    
  def losing_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.death()
    else:
      print("{name} received {damage} damage and now has {health} health!".format(name = self.name, damage = amount, health = self.health))  

  def equip_weapon(self, weapon):
    self.equipped_weapon.append(weapon)
    print("{name} eqipped {weapon} which does {damage} damage.".format(name = self.name, weapon = weapon.name, damage = weapon.damage))
  
  def attack(self, mob):
    if self.isDead == True:
      print("{name} is not able to attach because he is dead.".format(name = self.name))
    if mob.health <= 0:
      print("The {name} is dead, can't attack further.".format(name = mob.name))
    else:
      mob.losing_health(self.equipped_weapon[0].damage)
      print("{name} does {damage} damage. {mob_name} now has {health} health left.". format(name = self.name, damage = self.equipped_weapon[0].damage, mob_name = mob.name, health = mob.health))
    

  def exp_gain(mob):
    self.exp += mob.base_exp
    print("You have {exp} expirience and need {more} more to level up.".format(exp = self.exp, more = self.exp_needed - self.exp))

  def level_up():
    pass

class Weapon:
  
  def __init__(self, name, weapon_type, damage, durability):
    self.name = name
    self.weapon_type = weapon_type
    self.damage = damage
    self.durability = durability
    
  def __repr__(self):
    description = "{name} is a {weapon_type} that does {damage} damage and has {durability} durability left.".format(name = self.name, weapon_type = self.weapon_type, damage = self.damage, 
    durability = self.durability)
    return description

class Mob:

  def __init__(self, name, damage, health, base_exp):
    self.name = name
    self.damage = damage
    self.health = health
    self.base_exp = base_exp
    self.isDead = False

  def death(self):
    self.isDead = True
    print("{name} has died. You receive {exp} exp.".format(name = self.name, exp = self.base_exp))

    # A killed out hero can't have any health. This is a safety precaution. death() should only be called if heath was set to 0, but if somehow the hero had health left, it gets set to 0.
    if self.health != 0:
      self.health = 0

  def losing_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.death()
    else:
      print("{name} received {damage} damage and now has {health} health!".format(name = self.name, damage = amount, health = self.health))  

hero_one = Heroes("Hellendyre", "Paladin", 1)
hero_two = Heroes("Cerethor", "Death Knight", 1)

weapon_sword_1 = Weapon("Training Sword", "Two-Handed Sword", 99, 65)
weapon_1h_sword_1 = Weapon("Bastard Sword", "One-Handed Sword", 49, 65)

mob_one = Mob("Brigand", 2, 300, 33)


print(hero_one)
print(hero_two)

hero_one.equip_weapon(weapon_sword_1)
hero_two.equip_weapon(weapon_1h_sword_1)

hero_one.attack(mob_one)
hero_one.attack(mob_one)
hero_one.attack(mob_one)
hero_one.attack(mob_one)
hero_one.attack(mob_one)

