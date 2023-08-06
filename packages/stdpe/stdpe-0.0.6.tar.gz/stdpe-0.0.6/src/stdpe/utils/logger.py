"""
Module contains a Logger for output logs into the console and/or to Azure over the app insights sdk. 
"""

import datetime
import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler


class Logger():
  """Class to handle the console and the Azure (app insights sdk) logging output.

  Log level meanings
  ------------------
  DEBUG:    Detailed information
  INFO:     Confirmation that things are working as expected
  WARNING:  Warnings
  ERROR:    Serious problem
  CRITICAL: A serious error
  """
  # class variables
  logger = None
  properties = {
      'custom_dimensions': {
          'tenantIdentifier': None,
          'machineIdentifier': None,
      }
  }
  console_msg_format: str = '[%(asctime)s %(levelname)s] %(message)s'
  az_msg_format: str = '%(message)s'
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Logger, cls).__new__(cls)
      cls.logger = logging.getLogger('logger')
      cls.logger.setLevel(logging.DEBUG)
    return cls._instance

  @classmethod
  def add_console_handler(cls, log_level: int):
    """Creates an console output handler.

    Parameters
    ----------
    log level (int): Sets the log level of the console output (DEBUG: 10, INFO: 20, WARNING: 30, DEBUG: 40, CRITICAL: 50)
    """

    if log_level not in (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL):
      raise ValueError(
          f"log_level of {log_level} is not valid. Valid values are: DEBUG: 10, INFO: 20, WARNING: 30, DEBUG: 40, CRITICAL: 50"
      )

    handler_names = [i.name for i in cls.logger.handlers]
    if 'console' not in handler_names:
      # create console log handler
      c_handler = logging.StreamHandler()
      logging.Formatter.formatTime = (lambda self, record, datefmt=None: datetime.datetime.fromtimestamp(
          record.created, datetime.timezone.utc).astimezone().isoformat(sep=' ', timespec='milliseconds'))
      console_handler_fmt = logging.Formatter(fmt=cls.console_msg_format,)
      c_handler.setFormatter(fmt=console_handler_fmt)
      c_handler.setLevel(log_level)
      c_handler.name = 'console'
      cls.logger.addHandler(c_handler)

  @classmethod
  def add_az_handler(cls, log_level: int, app_insights_key: str):
    """Creates an Azure output handler with the app insights sdk.

    Parameters
    ----------
    log level (int):        Set the log level of the console output (DEBUG: 10, INFO: 20, WARNING: 30, DEBUG: 40, CRITICAL: 50)
    app_insights_key (str): Requires The app insights instrumentation key from Azure.
    """

    if log_level not in (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL):
      raise ValueError(
          f"log_level of {log_level} is not valid. Valid values are: DEBUG: 10, INFO: 20, WARNING: 30, DEBUG: 40, CRITICAL: 50"
      )
    handler_names = [i.name for i in cls.logger.handlers]
    if 'azure' not in handler_names:
      # create azure log handler
      az_handler = AzureLogHandler(connection_string=f'InstrumentationKey={app_insights_key}')
      azure_handler_fmt = logging.Formatter(fmt=cls.az_msg_format)
      az_handler.setFormatter(fmt=azure_handler_fmt)
      az_handler.setLevel(log_level)
      az_handler.name = 'azure'
      cls.logger.addHandler(az_handler)

  @classmethod
  def set_console_log_level(cls, level: int):
    """Sets the console log level

    Parameters
    ----------
    level (int):  Set the log level of the console output (DEBUG: 10, INFO: 20, WARNING: 30, DEBUG: 40, CRITICAL: 50)
    """

    if level not in (logging.DEBUG, logging.INFO, logging.WARNING, logging.DEBUG, logging.ERROR, logging.CRITICAL):
      raise ValueError()
    try:
      for idx, handler in enumerate(cls.logger.handlers):
        if handler.name == 'console':
          cls.logger.handlers[idx].level = level
    except Exception as e:
      print(e)

  @classmethod
  def set_az_log_level(cls, level: int):
    """Sets the azure log level

    Parameters
    ----------
    level (int):  Set the log level of the console output (DEBUG: 10, INFO: 20, WARNING: 30, DEBUG: 40, CRITICAL: 50)
    """

    if level not in (logging.DEBUG, logging.INFO, logging.WARNING, logging.DEBUG, logging.ERROR, logging.CRITICAL):
      raise ValueError()
    try:
      for idx, handler in enumerate(cls.logger.handlers):
        if handler.name == 'azure':
          cls.logger.handlers[idx].level = level
    except Exception as e:
      print(e)

  @classmethod
  def set_az_properties(cls, tenant_id: str = None, machine_id: str = None):
    """Sets the given properties to the azure handler properties. Propperties will be visible inside app insights on Azure.

    Parameters
    ----------
    tenant_id (str): Tenant identifier
    machine_id (str): Machine identifier
    """
    cls.properties['custom_dimensions']['tenantIdentifier'] = tenant_id
    cls.properties['custom_dimensions']['machineIdentifier'] = machine_id

  @classmethod
  def debug(cls, msg: str):
    cls.logger.debug(msg, extra=cls.properties)

  @classmethod
  def info(cls, msg: str):
    cls.logger.info(msg, extra=cls.properties)

  @classmethod
  def warning(cls, msg: str):
    cls.logger.warning(msg, extra=cls.properties)

  @classmethod
  def error(cls, msg: str):
    cls.logger.error(msg, extra=cls.properties)

  @classmethod
  def critical(cls, msg: str):
    cls.logger.critical(msg, extra=cls.properties)
