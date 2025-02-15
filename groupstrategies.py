import random
# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# Utilizes steal and split ratios to charecterize the opponent, then completes the best moves based on charecterization
def goldenBallersStrategy3(history):

    rounds_played = len(history)

    if rounds_played <= 3: # peaceful start to exploit strategies that are based off of the first moves.
        return "split"
    
    opponent_moves = [round[1] for round in history] # creates a list with all of the opponents moves
    steal_count = opponent_moves.count("steal")
    split_count = opponent_moves.count("split")

    steal_ratio = steal_count/rounds_played # ratio of steals to number of rounds
    split_ratio = split_count/rounds_played # ratio of splits to number of rounds


    if steal_ratio > 0.6: # punishes "selfish" strategies
        return "steal"
      
    elif split_ratio > 0.8: # exploites "naive" strategies
        return "steal"
        
    elif steal_ratio < 0.3: # splits with unpredictable strategies
        return "split" 
        
    elif steal_ratio == 0.5: #chooses randomly for strategies that do the same
        return random.choice(["split", "steal"])

    else: # steals 75% of the time as a last case scenerio
        return random.choice(["steal", "steal", "steal", "split"])