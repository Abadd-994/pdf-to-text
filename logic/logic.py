# Acer Class
class Acer:
    def execute(self):
        print('Acer IDE')

# Mac Class
class Mac:
    def execute(self):
        print('Surfing with Safari')
        print('Mac IDE')

# Laptop Class
class Laptop:
    def code(self, ide):
        ide.execute()  # This calls the execute method of the ide (Acer or Mac)

# Instantiate an IDE object (in this case, Mac)
ide = Mac()  # You can also try Acer() here instead of Mac

# Create a Laptop object
lapl = Laptop()

# Call the code method on the Laptop, passing in the IDE object
lapl.code(ide)  # This will call Mac's execute() method
