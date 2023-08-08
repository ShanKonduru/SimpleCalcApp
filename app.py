import subprocess
import threading
import os
from db.database import create_table
from config import APP_PORT, ADD_MICROSERVICE_PORT, SUBTRACT_MICROSERVICE_PORT, MULTIPLY_MICROSERVICE_PORT, DIVIDE_MICROSERVICE_PORT

# Call create_table() to ensure the database table exists
create_table()

# Launch the microservices using subprocess
microservices = [
    f'python api/add_microservice.py --port {ADD_MICROSERVICE_PORT}',
    f'python api/subtract_microservice.py --port {SUBTRACT_MICROSERVICE_PORT}',
    f'python api/multiply_microservice.py --port {MULTIPLY_MICROSERVICE_PORT}',
    f'python api/divide_microservice.py --port {DIVIDE_MICROSERVICE_PORT}'
]

for service in microservices:
    subprocess.Popen(service, shell=True)

# Launch the UI server
def launch_ui_server():
    os.chdir('ux')  # Change to the 'ux' folder
    os.system(f'python -m http.server {APP_PORT}')

ui_thread = threading.Thread(target=launch_ui_server)
ui_thread.start()
