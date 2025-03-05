# SimpleChatServer

A lightweight peer-to-peer chat server built using Python's `socket` and `threading` modules. This application allows multiple clients to connect and send messages to each other through a central server.

## Features
- Supports multiple clients using threading.
- Direct message feature: Users can send messages to specific recipients.
- Simple and easy-to-use format (`recipient: message`).
- Server logs messages for tracking deliveries.
- Handles client disconnections gracefully.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/SimpleChatServer.git
   cd SimpleChatServer
   ```
2. Install Python (if not already installed):
   - [Download Python](https://www.python.org/downloads/)
   - Ensure `python` is available in your system path.

## Usage

### 1. Configure the Server IP
Before running the server and client, update the `ip_address.py` file with your actual server's IP address.

```python
server_ip_add = 'xx.xx.xx.xx'  # Replace with your server's IP
```

### 2. Run the Server
Start the server to listen for client connections:
```sh
python server.py
```
The server will start listening on port `8080`.

### 3. Run the Client
Start a client instance to connect to the server:
```sh
python client.py
```
The client will prompt for a username and then allow message exchanges.

## How It Works
1. The **server** accepts multiple clients and stores their usernames.
2. The **client** enters a username and sends messages using the format:
   ```
   recipient: message
   ```
3. The server routes the messages to the correct recipient if they are online.
4. Clients can exit by typing `exit`.

## Example Chat Session

**Client A:**
```
Enter your username: Alice
Bob: Hi Bob, how are you?
Charlie: Hello Charlie!
```

**Client B (Bob):**
```
Enter your username: Bob
<Alice> Alice: Hi Bob, how are you?
```

**Client C (Charlie):**
```
Enter your username: Charlie
<Alice> Alice: Hello Charlie!
```
