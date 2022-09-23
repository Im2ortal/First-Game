class Heroes:

  def __init__(self, name, hero_class, level, energy_type, energy):
    self.name = name
    self.hero_class = hero_class
    self.level = level
    self.exp = 0
    self.exp_needed = (level / 0.07) ** 2
    self.health = (level * 0.3) ** 2
    self.energy_type = energy_type
    self.energy_type = energy
    self.isDead = False
    self.equipped_weapon = []

  def __repr__(self):
    description = "{name} is a {hero_class}, level {level}. To level up {name} needs {exp} experience.".format(name = self.name, hero_class = self.hero_class, level = self.level, exp = self.exp_needed)
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
  
  def attack():
    pass

  def exp_gain():
    pass

  def level_up():
    pass

class Weapon:
  
  def __init__(self, name, weapon_type, damage, durability):
    self.name = name
    self.weapon_type = weapon_type
    self.damage = damage
    self.durability = durability
    
  def __repr__(self):
    description = "{name} is a {weapon_type} that does {damage} damage and has {durability} durability left.".format(name = self.name, weapon_type = self.weapon_type, damage = self.damage, durability = self.durability)
    return description

hero_one = Heroes("Hellendyre", "Paladin", 1, "Holy Power", 5)

weapon_sword_1 = Weapon("Training Sword", "Two-Handed Sword", 99, 65)


print(hero_one)
print(weapon_sword_1)

hero_one.equip_weapon(weapon_sword_1)

