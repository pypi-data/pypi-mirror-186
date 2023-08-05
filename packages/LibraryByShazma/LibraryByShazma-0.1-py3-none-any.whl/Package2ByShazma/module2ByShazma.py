DEVELOPER = "Shazma Noor"
MENTOR = 'Dr. Arif Butt'
moduleNo = 2

#------------------------Help---------------------
def help():
  print(f'This module# {moduleNo}\nDeveloped By: {DEVELOPER}\nPurpose: Basic Calculator\nMentor: {MENTOR}')

#--------------BubbleSort-Ascending---------------
def myBubbleSortAsc(list):
      i = 0
      while i < len(list):
        j = i+1
        while j < len(list):
          if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
          j +=1
        i += 1

#--------------BubbleSort-Descending--------------
def myBubbleSortDesc(list):
      i = 0
      while i < len(list):
        j = i+1
        while j < len(list):
          if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
          j +=1
        i += 1
#--------------------InsertionSort---------------
def myInsertionSort(list):
    if (n := len(list)) <= 1:
      return
    for i in range(1, n):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j] :
                list[j+1] = list[j]
                j -= 1
        list[j+1] = key

#--------------------MergeSort------------------
def myMergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]
        myMergeSort(L)
        myMergeSort(R)
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
#help()
#list1 = [3, 6, 2, 1, 54,3, 2, 1]
#myInsertionSort(list1)
#myBubbleSortAsc(list1)
#myMergeSort(list1)
#print (list1)