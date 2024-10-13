# Realtime RAG Console

This repository is a fork of the OpenAI Realtime Console
(https://github.com/openai/openai-realtime-console).
RAG feature is added to the original one.

# Set API key

Copy `.env.example` to `.env` and set your OpenAI API key.

# Starting the backend

First, locate your PDFs to be refered as data source into `backend/src/pdf/` directory.

Then, start the backend with:

```shell
$ cd backend
$ docker-compose up
```

# Starting the console

```shell
$ npm i
```

Start your server with:

```shell
$ npm start
```

It should be available via `localhost:3000`.

# Using the console

To start a session you'll need to **connect**. This will require microphone access.
You can then choose between **manual** (Push-to-talk) and **vad** (Voice Activity Detection)
conversation modes, and switch between them at any time.

There are functions enabled;

You can freely interrupt the model at any time in push-to-talk or VAD mode.
