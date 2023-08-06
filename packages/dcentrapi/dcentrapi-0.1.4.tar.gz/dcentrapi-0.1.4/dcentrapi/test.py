from dcentrapi import MerkleTree
from dcentrapi.merkleTree import verify_leaf

tree = MerkleTree("develop", "Chainport", 'f3taga-mHNLlv8KDh_HE76oOGyU')
leaf1 = ("0x9D9fF3A3A147fb5F96d773E244BAc63Ffa1F21C9", 307835000000000028, 1)
leaf2 = ("0x9D9fF3A3A147fb5F96d773E244BAc63Ffa1F21C9", 99366666666666676687, 2)
leaf3 = ("0x9D9fF3A3A147fb5F96d773E244BAc63Ffa1F21C9", 38500000000000003, 3)
leaves = [leaf1, leaf2, leaf3]
encoding = "(address,uint256,uint256)"
root, layers = tree.build_tree(leaves, encoding)
print(root.hashValue.hex())


leaf_not_in_tree = ("0x9D9fF3A3A147fb5F96d773E244BAc63Ffa1F21C9", 38500000000000003, 4)
proof1 = tree.get_proof(leaf=leaf1)
proof1 = [bytes(p.hashValue) for p in proof1]
assert verify_leaf(root=root.hashValue.hex(), leaf=leaf1, proof=proof1, encoding=encoding)
assert verify_leaf(root=root.hashValue.hex(), leaf=leaf_not_in_tree, proof=proof1, encoding=encoding) is False

