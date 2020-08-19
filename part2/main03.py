from exercise03 import Player

if __name__ == "__main__":
    p1 = Player(name="Player 1", health=100, attack=50, guard=20)
    p2 = Player("Player 2", 0, 0, 0)
    p2.health = 200
    p2.attack = 10
    p3 = Player("Player 3", 10, 10, 10)
    
    p1.attack(p2)
    p1.attack(p3)
    p3.attack(p1)
    
    p1.display()
    p2.display()
    p3.display()