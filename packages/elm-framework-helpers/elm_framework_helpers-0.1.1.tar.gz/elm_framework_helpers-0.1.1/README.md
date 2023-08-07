# Helpers for the ELM framework scripts

## Logging

Here's a sample logging for production:

```
[loggers]
keys=root,Rx,rawsocket

[handlers]
keys=consoleHandler,fileHandler,socketFileHandler

[formatters]
keys=fileFormatter,consoleFormatter,socketFileFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[logger_Rx]
level=INFO
handlers=consoleHandler
qualname=Rx

[logger_rawsocket]
qualname=bittrade_kraken_websocket.connection.generic.raw
handlers=socketFileHandler

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=consoleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=fileFormatter
args=('logfile.log',)

[handler_socketFileHandler]
class=FileHandler
level=DEBUG
formatter=socketFileFormatter
args=('raw_socket.log',)

[formatter_fileFormatter]
format=%(asctime)s   - %(name)s - %(levelname)s - %(message)s
datefmt=%H:%M:%S

[formatter_socketFileFormatter]
format=%(asctime)s - %(message)s
datefmt=%H:%M:%S

[formatter_consoleFormatter]
format=%(asctime)s   - %(levelname)s - %(message)s
datefmt=%H:%M:%S
```