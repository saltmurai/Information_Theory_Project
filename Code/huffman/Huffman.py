import math
import argparse
from tabulate import tabulate
from io import StringIO
buf = StringIO()

parser = argparse.ArgumentParser()
parser.add_argument("textFile", help="Path to sound file")
args = parser.parse_args()
# Một nút cây Huffman
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # Xác suất của ký tự
        self.prob = prob
        # Ký tự
        self.symbol = symbol
        # Nút trái
        self.left = left
        # Nút phải
        self.right = right
        # Hướng của cây (0|1)
        self.code = ""


codes = dict()


def Calculate_Codes(node, val=""):
    """Hàm in mã ký tự khi đi qua Huffman Tree"""
    # Mã Huffman cho nút hiện tại
    newVal = val + str(node.code)

    if node.left:
        Calculate_Codes(node.left, newVal)
    if node.right:
        Calculate_Codes(node.right, newVal)
    if not node.left and not node.right:
        codes[node.symbol] = newVal

    return codes


def Calculate_Probability(data):
    """Hàm tính toán xác suất của các ký tự trong dữ liệu nhất định"""
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    for element in symbols:
        symbols[element] = symbols[element] / len(data)
    return symbols


def Output_Encoded(data, coding):
    """Hàm trợ giúp để lấy đầu ra được mã hóa"""
    encoding_output = []
    for c in data:
        # print(coding[c], end = '')
        encoding_output.append(coding[c])

    string = "".join([str(item) for item in encoding_output])
    return string


def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    etrpy = 0
    # print("Ký tự: ", symbols)
    # print("Xác suất: ", probabilities)
    # Tính Entropy của văn bản
    for symbol in symbols:
        etrpy = etrpy - symbol_with_probs[symbol] * math.log2(symbol_with_probs[symbol])
    # print("Entropy của văn bản là: ", etrpy)

    nodes = []

    # Chuyển đổi các ký hiệu và tần số thành các nút cây Huffman
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # Sắp xếp tất cả các nút theo thứ tự tăng dần dựa trên tần số của chúng
        nodes = sorted(nodes, key=lambda x: x.prob)

        # Chọn 2 nút nhỏ nhất
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        # Kết hợp 2 nút nhỏ nhất để tạo nút mới
        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    # print("Ký tự với mã: ", huffman_encoding)
    # Tính độ dài trung bình của văn bản
    l = 0
    for symbol in symbols:
        L = len(huffman_encoding[symbol])
        l = l + symbol_with_probs[symbol] * L
    # print("Độ dài trung bình của văn bản: ", l)
    kn = etrpy / l
    # print("Hệ số nén: {}/{} = {}".format(etrpy, l, kn))

    encoded_output = Output_Encoded(data, huffman_encoding)
    return (
        encoded_output,
        nodes[0],
        etrpy,
        huffman_encoding,
        l,
        kn,
        symbols,
        probabilities,
    )


def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == "1":
            huffman_tree = huffman_tree.right
        elif x == "0":
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = "".join([str(item) for item in decoded_output])
    return string


def main():

    with open(args.textFile, "r") as f:
        data = f.read()
        (
            encoding,
            tree,
            entrpy,
            huffman_encoding,
            l,
            kn,
            symbols,
            prob,
        ) = Huffman_Encoding(data)
        # Viet output ra file info_
        with open("info_" + args.textFile, 'w') as i:
            headers_1 = ["Ky tu", "Xac suat"]
            table_1 = zip(symbols, prob)
            print(tabulate(table_1, headers=headers_1, floatfmt=".6f", tablefmt="pretty", showindex=1), file=i)
            headers_2 = ["Ky tu", "Tu ma"]
            table_2 = zip(huffman_encoding.keys(), huffman_encoding.values())
            print(tabulate(table_2, headers=headers_2, floatfmt=".6f", tablefmt="pretty", showindex=1), file=i)
            print("Entropy: " + str(entrpy), file=i)
            print("Do dai trung binh cua van ban: " + str(l), file=i)
            print("He so nen: " + str(kn), file=i)
            print("Dau ra duoc ma hoa: " + encoding, file=i)
            print("Dau ra duoc giai ma: " + Huffman_Decoding(encoding, tree), file=i)
        # Print ra man hinh
        print(open('info_' + args.textFile, 'r').read())
        with open("binary_" + args.textFile, "w") as o:
            o.write(str(encoding))
if __name__ == "__main__":
    main()
