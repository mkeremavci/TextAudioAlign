# TextAudioAlign

## Installation

To build API, follow the commands:

    docker compose build

    docker compose up -d

## Inference

You should place text (.txt) and audio (.mp3) files in the corresponding folders under `public/file`. Text and audio pairs should have the same file name except their extentions.

    public
        ├── files
        │   ├── aligned
        │   ├── audio
        │   │   └── test.mp3
        │   ├── text
        │   │   └── test.txt
        │   └── text.csv
        └── logs.log

Then, you can send a request with `application/json` body in the format given below to the endpoint `http://0.0.0.0:3100/`:

    {
        'filename': 'test'
    }

If you want to run inference on multiple files, you can give the request body in the following format:

    {
        'filename': [
            'test0',
            'test1',
            'test2',
            'test3',
            ]
    }

## Logs



