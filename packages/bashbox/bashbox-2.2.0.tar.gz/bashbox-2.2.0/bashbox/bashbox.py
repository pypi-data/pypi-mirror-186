class bashbox:
	"""A bashbox."""
	def __init__(self, content):
		# inits with title and content strings
		# The title can optionally be set to a string, and it will be printed as a separate section of the box.
		self.title = None
		self.content = content

	def draw(self):
		"""Draw the bashbox."""
		# this variable determines the max width the box can be.
		maxWidth = 40

		# splits self.content into an array of strings that are all maxWidth long or less.
		content = __import__('textwrap').wrap(self.content, maxWidth)

		# gets max length that box needs to be
		boxSize = max((len(self.title) if self.title != None else 0), len(max(content, key=len)))

		# print title
		if self.title != None:
			print("+" + ("-" * (boxSize + 2)) + "+")
			print("| " + self.title + (" " * (boxSize - len(self.title))) + " |")

		# print border between title and content
		print("+" + ("-" * (boxSize + 2)) + "+")

		# print content
		for i in range(len(content)):
			print("| " + content[i] + (" " * (boxSize - len(content[i]))) + " |")

		print("+" + ("-" * (boxSize + 2)) + "+")