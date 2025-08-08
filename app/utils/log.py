import inspect
import os
from app.utils.enum.str_color import StrColor

str_color = StrColor()

def log_info(*message: str) -> None:
    caller_frame = inspect.stack()[1]

    abs_path = os.path.abspath(caller_frame.filename)

    path_parts = abs_path.split(os.sep)

    shortened_path = os.sep.join(path_parts[-3:])
    
    function_name = caller_frame.function

    full_message = " ".join(str(m) for m in message)

    print(f"{str_color.GREEN('INFO')}:{shortened_path}:{function_name} - {full_message}")

def log_error(*message: str) -> None:
    caller_frame = inspect.stack()[1]

    abs_path = os.path.abspath(caller_frame.filename)

    path_parts = abs_path.split(os.sep)

    shortened_path = os.sep.join(path_parts[-3:])
    
    function_name = caller_frame.function

    full_message = " ".join(str(m) for m in message)

    print(f"{str_color.RED('ERROR')}:{shortened_path}:{function_name} - {full_message}")