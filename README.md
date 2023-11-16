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

## Logs



