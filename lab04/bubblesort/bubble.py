def bubblesort(nums):
	# Sorts the list of nums with Bubblesort
	with open('bubblesorting.csv', 'w') as bubbles:
		bubbles.write(', '.join(map(str, nums))+'\n')
		while True:
			swapped = 0
			for i in range(len(nums))[:-1]:
				if nums[i] > nums[i+1]:
					nums[i], nums[i+1] = nums[i+1], nums[i]
					bubbles.write(', '.join(map(str, nums))+'\n')
					swapped = 1
			if swapped == 0: break