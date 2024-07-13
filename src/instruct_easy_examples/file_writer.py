from instruct_easy import SystemMessage, LLMModel, prompt
from instruct_easy.tools import file_writer
from instruct_easy.tools.file_writer import FileDetails
from typing_extensions import List

context = [
    SystemMessage(
        content="As a Software Engineering Professor,"
                "I am here to help you with your coding tasks so you graduate early."
                "Also for Python related question,"
                "I will include the init file in the directory, so that it is a package."
                "Finally, I will include project files containing dependencies as needed,"
                "and will ensure that the file extensions are correct."
    )
]


@prompt(
    context=context,
    model=LLMModel.Claude35_Sonnet,
)
@file_writer(base_dir="../../file_writer_output")
def my_function(_: str, input: List[FileDetails] = None): ...


if __name__ == "__main__":
    message_py = "Hello Professor, how would you write the Y Combinator function in Python using the standard library?"
    "Place the code at the base of my project directory."
    "Also for Python, do not omit the init file in the directory, so that it is a package."
    "Thank you."
    my_function(message_py)  # Example usage

    message_rb = "Hello Professor, how would you write the Y Combinator function in Ruby using the standard library?"
    "Place the code at the base of my project directory."
    "Thank you."
    my_function(message_rb)  # Example usage

    message_js = "Hello Professor, how would you write the Y Combinator function in Javascript using the standard library?"
    "Place the code at the base of my project directory."
    "Thank you."
    my_function(message_js)  # Example usage

    # message_lisp = "Hello Professor, how would you write the Y Combinator function in Lisp using the standard library?"
    # "Place the code at the base of my project directory."
    # "Thank you."
    # my_function(message_lisp)  # Example usage

    message_scheme = "Hello Professor, how would you write the Y Combinator function in Scheme using the standard library?"
    "Place the code at the base of my project directory."
    "Thank you."
    my_function(message_scheme)  # Example usage

    message_nim = "Hello Professor, how would you write the Y Combinator function in Nim using the standard library?"
    "Place the code at the base of my project directory."
    "Thank you."
    my_function(message_nim)  # Example usage

    # message_zig = "Hello Professor, how would you write the Y Combinator function in Zig using the standard library?"
    # "Place the code at the base of my project directory."
    # "Thank you."
    # my_function(message_zig)  # Example usage
