import socket
import time

def send_post_request():
    host = "example.com"
    port = 80
    resource = "/submit-form"

    # Define the form data
    form_data = "name=John&email=john@example.com&message=Hello, world!"

    # Create the HTTP request with customized header
    request = (
        f"POST {resource} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(form_data)}\r\n"
        f"Custom-Header: CustomValue\r\n"
        f"\r\n"
        f"{form_data}"
    )

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send the HTTP request
    client_socket.sendall(request.encode())

    # Receive the response
    response = b""
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data

    # Close the connection
    client_socket.close()

    # Print the response
    print(response.decode())

if __name__ == "__main__":
    send_post_request()
