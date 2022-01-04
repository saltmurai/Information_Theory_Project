def hamming_74(codeWord):
    """
    This function take 4 bit string in binary format and encode it following
    hamming(7,4) algorithm
    1   2   3   4   5   6   7
    p1  p2  x3  p4  x2  x1  x0
    """
    if len(codeWord) != 4:
        print("Error, must be a bit value")
        return -1
    x = [int(x) for x in list(codeWord)]
    p1 = x[0] ^ x[1] ^ x[3]
    p2 = x[0] ^ x[2] ^ x[3]
    p4 = x[1] ^ x[2] ^ x[3]
    hamming = [p1, p2, x[0], p4, x[1], x[2], x[3]]
    codedWord = [str(bit) for bit in hamming]
    codedWord = "".join(codedWord)
    return codedWord


def decodeHamming7_4(hammingCode):
    """
    Input: 7 bits Hamming code
    Return: original 4 bits coded word
    1   2   3   4   5   6   7
    p1  p2  x3  p4  x2  x1  x0
    Example: 1100110 -> 0110
    """
    if len(hammingCode) != 7:
        print("Error: Must be a 7 bit value")
        return -1

    hammingCode_int = [int(bit) for bit in hammingCode]

    # Getting the parity bits and data bits
    p1 = hammingCode_int[0]
    p2 = hammingCode_int[1]
    p4 = hammingCode_int[3]
    x3 = hammingCode_int[2]
    x2 = hammingCode_int[4]
    x1 = hammingCode_int[5]
    x0 = hammingCode_int[6]

    # Compute the check bits
    c1 = p1 ^ x3 ^ x2 ^ x0
    c2 = p2 ^ x3 ^ x1 ^ x0
    c3 = p4 ^ x2 ^ x1 ^ x0

    # Compute the position of 1 error bit
    pos = c1 * 1 + c2 * 2 + c3 * 4
    
    # If error flip the error bit
    if pos:
        if hammingCode_int[pos - 1] == 0:
            hammingCode_int[pos - 1] = 1
        else:
            hammingCode_int[pos - 1] = 0
    
    # Return the orginal codeword
    decoded = (
        str(hammingCode_int[2])
        + str(hammingCode_int[4])
        + str(hammingCode_int[5])
        + str(hammingCode_int[6])
    )
    return decoded


def main():
    print(hamming_74("0111"))
    print(decodeHamming7_4("0001110"))


if __name__ == "__main__":
    main()
