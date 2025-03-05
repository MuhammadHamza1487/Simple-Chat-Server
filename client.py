import socket
import threading
from ip_address import server_ip_add

def receive_messages(client_socket):
    """Function to continuously receive messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                username1 = message.split(':')[0]
                if message != 'Welcome to the server! Type your messages.':
                    print(f"<{username1}> {message}")
                else:
                    print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = server_ip_add
    
    try:
        # Connect to the server
        client_socket.connect((server_ip, 8080))
        print("Connected to the server.")
        
        # Set up username
        username = input("Enter your username: ")
        client_socket.send(username.encode())
        
        # Start a thread to receive messages
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()
        
        while True:
            # Send messages in the format 'recipient: message'
            message = input()
            if message.lower() == 'exit':
                break  # Exit the loop
            client_socket.send(message.encode())
        
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        client_socket.close()

start_client()
