# oterm - Generate and Execute Linux Commands using OpenAI

`oterm` is a tool that uses OpenAI to generate Linux commands based on natural language prompts. It supports several key flags for different functionalities.

## Features

- Generate Linux commands from natural language prompts.
- Explain the generated commands.
- Automatically execute the generated commands.
- Interactive mode for chatting and generating commands interactively.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/glassmansam/oterm.git
   cd oterm
   ```

2. Install dependencies:
   ```sh
   pip install openai
   ```

3. Make the `oterm.py` script executable:
   ```sh
   chmod +x oterm.py
   ```

4. Optionally, move the `oterm.py` script to a directory in your PATH for easier access:
   ```sh
   sudo mv oterm.py /usr/local/bin/oterm
   ```

5. Set your OpenAI API key in the `oterm.py` script:
   ```python
   openai.api_key = 'your-openai-api-key'
   ```

## Usage

- Generate a command:
  ```sh
  oterm "List all files in the current directory"
  ```

- Explain the generated command:
  ```sh
  oterm "List all files in the current directory" -e
  ```

- Automatically execute the generated command:
  ```sh
  oterm "List all files in the current directory" -y
  ```

- Start an interactive session:
  ```sh
  oterm -i
  ```

## Flags

- `-e`, `--explain`: Explain the generated command.
- `-y`, `--yes`: Automatically execute the generated command.
- `-i`, `--interactive`: Start an interactive session.

## Example

```sh
oterm "Show the current disk usage"
```

```sh
oterm "Show the current disk usage" -e
```

```sh
oterm "Show the current disk usage" -y
```

```sh
oterm -i
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.
