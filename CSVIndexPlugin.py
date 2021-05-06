import sys
import numpy
import random
import PyPluMA

class CSVIndexPlugin:
   def input(self, filename):
      #self.myfile = filename
      txtfile = open(filename, 'r')
      parameters = dict()
      for line in txtfile:
         contents = line.split('\t')
         parameters[contents[0]] = contents[1].strip()
      filestuff = open(PyPluMA.prefix()+"/"+parameters['csvfile'], 'r')
      filestuffI = open(PyPluMA.prefix()+"/"+parameters['indexfile'], 'r')
      self.lines = []
      for line in filestuff:
         self.lines.append(line.strip())
      self.indices = []
      for index in filestuffI:
         self.indices.append(int(index.strip()))

   def run(self):
      self.newlines = []
      for i in range(len(self.lines)):
            newline = ""
            contents = self.lines[i].split(',')
            for j in range(len(self.indices)):
               newline += contents[self.indices[j]]
               if (j != len(self.indices)-1):
                  newline += ','
            self.newlines.append(newline)

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(len(self.newlines)):
         filestuff2.write(self.newlines[i])
         if (i != len(self.newlines)-1):
            filestuff2.write('\n')



