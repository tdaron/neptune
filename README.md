# Neptune - Dynamic Code Execution Server

## Overview

Neptune is a dynamic code execution server that allows you to execute Python code snippets remotely. It uses a Unix socket for communication between the server and the client, enabling you to send code snippets to be executed within a persistent global context. This setup can be useful for various applications, such as rapid prototyping, debugging, or running code in a controlled environment.

## Features

- **Remote Code Execution**: Neptune allows you to execute Python code snippets remotely by sending them to the server via a Unix socket.
- **Shared Global Context**: The server maintains a shared global context across multiple code executions, enabling variables and functions defined in previous snippets to be accessed by subsequent ones.
- **Flexible Usage**: You can use Neptune to run individual code snippets or sequences of code snippets, enabling interactive experimentation and development.

## Prerequisites

To use Neptune, you need:

- Python 3.x installed on your system.
- Basic knowledge of Unix sockets and Python programming.

## Installation

1. Clone the Neptune repository to your local machine:

    ```bash
    git clone https://github.com/tdaron/neptune.git
    ```

2. Navigate to the Neptune directory:

    ```bash
    cd neptune
    ```

3. Run the server script to start the Neptune server:

    ```bash
    python neptune.py
    ```

## Usage

### Sending Code Snippets

You can send code snippets to the Neptune server using the provided client script or any other method that can communicate via Unix sockets.

#### Using the Client Script

1. Run the client script, providing the code snippet via stdin:

    ```bash
    echo -e 'a = 5\nprint(a)' | python client.py
    ```

2. The client script sends the code snippet to the Neptune server via the Unix socket, and the server executes it within the shared global context.

### Syntax for Code Snippets

- You can define variables, functions, and execute any valid Python code within the snippet.
