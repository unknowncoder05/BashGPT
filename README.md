# BashGPT Docker Project

This project demonstrates how to create a Docker container for running a Python script that interacts with the ChatGPT API to execute commands in the Bash shell. With this setup, you can send text commands to ChatGPT, and it will execute those commands in a Bash shell environment within the Docker container.

## Prerequisites

Before you start, ensure you have the following prerequisites:

- Docker and DockerCompose installed on your system.
- ChatGPT API credentials. You can obtain these credentials by signing up for the OpenAI API.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chatgpt-docker-project.git
   cd chatgpt-docker-project
   ```

2. Create a `.env` file in the project directory and add your ChatGPT API credentials:

   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

3. Build the Docker image:
     ```bash
   make build
   ```

   or

   ```bash
   docker-compose build
   ```

4. Run the Docker container:

    ```bash
   make command USER_INPUT="create facebook in python"
   ```
    or
   ```bash
   USER_INPUT="create facebook in python" docker-compose up
   ```

   This will start the Python script inside the Docker container, and you will be able to enter text commands.

5. Enter text commands, and ChatGPT will execute them in the Bash shell environment. For example, you can type:

   ```
   Execute the following commands:
   echo "Hello, ChatGPT"
   ls -l
   ```

   ChatGPT will process the input and execute the provided commands.

6. To exit the Docker container, simply type `exit`.

## Note

- Ensure that you have properly set up your ChatGPT API key in the `.env` file.
- Always be cautious when executing shell commands obtained from external sources, as they can potentially be harmful.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

