import ast
import logging


def evaluate_recursively(obj, logger: logging.Logger = None):
    """ Evaluates a python object

        Example
            '{give_away': {'amount': 500}}'
            returns
            {give_away': {'amount': 500}}

        Args:
            obj: any python object
            logger: logging

        Return:
            The actual evaluated python object down to the root element
    """
    try:
        if isinstance(obj, list):
            data = [evaluate_recursively(el, logger) for el in obj]
        elif isinstance(obj, dict):
            data = obj
        else:
            data = ast.literal_eval(obj)
        for k, v in data.items():
            data[k] = evaluate_recursively(v, logger)
    except (TypeError, AttributeError, ValueError, SyntaxError) as e:
        logger.warning(f"Warning: object could not be parsed. Error received: {str(e)}")
        return obj
    return data
