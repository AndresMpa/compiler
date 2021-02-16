
  # ____ ___  _   _ ____ _____  _    _   _ _____ ____  
 # / ___/ _ \| \ | / ___|_   _|/ \  | \ | |_   _/ ___| 
# | |  | | | |  \| \___ \ | | / _ \ |  \| | | | \___ \ 
# | |__| |_| | |\  |___) || |/ ___ \| |\  | | |  ___) |
 # \____\___/|_| \_|____/ |_/_/   \_\_| \_| |_| |____/ 

DIGITS = '0123456789'

 # _____ ____  ____   ___  ____  ____  
# | ____|  _ \|  _ \ / _ \|  _ \/ ___| 
# |  _| | |_) | |_) | | | | |_) \___ \ 
# | |___|  _ <|  _ <| |_| |  _ < ___) |
# |_____|_| \_\_| \_\\___/|_| \_\____/ 

# This class will manage the error that we write on the code
class Error:
  def __init__(self, pos_start, pos_end, error_name, details):
    self.pos_start = pos_start
    self.pos_end = pos_end
    self.error_name = error_name
    self.details = details
    # Display errors as strings
    def as_strimg(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

# This class basically throw error when we write ilegal character like letters
class IllegalCharError(Error):
  def __init__(self, pos_start, pos_end, details):
    super().__init__(pos_start, pos_end, 'IllegalCharError', details)
