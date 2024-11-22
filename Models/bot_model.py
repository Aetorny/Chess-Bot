import pickle
import os
from settings import CURRENT_DIR


def save_model(model: dict[str, dict[str, int]], model_name: str = 'base_model') -> None:
    with open(os.path.join(CURRENT_DIR, 'Models', f'{model_name}.pkl'), 'wb') as file:
        pickle.dump(model, file)


def load_model(model_name: str = 'base_model') -> dict[str, dict[str, int]]:
    if not os.path.exists(os.path.join(CURRENT_DIR, 'Models', f'{model_name}.pkl')):
        save_model({}, model_name)

    with open(os.path.join(CURRENT_DIR, 'Models', f'{model_name}.pkl'), 'rb') as file:
        return pickle.load(file)


def get_key_from_fen_notation(board_fen: str) -> str:
    return ' '.join(board_fen.split(' ')[:-2])


def optimize_model(model: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    for key in model.keys():
        mx = None
        for move in model[key].keys():
            if mx is None or model[key][move] > mx[0]:
                mx = (model[key][move], move)
        
        if mx is not None:
            model[key] = {mx[1]: mx[0]}

    return model
