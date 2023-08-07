class bashbox:
	def __init__(self, content):
		self.content = content

	def draw(self):
		print("+" + "-" * (len(self.content) + 0) + "+")
		print("|" + self.content + "|")
		print("+" + "-" * (len(self.content) + 0) + "+")