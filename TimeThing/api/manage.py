import logging

logging.basicConfig(
        filename='public/logs.log',
        filemode='a',
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        level=logging.INFO
        )

LOGGER = logging.getLogger('timething')

from fastapi import FastAPI, Request
from datetime import datetime
import os
import shutil
import pandas as pd

app = FastAPI()

FILEDIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public', 'files')
OUTDIR = os.path.join(FILEDIR, 'aligned')
CSVPATH = os.path.join(FILEDIR, 'text.csv')
COMMAND = f"timething align --language english --metadata {CSVPATH} --alignments-dir {OUTDIR} --batch-size {16} --n-workers {8}"

os.umask(0o000)
os.makedirs(OUTDIR, exist_ok=True)

@app.post("/")
async def root(request: Request):
    data = await request.json()

    LOGGER.info('Request received')

    # Inference on only one file
    if type(data['filename']) == str:
        LOGGER.info('Number of files: 1')
        LOGGER.info(f"- Filename: {data['filename']}")

        text_path = os.path.join(FILEDIR, 'text', f"{data['filename']}.txt")
        mp3_path = os.path.join(FILEDIR, 'audio', f"{data['filename']}.mp3")

        with open(text_path, 'r') as f:
            text = ' '.join([line.strip() for line in f.readlines()])
        pd.DataFrame({'mp3': [mp3_path], 'text': [text]}).to_csv(CSVPATH, index=False, header=False, sep='|')
    # Inference on multiple files
    elif type(data['filename']) == list:
        LOGGER.info(f"Number of files: {len(data['filename'])}")
        for filename in data['filename']:
            LOGGER.info(f"- Filename: {filename}")

        text_paths = [os.path.join(FILEDIR, 'text', f"{filename}.txt") for filename in data['filename']]
        mp3_paths = [os.path.join(FILEDIR, 'audio', f"{filename}.mp3") for filename in data['filename']]

        texts = []
        for text_path in text_paths:
            with open(text_path, 'r') as f:
                texts.append(' '.join([line.strip() for line in f.readlines()]))
        pd.DataFrame({'mp3': mp3_paths, 'text': texts}).to_csv(CSVPATH, index=False, header=False, sep='|')
    # Error
    else:
        LOGGER.info('Error: Invalid request')
        return {'success': False}

    LOGGER.info('Metadata file created')
    LOGGER.info('Running command')
    os.system(COMMAND)

    LOGGER.info('Command finished')

    return {'success': True}
