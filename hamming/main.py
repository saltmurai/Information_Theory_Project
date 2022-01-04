import numpy
from channel import Channel
import hamming
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


def plotSound(path):
    input = read(path)
    audio = input[1]
    plt.plot(audio[0:33100])
    plt.ylabel("Amplitude")
    plt.xlabel("Time (1/10 ms)")
    plt.title(path)
    plt.show()
    plt.clf()
    return audio


def main():
    audio = plotSound("sound.wav")
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

    # Q11
    # get the audio values coded on 8 bits through the channel
    # with a bit error probability of 'errorRate' percent
    errorRate = 1

    # reminder :audioCodedValue : list of 8 bits strings
    channel = Channel(audioCodedValue, errorRate)
    # print("audioCodedValue : ")
    # print(audioCodedValue)
    # print("audioCodedValue uncorrupted message : ")
    # print(channel.getMessage())
    # print("audioCodedValue corrupted message :")
    # print(channel.getCorruptedMessage())

    corruptedMsg = channel.getCorruptedMessage()

    # translation of the corrupted msg from bits to integers
    for i in range(len(corruptedMsg)):
        corruptedMsg[i] = int(corruptedMsg[i], 2)

    # plot of the corrupted msg
    plt.plot(corruptedMsg[0:33100])
    plt.ylabel("Amplitude")
    plt.xlabel("Time (in 10th of ms) ")
    plt.title("corrupted sound")
    plt.show()
    plt.clf()

    dt = numpy.dtype(numpy.uint8)
    data = numpy.array(corruptedMsg, dtype=dt)
    write("corruptedSound.wav", 11025, data)

    # Q12
    # each audio value was coded on 8bit. In order to code them as hamming codes,
    # they were cut in 2 half word of 4 bits. Each of these coded half words
    # are at the same index
    # in the corresponding codedAudio list. So first half is in codedAudio1 and
    # second half is in codedAudio2, at the same index.
    # We know make them go through our channel.

    # reminder : codedAudio1,2 are lists of 7bits string representing half
    # of a 8 bit value in a hamming code
    errorRate = 1
    channelAudio1 = Channel(codedAudio1, errorRate)
    channelAudio2 = Channel(codedAudio2, errorRate)

    # print("codedAudio1 : ")
    # print(codedAudio1)

    decodedHammingAudioBinary = []
    # we get the 7 bits corrupted values from channelAudio1,2
    corruptedHamMsg1 = channelAudio1.getCorruptedMessage()
    corruptedHamMsg2 = channelAudio2.getCorruptedMessage()

    # print("corruptedHamMsg1 : ")
    # print(corruptedHamMsg1)

    # we go through all corrupted messages and decode them
    for i in range(len(corruptedHamMsg1)):
        half1 = hamming.decodeHamming7_4(corruptedHamMsg1[i])
        half2 = hamming.decodeHamming7_4(corruptedHamMsg2[i])
        decodedWord = half1 + half2
        decodedHammingAudioBinary.append(decodedWord)

    # decodedHammingAudioBinary contains all corrected word
    # we can now convert it back to int, plot it and listen to it.
    # translation of the corrupted msg from bits to integers

    # translation from bit to integers
    for i in range(len(decodedHammingAudioBinary)):
        decodedHammingAudioBinary[i] = int(decodedHammingAudioBinary[i], 2)

    # print("decodedHammingAudioBinary : ")
    # print(decodedHammingAudioBinary)

    # plot of the corrected msg
    plt.plot(decodedHammingAudioBinary[0:33100])
    plt.ylabel("Amplitude")
    plt.xlabel("Time (in 10th of ms) ")
    plt.title("decoded and corrected sound ")
    plt.show()

    dt = numpy.dtype(numpy.uint8)
    data = numpy.array(decodedHammingAudioBinary, dtype=dt)
    write("correctedSound.wav", 11025, data)


if __name__ == "__main__":
    main()
