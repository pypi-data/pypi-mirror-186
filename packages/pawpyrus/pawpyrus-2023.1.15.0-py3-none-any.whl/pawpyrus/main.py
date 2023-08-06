from pawpyrus.alphanumeric_encoding import *
from pawpyrus.const import *
from pawpyrus.const import __version__, __repository__
from pawpyrus.detection import *
from pawpyrus.draw import *
from pawpyrus.pawprints import *

import argparse #
import glob
import logging
import os
import sys
import tqdm #

# -----=====| LOGGING |=====-----

logging.basicConfig(format='[%(levelname)s] %(message)s', level = C_LOGGING_LEVEL)


# -----=====| ENCODE MAIN |=====-----

def EncodeMain(JobName, InputFileName, OutputFileName): # pragma: no cover
	logging.info(f'pawpyrus {__version__} Encoder')
	logging.info(f'Job Name: {JobName}')
	logging.info(f'Input File: "{os.path.realpath(InputFileName)}"')
	logging.info(f'Output File: "{os.path.realpath(OutputFileName)}"')
	# Read rawdata
	RawData = open(InputFileName, 'rb').read()
	# Create codes dataset
	Encoder = AlphaEncoder(C_ALPHANUMERIC_STRING, C_PADDING_CHAR, C_ENCODER_CHAR_CHUNK_SIZE, C_ENCODER_OFFSET_BLOCK_SIZE, C_ENCODER_RUNID_BLOCK_SIZE, C_ENCODER_BLOCKNUM_BLOCK_SIZE)
	Dataset = Encoder.Encode(RawData, random.random(), C_ENCODER_DATA_CHUNK_SIZE)
	logging.info(f'Run ID: {Dataset["RunID"]}')
	logging.info(f'SHA-256: {Dataset["Hash"]}')
	logging.info(f'Blocks: {Dataset["Length"]}')
	# Create pixelsheets
	Pages = CreatePixelSheets(Dataset['Codes'], C_PDF_COLUMNS, C_PDF_ROWS, C_QR_SPACING_SIZE, C_PDF_DOT_SPACING_SIZE, C_QR_VERSION, C_QR_CORRECTION_LEVEL, C_ARUCO_DICT, C_TQDM_ASCII)
	# Draw SVG
	SvgPages = DrawSvg(Pages, C_PDF_PAGE_WIDTH, C_PDF_PAGE_HEIGHT, C_PDF_LEFT_MARGIN, C_PDF_RIGHT_MARGIN, C_PDF_TOP_MARGIN + (5 * C_PDF_LINE_HEIGHT), C_TQDM_ASCII)
	# Draw PDF
	CreatePDF(Dataset, SvgPages, OutputFileName, JobName, C_PDF_LEFT_MARGIN, C_PDF_TOP_MARGIN, C_PDF_LINE_HEIGHT, C_PDF_FONT_FAMILY, C_PDF_FONT_SIZE, C_PDF_PAGE_HEIGHT, C_TQDM_ASCII)
	logging.info(f'Job finished')


# -----=====| DECODE MAIN |=====-----

def DecodeMain(MaskedImageInput, TextInput, DebugDir, OutputFileName): # pragma: no cover
	ImageInput = list()
	if MaskedImageInput is not None:
		for i in MaskedImageInput: ImageInput.extend([os.path.realpath(f) for f in glob.glob(i)])
		ImageInput = sorted(list(set(ImageInput)))
	if (not ImageInput) and (TextInput is None): raise ValueError(f'Input is empty: no images, no text!')
	logging.info(f'pawpyrus {__version__} Decoder')
	
	# -----DEBUG-----
	if DebugDir is not None:
		logging.info(f'DEBUG MODE ON')
		os.mkdir(DebugDir)
	# ---------------
	
	if ImageInput: logging.info(f'Image Input File(s): {", ".join(ImageInput)}')
	if TextInput is not None: logging.info(f'Text Input File: {os.path.realpath(TextInput)}')
	logging.info(f'Output File: {os.path.realpath(OutputFileName)}')
	AnnotatedBlocks = list()
	for FileIndex, FileName in enumerate(ImageInput):
		logging.info(f'Processing "{FileName}"')
		AnnotatedBlocks += ReadPage(FileName, DebugDir, FileIndex + 1, C_ARUCO_DICT, C_OPENCV_MIN_MARKER_PERIMETER_RATE, C_TQDM_ASCII)
	
	# -----DEBUG-----
	if DebugDir is not None:
		DetectionStatistics = {
			'total': len(AnnotatedBlocks),
			'pyzbar_only': [(not block['Detected']['opencv']) and block['Detected']['pyzbar'] for block in AnnotatedBlocks].count(True),
			'opencv_only': [block['Detected']['opencv'] and (not block['Detected']['pyzbar']) for block in AnnotatedBlocks].count(True),
			'both': [block['Detected']['opencv'] and block['Detected']['pyzbar'] for block in AnnotatedBlocks].count(True),
			'neither': [(not block['Detected']['opencv']) and (not block['Detected']['pyzbar']) for block in AnnotatedBlocks].count(True)
			}
		json.dump(DetectionStatistics, open(os.path.join(DebugDir, 'detection_stats.json'), 'wt'), indent = 4)
	# ---------------
	
	Blocks = [block['Contents'] for block in AnnotatedBlocks]
	if TextInput is not None:
		with open(TextInput, 'rt') as TF:
			Blocks += [ Line.rstrip('\n').rstrip(C_PADDING_CHAR) for Line in TF.readlines() ]
			Blocks = [ Line for Line in Blocks if Line ]
	
	# -----DEBUG-----
	if DebugDir is not None:
		with open(os.path.join(DebugDir, 'blocks.txt'), 'wt') as BF: BF.write('\n'.join(Blocks))
	# ---------------
	
	Encoder = AlphaEncoder(C_ALPHANUMERIC_STRING, C_PADDING_CHAR, C_ENCODER_CHAR_CHUNK_SIZE, C_ENCODER_OFFSET_BLOCK_SIZE, C_ENCODER_RUNID_BLOCK_SIZE, C_ENCODER_BLOCKNUM_BLOCK_SIZE)
	Result = Encoder.Decode(Blocks)
	logging.info(f'Run ID: {Result["RunID"]}')
	logging.info(f'Blocks: {Result["Blocks"]}')
	logging.info(f'SHA-256: {Result["Hash"]}')
	with open(OutputFileName, 'wb') as Out: Out.write(Result['Data'])
	logging.info(f'Job finished')


## ------======| PARSER |======------

def CreateParser(): # pragma: no cover
	Default_parser = argparse.ArgumentParser(
			formatter_class = argparse.RawDescriptionHelpFormatter,
			description = f'pawpyrus {__version__}: Minimalist paper data storage based on QR codes',
			epilog = f'Bug tracker: https://github.com/regnveig/pawpyrus/issues'
			)
	Default_parser.add_argument ('-v', '--version', action = 'version', version = __version__)
	Subparsers = Default_parser.add_subparsers(title = 'Commands', dest = 'command')
	# Encode parser
	EncodeParser = Subparsers.add_parser('Encode', help=f'Encode data as paper storage PDF file')
	EncodeParser.add_argument('-n', '--name', required = True, type = str, dest = 'JobName', help = f'Job name. Will be printed in page header. Required.')
	EncodeParser.add_argument('-i', '--input', required = True, type = str, dest = 'InputFile', help = f'File to encode. Required.')
	EncodeParser.add_argument('-o', '--output', required = True, type = str, dest = 'OutputFile', help = f'PDF file to save. Required.')
	# Decode parser
	DecodeParser = Subparsers.add_parser('Decode', help=f'Decode data from paper storage scans')
	DecodeParser.add_argument('-i', '--image', nargs = '*', type = str, dest = 'ImageInput', help = f'Paper storage scans to decode.')
	DecodeParser.add_argument('-t', '--text', type = str, default = None, dest = 'TextInput', help = f'Files with lists of QR codes content, gathered manually.')
	DecodeParser.add_argument('-o', '--output', required = True, type = str, dest = 'OutputFile', help = f'File to save decoded data. Required.')
	DecodeParser.add_argument('-d', '--debug-dir', type = str, default = None, dest = 'DebugDir', help = f'Directory where to collect debug data if necessary.')
	
	return Default_parser


# -----=====| MAIN |=====-----

def main(): # pragma: no cover
	Parser = CreateParser()
	Namespace = Parser.parse_args(sys.argv[1:])
	if Namespace.command == 'Encode':
		EncodeMain(
			InputFileName = Namespace.InputFile,
			JobName = Namespace.JobName,
			OutputFileName = Namespace.OutputFile
			)
	elif Namespace.command == 'Decode':
		DecodeMain(
			MaskedImageInput = Namespace.ImageInput,
			TextInput = Namespace.TextInput,
			DebugDir = Namespace.DebugDir,
			OutputFileName = Namespace.OutputFile
			)
	else: Parser.print_help()


if __name__ == '__main__': main()
