"""
The logging module lets you display logging messages.
Log messages create a "breadcrumb trail" of what your program is doing.
After calling logging.basicConfig() to set up logging, call logging.debug(‘This is the message') to create a log message.
When done, you can disable the log messages with logging.disable(logging.CRITICAL)
Don't use print() for log messages: It's hard to remove the mall when you're done debugging.
The five log levels are: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
You can also log to a file instead of the screen with the filename keyword argument in the logging.basicConfig() function.
"""
#este modulo te permite mostrar log messages en tu pantalla mientras tu programa corre
import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #muestra los log messages en consola
logging.basicConfig(filename= "myProgramLog.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #manda los log messages a un file
#logging.disable(logging.CRITICAL) #deshabilita todos los log messages, comentar esta linea si las queremos


logging.debug("Start of program")
def factorial(n):
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i,total))

    logging.debug("Return value is %s" % (total))
    return total

print(factorial(5))
logging.debug("End of program")