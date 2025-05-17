import requests
import time
import random
import getpass

# ASCII Header
def print_header():
    header = """
    ╔════════════════════════════════════╗
    ║      Hyperbolic Chatbot v1.0       ║
    ║ Powered by Hyperbolic API          ║
    ╚════════════════════════════════════╝
    """
    print(header)

# API Configuration
URL = "https://api.hyperbolic.xyz/v1/chat/completions"

# List of 100 unique questions
questions = [
    "What's the best way to learn programming?",
    "How does quantum computing work?",
    "What are some healthy breakfast ideas?",
    "Can you explain blockchain technology?",
    "What's the weather like on Mars?",
    "How do I improve my photography skills?",
    "What are the benefits of meditation?",
    "How does artificial intelligence work?",
    "What's the history of the internet?",
    "Can you suggest some good books to read?",
    "What’s the meaning of life?",
    "How do I make a perfect cup of coffee?",
    "What are the latest space discoveries?",
    "How can I stay motivated to exercise?",
    "What’s the future of electric cars?",
    "How do I start a small business?",
    "What are some fun weekend activities?",
    "Can you explain the theory of relativity?",
    "What’s the best way to learn a language?",
    "How does the stock market work?",
    "What’s the best way to save money?",
    "How do I plan a trip abroad?",
    "What are the effects of climate change?",
    "How does Wi-Fi actually work?",
    "What’s the history of video games?",
    "How can I improve my public speaking?",
    "What’s the science behind rainbows?",
    "How do I grow indoor plants successfully?",
    "What are the benefits of drinking water?",
    "How does cryptocurrency mining work?",
    "What’s the history of chocolate?",
    "How can I reduce stress in my life?",
    "What are some tips for better sleep?",
    "How do solar panels generate electricity?",
    "What’s the best way to cook steak?",
    "How does the human brain process memory?",
    "What are some must-visit places in Europe?",
    "How do I start investing in stocks?",
    "What’s the difference between viruses and bacteria?",
    "How can I make my home more eco-friendly?",
    "What’s the history of the Olympic Games?",
    "How do I train a dog effectively?",
    "What are the benefits of yoga?",
    "How does 3D printing work?",
    "What’s the best way to learn guitar?",
    "How do airplanes stay in the air?",
    "What are some creative writing tips?",
    "How does the immune system fight diseases(Author: Grok, Created by xAI) fight diseases?",
    "What’s the future of space travel?",
    "How can I improve my time management?",
    "What’s the history of pizza?",
    "How do I create a budget?",
    "What are the benefits of recycling?",
    "How does virtual reality work?",
    "What’s the best way to study for exams?",
    "How do I make homemade bread?",
    "What are the causes of global warming?",
    "How does GPS technology work?",
    "What’s the history of photography?",
    "How can I boost my creativity?",
    "What are some tips for healthy eating?",
    "How do self-driving cars function?",
    "What’s the best way to learn cooking?",
    "How does the moon affect tides?",
    "What are some fun science experiments?",
    "How do I start a podcast?",
    "What’s the history of democracy?",
    "How can I improve my drawing skills?",
    "What are the benefits of journaling?",
    "How does nuclear energy work?",
    "What’s the best way to plan a party?",
    "How do I maintain a car properly?",
    "What are some tips for traveling cheap?",
    "How does the internet of things work?",
    "What’s the history of coffee?",
    "How can I learn to code faster?",
    "What are the benefits of team sports?",
    "How do black holes form?",
    "What’s the best way to declutter my home?",
    "How does machine learning differ from AI?",
    "What are some tips for gardening?",
    "How do I make a good first impression?",
    "What’s the history of the English language?",
    "How can I stay productive working from home?",
    "What are the benefits of learning history?",
    "How does the human eye see color?",
    "What’s the best way to train for a marathon?",
    "How do I start a blog?",
    "What are some unusual animal facts?",
    "How does sound travel through the air?",
    "What’s the history of fashion?",
    "How can I improve my negotiation skills?",
    "What are the benefits of mindfulness?",
    "How do I build a simple website?",
    "What’s the best way to learn math?",
    "How does evolution work?",
    "What are some tips for reducing waste?",
    "How do I choose a good wine?",
    "What’s the future of renewable energy?"
]

# Verify we have 100 questions
print(f"Total questions loaded: {len(questions)}")

# Function to get API key from user
def get_api_key():
    return getpass.getpass("Please enter your Hyperbolic API key: ")

# Function to send API request
def send_chat_request(question, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# Main bot loop
def run_chat_bot():
    print_header()
    print("Starting advanced chat bot...")
    
    # Get API key from user
    api_key = get_api_key()
    
    question_count = 0
    available_questions = questions.copy()  # Work with a copy to preserve original list
    
    try:
        while True:
            # Reset available questions if empty
            if not available_questions:
                print("Resetting question list after exhausting all questions...")
                available_questions = questions.copy()
            
            # Pick and remove a random question to avoid repetition
            question = random.choice(available_questions)
            available_questions.remove(question)
            
            question_count += 1
            
            # Send request and print results
            print(f"\nQuestion {question_count}: {question}")
            answer = send_chat_request(question, api_key)
            print(f"Answer: {answer}")
            
            # Random delay between 1-2 minutes (60-120 seconds)
            delay = random.uniform(60, 120)
            print(f"Waiting {delay:.1f} seconds before next question...")
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("\nChat bot stopped by user!")
        print(f"Total questions asked: {question_count}")

# Run the bot
if __name__ == "__main__":
    run_chat_bot()
