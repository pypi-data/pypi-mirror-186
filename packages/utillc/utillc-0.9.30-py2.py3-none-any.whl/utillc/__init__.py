from .utillc import *
from .utillc import utillc_version
try :
    from .qtp  import video
except Exception as e22  :
    print ("no qt5 " + str(e22))
#from .expression import *

__version__ = utillc_version
