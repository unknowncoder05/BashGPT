# BashGPT Docker Project

This project demonstrates how to create a Docker container for running a Python script that interacts with the ChatGPT API to execute commands in the Bash shell. With this setup, you can send text commands to ChatGPT, and it will execute those commands in a Bash shell environment within the Docker container.

# Security concerns

Yes, Every command ChatGPT provides will be executed, which includes actions such as modifying and creating files, as well as accessing the internet. It has the capability to interact with external resources

No, it does not have access to local files outside the project directory. Its environment is securely encapsulated using Docker, ensuring a restricted scope of operation (at least for now)

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
   make command USER_INPUT="give me a list of astronauts on space right now"
   ```
    or
   ```bash
   USER_INPUT="give me a list of astronauts on space right now" docker-compose up
   ```

   This will start the Python script inside the Docker container, and you will be able to enter text commands.

5. ChatGPT will generate commands that then will be executed and finally be returned to the user

   ```sh
$ sudo make command USER_INPUT="give me a list of astronauts on space right now"
USER_INPUT="give me a list of astronauts on space right now" docker-compose up
Starting bashgpt_main_1 ... done
Attaching to bashgpt_main_1
main_1  | assistant: None
main_1  | Executing: curl -s http://api.open-notify.org/astros.json
main_1  | Command executed successfully
main_1  | internal> function execute_commands: ["{\"people\": [{\"craft\": \"Tiangong\", \"name\": \"Jing Haiping\"}, {\"craft\": \"Tiangong\", \"name\": \"Gui Haichow\"}, {\"craft\": \"Tiangong\", \"name\": \"Zhu Yangzhu\"}, {\"craft\": \"ISS\", \"name\": \"Jasmin Moghbeli\"}, {\"craft\": \"ISS\", \"name\": \"Andreas Mogensen\"}, {\"craft\": \"ISS\", \"name\": \"Satoshi Furukawa\"}, {\"craft\": \"ISS\", \"name\": \"Konstantin Borisov\"}, {\"craft\": \"ISS\", \"name\": \"Oleg Kononenko\"}, {\"craft\": \"ISS\", \"name\": \"Nikolai Chub\"}, {\"craft\": \"ISS\", \"name\": \"Loral O'Hara\"}], \"number\": 10, \"message\": \"success\"}"]
main_1  | assistant: Currently, there are 10 astronauts in space. Here is the list of astronauts:
main_1  | 
main_1  | 1. Jing Haiping - aboard the spacecraft Tiangong
main_1  | 2. Gui Haichow - aboard the spacecraft Tiangong
main_1  | 3. Zhu Yangzhu - aboard the spacecraft Tiangong
main_1  | 4. Jasmin Moghbeli - aboard the International Space Station (ISS)
main_1  | 5. Andreas Mogensen - aboard the International Space Station (ISS)
main_1  | 6. Satoshi Furukawa - aboard the International Space Station (ISS)
main_1  | 7. Konstantin Borisov - aboard the International Space Station (ISS)
main_1  | 8. Oleg Kononenko - aboard the International Space Station (ISS)
main_1  | 9. Nikolai Chub - aboard the International Space Station (ISS)
main_1  | 10. Loral O'Hara - aboard the International Space Station (ISS)
main_1  | 
main_1  | Please let me know if there's anything else I can help you with!
   ```

## Note

- Ensure that you have properly set up your ChatGPT API key in the `.env` file.
- Do not use personal or private data
- The model is subject to reject petitions based on the companies restrictions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

