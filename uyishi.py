def calculate_coins(L1, L2):
    player1_coins = 0
    player2_coins = 0
    for action1, action2 in zip(L1, L2):
        if action1 == "share" and action2 == "share":
            player1_coins += 5
            player2_coins += 5
        elif action1 == "share" and action2 == "steal":
            player1_coins += 0
            player2_coins += 3
        elif action1 == "steal" and action2 == "share":
            player1_coins += 3
            player2_coins += 0
        elif action1 == "steal" and action2 == "steal":
            player1_coins += 0
            player2_coins += 0
    return [player1_coins, player2_coins]

# 1-shart
L1 = ["share"]
L2 = ["share"]
# # 2-shart
# L1 = ["steal"]
# L2 = ["share"]
# 3-shart
# L1 = ["steal"]
# L2 = ["steal"]
# 4-shart
# L1 = ["share","share","share"]
# L2 = ["steal","share","steal"]

result = calculate_coins(L1, L2)
print(result)
