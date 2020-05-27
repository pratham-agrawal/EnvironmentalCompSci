import time
import random
import math
from PIL import Image
global imageSize
imageSize=[]

def imageToRgb(fileName):
  im = Image.open(fileName)
  pixels = list(im.getdata())
  imageSize.append(im.width)
  imageSize.append(im.height)
  return (pixels)

def formatXY(pixels):
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
  temp = []
  for i in range(startY,stopY):
    for l in range(startX,stopX):
      temp.append(pixelsF[i][l])
  return (temp)

def splitToPercentage(pixelsFormatted, numPerSide):
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
  pixels = imageToRgb(fileName)
  newPixels = formatXY(pixels)
  splitBySize = splitToPercentage(newPixels, size)
  return splitBySize

def greenCheck(pixel):
  if pixel[1] <= 55 or pixel[0]+15 > pixel[1] or pixel[2]+15 > pixel[1]:
    return False
  else:
    return True

def comparator(file1,file2,size):
  image1= fullFormat(file1,size)
  image2= fullFormat(file2,size)
  image1L = []
  image2L = []

  for i in range (len(image1)):
    newInt = 0
    for l in range (len(image1[i])):
      if greenCheck(image1[i][l]) == True:
        newInt+=1
    image1L.append(newInt/len(image1[i]))
  print (image1L)

  for i in range (len(image2)):
    newInt = 0
    for l in range (len(image2[i])):
      if greenCheck(image2[i][l]) == True:
        newInt+=1
    image2L.append(newInt/len(image2[i]))
  print (image2L)

  totalPercent = 0
  for i in range (len(image1L)):
    percent = image2L[i]/image1L[i]*100
    totalPercent = (totalPercent * i + percent)/(i+1)
  totalPercent-=100
  return (totalPercent)

def formatterForDecryption(decryptFile):
  file= open(decryptFile,'r')
  lines = file.readlines()
  file.close
  newList=[]
  for i in lines:
    temp=i.split(", ",5)
    temp[0]=float(temp[0].strip('['))
    temp[1]=int(temp[1])
    temp[2]=int(temp[2])
    temp[3]=int(temp[3].strip('('))
    temp[4]=int(temp[4])
    temp[5]=int(temp[5].strip(")]\n"))
    temp[3]=(temp[3],temp[4],temp[5])
    del temp[5]
    del temp[4]
    newList.append(temp)
  return (newList)

def encryptor(image,fileName):
  imageProper = formatXY(imageToRgb(image))
  tempList = formatterForDecryption(fileName)
  ticks = time.time()
  itrack=0
  for i in imageProper:
    ltrack=0
    for l in imageProper[itrack]:
      appendList=[ticks, itrack,ltrack,l]
      tempList.append(appendList)
      ltrack +=1
    itrack +=1
  random.shuffle(tempList)
  file = open(fileName,'w+')
  file.write(str(tempList[0]))
  file.close
  file = open(fileName,'a')
  for i in range (1,len(tempList)):
    file.write("\n")
    file.write(str(tempList[i]))
  file.close()

def fileClearer(fileName):
  file = open(fileName, 'w')
  file.close


def decryptRegular(fileName):
  listToSort = formatterForDecryption(fileName)
  listToSort.sort()
  imageTime=[]
  for i in listToSort:
    if i[0] not in imageTime:
      imageTime.append(i[0])
  for i in imageTime:
    l = 0
    globals()[i] = []
    k = len(listToSort)
    while l in range(0, k):
      if listToSort[l][0] == i:
        globals()[i].append(listToSort[l])
        del listToSort[l]
        k -= 1
      else:
        l += 1

  file = open('holdMyStuff.txt', 'a')
  for i in imageTime:
    for l in globals()[i]:
      file.write(str(l))
      file.write('\n')
  file.close

decryptRegular('image.txt')

#exceptions: size, shape, file type, 3 strand
#globals()[user_input]
