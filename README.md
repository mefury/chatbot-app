# Hyperbolic Labs Chatbot
This repository contains a simple automated chatbot built using the [Hyperbolic Labs API](https://app.hyperbolic.xyz). The chatbot asks 100 unique, pre-defined questions and retrieves answers from the API, simulating a conversational AI experience. It’s a fun demonstration of how to integrate Hyperbolic Labs' AI models into a Python application.

## About Hyperbolic
[Hyperbolic Labs](https://hyperbolic.xyz) provides an accessible and affordable platform for AI development, offering open-access AI models and scalable computing resources via their API.
* This project uses their language model (`meta-llama/Meta-Llama-3.1-8B-Instruct`) to generate responses to a variety of questions, showcasing the power of their tools for developers.
* Check out their [official documentation](https://docs.hyperbolic.xyz) for more details.

## Features
- Contains a list of 100 unique questions on diverse topics.
- Randomly selects and asks questions without repetition.
- Integrates with the Hyperbolic Labs API to fetch answers.
- Adds random delays (1-2 minutes) between questions to simulate natural pacing.
- Built with Python and the `requests` library.

## Prerequisites
- Python 3.6+
- A [Hyperbolic API key](https://app.hyperbolic.xyz/settings) (replace the placeholder in the code with your own key)

## Setup
1. **Install Packages**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install git screen python3 python3-pip python3-venv -y
   ```
2. **Clone the Repository**
   ```bash
   git clone https://github.com/mefury/chatbot-app.git
   cd chatbot-app
   ```
3. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install requests
   ```
4. **Get your API Key**

The bot will ask your Hyperbolic API key, Get your hyperbolic API Key from here [Hyperbolic API Key](https://app.hyperbolic.xyz/settings):

5. **Run the Chatbot**

* You can enter `screen -S chat` before running it to run the script on a minimizable screen in background.
* To minimize screen: `CTRL+A+D`
* To kill screen: `Ctrl+C` or command: `screen -XS chat quit`

Execute the script to start the chatbot:
   ```bash
   python3 chatbot.py
   ```






