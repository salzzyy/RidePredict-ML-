import traceback
import sys


class CustomException(Exception):
    """
    A custom exception class that provides detailed error messages, including the filename and line number.
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail: sys):
        """
        Extracts detailed error information, including the filename and line number where the error occurred.

        :param error_message: The actual error message.
        :param error_detail: sys module to extract traceback details.
        :return: A formatted error string.
        """
        _, _, exc_tb = error_detail.exc_info()  # Fixed method name
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return f"Error in {file_name}, line {line_number}: {error_message}"

    def __str__(self):
        return self.error_message
