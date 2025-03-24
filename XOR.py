def or_gate(a, b):
    return a | b  # OR operation

def nand_gate(a, b):
    return not (a and b)  # NAND operation

def and_gate(a, b):
    return a & b  # AND operation

# Implement XOR Gate 
def xor_gate(a, b):
    c = or_gate(a, b)  # OR Gate
    d = nand_gate(a, b) #  NAND Gate
    return and_gate(c, d)  #  AND Gate

# ✅ Testing the XOR Gate
def test_xor_gate():
    assert xor_gate(0, 0) == 0  
    assert xor_gate(0, 1) == 1 
    assert xor_gate(1, 0) == 1 
    assert xor_gate(1, 1) == 0  
    print("All tests passed! ")

test_xor_gate()
