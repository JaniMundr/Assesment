#cageFilling.py implementing the First Fit Decreasing Algorithm

import pandas as pd
import numpy as np
import scipy as sc

def cageFill(productsFile, height ,width, length):

  #load the cage_products datafile into panda dataframes
  df = pd.read_csv(productsFile)
  
  #Calculate product volume and sort in decreasing order
  df['productVolume'] = df['Height (mm)'] * df['Width (mm)'] * df['Length (mm)']
  df['productQtyVolume'] = df['productVolume'] * df['Quantity needed']
  Items = df.sort_values('productVolume',ascending=False)
  TotalItems = df['Quantity needed'].sum()
  TotalProductsVolume = df['productQtyVolume'].sum()

  
  #copy cage measurements
  cageHeight = height
  cageWidth  = width
  cageDepth  = length
  cageVolume = (cageHeight *  cageWidth * cageDepth)

  """Decide on a packing direction. The longest side of the bin
    corresponds to the packing direction.
	Each bin has three directions in which to pack, a width (or x) direction, a
    height (or y) direction, a depth (or z) direction.
	Pack one bin at a time
  """
  if (cageWidth < cageHeight && cageWidth < cageDepth):
     packByWidth=true
     packByHeight=false
  elif (cageDepth < cageHeight && cageDepth < cageWidth):
     packByWidth=false
     packByHeight=false #both false implies pack by depth
  elif (cageHeight < cageWidth && cageHeight < cageDepth):
     packByWidth=false
     packByHeight=true
  
  """
    first choose a pivot point. The pivot is an (x, y, z)
    coordinate which represents a point in a particular 3D bin
    at which an attempt to pack an item will be made. 
	 The back lower left corner of the item will be placed at the
     pivot. If the item cannot be packed at the pivot position
     then it is rotated until it can be packed at the pivot point
     or until all 6 possible rotation types (rotate at 0, x, y, z,(x,y),(x,z)) are tried
  """ 
 
  notPacked=Items #copy all items considering 'Quantity needed' from cage_products.csv
  while (len(notPacked) = 0):

      toPack=notPacked
      notPacked.clear()
      
	  Create a new bin called currentBin
      and check whether the item toPack[0]
      is able to fit in this bin at
      position (x,y,z)=(0,0,0)
	  
	  cages = []
      for i in len(toPack)-1:

          currentItem=toPack[i]
          fitted=false
		  
		  #compute the pivot
          for p in range(0,2):
		      k=0
			  while (NOT fitted) && (k < len(currentBin)):
			  
			    binItem = currentBin[k]
				if (packByWidth):
				     pivot = p #Choose (pivotX, pivovY, pivotZ ) as the back lower right corner of binItem
				elif (packByHeight):
				     compute pivote p for height, 
					  Choose (pivotX, pivovY, pivotZ ) as the front lower left corner of binItem
				else:
                     #pack by depth
				     compute pivot p for depth,
					   Choose (pivotX, pivovY, pivotZ ) as the back upper left corner of binItem
					   
			    
				if (currentItem can be packed in currentBin at position(pivotX, pivotY, pivotZ ) ):
                   Pack currentItem into currentBin at position (pivotX, pivotY ,pivotZ)
                   fitted=true
					 
			    else:
                   #try rotating item 
				   while currentItem cannot be packed in currentBin at position(pivotX,pivotY) &&
				         (not all rotations for currentItem checked): Rotate currenItem
						
                   if (currentItem can be packed in currentBin at position(pivotX, pivotY ,pivotZ) ):
                          Pack currentItem into currentBin at position(pivotX, pivotY ,pivotZ)
                          fitted=true
						  #Adding item to bin
						  Bin.append(i)
				   else:
                         Restore currentItem to its original rotation type

						 
		        if (not fitted):
                     #Add currentItem to the list notPacked
					 notPacked.append(currentItem)
		
					 
      # item did not fit into any cage, start a new one	
	  cages.append(bin)

  #finally calculate the volume utilisation percentage of the cages 	  
  cagesVolume = cages * cageVolume
  volUsedPCT = (TotalProductsVolume/cagesVolume)
  
 return [cages, volUsedPCT]


--------------------------------------------------------------------------
--UnitTest.py
#run the tests with: python UnitTest.py

import cageFilling as cf
import unittest

#passing the cage dimensions in mm (but unit conversion can be handled in the code)
cageDetails = {"productsFile": "cage_products.csv", "height": "1603" ,"width": "697", "length": "846"}
values = cf.cageFill(**cageDetails)

print "No# of cages required: ", values[0]
print "Volume utilisation percentage of the cages: ", values[1] 
