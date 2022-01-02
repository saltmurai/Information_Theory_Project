def hamming7_4(codeWord):
    """
    Input: 4 bits binary codeword
    Return: 7 bits binary hamming code
    Example: 0110 -> 1100110
    """
    if len(codeWord) != 4:
        print("error : word is not 4 bits long \n")
        return -1

    index = 0
    # Init Hamming code
    hamming = [-1, -1, 2, -1, 2, 2, 2]

    for bit in codeWord:
        while hamming[index] == -1:
            index += 1

        # Transfer data from codeword to Hamming
        if bit == "1":
            hamming[index] = 1
        if bit == "0":
            hamming[index] = 0
        index += 1

    # Set the parity bits
    for i in range(7):

        # if parity bit
        if hamming[i] == -1:
            bitToCheck = i + 1
            bitChecked = 0
            j = i
            parityCount = 0

            while j < 7:

                # check elements
                while bitChecked < bitToCheck:
                    if hamming[j] == 1:
                        parityCount += 1
                    bitChecked += 1
                    j += 1

                bitChecked = 0
                j += bitToCheck

            # if even number of bit 1
            if (parityCount % 2) == 0:
                hamming[i] = 0
            # if odd number of bit 1
            else:
                hamming[i] = 1

    codedWordStr = ""
    for bit in hamming:
        codedWordStr += str(bit)
    return codedWordStr


def decodeHamming7_4(hammingCode):
    """
    Input: 7 bits Hamming code
    Return: original 4 bits coded word
    Example: 1100110 -> 0110
    """
    if len(hammingCode) != 7:
        print("error : word is not 7 bits long \n")
        return -1

    correctMsg = ""

    # getting the parity bit
    parityBit1 = int(hammingCode[0])
    parityBit2 = int(hammingCode[1])
    parityBit4 = int(hammingCode[3])

    # computing the parity bit
    realPB1 = (int(hammingCode[2]) + int(hammingCode[4]) + int(hammingCode[6])) % 2
    realPB2 = (int(hammingCode[2]) + int(hammingCode[5]) + int(hammingCode[6])) % 2
    realPB4 = (int(hammingCode[4]) + int(hammingCode[5]) + int(hammingCode[6])) % 2

    errorBit = 0

    # computing the index of the erroneous bit if any
    if realPB1 != parityBit1:
        errorBit += 1
    if realPB2 != parityBit2:
        errorBit += 2
    if realPB4 != parityBit4:
        errorBit += 4
    errorBit -= 1

    corrected = []
    for bit in hammingCode:
        corrected.append(bit)

    # if error detected, correct the error in corrected
    if errorBit != -1:
        if corrected[errorBit] == "0":
            corrected[errorBit] = "1"
        elif corrected[errorBit] == "1":
            corrected[errorBit] = "0"
        else:
            print("error in decodeHamming7_4 : character was not a bit ")

    # after correction, extraction of the data bits and concatenation with the resulting string
    correctMsg += corrected[2]
    correctMsg += corrected[4]
    correctMsg += corrected[5]
    correctMsg += corrected[6]

    return correctMsg


def main():
    test = hamming7_4("0110")
    print(test)
    print(decodeHamming7_4("1100110"))


if __name__ == "__main__":
    main()
