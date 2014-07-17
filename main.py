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

def fn_hex_grid( input_text, hex_range ):
	# Init grid.
	grid = _np.zeros((256,256))
	# For each combination of letters, populate grid.
	for e,each_char in enumerate(input_text):
		if e > 0: # Cannot check first one.
			y_ix = hex_range.index(each_char.encode('hex'))
			x_ix = hex_range.index(input_text[e-1].encode('hex'))
			grid[y_ix,x_ix] += 1
	# Done > return grid
	return grid
	##################

##################
##################




##################
## MAIN
##
##
if __name__=="__main__":

	# Load text and encrypt the text (CFB?).
	text = fn_load_text()
	text_enc = fn_encrypt( message=text, passphrase='ThisIsNotEncrypt' )

	hex_range = fn_hex_range()

	# Create grids.
	text_grid = fn_hex_grid( input_text=text, hex_range=hex_range )
	text_enc_grid = fn_hex_grid( input_text=text_enc, hex_range=hex_range )

	# VISUALIZE
	_plt.figure( figsize=(17, 9) )
	_plt.subplot(1,2,1)
	_plt.pcolor(text_grid, cmap=_plt.cm.OrRd)
	_plt.xlim([0, 120])
	_plt.ylim([0, 120])
	_plt.subplot(1,2,2)
	_plt.pcolor(text_enc_grid, cmap=_plt.cm.OrRd)
	_plt.xlim([0, 120])
	_plt.ylim([0, 120])
	_plt.colorbar()
	_plt.show()


##################
##################
