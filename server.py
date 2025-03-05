import socket
import threading
from ip_address import server_ip_add

clients = {}  # Dictionary to store clients {username: socket}

def handle_client(client_socket, client_address):
    """Handle communication with the client."""
    try:
        # Receive and store the username
        username = client_socket.recv(1024).decode()
        if username:
            clients[username] = client_socket
            print(f"User '{username}' connected from {client_address}.")
            client_socket.send("Welcome to the server! Type your messages.".encode())
        
        while True:
            # Receive message from the client
            message = client_socket.recv(1024).decode()
            if message:
                # Parse the message to extract the recipient and text
                try:
                    recipient, text = message.split(":", 1)
                    recipient = recipient.strip()  # Remove extra spaces
                    text = text.strip()  # Remove extra spaces
                    if recipient in clients:
                        # Send message to the recipient
                        clients[recipient].send(f"{username}: {text}".encode())
                        # Log the message path without showing content
                        print(f"Message from '{username}' to '{recipient}' delivered.")
                    else:
                        client_socket.send(f"User '{recipient}' not found.".encode())
                        print(f"Message from '{username}' to '{recipient}' failed (User not found).")
                except ValueError:
                    client_socket.send("Invalid message format. Use 'recipient: message'.".encode())
            else:
                break
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        # Remove client from the list when they disconnect
        if username in clients:
            del clients[username]
        client_socket.close()
        print(f"User '{username}' disconnected.")

def start_server():
    """Start the server to accept multiple clients."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip_add, 8080))  # Accept connections from all interfaces
    server_socket.listen(5)
    print("Server is listening on port 8080...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


start_server()
