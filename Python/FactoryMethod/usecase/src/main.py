from usecase.src import NPCFactory, EnemyFactory

if __name__ == "__main__":
    spawners = [NPCFactory(), EnemyFactory()]

    npc = spawners[0].spawn_charactor("Charlie")
    enemy = spawners[1].spawn_charactor("Davide")

    npc.introduce()
    enemy.introduce()
    npc.greeting()
    enemy.greeting()