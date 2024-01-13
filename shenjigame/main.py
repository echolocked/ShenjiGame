from shenjigame.backend.game_logic.GameState import GameState
import time

game_state = GameState()

def update_game_state():
    game_state.update()

def main():
    game_state.add_population(10)
    day = 0

    while True:
        day += 1
        print(f"Day {day}")

        game_state.update()

        # Display current state (for testing purposes)
        print(f"Population: {game_state.population}")
        print(f"Food: {game_state.food}, Wood: {game_state.wood}, Stone: {game_state.stone}")
        print(f"Technologies: {game_state.technologies}")
        print(f"Buildings: {game_state.buildings}")

        if game_state.check_game_over():
            print("Game Over")
            break

        time.sleep(1)

if __name__ == '__main__':
    main()
