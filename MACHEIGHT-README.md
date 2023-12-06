# Macheight technical challenge

Welcome to the initial technical evaluation for joining macheight. In this assessment, we expect you to showcase your debugging proficiency, ability to write clean code, and your expertise in algorithms and data structures.

For this test, we have taken an open-source project. This project is a pair programming AIDER powered by LLM that helps you write code with simple instructions in natural language. You can Refer to the official documentation here: [AIDER](https://aider.chat/)

We have made the following modifications to the source code:
- Added a proxy so you do not have to use an OpenAI API key.

## Installation Instructions
- Begin by cloning this repository: `git clone https://github.com/jahelsantiago/aider.git`
- Establish a new branch with your name: `git checkout -b <your-name>`
- Set up a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install the necessary dependencies: `pip install -r requirements.txt`

## Run instructions 
- Execute the LLM proxy `litellm --model huggingface/codellama/CodeLlama-34b-Instruct-hf --max_tokens 2048`
- Open a new terminal tab
- Launch the application using: `python -m aider.main --openai-api-base http://0.0.0.0:8000`


## First task

Aider supports commands from within the chat, which all start with /. Here are some of the most useful in-chat commands:

* `/add <file>`: Add matching files to the chat session.
* `/drop <file>`: Remove matching files from the chat session.
* `/undo`: Undo the last git commit if it was done by aider.
* `/diff`: Display the diff of the last aider commit.
* `/run <command>`: Run a shell command and optionally add the output to the chat.
* `/voice`: Speak to aider to [request code changes with your voice](https://aider.chat/docs/voice.html).
* `/help`: Show help about all commands.

When the user types a command that is not available, the application returns a recommendation with the command that is more similar to the one that the user typed. Example:

<img width="228" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/ffea2120-da3d-498b-9564-1df9e9f1cdc1">

However, one of our users reported a strange behavior that you should check. Here are the steps to reproduce the bug state:

- Initially, start the application. You can refer to the [Run instructions](#Run).
- Once the application is running, write the command `/drop` and then the command `/clear`
- After doing this, input the command `/show-chat-history`, which makes the application hang for a few seconds and then shows the message:

    <img width="316" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/f9db8ae6-0721-4763-9925-71af1d920a77">

The unusual behavior is that the applications hang for more time when the invalid command `/show-chat-history` is typed compared with commands as `/close` or `/report` are entered.

Rectify the reported issue and fix it.

## Second task

The `/add` command is used to add files to the chat session. The chat session is visible at the top of the input. For example, if `/add hello.py` is typed, the chat session will show:

<img width="320" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/898d0437-3803-4ee7-b148-99dadf33d2af">

It is also possible to add multiple files at once by typing them separated by a space: `/add hello.py setup.py` and the chat session will show:

<img width="342" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/5d6edf87-2694-4565-8b1d-29d94d46434d">


If a folder is provided, it should add all the files in that folder and its subfolders. For example, given the structure:

```bash
- folder
    - text1.txt
    - text2.txt
    - subfolder1
        - text3.txt
        - subfolder2
            - text4.txt
```

If `/add folder` is typed, the chat session should show all the files in the directory folder and its subfolders:

<img width="864" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/ac9f204d-a1dc-46cf-9842-89de18909734">

However, the application is not working as expected. When `/add folder` is typed, the chat session incorrectly shows:

<img width="217" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/3edad6ba-5fc8-4642-bc71-29b71da7e150">

A similar case happens with wild cards. If `/add folder/*` is typed, It should add all the files in the folders and subfolders:

<img width="878" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/13f0e3e9-0a7a-4c3b-991b-fc672020467b">


But instead, it shows:

<img width="335" alt="image" src="https://github.com/jahelsantiago/aider/assets/47577344/c8882e5a-9b3f-482e-b342-8ec1c74bb428">

Rectify the reported issue and fix it.


## Evaluation Criteria
- Finding and solving the bugs
- Written tests around the solutions implemented
- Quality and readability of code


## Deliverables
- [ ] Create one commit for each task. Upload a Pull request with your changes to the repository that was assigned to you.
- [ ] Send us an email once you are finished.
