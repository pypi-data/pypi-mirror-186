import cv2 #
import itertools
import logging
import math
import numpy #
import os
from pyzbar.pyzbar import decode #
import tqdm #

def FindCenter(CoordBlock):
	return (
		CoordBlock[0][0] + ((CoordBlock[2][0] - CoordBlock[0][0]) / 2),
		CoordBlock[0][1] + ((CoordBlock[2][1] - CoordBlock[0][1]) / 2)
		)


def DecodeQR(Barcode): # pragma: no cover
	Result = { 'Contents': None, 'Detected': { } }
	# pyzbar
	Code = decode(Barcode)
	if Code:
		Result['Contents'] = str(Code[0].data.decode('ascii'))
		Result['Detected']['pyzbar'] = True
	else: Result['Detected']['pyzbar'] = False
	# opencv
	detector = cv2.QRCodeDetector()
	Code = detector.detectAndDecode(Barcode)[0]
	if Code:
		if Result['Contents'] is not None:
			assert Result['Contents'] == Code, f'Different results with different QR decoders? OpenCV = {Code}, PyZBar = {Result["Contents"]}'
		else: Result['Contents'] = str(Code)
		Result['Detected']['opencv'] = True
	else: Result['Detected']['opencv'] = False
	return Result


def ReadPage(FileName, DebugDir, FileIndex, ArUcoDictionary, MinMarkerPerimeterRate, TqdmAscii): # pragma: no cover
	# Read and binarize image
	Picture = cv2.imread(FileName, cv2.IMREAD_GRAYSCALE)
	Threshold, Picture = cv2.threshold(Picture, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	
	# -----DEBUG-----
	if DebugDir is not None:
		DebugArray = cv2.cvtColor(numpy.copy(Picture), cv2.COLOR_GRAY2RGB)
	# ---------------
	
	logging.info(f'Image binarized (threshold: {Threshold})')
	# Detect markers
	ArUcoDict = cv2.aruco.Dictionary_get(ArUcoDictionary)
	ArUcoParams = cv2.aruco.DetectorParameters_create()
	ArUcoParams.minMarkerPerimeterRate = MinMarkerPerimeterRate
	Markers = cv2.aruco.detectMarkers(Picture, ArUcoDict, parameters = ArUcoParams)
	# Check markers
	if Markers is None: raise RuntimeError('No markers were found')
	
	# -----DEBUG-----
	if DebugDir is not None:
		for item in range(len(Markers[1])):
			for LineStart, LineEnd in ((0, 1), (1, 2), (2, 3), (3, 0)):
				cv2.line(
					DebugArray,
					tuple(int(i) for i in Markers[0][item][0][LineStart]),
					tuple(int(i) for i in Markers[0][item][0][LineEnd]),
					(255, 0, 0),
					4
				)
			cv2.putText(
				DebugArray,
				f'id={Markers[1][item][0]}',
				(int(Markers[0][item][0][0][0]), int(Markers[0][item][0][0][1]) - 20),
				cv2.FONT_HERSHEY_SIMPLEX,
				1.5,
				(0, 255, 0),
				4
			)
	# ---------------
	
	# Check markers
	Markers = { int(Markers[1][item][0]): {'Coords': Markers[0][item][0]} for item in range(len(Markers[1])) }
	if tuple(sorted(Markers.keys())) != (0, 1, 2, 3): raise RuntimeError(f'Some markers were not found')
	# Align grid
	MarkerLength = math.dist(Markers[0]['Coords'][0], Markers[0]['Coords'][1])
	for item in Markers:
		Markers[item]['Center'] = FindCenter(Markers[item]['Coords'])
	Width = math.dist(Markers[0]['Center'], Markers[1]['Center'])
	Height = math.dist(Markers[0]['Center'], Markers[2]['Center'])
	CellSize = math.dist(Markers[0]['Center'], Markers[3]['Center'])
	ColNum, RowNum = round(Width / CellSize), round(Height / CellSize)
	logging.info(f'Layout detected: {ColNum} x {RowNum}')
	CellSizeX, CellSizeY = Width / ColNum, Height / RowNum
	VectorX = (
		(Markers[1]['Center'][0] - Markers[0]['Center'][0]) / Width,
		(Markers[1]['Center'][1] - Markers[0]['Center'][1]) / Width
		)
	VectorY = (
		(Markers[2]['Center'][0] - Markers[0]['Center'][0]) / Height,
		(Markers[2]['Center'][1] - Markers[0]['Center'][1]) / Height
		)
	for item in Markers:
		Markers[item]['Center'] = (Markers[item]['Center'][0] + (MarkerLength * VectorX[0]), Markers[item]['Center'][1] + (MarkerLength * VectorY[1]))
	# Chunking by grid
	Chunks = list()
	Cells = itertools.product(range(ColNum), range(RowNum))
	for X, Y in Cells:
		CoordStart = Markers[0]['Center']
		FullVectorX = tuple(item * CellSizeX for item in VectorX)
		FullVectorY = tuple(item * CellSizeY for item in VectorY)
		Chunk = [
			[
				CoordStart[0] + (x * FullVectorX[0]) + (y * FullVectorY[0]),
				CoordStart[1] + (x * FullVectorX[1]) + (y * FullVectorY[1])
				]
				for x, y in ((X, Y), (X + 1, Y), (X + 1, Y + 1), (X, Y + 1))
			]
		Xs, Ys = [x for x, y in Chunk], [y for x, y in Chunk]
		Fragment = Picture[round(min(Ys)):round(max(Ys)), round(min(Xs)):round(max(Xs))]
		Chunks.append({
			'Cell': (int(X) + 1, int(Y) + 1),
			'Coords': Chunk,
			'Image': Fragment
			})
	# Detect and decode
	Codes = list()
	for Chunk in tqdm.tqdm(Chunks, total = len(Chunks), desc = f'Detect QR codes', ascii = TqdmAscii):
		Code = DecodeQR(Chunk['Image'])
		if Code['Contents'] is not None:
			Color = (0, 255, 0)
			Codes.append(Code)
		else: Color = (0, 0, 255)
		
		# -----DEBUG-----
		if DebugDir is not None:
			if not Code: cv2.imwrite(os.path.join(DebugDir, f'unrecognized.page-{FileIndex}.x-{Chunk["Cell"][0]}.y-{Chunk["Cell"][1]}.jpg'), Chunk['Image'])
			for LineStart, LineEnd in ((0, 1), (1, 2), (2, 3), (3, 0)):
				cv2.line(
					DebugArray,
					tuple(int(i) for i in Chunk['Coords'][LineStart]),
					tuple(int(i) for i in Chunk['Coords'][LineEnd]),
					(255, 0, 0),
					4
				)
			cv2.putText(
				DebugArray,
				f'({Chunk["Cell"][0]},{Chunk["Cell"][1]})',
				(int(Chunk['Coords'][3][0]) + 10, int(Chunk['Coords'][3][1]) - 30),
				cv2.FONT_HERSHEY_SIMPLEX,
				1.5,
				Color,
				4
			)
		# ---------------
	
	# -----DEBUG-----
	if DebugDir is not None:
		cv2.imwrite(os.path.join(DebugDir, f'page-{FileIndex}.jpg'), DebugArray)
	# ---------------
	
	return Codes
