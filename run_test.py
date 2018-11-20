import urllib2
import re
import random
from collections import defaultdict, deque

print "----------------------------------------------------------------"
print "Ancient Epic Generator"
print "----------------------------------------------------------------"

print """

            ^^                   @@@@@@@@@
       ^^       ^^            @@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@              ^^
                           @@@@@@@@@@@@@@@@@@@@
 ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
 ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
   ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~
   ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~
 ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
       ~             ~        ~      ~      ~~   ~             ~

Special thanks to Christopher Johnson for the wine-dark sea ASCII art. And to CodeAcademy for the base of the Markov Chain module.

"""

class MarkovChain:

  def __init__(self, num_key_words=20):
    self.num_key_words = num_key_words
    self.lookup_dict = defaultdict(list)
    #store a regular expression object with all punctuation and new lines
    self._punctuation_regex = re.compile('[,.!;\?\:\-\[\]\n]+')
    self._seeded = False
    self.__seed_me()
    print "Punctuation Regex: " + str(self._punctuation_regex)

  #this allows you to seed the random numbers you generate 
  def __seed_me(self, rand_seed=None):
    if self._seeded is not True:
      try:
        if rand_seed is not None:
          random.seed(rand_seed)
          print "random seed = " + str(random.seed(rand_seed))
        else:
          #seed random numbers using current time
          random.seed()
          print "random seed = " + str(random.seed())
        self._seeded = True
      except NotImplementedError:
        self._seeded = False

  """
  " Build Markov Chain from data source.
  " Use add_file() or add_string() to add the appropriate format source
  """
  def add_file(self, file_path):
    content = ''
    with open(file_path, 'r') as fh:
      self.__add_source_data(fh.read())

  def add_string(self, str):
    self.__add_source_data(str)

  def __add_source_data(self, str):
    #replace all punctuation and new lines with spaces using regex object, then lowercase everything
    clean_str = self._punctuation_regex.sub(' ', str).lower()
    print "Clean string: " + clean_str
    tuples = self.__generate_tuple_keys(clean_str.split())
    for t in tuples:
      if yes_tuple.lower() == "y":
        print t
        self.lookup_dict[t[0]].append(t[1])
      else:
        self.lookup_dict[t[0]].append(t[1])

  def __generate_tuple_keys(self, data):
    if len(data) < self.num_key_words:
      return

    for i in xrange(len(data) - self.num_key_words):
      yield [ tuple(data[i:i+self.num_key_words]), data[i+self.num_key_words] ]

  """
  " Generates text based on the data the Markov Chain contains
  " max_length is the maximum number of words to generate
  """
  def generate_text(self, story_length):
    context = deque()
    output = []
    if len(self.lookup_dict) > 0:
      self.__seed_me(rand_seed=len(self.lookup_dict))
      print "length of dictionary: " + str(len(self.lookup_dict))

      idx = random.randint(0, len(self.lookup_dict)-1)
      print "idx: " + str(idx) 
      chain_head = list(self.lookup_dict.keys()[idx])
      print "chain head: " + str(chain_head)
      context.extend(chain_head)

      while len(output) < (story_length - self.num_key_words):
        next_choices = self.lookup_dict[tuple(context)]
        if len(next_choices) > 0:
          next_word = random.choice(next_choices)
          context.append(next_word)
          output.append(context.popleft())
        else:
          break
      output.extend(list(context))
    return output

while True:

		explication = raw_input("Before we get started, would you like to know how I modified the Markov Chain module from CodeAcademy? [y or n]: ")
		if explication.lower() == "y":
			print """ First, I learned about information theory and how Markov chains work from Khan Academy. Then I looked up every line of code that I did not recognize in the module. After that I commented on the source code and clarified how it all works for other curious novice coders. Then I enabled straightforward explication and user control of key Markov chain parameters. After that I sourced the text of Homer's Odyssey from the Gutenberg Project using Urllib. And now you're ready to use this program to create your own computer-generated ancient epic! 
			"""
		else:
			continue
	
		url = urllib2.urlopen('http://www.gutenberg.org/files/24269/24269-0.txt')

		author = url.read(100000)
		print "----------------------------------------------------------------"
		print "MARKOV CHAIN INITIALIZER:"
		print "----------------------------------------------------------------"
		yes_tuple = raw_input("Would you like to print the tuples before we display the story text?[y or n]: ")
		print " "
		story_length = raw_input("How many words would you like your story to be? Enter a number: ")
		story_length = int(story_length)
		print " "
		key_words = raw_input("The more coherent the machine's story is, the less original it will be. How coherent would you like your story to be? Enter a number from 1 to 10: ")
		key_words = int(key_words)
		key_words = key_words * 2
		print "----------------------------------------------------------------"
		print "MARKOV INTERNALS:"
		print "----------------------------------------------------------------"
		markov = MarkovChain(key_words)
		markov.add_string(author)
		text_list = markov.generate_text(story_length)
		output = " ".join(text_list)
		print "----------------------------------------------------------------"
		print "STORY:"
		print "----------------------------------------------------------------"
		print output
		print "----------------------------------------------------------------"
		controller = raw_input("Would you like to exit?:[y or n] ")
		if controller.lower() == "y":
			break
		else:
			continue 



