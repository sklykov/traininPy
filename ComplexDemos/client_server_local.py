# -*- coding: utf-8 -*-
"""
Client-server communication on localhost.

@author: sklykov

"""
# %% Imports
import socket
import time

# %% Global parameters
default_port = 8095; timeout_connection_s = 2.5; max_iterations = 3


# %% Functions
def launch_server():
    pass


def launch_client(port: int = 8096):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.settimeout(timeout_connection_s)
        try:
            connection.connect(('localhost', port))  # Try to connect to the listening server
            # Send 'Ping' command and get the answer
            connection.send(b"Ping"); time.sleep(0.005)
            print("Received back:", str(connection.recv(1024), 'utf-8'))
            actions_loop = True; iteration = 1
            # Loop with actions
            while actions_loop:
                if iteration % 2 == 0:
                    connection.send(b"Ping"); time.sleep(0.1)
                # Imitation of interaction with a server
                try:
                    data = connection.recv(1024)  # ??? If TimeoutError happened, then connection.recv() won't
                    # read any data further
                    if len(data) > 0:
                        print("Received back:", str(connection.recv(1024), 'utf-8'), flush=True)
                        iteration += 1
                    else:
                        print("Empty response received from a server", flush=True)
                except ConnectionAbortedError:
                    actions_loop = False; break
                except TimeoutError:
                    iteration += 1
                    print("Nothing received from a server, timeout", flush=True)
                if iteration > max_iterations:
                    actions_loop = False; break
            # Send 'Quit' command to the server
            try:
                connection.send(b'Quit'); time.sleep(0.005)
                print(connection.recv(1024).decode('utf-8'))
            except ConnectionAbortedError:
                print("The connection with server has been closed by the server")
        except (ConnectionRefusedError, TimeoutError):
            print("No Server found on port:", port); connection.close()


def launch():
    pass


# %% Testing as the main script
if __name__ == "__main__":
    time.sleep(0.05); launch_client(port=default_port)
