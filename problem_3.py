import sys

class Node():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def get_char(self):
        return self.char

    def get_freq(self):
        return self.freq

    def get_node(self):
        return (self.char, self.freq)

    def set_left_child(self, node):
        self.left = node
        
    def set_right_child(self, node):
        self.right = node
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def is_leaf(self):
        return (self.get_left_child() == None and self.get_right_child() == None)

class PriorityQueue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i.get_node()) for i in self.queue])
    
    def length(self):
        return len(self.queue)

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        min_index = 0
        if self.length() > 0:
            for i in range(len(self.queue)):
                #finds the item with the lowest frequency to pop
                if self.queue[i].get_freq() < self.queue[min_index].get_freq():
                    min_index = i
            min_item = self.queue[min_index]
            self.queue.remove(min_item)
            return min_item
        return

#generates the frequencies for the inputted data
def find_freq(string):
    frequencies = dict()
    for char in string:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    return frequencies

#intializes and sets up the queue for popping
def queue_setup(string):
    if len(string) <= 1:
        return None
    frequencies = find_freq(string)
    queue = PriorityQueue()
    while len(frequencies) > 0:
        curr = frequencies.popitem()
        queue.push(Node(curr[0], curr[1]))
    return queue

#variation of preorder that encodes the data
def encode(root, string, bin_dict):
    if root is None:
        return

    if root.get_char():
        bin_dict[root.get_char()] = string
        
    encode(root.left, string + '0', bin_dict)
    encode(root.right, string + '1', bin_dict)
    return bin_dict

#constructs the huffman tree and returns the encoded data and the root node
def huffman_encoding_helper(data):
    queue = queue_setup(data)
    bin_string = ''
    
    if queue is None:
        return ("This data can't be encoded", None)

    if queue.length() == 1:
        child = queue.pop()
        for i in range(child.get_freq()):
            bin_string += '0'
        return (bin_string, child)
            
    while queue.length() > 1:
        min1 = queue.pop()
        min2 = queue.pop()
        node = Node(None, min1.get_freq() + min2.get_freq())
        node.set_left_child(min1)
        node.set_right_child(min2)
        queue.push(node)
    bin_dict = encode(node, '', dict())
    for char in data:
        bin_string += bin_dict[char]
    return (bin_string, node)

#returns the encoded data
def huffman_encoding(data):
    return huffman_encoding_helper(data)[0]

#returns the root node
def root(data):
    return huffman_encoding_helper(data)[1]

#returns the decoded binary data
def huffman_decoding(data, root):
    if data == "" or root is None:
        return "This data can't be decoded"
    decoded_string = ''
    curr = root
    for char in data:
        if not curr.is_leaf():
            if char == '0':
                curr = curr.left
            if char == '1':
                curr = curr.right
        if curr.is_leaf():
            decoded_string += curr.get_char()
            curr = root
    return decoded_string

if __name__ == "__main__":

    #Test Case 1

    print("Test Case 1\n")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, root(a_great_sentence))

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Test Case 2

    print("Test Case 2\n")
    a_great_sentence = "TTTT"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, root(a_great_sentence))

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Test Case 3

    print("Test Case 3\n")
    a_great_sentence = ""

    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = huffman_encoding(a_great_sentence)

    
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, root(a_great_sentence))

    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Test Case 4
    
    print("Test Case 4\n")
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, root(a_great_sentence))

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
