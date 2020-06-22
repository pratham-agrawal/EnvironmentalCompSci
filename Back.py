import time
import random
import math
from PIL import Image
global imageSize
imageSize=[]

def imageToRgb(fileName):
  '''
      Converts an image to pixels

      Converts an image from filename to a list of pixels with height and width values appended

      Parameters
      ----------
      fileName: str
          The location of image or filename

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  im = Image.open(fileName)
  pixels = list(im.getdata())
  imageSize.append(im.width)
  imageSize.append(im.height)
  return (pixels)

def formatXY(pixels):
  '''
      Converts list into more manageable list

      Takes the pixels from imageToRgb and does some formatting

      Parameters
      ----------
      pixels: list
          List of pixels given by imageToRgb

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  pixelsFormatted = [[]]
  x=0
  y=0
  for i in (pixels):
    pixelsFormatted[y].append(i)
    x+=1
    if x == imageSize[0] and y!= imageSize[1]-1:
      y+=1
      pixelsFormatted.append([])
      x=0
  return pixelsFormatted

def splitHelper(pixelsF,startY,stopY,startX,stopX):
  '''
      Helps splitToPercentage format pixels

      Gets called from splitToPercentage to split into some number of sections

      Parameters
      ----------
      pixelsF: List
          The pixels from formatXY

      startY: int
          Starting Y location on image

      stopY: int
          Stopping Y location on image

      startX: int
          Starting X location on image

      stopX: int
          Stopping X location on image

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  temp = []
  for i in range(startY,stopY):
    for l in range(startX,stopX):
      temp.append(pixelsF[i][l])
  return (temp)

def splitToPercentage(pixelsFormatted, numPerSide):
  '''
      Converts list into final list

      Takes the pixels from formatXY and does the final formatting into sections of the image (top left pixels, top middle pixels, top right pixels etc.)

      Parameters
      ----------
      pixelsFormatted: list
          List of pixels given by formatXY

      numPerSide: int
          The number of sections to split the image into per side

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  percentage = 1/numPerSide
  sizeW = int(len(pixelsFormatted[0]) * percentage)
  sizeH = int(len(pixelsFormatted) * percentage)
  x=0
  y=0
  finalList = []
  for i in range(numPerSide):
    for l in range(numPerSide):
      finalList.append(splitHelper(pixelsFormatted,y,y+sizeH,x,x+sizeW))
      x+= sizeW
    x=0
    y+= sizeH
  return finalList

def fullFormat(fileName,size):
  '''
      Runs all the other formatting functions

      Runs the formatting functions in one simple place

      Parameters
      ----------
      fileName: str
          The name/location of the image file

      size: int
          The number of sections per side for the image to be cut into

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  pixels = imageToRgb(fileName)
  newPixels = formatXY(pixels)
  splitBySize = splitToPercentage(newPixels, size)
  return splitBySize

def greenCheck(pixel):
  '''
      Checks if a pixel is green

      Checks a pixel's RGB to determine whether or not it's green

      Parameters
      ----------
      pixel: tuple
          The RGB of a pixel

      Returns
      -------
      Boolean

      Raises
      ------
      None

      '''
  if pixel[1] <= 55 or pixel[0]+15 > pixel[1] or pixel[2]+15 > pixel[1]:
    return False
  else:
    return True

def encryptorNew(imagePercentGreen, saveName, fileName):
  '''
      Saves the RGB percentage of an image

      Saves and encrypts the green percentage of an image

      Parameters
      ----------
      imagePercentGreen: list
          List of green percent by section

      saveName: str
          The name to save the percentage green list under

      fileName: str
          The location to save the information to

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  tempList = newFormatterForDecryption(fileName)
  l = 0
  for i in imagePercentGreen:
    appendList = [saveName, l, i]
    tempList.append(appendList)
    l += 1
  random.shuffle(tempList)
  file = open(fileName, 'w+')
  file.write(str(tempList[0]))
  file.close
  file = open(fileName, 'a')
  for i in range(1, len(tempList)):
    file.write("\n")
    file.write(str(tempList[i]))
  file.close()

def newFormatterForDecryption(decryptFile):
  '''
      Helps decrypt file

      Takes the file that has been encrypted and decrypts it into a list

      Parameters
      ----------
      decryptFile: str
          The file that needs to be decrypted

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  file = open(decryptFile, 'r')
  lines = file.readlines()
  file.close
  newList = []
  for i in lines:
    temp = i.split(", ", 2)
    temp[0] = temp[0].strip("['")
    temp[0] = temp[0].strip("'")
    temp[1] = int(temp[1])
    temp[2] = float(temp[2].strip("]\n"))
    newList.append(temp)
  return (newList)

def decryptNew(saveName, fileName):
  '''
      Decrypts file

      Decrypts file and finds the green percentage list

      Parameters
      ----------
      fileName: str
          The encrypted file

      saveName: str
          The name of the saved image

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  listToSort = newFormatterForDecryption(fileName)
  listToSort.sort()
  globals()[saveName] = []
  for i in listToSort:
    if i[0] == saveName:
      globals()[saveName].append(i[2])
  return globals()[saveName]

'''
def decryptorBubbleLinear(saveName, fileName):
  listToSort = newFormatterForDecryption(fileName)
  k=0
  n=len(listToSort)
  while (k< n-1):
    i=0
    while (i < n-k-1):
      if listToSort[i] > listToSort[i+1]:
        temp = listToSort[i]
        listToSort[i] = listToSort[i+1]
        listToSort[i+1] = temp
      i+=1
    k+=1
  globals()[saveName] = []
  for i in listToSort:
    if i[0] == saveName:
      globals()[saveName].append(i[2])
  return globals()[saveName]

def decryptorSelectionBinary(saveName,fileName):
  listToSort = newFormatterForDecryption(fileName)
  n = len(listToSort)
  i=0
  while (i < n-1):
    minimum = i
    j = i+1
    while (j < n):
      if(listToSort[ j ] < listToSort[ minimum ]):
        minimum = j
      j+=1
    temp = listToSort[minimum]
    listToSort[minimum] = listToSort[i]
    listToSort[i]=temp
    i+=1

  tempList=[]
  for i in listToSort:
    tempList.append(i[0])
  low = 0
  high = len(tempList)
  key = saveName
  while(low<=high):
    mid = int((low + high) / 2)
    if(tempList[mid]<key):
      low=mid+1
    elif(tempList[mid]>key):
      high=mid-1
    else:
      mid = mid - listToSort[mid][1]
      finalList=[]
      k=0
      while (k < 16):
        finalList.append(listToSort[mid+k][2])
        k+=1
      return (finalList)
'''

def fileClearer(fileName):
  '''
      Clears files

      Parameters
      ----------
      fileName: str
          The file needed to be cleared

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  file = open(fileName, 'w')
  file.close

def splitToPercentGreen(file1, size):
  '''
      Gets the percentage green of an image

      Runs the full formatting and checks each pixel for greenery in terms of percents

      Parameters
      ----------
      file1: str
          The location or name of the image

      size: int
          The number of sections per side of the image

      Returns
      -------
      List

      Raises
      ------
      None

      '''
  image1 = fullFormat(file1, size)
  image1L = []
  for i in range(len(image1)):
    newInt = 0
    for l in range(len(image1[i])):
      if greenCheck(image1[i][l]) == True:
        newInt += 1
    image1L.append(newInt / len(image1[i]))
  return (image1L)

def comparator(usersName,file1, file2, size, directory1, directory2, save1, saveName1, save2, saveName2, fileName):
  '''
      Compares two images

      Compares two images that can come from various locations and be saved or retrieved to directory

      Parameters
      ----------
      usersName: str
          The user's username

      file1: str
          The name or location of the saved image

      file2: str
          The name or location of the saved image

      size: int
          The number of sections per image side to compare to

      directory1: bool
          Whether or not the first image is from the directory

      directory2: bool
          Whether or not the second image is from the directory

      save1: bool
          Whether or not to save the first image to directory

      saveName1: str
          The name to save the image under or the name to retrieve the image from

      save2: bool
          Whether or not to save the second image to directory

      saveName2: str
          The name to save the image under or the name to retrieve the image from

      fileName: str
          The location of the image directory

      Returns
      -------
      Str

      Raises
      ------
      None

      '''

  if directory1 == False:
    image1L = splitToPercentGreen(file1, size)
    if save1 == True:
      encryptorNew(image1L, saveName1, fileName)
      fileImageNames = usersName + "_image_names.txt"
      file = open(fileImageNames, 'a')
      file.write(saveName1)
      file.write('\n')
      file.close()
  else:
    image1L = decryptNew(saveName1, fileName)

  if directory2 == False:
    image2L = splitToPercentGreen(file2, size)
    if save2 == True:
      encryptorNew(image2L, saveName2, fileName)
      fileImageNames = usersName + "_image_names.txt"
      file = open(fileImageNames, 'a')
      file.write(saveName2)
      file.write('\n')
      file.close()
  else:
    image2L = decryptNew(saveName2, fileName)


  totalPercent = 0
  for i in range(len(image1L)):
    percent = image2L[i] / image1L[i] * 100
    totalPercent = (totalPercent * i + percent) / (i + 1)
  totalPercent -= 100
  totalPercent = str(int(totalPercent))
  return ("Image 2 has " + totalPercent + "% greenery in respect to image 1")
