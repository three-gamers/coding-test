
def solution(bandage, health, attacks):
    answer = 0

    currTime = 0
    healPersistTime = bandage[0]
    healAmount = bandage[1]
    healAdditionAmount = bandage[2]
    maximumHealth = health
    for attack in attacks:
        targetTime = attack[0]
        healContinuousTime = healPersistTime
        
        if currTime != targetTime - 1:
            while currTime < targetTime - 1:
                if health < maximumHealth:
                    health = min(healAmount + health, maximumHealth)
                    healContinuousTime -= 1
                    if healContinuousTime == 0:
                        healContinuousTime = healPersistTime
                        health = min(health + healAdditionAmount, maximumHealth)
                currTime += 1

                # print("currTime::::", currTime, "targetTime:::", targetTime, "Health:::", health)

        health = health - attack[1]
        currTime += 1

        # print("currTime::::", currTime, "targetTime:::", targetTime, "Health:::", health)
        if health <= 0:
            return -1



    return health