import random


class Channel:
    """
    Msg: list of hamming code
    prob: Probablity for a bit in the message to be flip
    """
    def __init__(self, msg, prob):
        self.message = msg
        self.corruptedMessage = []

        for word in self.message:
            corruptedWord = ""
            for bit in word:
                error = False
                rand = random.randint(0, 100)
                # Simulation of a random error
                if rand < prob:
                    error = True
                # Depending on the error factor, bits are corrupted or not
                if bit == "0":
                    if error:
                        corruptedWord += "1"
                    else:
                        corruptedWord += "0"

                elif bit == "1":
                    if error:
                        corruptedWord += "0"
                    else:
                        corruptedWord += "1"

            self.corruptedMessage.append(corruptedWord)

    def getMessage(self):
        return self.message

    def getCorruptedMessage(self):
        return self.corruptedMessage
