import chess
from Models import bot_model
from random import randint


class ChessBot:
    def __init__(self, model: dict[str, dict[str, int]]) -> None:
        '''
        EN: Load only optimized model!
        RU: Загружайте только оптимизированную модель!
        '''
        self.model = model


    def make_move(self, board_fen: str) -> tuple[str, str]:
        key = bot_model.get_key_from_fen_notation(board_fen)
        board = chess.Board(board_fen)

        if key in self.model:
            move = list(self.model[key].keys())[0]
            return (move, board.uci(board.push_san(move)))
        
        legal_moves = list(board.legal_moves)
        move = legal_moves[randint(0, len(legal_moves) - 1)]
        return (board.san(move), board.uci(move))

