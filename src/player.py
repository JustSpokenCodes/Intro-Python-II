# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,health,speed,defense,fatique,room):
        self.health = health
        self.speed = speed
        self.defense = defense
        self.fatique = fatique
        self.room = room 