import matplotlib.pyplot as plt
import argparse
import numpy
from scipy.io.wavfile import read, write

import hamming
from channel import Channel

parser = argparse.ArgumentParser()
parser.add_argument("soundPath", help="Path to sound file")
parser.add_argument("errorRate", help="Errror rate of channel")
args = parser.parse_args()


def plotSound(path):
    """
    This function take input as a 8-bit
    audio file and plot the sound wave
    """
    input = read(path)
    audio = input[1]
    plt.plot(audio[0:33100])
    plt.ylabel("Amplitude")
    plt.xlabel("Time (1/10 ms)")
    plt.title("original " + path)
    plt.show()
    plt.clf()
    return audio


def main():
    audio = plotSound(args.soundPath)
    audioCodedValue = []
    for value in audio:
        audioCodedValue.append(f"{value:08b}")
    codedAudio1 = []
    codedAudio2 = []
    for codeWord in audioCodedValue:
        halfCodedWord1 = codeWord[0:4]
        halfCodedWord2 = codeWord[4:]
        coded1 = hamming.hamming_74(halfCodedWord1)
        coded2 = hamming.hamming_74(halfCodedWord2)

        codedAudio1.append(coded1)
        codedAudio2.append(coded2)

    errorRate = int(args.errorRate)

    # Pass the audio through the channel
    channel = Channel(audioCodedValue, errorRate)
    corruptedMsg = channel.getCorruptedMessage()

    # translation of the corrupted msg from bits to integers
    for i in range(len(corruptedMsg)):
        corruptedMsg[i] = int(corruptedMsg[i], 2)

    # plot of the corrupted msg
    plt.plot(corruptedMsg[0:33100])
    plt.ylabel("Amplitude")
    plt.xlabel("Time (1/10 ms) ")
    plt.title("Corrupted " + args.soundPath)
    plt.show()
    plt.clf()
    dt = numpy.dtype(numpy.uint8)
    data = numpy.array(corruptedMsg, dtype=dt)
    write("corrupted_" + args.soundPath, 11025, data)
    channelAudio1 = Channel(codedAudio1, errorRate)
    channelAudio2 = Channel(codedAudio2, errorRate)
    decodedHammingAudioBinary = []
    # we get the 7 bits corrupted values from channelAudio1,2
    corruptedHamMsg1 = channelAudio1.getCorruptedMessage()
    corruptedHamMsg2 = channelAudio2.getCorruptedMessage()

    # Decoded the message
    for i in range(len(corruptedHamMsg1)):
        half1 = hamming.decodeHamming7_4(corruptedHamMsg1[i])
        half2 = hamming.decodeHamming7_4(corruptedHamMsg2[i])
        decodedWord = half1 + half2
        decodedHammingAudioBinary.append(decodedWord)

    # Translation from bit to integers
    for i in range(len(decodedHammingAudioBinary)):
        decodedHammingAudioBinary[i] = int(decodedHammingAudioBinary[i], 2)

    # plot of the corrected msg
    plt.plot(decodedHammingAudioBinary[0:33100])
    plt.ylabel("Amplitude")
    plt.xlabel("Time (1/10 of ms) ")
    plt.title("Decoded and Corrected sound")
    plt.show()

    dt = numpy.dtype(numpy.uint8)
    data = numpy.array(decodedHammingAudioBinary, dtype=dt)
    write("corrected_" + args.soundPath, 11025, data)


if __name__ == "__main__":
    main()
