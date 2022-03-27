# _Real-Time Speech to Image Generation_
## ASU HACKML 2022

This project was inspired by a paper called [Zero-Shot Text-to-Image Generation](https://arxiv.org/abs/2102.12092), by Open AI, that introduces an autoregressive language model called [DALL·E](https://openai.com/blog/dall-e/) trained on images broken into segments that are given natural language descriptions. 

Using the Assembly AI audio transcription API we are able to reproduce elements of the zero-shot capabilities presented in the DALL·E paper, in real-time, using a much less complex model that is trained on a summarized version of the training data they refer to as a meta-data set in the paper [Less is More: Summary of Long Instructions is Better for Program Synthesis](https://arxiv.org/abs/2203.08597).

This is only possible with the combination of robust features present in the Assembly AI API that allow for seamless integration with the machine learning model and web interface framework as well as the corrective language modeling they use to repair malformed input and isolate sentences as they are spoken.

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

### [Assembly AI](https://docs.assemblyai.com/) Real-Time Streaming Transcription
- https://docs.assemblyai.com/walkthroughs#realtime-streaming-transcription
- https://github.com/AssemblyAI/realtime-transcription-browser-js-example


### Zero-Shot Text-to-Image Generation
- https://github.com/lucidrains/DALLE-pytorch

This OpenAI paper analyzes zero-, one-, and few-shot performance on Natural Language Processing tasks using autoregressive language modeling.

    @article{DBLP:journals/corr/abs-2102-12092,
      author    = {Aditya Ramesh and
                   Mikhail Pavlov and
                   Gabriel Goh and
                   Scott Gray and
                   Chelsea Voss and
                   Alec Radford and
                   Mark Chen and
                   Ilya Sutskever},
      title     = {Zero-Shot Text-to-Image Generation},
      journal   = {CoRR},
      volume    = {abs/2102.12092},
      year      = {2021},
      url       = {https://arxiv.org/abs/2102.12092},
      eprinttype = {arXiv},
      eprint    = {2102.12092},
      timestamp = {Tue, 02 Mar 2021 12:11:01 +0100},
      biburl    = {https://dblp.org/rec/journals/corr/abs-2102-12092.bib},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }

### LAFITE: Towards Language-Free Training for Text-to-Image Generation
- https://github.com/drboog/Lafite

The model proposed in this paper is able to produce similar performance on zero-shot benchmarks with 1% of the model size and training data used by the DALL·E model.

    @article{DBLP:journals/corr/abs-2111-13792,
      author    = {Yufan Zhou and
                   Ruiyi Zhang and
                   Changyou Chen and
                   Chunyuan Li and
                   Chris Tensmeyer and
                   Tong Yu and
                   Jiuxiang Gu and
                   Jinhui Xu and
                   Tong Sun},
      title     = {{LAFITE:} Towards Language-Free Training for Text-to-Image Generation},
      journal   = {CoRR},
      volume    = {abs/2111.13792},
      year      = {2021},
      url       = {https://arxiv.org/abs/2111.13792},
      eprinttype = {arXiv},
      eprint    = {2111.13792},
      timestamp = {Thu, 02 Dec 2021 09:37:06 +0100},
      biburl    = {https://dblp.org/rec/journals/corr/abs-2111-13792.bib},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }

### Training Generative Adversarial Networks with Limited Data
- https://github.com/NVlabs/stylegan2-ada-pytorch

This paper presents a more efficient pretraining paradigm that uses a summarized version of training data to reduce superfluous relationships in the data.

    @article{DBLP:journals/corr/abs-2006-06676,
      author    = {Tero Karras and
                   Miika Aittala and
                   Janne Hellsten and
                   Samuli Laine and
                   Jaakko Lehtinen and
                   Timo Aila},
      title     = {Training Generative Adversarial Networks with Limited Data},
      journal   = {CoRR},
      volume    = {abs/2006.06676},
      year      = {2020},
      url       = {https://arxiv.org/abs/2006.06676},
      eprinttype = {arXiv},
      eprint    = {2006.06676},
      timestamp = {Wed, 17 Jun 2020 14:28:54 +0200},
      biburl    = {https://dblp.org/rec/journals/corr/abs-2006-06676.bib},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }


### Learning Transferable Visual Models From Natural Language Supervision
- https://github.com/openai/CLIP

CLIP is an OpenAI model that is able to produce an evaluation metric for good vs bad images necessary for the GANs to properly evaluate images used in the generation aspects of the other papers.

    @article{DBLP:journals/corr/abs-2103-00020,
      author    = {Alec Radford and
                   Jong Wook Kim and
                   Chris Hallacy and
                   Aditya Ramesh and
                   Gabriel Goh and
                   Sandhini Agarwal and
                   Girish Sastry and
                   Amanda Askell and
                   Pamela Mishkin and
                   Jack Clark and
                   Gretchen Krueger and
                   Ilya Sutskever},
      title     = {Learning Transferable Visual Models From Natural Language Supervision},
      journal   = {CoRR},
      volume    = {abs/2103.00020},
      year      = {2021},
      url       = {https://arxiv.org/abs/2103.00020},
      eprinttype = {arXiv},
      eprint    = {2103.00020},
      timestamp = {Thu, 04 Mar 2021 17:00:40 +0100},
      biburl    = {https://dblp.org/rec/journals/corr/abs-2103-00020.bib},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }
