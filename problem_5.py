import datetime
import hashlib

class Block:

      def __init__(self, timestamp, data, previous_hash):
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calc_hash()
            self.next = None

      def calc_hash(self):
            sha = hashlib.sha256()
            sha.update(self.data.encode('utf-8'))
            return sha.hexdigest()

class Blockchain:
      
      def __init__(self):
            self.head = None
            self.tail = None

      def append(self, data):
            if data is None or data == "":
                  return
            
            elif self.head is None:
                  self.head = Block(self.get_timestamp(), data, 0)
                  self.tail = self.head
            else:
                  self.tail.next = Block(self.get_timestamp(), data, self.tail.hash)
                  self.tail = self.tail.next

      def get_timestamp(self):
            timestamp = datetime.datetime.utcnow()
            return timestamp.strftime("%H:%M:%S %m/%d/%Y")
        
      def get_chain(self):
            output = []
            block = self.head
            while block:
                  output.append([block.data, block.timestamp, block.hash, block.previous_hash])
                  block = block.next
            return output


blockchain = Blockchain()
blockchain.append("first")
blockchain.append("next")
blockchain.append("last")
print(blockchain.get_chain()) #list should have first, next, and last blocks

second_blockchain = Blockchain()
second_blockchain.append("") 
print(second_blockchain.get_chain()) #list should be empty
second_blockchain.append("test")
second_blockchain.append("")
print(second_blockchain.get_chain()) #list should have one block, "test"
      

