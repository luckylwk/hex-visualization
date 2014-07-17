##
##
import base64
from Crypto import Random as _crypto_random
from Crypto.Cipher import AES as _crypto_AES
import numpy as _np
import matplotlib.pyplot as _plt




##################
## FUNCTIONS & CLASSES
##
##
def fn_load_text():
	with open('_data/text.txt','rb') as f:
		content = f.read()
	return content
	##################

def fn_hex_range():
	init_int = range(0,16)
	init_hex = [ hex(x)[2] for x in init_int ]
	hex_range = []
	for each_hex in init_hex:
		hex_range += [ each_hex + x for x in init_hex ]
	# Done > return
	return hex_range
	##################

def fn_encrypt( message, passphrase ):
	BLOCK_SIZE = 16
	IV = _crypto_random.new().read(BLOCK_SIZE)
	aes = _crypto_AES.new( passphrase, _crypto_AES.MODE_CFB, IV )
	return base64.b64encode(aes.encrypt(message))
	##################

##################
##################




##################
## MAIN
##
##
if __name__=="__main__":

	text = fn_load_text()

	hex_range = fn_hex_range()

	text_grid = _np.zeros((255,255))
	for e,each_char in enumerate(text):
		if e > 0: # Cannot check first one.
			y_ix = hex_range.index(each_char.encode('hex'))
			x_ix = hex_range.index(text[e-1].encode('hex'))
			text_grid[y_ix,x_ix] += 1


	# ENCRYPT TEXT
	text_enc = fn_encrypt( message=text, passphrase='ThisIsNotEncrypt' )
	text_enc_grid = _np.zeros((255,255))
	for e,each_char in enumerate(text_enc):
		if e > 0: # Cannot check first one.
			y_ix = hex_range.index(each_char.encode('hex'))
			x_ix = hex_range.index(text_enc[e-1].encode('hex'))
			text_enc_grid[y_ix,x_ix] += 1


	# VISUALIZE
	_plt.figure( figsize=(17, 9) )
	_plt.subplot(1,2,1)
	_plt.pcolor(text_grid, cmap=_plt.cm.OrRd)
	_plt.xlim([0, 255])
	_plt.ylim([0, 255])
	_plt.subplot(1,2,2)
	_plt.pcolor(text_enc_grid, cmap=_plt.cm.OrRd)
	_plt.colorbar()
	_plt.show()


##################
##################
