#define the class animal
class animal:
	def __init__(self, arm_len, leg_len, num_eyes, has_tail, is_furry):  #set attributes of animal to self function

		#set attributes 
		self.arm_length = arm_len
		self.leg_length = leg_len
		self.eyes = num_eyes
		self.tail = has_tail
		self.fur = is_furry

#initializing class and setting variables to attributes
falcon = animal(arm_len=3.5, leg_len=1.5, num_eyes=2, has_tail=True, is_furry=False)

#print and label the attributes
def main():
	print("Prairie Falcon Stats")
	print("Wingspan:" ,falcon.arm_length)
	print("Body length:", falcon.leg_length)
	print("Number of eyes:", falcon.eyes)
	print("Tail:", falcon.tail)
	print("Fur:", falcon.fur)
if __name__ == "__main__":
	main()