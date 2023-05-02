#TranscribeBot

This project will aim to transcribe a video or a bunch of videos to a text file and then create a chat bot that answers questions based on that.

To transcribe the bot, i thought of using the Whisper Model by OpenAI. However, looking at other inferences of it, namely whisper.cpp and whisper-jax, I decided to go with them because of better performance. Seeing how whisper-jax doesn't work on windows, I narrowed it down to whisper.cpp

##Automating whisper.cpp

First, we have to install all the dependencies and the whole process of converting an mp3 file to a text file is quite cumbersome, so we have to automate it.

Step 1 : Download whisper.cpp assets from this link
Step 2 : Download ffmpeg which lets us convert mp3 files to wav files which is the required format from this link
Step 3 : Download the reuqired Whisper model from this link
Step 4 : Extract the files and add the bin folders of both the folders to path.
Step 5 : Create a batch file as I have. The code can be copied from the above files.
And you have automated all the major tasks.\

Now open command prompt and type in the following to transcribe the mp3 file to a text file:
gentext.bat audio.mp3

##Starting with the script

The video that I have transcribed right now is just for trial purposes. At the end I will transcribe Andrej Karpathy's amazing playlist in which he teaches us so much about deep learning. For the vector database i have gone with chromadb instead of pinecone because it is opensource, and will probably choose llama llm because again, it is open source. The end goal here is to allow the user to ask questions from different sources as well, so, maybe allow the users to communicate with different videos, and different creators.

##Choosing llm
Finding opensource llms is a head-ache. I tried to used the llama-cpp-python library but i was unable to install it. After hours of trying, I gave up trying to set it up. Got it to work on colab, so now I have shifted onto there for now as I continue finding open source llms for this project.
