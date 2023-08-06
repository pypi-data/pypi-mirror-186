import cv2 # opencv-python + opencv-contrib-python
import itertools
import math
import more_itertools #
import numpy #
import qrcode #
import tqdm #

# QR Code
def TomcatPawprint(Data, Version, ErrorCorrection):
	WrappedData = qrcode.util.QRData(Data.encode('ascii'), mode = qrcode.util.MODE_ALPHA_NUM)
	QR = qrcode.QRCode(version = Version, error_correction = ErrorCorrection, border = 0)
	QR.add_data(WrappedData)
	QR.make(fit = False)
	Matrix = numpy.array(QR.get_matrix())
	Matrix = numpy.vectorize(lambda x: int(x))(Matrix)
	return Matrix

# ArUco Marker
def KittyPawprint(ArUcoIndex, Dictionary, SpacingSize):
	Matrix = cv2.aruco.Dictionary_get(Dictionary).drawMarker(ArUcoIndex, SpacingSize)
	Matrix = numpy.vectorize(lambda x: int(not bool(x)))(Matrix)
	return Matrix

def CreatePixelSheets(Codes, ColNum, RowNum, SpacingSize, DotSpacing, QRVersion, QRErrorCorrection, ArUcoDict, TqdmAscii):
	PawSize = (4 * QRVersion) + 17
	CellSize = PawSize + SpacingSize
	PageWidth = CellSize * ColNum + SpacingSize
	PageHeight = CellSize * RowNum + SpacingSize
	# Create output list
	Result = list()
	# Chunk codes to rows and pages
	PageData = list(more_itertools.sliced(list(more_itertools.sliced(Codes, ColNum)), RowNum))
	for PageNumber, Page in enumerate(PageData):
		# Create page
		Matrix = numpy.zeros((PageHeight, PageWidth))
		for Row, Col in tqdm.tqdm(
			itertools.product(range(RowNum), range(ColNum)),
			total = sum([len(item) for item in Page]),
			desc = f'Create pawprints, page {PageNumber + 1} of {len(PageData)}',
			ascii = TqdmAscii
		):
			try:
				# Create pawprint on the page
				StartX = (SpacingSize * 2) + (CellSize * Col)
				StartY = (SpacingSize * 2) + (CellSize * Row)
				Pawprint = TomcatPawprint(Page[Row][Col], QRVersion, QRErrorCorrection)
				Matrix[StartY:StartY + PawSize, StartX:StartX + PawSize] = Pawprint
			except IndexError:
				# If there are no codes left
				break
		# Create dot margin (beauty, no functionality)
		DotCentering = math.floor(SpacingSize / 2)
		Matrix[DotCentering, SpacingSize + 2::DotSpacing] = 1
		Matrix[SpacingSize + 2:CellSize * len(Page):DotSpacing, DotCentering] = 1
		# Create markers
		Grid = {
			0: (0, 0),
			1: (CellSize * ColNum, 0),
			2: (0, CellSize * len(Page)),
			3: (CellSize, 0)
			}
		for Index, Item in Grid.items(): 
			Matrix[Item[1]:Item[1] + SpacingSize, Item[0]:Item[0] + SpacingSize] = KittyPawprint(Index, ArUcoDict, SpacingSize)
		# Append page
		Result.append(Matrix)
	# Return
	return Result
