# -*- coding: utf-8 -*-
"""
Client-server communication on the localhost machine.

@author: sklykov

"""
# %% Imports
import socket
import time
from threading import Thread

# %% Global parameters
default_port = 8098; timeout_connection_s = 2.5; max_iterations = 3


# %% Functions
def launch_server(port: int = 8096, timeout_connection_sec: int = 3.0, max_bytes_received: int = 2048):
    """
    Launch a server on localhost and specified network port.

    Parameters
    ----------
    port : int, optional
        Network port for establishing TCP connection. The default is 8096.
    timeout_connection_sec : int, optional
        Maximum timeout in seconds for establishing the connection with a client. The default is 3.0.
    max_bytes_received : int, optional
        Maximum number of bytes for receiving through single receiving request. The default is 2048.

    Returns
    -------
    None.

    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout_connection_sec)  # prevent to wait too long for some client connected
        s.bind(('localhost', port)); s.listen()
        try:
            (connection, address) = s.accept()
            event_loop = True  # for command processing loop
            with connection:
                while event_loop:
                    try:
                        data = connection.recv(max_bytes_received)
                        command = data.decode('utf-8')
                        print("Received from a client:", command)
                        # Ping command - for checking the connection
                        if "Ping" in command:
                            connection.send(b'Echo from the local server')
                        # Some 'Command 1' received (e.g., button clicked)
                        elif "Command 1" in command:
                            time.sleep(1.5)  # imitation of the work
                            connection.send(b'Command 1 successfully processed')
                        # Some 'Command 2' received (e.g., launch data processing / acquisition)
                        elif "Command 2" in command:
                            time.sleep(2.0)  # imitation of the work
                            connection.send(b'Command 2 successfully processed')
                        # Quit command received - normal finishing of work and closing the server
                        elif "Quit" in command:
                            time.sleep(2.0)  # imitation of the work
                            connection.send(b'Server closed'); event_loop = False
                        # One of way of checking preserved connection - check that the received command not empty
                        if len(command) == 0:
                            print("The empty string received from the client, most likely it finished working")
                            event_loop = False
                    except (ConnectionAbortedError, ConnectionRefusedError):
                        print("Client has closed the connection")
                        event_loop = False; break
        except (ConnectionRefusedError, TimeoutError):
            print("No connection with a client established on port:", port)


def launch_client(port: int = 8096, timeout_connection_sec: int = 2.0, max_bytes_sent: int = 1024):
    """
    Launch a client on localhost and specified network port.

    Parameters
    ----------
    port : int, optional
        Network port for establishing TCP connection. The default is 8096.
    timeout_connection_sec : int, optional
        Maximum timeout in seconds for establishing the connection with a server. The default is 2.0.
    max_bytes_sent : int, optional
        Maximum number of bytes for sending through single send request. The default is 1024.

    Returns
    -------
    None.

    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.settimeout(timeout_connection_sec)
        try:
            connection.connect(('localhost', port))  # Try to connect to the listening server
            # Send 'Ping' command and get the answer
            time.sleep(0.2); connection.send(b"Ping")
            response = connection.recv(max_bytes_sent).decode('utf-8')
            print("Received back:", response)
            actions_loop = True; iteration = 0; quit_sent = False
            # Loop with actions
            while actions_loop:
                # Some command send to the server and awaiting the response from it
                if iteration == 0:
                    time.sleep(0.85); connection.send(b"Command 1"); iteration += 1
                elif iteration == 1:
                    connection.send(b"Command 2"); iteration += 1
                else:
                    connection.send(b"Quit"); iteration += 1
                    quit_sent = True; actions_loop = False
                # Wait response from the server
                try:
                    data = connection.recv(max_bytes_sent)
                    # Check that data has been received
                    if len(data) > 0:
                        print("Received from a server:", str(data, 'utf-8'), flush=True)
                    else:
                        print("Empty response received from a server", flush=True)
                except ConnectionAbortedError:
                    print("Server have been closed / stoped working", flush=True)
                    actions_loop = False; break
                except TimeoutError:
                    print("Nothing received from a server, timeout", flush=True)
                # Making some delay between commands
                if iteration == 1:
                    time.sleep(timeout_connection_sec - 0.5)  # less than timeout
                elif iteration == 2:
                    time.sleep(4*timeout_connection_sec)  # more than timeout, long delay between Command 2 and Quit - e.g. clicking buttons
                # Check for exit from the loop
                if iteration > max_iterations:
                    actions_loop = False; break
            # Send 'Quit' command to the server, if not sent by the action above
            if not quit_sent:
                try:
                    connection.send(b'Quit'); time.sleep(0.005)
                    print(connection.recv(max_bytes_sent).decode('utf-8'))
                except (ConnectionAbortedError, ConnectionRefusedError):
                    print("The connection has been closed by the server before sending 'Quit' command")
        except (ConnectionRefusedError, TimeoutError):
            print("No connection with a server established on port:", port); connection.close()


def launch():
    """
    Launch a server and a client connected with each other and communicating through TCP connection.

    Both server and client are opened in the dedicated thread.

    Returns
    -------
    None.

    """
    # Launch server on the separate thread
    server_thread = Thread(target=launch_server, args=(8091, timeout_connection_s+1.5)); server_thread.start()
    # Launch client on the separate thread
    client_thread = Thread(target=launch_client, args=(8091, timeout_connection_s-0.25)); client_thread.start()
    # Wait for all threads exit
    if client_thread.is_alive():
        client_thread.join()  # client should exit normally by itself
    if server_thread.is_alive():
        server_thread.join(timeout=2.0*timeout_connection_s)


# %% Testing as the main script
if __name__ == "__main__":
    # launch_client(port=default_port)
    # launch_server()
    launch()
