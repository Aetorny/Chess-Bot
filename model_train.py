from typing import Literal
from Models import bot_model
from settings import CURRENT_DIR
import os
import chess


MODEL_NAME = 'base_model'
model = bot_model.load_model(MODEL_NAME)


def change_model(key: str, move: str, value: int) -> None:
    if key not in model:
        model[key] = {}
    model[key][move] = model[key].get(move, 0) + value


def main() -> None:
    dataset_path = os.path.join(CURRENT_DIR, 'Datasets',
                                'lichess_db_standard_rated_2013-01.txt')
    start_from = 0

    counter = 0
    with open(dataset_path, 'r') as file:
        for line in file:
            while counter < start_from:
                counter += 1
                continue

            if '{' in line or line == '': 
                counter += 1
                print(counter, 'Skipped')
                continue
            board = chess.Board()
            moves: list[str] = line.split(' ')
            is_white_wins = True if moves[-1] == '1-0' else False if moves[-1] == '0-1' else None

            if is_white_wins is not None:
                if moves[-2][-1] == '#':
                    moves[-2] = moves[-2][:-1]
            
            if is_white_wins is True:
                model_changes = (3, -3)
            elif is_white_wins is False:
                model_changes = (-3, 3)
            else:
                model_changes = (1, 1)
            
            moves = [move for move in moves if '.' not in move]
            moves.pop()

            who_moves: Literal[0, 1] = 0
            for move in moves:
                key = bot_model.get_key_from_fen_notation(board.fen())
                board.push_san(move)
                change_model(key, move, model_changes[who_moves])
                who_moves = 1 if who_moves == 0 else 0
        
            counter += 1
            if counter % 25000 == 0:
                bot_model.save_model(model, MODEL_NAME)
                print(counter, 'Done and saved')

    bot_model.save_model(model, MODEL_NAME)


if __name__ == '__main__':
    main()
