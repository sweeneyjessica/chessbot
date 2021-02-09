# chessbot

Final project for Ling 575 Spoken Dialog Systems.

run `conda env create -f environment.yml` to copy the environment

When you run `mvp.py`, it will start a loop that listens for 6 seconds to your chess move, then sends that sound file to Wit.ai and returns the processed message. Your move, as understood by their ASR, is read back to you. You can either hit enter to continue providing data, or type "stop" to stop.

Once you've given the data, it'll show up in the "Understanding" tab on our project page. To correct an utterance and add it for training, you have to listen to it, then click the check-mark on the side, then click the down arrow on the right. You can edit the string, the intent, the entities, and their values; once they're correct, click "Train and validate". I don't know why it doesn't delete it from the list after this, but you can click X to make it go away (it'll still be used for training and show up in the Utterances list afterwards).   