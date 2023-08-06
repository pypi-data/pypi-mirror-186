import damv1manipulation as mpl
from .mytime7 import currentTime7 as cT7
from .mylogger import logger

def printlf_dump_v1(_writeOnFile, _fullfilename = '', _file = None, *_messaagePrintlf, **kwargs):
    f = _file
    text_message = ''
    if len(_messaagePrintlf)!=0:
        text_message = ' '.join(_messaagePrintlf)
        text_message = str(text_message.removesuffix('\n')).rstrip()

        logger(cT7(), text_message)
        if _writeOnFile == True:
            if f == None: 
                f = open(_fullfilename,'w')
                f.write(cT7());f.write('\n')
            f.write(cT7() + ' ' + text_message + '\n')
    return f