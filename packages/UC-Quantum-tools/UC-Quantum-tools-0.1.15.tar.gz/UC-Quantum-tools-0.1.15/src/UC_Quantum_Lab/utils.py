# generates binary strings
def _getbin(n, s=['']):
    global _config
    if n > 0: return [*_getbin(n - 1, [i + '0' for i in s]), *_getbin(n - 1, [j + '1' for j in s])]
    return s

def get_binary_strings(num_qubits:int) -> list[str]:
    return _getbin(num_qubits)