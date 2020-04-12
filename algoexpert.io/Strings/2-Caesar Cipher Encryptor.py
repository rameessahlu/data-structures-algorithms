import string

def caesarCipherEncryptor(_string, key):
	alphabet_dic_indexing_key = dict(zip(string.ascii_lowercase, range(1,27)))
	alphabet_dic_indexing_number = dict( zip(range(1,27),string.ascii_lowercase))
	cipher_text = ''
	for s  in _string:
		_index = (alphabet_dic_indexing_key[s] + key) % 26
		if _index == 0:
			_index = 26
		cipher_text = cipher_text + alphabet_dic_indexing_number[_index]
	return cipher_text
		