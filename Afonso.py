import random
from time import sleep

# Constants
MIN_ATTACK = 10
MAX_ATTACK = 30

# Player A
player_a = "player_a"
player_a_health = 100
player_a_attack = random.randint(MIN_ATTACK, MAX_ATTACK)

# Player B
player_b = "player_b"
player_b_health = 100
player_b_attack = random.randint(MIN_ATTACK, MAX_ATTACK)

# Game Properties
player_state = player_a
is_running = True
winner = ""

# Main Loop
while is_running:
    if player_state == player_a and player_a_health > 0:
        player_a_attack = random.randint(MIN_ATTACK, MAX_ATTACK)
        player_b_health = player_b_health - player_a_attack
        if player_b_health <= 0:
            winner = player_a
            is_running = False
            print(f"O Player A atacou com {player_a_attack} pontos, o Player B ficou com 0 de vida.")
            print(f"O Player A é o vencedor")
            break

        print(f"O Player A atacou com {player_a_attack} pontos, o Player B ficou com {player_b_health} de vida.")
        player_state = player_b
        sleep(2)

    if player_state == player_b and player_b_health > 0:
        player_b_attack = random.randint(MIN_ATTACK, MAX_ATTACK)
        player_a_health = player_a_health - player_b_attack
        if player_a_health <= 0:
            winner = player_b
            is_running = False
            print(f"O Player B atacou com {player_b_attack} pontos, o Player A ficou com 0 de vida.")
            print(f"O Player B é o vencedor")
            break

        print(f"0 Player B atacou com {player_b_attack}pontos, o Player A ficou com {player_a_health} de vida ")
        player_state = player_a
        sleep(2)
