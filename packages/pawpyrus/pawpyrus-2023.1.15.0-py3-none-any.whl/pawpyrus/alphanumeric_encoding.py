import bitarray #
import logging
import random
import hashlib
import json

class AlphaEncoder:
	
	def __init__(self, EncodingString, PaddingChar, CharChunk, OffsetBlockSize, RunIDBlockSize, ChunkNumBlockSize):
		self.EncodingString = str(EncodingString)
		self.PaddingChar = str(PaddingChar)
		self.CharChunk = int(CharChunk)
		self.OffsetSize = int(OffsetBlockSize)
		self.RunIDSize = int(RunIDBlockSize)
		self.BlockNumSize = int(ChunkNumBlockSize)
		self.DecodingDict = { Char: Num for Num, Char in enumerate(self.EncodingString) }
		self.Basis = len(self.EncodingString)
		self.RunIDMax = (self.Basis ** self.RunIDSize) - 1
		self.BlockMax = (self.Basis ** self.BlockNumSize) - 1
		self.BitChunk = self.CalculateBitChunk()
		LossPercentage = ((self.Basis ** self.CharChunk) - (2 ** self.BitChunk)) / (self.Basis ** self.CharChunk) * 100
		self.HashSize = self.CalculateHashSize()
		self.MinDataChunkSize = self.RunIDSize + (self.BlockNumSize * 2) + self.HashSize
		# Debug logging
		DebugData = {
			'Encoding string':     self.EncodingString,
			'Padding char':        self.PaddingChar,
			'Basis':               self.Basis,
			'Char chunk size':     self.CharChunk,
			'Bits chunk size':     self.BitChunk,
			'Offset block size':   self.OffsetSize,
			'Max offset':          self.Basis ** self.OffsetSize,
			'Efficiency loss [%]': LossPercentage,
			'Run ID Block Size':   self.RunIDSize,
			'Run ID Range':        [0, self.RunIDMax],
			'Block Num Size':      self.BlockNumSize,
			'Max Blocks':          self.BlockMax,
			'Hash block size':     self.HashSize,
			'Min data chunk size': self.MinDataChunkSize
		}
		logging.debug(f'AlphaEncoder Object Metadata: ' + json.dumps(DebugData, indent = 4))
	
	def CalculateBitChunk(self):
		it = 0
		while 1:
			it += 1
			if ((self.Basis ** self.CharChunk) / (2 ** it)) < 1: break
		return it - 1
	
	def CalculateHashSize(self):
		it = 0
		while 1:
			it += 1
			if ((self.Basis ** it) / (2 ** 256)) > 1: break
		return int(it)
	
	def EncodeInt(self, Int, CharSize):
		Line = str()
		for it in range(CharSize): Line += self.EncodingString[int(Int % (self.Basis ** (it + 1)) / (self.Basis ** it))]
		return Line
	
	def DecodeInt(self, Code):
		CharSize = len(Code)
		Int = 0
		for it in range(CharSize): Int += self.DecodingDict[Code[it]] * (self.Basis ** it)
		return Int
	
	def Encode(self, RawData, RunID_float, ChunkSize = None):
		if ChunkSize is None: ChunkSize = self.MinDataChunkSize
		if ChunkSize < self.MinDataChunkSize: raise ValueError('Too small chunk size')
		# Create output struct
		Result = { 'RunID': None, 'Hash': None, 'Length': None, 'Codes': [] }
		# Run ID: unique program run identifier
		RunID_int = int(self.RunIDMax * RunID_float)
		Result['RunID'] = hex(RunID_int)[2:].zfill(len(hex(self.RunIDMax)[2:]))
		RunID = self.EncodeInt(RunID_int, self.RunIDSize)
		# Compute data hash
		Hash_obj = hashlib.sha256(RawData)
		Result['Hash'] = Hash_obj.hexdigest()
		Hash_int = int.from_bytes(Hash_obj.digest(), 'little')
		Hash = self.EncodeInt(Hash_int, self.HashSize)
		# Encode data
		BitArray = bitarray.bitarray(endian = 'little')
		BitArray.frombytes(RawData)
		Offset = self.BitChunk - (len(BitArray) % self.BitChunk)
		BitArray.extend(bitarray.bitarray('0' * Offset, endian = 'little'))
		Line = str()
		for it in range(0, len(BitArray), self.BitChunk):
			Int = int.from_bytes(BitArray[it:it + self.BitChunk], 'little')
			Line += self.EncodeInt(Int, self.CharChunk)
		Line += self.EncodeInt(Offset, self.OffsetSize)
		PureChunkSize = ChunkSize - self.RunIDSize - self.BlockNumSize
		# Encode length
		BlocksPositions = range(0, len(Line), PureChunkSize)
		Result['Length'] = int(len(BlocksPositions) + 1)
		if Result['Length'] >= self.BlockMax: raise OverflowError('Too many blocks')
		Length = self.EncodeInt(Result['Length'], self.BlockNumSize)
		# Create chunks
		ZeroBlockNumber = self.EncodeInt(0, self.BlockNumSize)
		Result['Codes'].append((RunID + ZeroBlockNumber + Length + Hash).ljust(ChunkSize, self.PaddingChar))
		for index, it in enumerate(BlocksPositions):
			BlockNumber = self.EncodeInt(index + 1, self.BlockNumSize)
			DataChunk = Line[it:it + PureChunkSize]
			Result['Codes'].append((RunID + BlockNumber + DataChunk).ljust(ChunkSize, self.PaddingChar))
		return Result

	def ExtractData(self, Line):
		Result = {
			'RunID': hex(self.DecodeInt(Line[: self.RunIDSize]))[2:].zfill(len(hex(self.RunIDMax)[2:])),
			'Index': self.DecodeInt(Line[self.RunIDSize : self.RunIDSize + self.BlockNumSize]),
			'Content': Line[self.RunIDSize + self.BlockNumSize :].rstrip(self.PaddingChar)
			}
		return Result
	
	def ExtractMetadata(self, Content):
		Result = {
			'Length': self.DecodeInt(Content[: self.BlockNumSize]),
			'Hash': self.DecodeInt(Content[self.BlockNumSize : self.BlockNumSize + self.HashSize]).to_bytes(32, 'little').hex().zfill(64)
			}
		return Result
	
	def Decode(self, Codes):
		Result = list()
		# Extract blocks
		Extracted = [self.ExtractData(Line) for Line in Codes]
		Extracted = { item['Index']: item for item in Extracted }
		# Check header
		try:
			Header = Extracted[0]
		except KeyError:
			raise RuntimeError(f'No root block in input data!')
		# Extract metadata
		Metadata = self.ExtractMetadata(Header['Content'])
		# Check blocks
		MissingBlocks = list()
		for Index in range(1, Metadata['Length']):
			try:
				Extracted[Index]
				if Extracted[Index]['RunID'] != Header['RunID']: raise RuntimeError(f'Some blocks are not of this header')
				Result.append(Extracted[Index]['Content'])
			except KeyError:
				MissingBlocks.append(str(Index))
		if MissingBlocks: raise RuntimeError(f'Some blocks are missing: {"; ".join(MissingBlocks)}')
		# Decode
		Code = ''.join(Result)
		Output = { 'RunID': str(Header['RunID']), 'Blocks': int(Metadata['Length']), 'Hash': str(Metadata['Hash']), 'Data': None }
		BitArray = bitarray.bitarray(endian = 'little')
		Offset = self.DecodeInt(Code[-self.OffsetSize:])
		EncodedData = Code[:-self.OffsetSize]
		for it in range(0, len(EncodedData), self.CharChunk):
			Int = self.DecodeInt(EncodedData[it:it + self.CharChunk])
			NewBits = bitarray.bitarray(endian = 'little')
			NewBits.frombytes(Int.to_bytes(int(self.BitChunk / 8) + 1, byteorder = 'little'))
			BitArray.extend(NewBits[:self.BitChunk])
		BitArray = BitArray[:-Offset]
		Output['Data'] = BitArray.tobytes()
		if hashlib.sha256(Output['Data']).hexdigest() != Output['Hash']: raise RuntimeError(f'Data damaged (hashes are not the same)')
		return Output
