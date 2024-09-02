# db/config.py

import os

# Используйте переменные окружения для конфиденциальных данных
DB_NAME = os.getenv('DB_NAME', 'aptikeev.rn')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'tx_quk5h9DQNKTw')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
