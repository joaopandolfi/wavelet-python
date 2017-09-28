print("Importando libs")
import pywt
import cv2
import numpy as np
import glob

'''
Wavelets
https://www.mathworks.com/help/wavelet/ref/waveletfamilies.html?requestedDomain=www.mathworks.com
===================================
Haar              		haar           
Daubechies        		db             
Symlets           		sym            
Coiflets          		coif           
BiorSplines       		bior           
ReverseBior       		rbio           
Meyer             		meyr           
DMeyer            		dmey           
Gaussian          		gaus           
Mexican_hat       		mexh           
Morlet            		morl           
Complex Gaussian  		cgau           
Shannon           		shan           
Frequency B-Spline		fbsp           
Complex Morlet    		cmor           
===================================
'''

print("Executando")

print("Lendo diretorio")
files = glob.glob("in/*.jpg")

# Read the two image
#I1 = cv2.imread('i1.bmp',0)
# First: Do wavelet transform on each image
wavelets = ["haar","db","sym","coif",
"bior","rbio","meyr","dmey","gaus","mexh",
"morl","cgau","shan","fbsp","cmor",
"db1","db2","db3","db4",                       
"db5","db6","db7","db8",           
"db9","db10"
]

def funcaofeia(p_wavelet,p_name,I1):
	wavelet = p_wavelet#wavelets[0]#'db1'
	
	
	cooef1 = pywt.wavedec2(I1[:,:], wavelet)

	'''
	for a in range(len(cooef1)):
		print(len(cooef1[a]))

	print("IMAGEM")
	print(I1[:,:])

	print("PRIMEIRA LINHA")
	print(cooef1[0][0])
	print(cooef1[0][1])

	print("SEGUNDA LINHA")

	print(cooef1[1][0])
	print(cooef1[1][1])
	print(cooef1[1][2])
	'''

	# for line in cooef1:
	# 	for cell in line:
	# 		if(cell != 0):
	# 			pass
	
	fusedImage = pywt.waverec2(cooef1, wavelet)

	'''

	print("IMAGEM FUDIDA")
	print(len(fusedImage))

	countLine = 0
	countCol = 0
	countGeral = 0

	print("Elementos não nulos por linha")

	for line in fusedImage:
		countLine = 0
		for cell in line:
			if(cell != 0):
				countLine +=1
		#print(countLine)
		countGeral +=countLine
		if(countLine != 0):
			countCol +=1

	print("COUNT GERAL=>",countGeral)
	print("COUNT LINE =>",countCol)
	print("ZERO LINE =>", len(fusedImage)-countCol)
	'''

	# MAGIA DO STACK
	# Forth: normmalize values to be in uint8
	fusedImage = np.multiply(np.divide(fusedImage - np.min(fusedImage),(np.max(fusedImage) - np.min(fusedImage))),255)
	fusedImage = fusedImage.astype(np.uint8)

	cv2.imwrite(p_name+"-XABLAU.jpg",fusedImage)

	#print(len(cooef1))

	cooef2 = pywt.dwt(I1[:,:], wavelet)
	#cooef3 = pywt.dwt(I1[:,:], wavelet)

	#print("COEF 2")
	#print(cooef2[0])
	#for cell in cooef2[0]:
	#	print(cell, end=" ")
	#print(len(cooef2[1]))

	cv2.imwrite(p_name+"-Digital-BIGODINHO-0.jpg",cooef2[0])
	cv2.imwrite(p_name+"-Digital-BIGODINHO-1.jpg",cooef2[1])

	#cv2.imwrite(p_name+"-Anal-DANONINHO-0.jpg",cooef3[0])
	#cv2.imwrite(p_name+"-Anal-DANONINHO-1.jpg",cooef3[1])



for boi in files:
	print("===================> RODANDO IMAGEM "+ boi)
	img1 = cv2.imread(boi,0)

	for suamae in wavelets:
		print("================> RODANDO WAVELET "+ suamae)
		try:
			funcaofeia(suamae,"img\\"+boi[3:-4]+"-"+suamae,img1)
		except Exception as e:
			print("Mascou a "+suamae)
			print(e)

#for a in range(len(cooef2)):
#	print(len(cooef2[a]))


