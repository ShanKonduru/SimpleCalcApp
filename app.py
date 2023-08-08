import subprocess
import threading
import os
from db.database import create_table

# Call create_table() to ensure the database table exists
create_table()

# Launch the microservices using subprocess
microservices = [
    'python api/add_microservice.py',
    'python api/subtract_microservice.py',
    'python api/multiply_microservice.py',
    'python api/divide_microservice.py'
]

for service in microservices:
    subprocess.Popen(service, shell=True)

# Launch the UI server
def launch_ui_server():
    os.chdir('ux')  # Change to the 'ux' folder
    os.system('python -m http.server 8000')

ui_thread = threading.Thread(target=launch_ui_server)
ui_thread.start()
