import datetime
import io
import itertools
import logging
import numpy #
from reportlab.graphics import renderPDF #
from reportlab.lib.units import mm #
from reportlab.pdfgen import canvas #
from svglib.svglib import svg2rlg #
import tqdm #

from pawpyrus.const import __version__, __repository__

# numpy 2D array to black pixel coordinates
def MatrixToPixels(Matrix):
	PixelCoordinates = itertools.product(range(Matrix.shape[0]), range(Matrix.shape[1]))
	Result = [ (X, Y) for Y, X in PixelCoordinates if Matrix[Y][X] ]
	return Result

def DrawSvg(PixelSheets, PdfPageWidth, PdfPageHeight, PdfLeftMargin, PdfRightMargin, PdfTopMargin, TqdmAscii):
	SvgPages = list()
	DrawingWidth = PixelSheets[0].shape[1]
	ContentWidth = PdfPageWidth - PdfLeftMargin - PdfRightMargin
	PixelSize = ContentWidth / DrawingWidth
	logging.debug(f'Pixel Size: {PixelSize:.3f} mm')
	for PageNumber, PageMatrix in enumerate(PixelSheets):
		# Create Pixels
		Page = MatrixToPixels(PageMatrix)
		# Draw page
		SvgPage = [
			f'<svg width="{PdfPageWidth}mm" height="{PdfPageHeight}mm" viewBox="0 0 {PdfPageWidth} {PdfPageHeight}" version="1.1" xmlns="http://www.w3.org/2000/svg">',
			f'<path style="fill:#000000;stroke:none;fill-rule:evenodd" d="'
			]
		Paths = list()
		# Add Pixels
		for X, Y in tqdm.tqdm(
			Page,
			total = len(Page),
			desc = f'Draw pixels, page {PageNumber + 1} of {len(PixelSheets)}',
			ascii = TqdmAscii):
			Paths.append(f'M {PdfLeftMargin + (X * PixelSize):.3f},{PdfTopMargin + (Y * PixelSize):.3f} H {PdfLeftMargin + ((X + 1) * PixelSize):.3f} V {PdfTopMargin + ((Y + 1) * PixelSize):.3f} H {PdfLeftMargin + (X * PixelSize):.3f} Z')
		SvgPage.append(f' '.join(Paths))
		SvgPage.append(f'">')
		SvgPage.append(f'</svg>')
		# Merge svg
		SvgPages.append(''.join(SvgPage))
	return SvgPages

def CreatePDF(Dataset, SvgPages, OutputFileName, JobName, PdfLeftMargin, PdfTopMargin, PdfLineSpacing, PdfFontFamily, PdfFontSize, PdfPageHeight, TqdmAscii): # pragma: no cover
	CanvasPDF = canvas.Canvas(OutputFileName)
	Timestamp = str(datetime.datetime.now().replace(microsecond = 0))
	for PageNumber, Page in tqdm.tqdm(
		enumerate(SvgPages),
		total = len(SvgPages),
		desc = f'Convert pages to PDF',
		ascii = TqdmAscii
	):
		# Set font
		CanvasPDF.setFont(PdfFontFamily, PdfFontSize)
		# Convert SVG page
		ObjectPage = svg2rlg(io.StringIO(Page))
		# Captions
		CanvasPDF.drawString(PdfLeftMargin * mm, (PdfPageHeight - PdfTopMargin - (PdfLineSpacing * 1)) * mm, f'Name: {JobName}')
		CanvasPDF.drawString(PdfLeftMargin * mm, (PdfPageHeight - PdfTopMargin - (PdfLineSpacing * 2)) * mm, f'{Timestamp}, run ID: {Dataset["RunID"]}, {Dataset["Length"]} blocks, page {PageNumber + 1} of {len(SvgPages)}')
		CanvasPDF.drawString(PdfLeftMargin * mm, (PdfPageHeight - PdfTopMargin - (PdfLineSpacing * 3)) * mm, f'SHA-256: {Dataset["Hash"]}')
		CanvasPDF.drawString(PdfLeftMargin * mm, (PdfPageHeight - PdfTopMargin - (PdfLineSpacing * 4)) * mm, f'pawpyrus {__version__}. Available at: {__repository__}')
		# Draw pawprints
		renderPDF.draw(ObjectPage, CanvasPDF, 0, 0)
		# Newpage
		CanvasPDF.showPage()
	# Save pdf
	CanvasPDF.save()
