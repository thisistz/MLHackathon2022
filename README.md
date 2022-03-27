# MLHackathon2022

This is a speech to image generation using Assembly AI and Lafite GAN. 

The idea is to transcribe real-time voice input and generate images in real-time.

### Install and Build the Environment

starting from the top level directory

1. `cd realtime-transcription`
1. `npm install`
1. open a seperate terminal and run `npm run server`
1. open a seperate terminal and run `npm run client`
1. install selenium driver according to operating system https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
1. `cd ..` return to the top level directory
1. `python -m venv venv`
1. `source venv/bin/activate`
1. `pip install selenium`
  1. The execuation path for the chrome driver is looking for `../selenium/chromedriver` in `Lafite/model.py` so save the chrome driver there are change the `executable_path='../selenium/chromedriver'` argument in `model.py`
1. `cd Lafite`
1. `pip install pip install clip-by-openai`
1. `sudo wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1tMD6MWydRDMaaM7iTOKsUK-Wv2YNDRRt' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1tMD6MWydRDMaaM7iTOKsUK-Wv2YNDRRt" -O "COCO2014_CLIP_ViTB32_all_text.pkl" && rm -rf /tmp/cookies.txt`
1. open a seperate termina and run `python model.py`





https://github.com/drboog/Lafite

https://docs.assemblyai.com/walkthroughs#realtime-streaming-transcription

https://www.assemblyai.com/blog/real-time-speech-recognition-with-python/?_ga=2.67064554.535427374.1648252128-2040114862.1648252128&_gac=1.215489893.1648252155.Cj0KCQjw0PWRBhDKARIsAPKHFGjWPjrvsxOa-noZCEs0dHDA1ysmYWx_ceFbMiPAx6WXvo1zIhqskBQaAvfVEALw_wcB

https://github.com/AssemblyAI/realtime-transcription-browser-js-example




