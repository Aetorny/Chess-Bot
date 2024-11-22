from Models import bot_model
from bot import ChessBot


def main() -> None:
    model_name = 'base_model'
    bot = ChessBot(bot_model.load_model(model_name))


if __name__ == '__main__':
    main()
