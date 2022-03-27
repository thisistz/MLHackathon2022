# MLHackathon2022

This is a speech to image generation using Assembly AI and Lafite GAN. 

The idea is to transcribe voice input and generate images in real-time.

## Install and Build the Environment

#### starting from the top level directory of `/MLHackathon2022/`

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cd realtime-transcription`
5. `npm install`
6. open a separate terminal and run `npm run server`
7. open a separate terminal and run `npm run client`
8. `cd ../Lafite` switch to the **Lafite** directory
9. `sudo wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1tMD6MWydRDMaaM7iTOKsUK-Wv2YNDRRt' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1tMD6MWydRDMaaM7iTOKsUK-Wv2YNDRRt" -O "COCO2014_CLIP_ViTB32_all_text.pkl" && rm -rf /tmp/cookies.txt`
10. open a separate terminal and run `python model.py`

## References and Resources

https://github.com/drboog/Lafite

https://docs.assemblyai.com/walkthroughs#realtime-streaming-transcription

https://www.assemblyai.com/blog/real-time-speech-recognition-with-python/?_ga=2.67064554.535427374.1648252128-2040114862.1648252128&_gac=1.215489893.1648252155.Cj0KCQjw0PWRBhDKARIsAPKHFGjWPjrvsxOa-noZCEs0dHDA1ysmYWx_ceFbMiPAx6WXvo1zIhqskBQaAvfVEALw_wcB

https://github.com/AssemblyAI/realtime-transcription-browser-js-example




