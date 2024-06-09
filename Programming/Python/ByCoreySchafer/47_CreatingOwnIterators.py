#by class
class Sentence:
	def __init__(self,sentence):
		self.sentence=sentence
		self.index=0
		self.words=self.sentence.split()
	def __iter__(self):
		return self
	def __next__(self):
		if self.index>=len(self.words):
			raise StopIteration
		index=self.index
		self.index+=1
		return self.words[index]

my_sentence=Sentence('This is the test')
for word in my_sentence:
	print(word)
my_sentence=Sentence('This is the test')
print("next: ",next(my_sentence))
print("next: ",next(my_sentence))
print("next: ",next(my_sentence))


#by generator
def sentence(sentence):
	for word in sentence.split():
		yield word
my_sentence=sentence('This is the test')
for word in my_sentence:
	print("inside for loop: ",word)
my_sentence=sentence('This is the test')
print("next: ",next(my_sentence))
print("next: ",next(my_sentence))
print("next: ",next(my_sentence))
print("next: ",next(my_sentence))

'''
output must be like :
This
is
the
test
'''