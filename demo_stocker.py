from modules.stocker.stocker import Stocker

s = Stocker('MSFT')
s.predict_future(365)