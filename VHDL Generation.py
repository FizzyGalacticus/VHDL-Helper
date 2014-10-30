#!/usr/bin/env python
#Script for generating VHDL modules.

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class vhdl:
	"""A helper class for generating VHDL code!"""
	def __init__(self):
		self.name = raw_input("Please enter the name of your module: ")
		self.numInputs = input("Number of input variables: ")
		self.numOutputs = input("Number of output variables: ")
		self.numSignals = input("Number of signal variables: ")
		
	def getInputNames():
		self.inputNames = []
		for i in range(self.numInputs):
			self.inputNames.append(raw_input("Please enter the variable name for input #%s: " % (i+1)))
		
	def getOutputNames():
		self.outputNames = []
		for i in range(self.numOutputs):
			self.outputNames.append(raw_input("Please enter the variable name for output #%s: " % (i+1)))

def getInfo():
	module = raw_input("Please enter the name of your module: ")
	numInputs = input("Number of input variables: ")
	numOutputs = input("Number of output variables: ")
	
	return (module, numInputs, numOutputs)

#Working!
def generateEntity(info):
	moduleName, inputs, outputs = info
	
	entityDef = "ENTITY %s IS\n	PORT(" % moduleName
	
	for i in range(inputs):
		entityDef += "x%s" % (i+1)
		if(i != (inputs-1)):
			entityDef += ", "
	
	entityDef += "	:IN STD_LOGIC;\n		"
	
	for i in range(outputs):
		entityDef += alpha[i]
		
		if(i != (outputs-1)):
			entityDef += ", "
		
	entityDef += "	:OUT STD_LOGIC);\nEND ENTITY %s;" % moduleName
	
	return entityDef	

def generateArchitecture(module):
	return ("ARCHITECTURE LogicFunc OF %s IS\nBEGIN\n	-- Insert function definition here\nEND LogicFunc;" % module)

moduleName, inputs, outputs = getInfo()
print "LIBRARY ieee;\nUSE ieee.std_logic_1164.all;"
print generateEntity((moduleName, inputs, outputs))
print ""
print generateArchitecture(moduleName)
