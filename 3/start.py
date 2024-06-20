# import discount
import pakiet
import pakiet.fun as pf  # import jako alias
from pakiet import fun

# pakiet.powitanie()  # AttributeError: module 'pakiet' has no attribute 'powitanie'
pf.powitanie()
fun.powitanie()
pakiet.fun.powitanie()
# Po dodaniu w __init__.py __all__ = ['powitanie'] działą
pakiet.powitanie()
# info() nie jest w pliku __init__
# uzyjemy z bezpośredniego importu
pf.info()
