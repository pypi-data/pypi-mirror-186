DEVELOPER = "Shazma Noor"
MENTOR = 'Dr. Arif Butt'
moduleNo = 3

#------------------------Help---------------------
def help():
  print('This module# {}\nDeveloped By: {}\nPurpose: Basic Calculator\nMentor: {}'.format(moduleNo, DEVELOPER, MENTOR))

#--------------LinearSearch---------------
def myLinearSearch(list, target):
    for i in list:
      if i == target:
        return f'{target} found at index:   {list.index(i)}'

#--------------BinarySearch---------------
def myBinarySearch(list, target):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = low + (high - low) // 2

		if list[mid] == target:
			return  f'{target} found at index:   {mid}'
		elif list[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return f'{target} not found'
list1 = [1, 2, 3, 4]
print(myBinarySearch(list1, 4))
