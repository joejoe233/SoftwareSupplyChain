#coding:utf-8
import hashlib as hasher
import datetime

def create_genesis_block():
    '''Constructs a block with index 0 and arbitrary previous hash'''
    return Block(0, datetime.datetime.now(), "Genesis Block" ,"0","0","0","0")
#操作的是区块对象
class Block():
    def __init__(self, index, timestamp, software,company, addr,cite,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.software = software
        self.company = company
        self.addr = addr
        self.cite = cite #引用字段
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def  hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode("utf-8")
            + str(self.timestamp).encode("utf-8")
            + str(self.software).encode("utf-8")
            + str(self.company).encode("utf-8")
            + str(self.addr).encode("utf-8")
            + str(self.cite).encode("utf-8")
            + str(self.previous_hash).encode("utf-8")
        )
        return sha.hexdigest()

# Create the blockchain and add genesis block.
blockchain = [create_genesis_block()]
#print(blockchain[0].cite)
previous_block = blockchain[0]
#print(previous_block)

# How many blocks to add after the genesis block?
#num_of_blocks_to_add = 10


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    #this_data = "Hey! I'm block " + str(this_index)
    this_software = input("请输入第 #{} 个区块的软件名 : ".format(this_index))
    this_company = input("请输入第 #{} 个区块的公司名 : ".format(this_index))
    this_addr = input("请输入第 #{} 个区块的软件地址 : ".format(this_index))
    this_cite = input("请输入第 #{} 个区块的引用记录 : ".format(this_index))
    return Block(this_index, this_timestamp, this_software, this_company,this_addr,this_cite,last_block.hash)


# Add blocks to the chain.
#for i in range(num_of_blocks_to_add):
while 1:
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print("区块 #{} 成功上链！".format(block_to_add.index))
    print("软件名 :{}".format(block_to_add.software))
    print("公司名 :{}".format(block_to_add.company))
    print("软件地址 :{}".format(block_to_add.addr))
    print("引用记录: {}".format(block_to_add.cite))
    print("哈希值: {}".format(block_to_add.hash))
    print("时间戳: {}\n".format(block_to_add.timestamp))
    #存入数据库
# print(blockchain[0].previous_hash)




