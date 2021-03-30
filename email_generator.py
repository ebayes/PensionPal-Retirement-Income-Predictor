import os
cwd = os.getcwd()
outfile_name = os.path.join(cwd, 'message.eml')

class Gen_Emails(object):

    # ...

    def SaveToFile(self,msg):
        with open(outfile_name, 'w') as outfile:
            gen = generator.Generator(outfile)
            gen.flatten(msg)
