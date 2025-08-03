# AI Calling Agent

## Project Structure & Approach

This is a real-time AI voice agent. In which i have used **Twilio (for phone calls)** which connects with **Deepgram (for speech-to-text and text-to-speech)**, and i am using Python's asyncio and websockets for concurrency and real-time streaming.

### How my project works

I am using **WebSocket Server:** The server listens on localhost:5000 for incoming WebSocket connections from Twilio's Voice Stream.

### Audio Streaming

Incoming audio from Twilio is received, decoded, and queued. Audio is sent to Deepgram's Agent API for transcription and AI-driven conversation.  

Responses (text and audio) from Deepgram are sent back to Twilio.

### Function Calls

The agent can trigger "function calls" (open_call, collect_customer_info, etc.) as defined in ```functions.py```.
These functions use business logic like eligibility checks and call logging.

### Configurable Agent

The agent's behavior, prompt, and available functions are defined in ```config.json``` This allows me to customize the agent's script and logic without changing code.

### Local Development

I have used ngrok to expose local server to Twilio for webhook testing. It creates a secure tunnel from a public endpoint (a URL provided by ngrok) to my locally running server.

### Key Files

- ```main.py:``` Main server logic, handles WebSocket connections, audio streaming, and function call routing.  
- ```functions.py:``` Implements business logic functions the agent can call.  
- ```config.json:``` Agent configuration, prompt, and function definitions.
- ```README.md:``` Project overview and setup instructions.

## Tech Architecture

1. [Python 3.11](https://www.python.org/)
2. [Deepgram](https://deepgram.com/) — Real-time Speech-to-Text API for transcription
3. [Twilio](https://www.twilio.com/en-us) — Programmable Voice API to handle calls
4. [ngrok](https://ngrok.com/) — Secure tunnel to expose localhost for webhook testing

### Thank You

**Akash Jha**  
[Connect on LinkedIn](https://www.linkedin.com/in/iamakashjha1/)  
Data Scientist & AI/ML Engineer
