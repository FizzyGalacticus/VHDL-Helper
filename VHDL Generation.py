#!/usr/bin/env python
#Script for generating VHDL modules.

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class vhdl:
	"""A helper class for generating VHDL code!"""
	def __init__(self):
		self.entityName = raw_input("Please enter the name of your entity: ")
		self.architectureName = raw_input("Please enter the name of your architecture: ")
		self.numInputs = input("Number of input variables: ")
		self.numOutputs = input("Number of output variables: ")
		self.numEntitySignals = input("Number of signal variables in entity: ")
		self.numArchitectureSignals = input("Number of signal variables in architecture: ")
		self.inputNames, self.outputNames = [], []
		
		choice = raw_input("Do you want to name your variables? [Y/N]: ")
		if choice.lower() == 'y':
			self.getInputNames()
			self.getOutputNames()
		
	def getInputNames(self):
		for i in range(self.numInputs):
			self.inputNames.append(raw_input("Please enter the variable name for input #%s: " % (i+1)))
		
	def getOutputNames(self):
		for i in range(self.numOutputs):
			self.outputNames.append(raw_input("Please enter the variable name for output #%s: " % (i+1)))
		
	def generateEntity(self):
		self.entity = "ENTITY %s IS\n	PORT(" % self.entityName
		
		if self.numInputs == len(self.inputNames):
			for i in range(self.numInputs):
				self.entity += self.inputNames[i]
				if i != (self.numInputs-1):
					self.entity += ', '
		else:
			for i in range(self.numInputs):
				self.entity += "x%s" % i
				if i != (self.numInputs-1):
					self.entity += ', '
		
		self.entity += "	:IN STD_LOGIC;\n		"
		
		if self.numOutputs == len(self.outputNames):
			for i in range(self.numOutputs):
				self.entity += self.outputNames[i]
		
				if(i != (self.numOutputs-1)):
					self.entity += ", "
		else:
			for i in range(self.numOutputs):
				self.entity += alpha[i]
				if i != (self.numOutputs-1):
					self.entity += ', '
		
		self.entity += "	:OUT STD_LOGIC);\nEND ENTITY %s;" % self.entityName
		
	def generateArchitecture(self):
		self.architecture = "ARCHITECTURE %s OF %s IS\nBEGIN\n" % (self.architectureName, self.entityName)
		
		if self.numOutputs == len(self.outputNames):
			for i in range(self.numOutputs):
				self.architecture += "	%s <= --define variable here!\n" % self.outputNames[i]
		else:
			for i in range(self.numOutputs):
				self.architecture += "	%s <= --define variable here!\n" % alpha[i]
		
		self.architecture += "END LogicFunc;"
	
	def generatePackage(self):
		self.packageName = raw_input("Please enter a name for the package: ")
		
		self.package = "LIBRARY ieee;\nUSE ieee.std_logic_1164.all;"
		self.package += "PACKAGE %s IS\n" % self.packageName
		self.package += "	COMPONENT %s\n" % self.entityName
		self.package += "		PORT("
		
		for i in range(self.numInputs):
			if len(self.inputNames) > 0:
				self.package += inputNames[i]
			else:
				self.package += "x%s" % i
			
			if i != (self.numInputs - 1):
				self.package += ', '
		
		self.package += "	: IN STD_LOGIC;\n"
		self.package += "			"
		
		for i in range(self.numOutputs):
			if len(self.outputNames) > 0:
				self.package += outputNames[i]
			else:
				self.package += alpha[i]
			
			if i != (self.numOutputs - 1):
				self.package += ', '
		
		self.package += "	: OUT STD_LOGIC);\n"
		self.package += "	END COMPONENT;\n"
		self.package += "END %s;" % self.packageName
	
	def printVHDL(self):
		self.generateEntity()
		self.generateArchitecture()
		print "LIBRARY ieee;\nUSE ieee.std_logic_1164.all;"
		print ""
		print self.entity
		print ""
		print self.architecture
		
		choice = raw_input("Do you want to package the entity? [Y/N]: ")
		if choice.lower() == 'y':
			self.generatePackage()
			print ""
			print self.package

myVHDL = vhdl()
myVHDL.printVHDL()
