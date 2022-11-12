from main import create_app
from config import DevConfig

PORT = 8000

if __name__ == '__main__':
    app = create_app(DevConfig)
    app.run(port=PORT)
