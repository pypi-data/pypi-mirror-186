import logging
import sys

import argh
from doc2tei import _process_doc
import os
import shutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def _convert_file(
    input_file_path: str,
    keep_transient_files: bool = False,
    validation_schema: str = "metopes",
    out_dir: str = ".",
):
    """
    Converts a *.docx file to XML TEI.
    """
    destination_folder = os.getcwd()
    if out_dir != ".":
        os.makedirs(out_dir, exist_ok=True)
        copy_dest = os.path.join(out_dir, os.path.basename(input_file_path))
        shutil.copy(input_file_path, copy_dest)
        input_file_path = copy_dest
        destination_folder = out_dir
    if not os.path.exists(input_file_path):
        sys.exit(f"no such file: {input_file_path}")
    _process_doc(
        input_file_path,
        destination_folder,
        logger,
        keep_transient_files,
        validation_schema,
    )


def run_cli():
    argh.dispatch_command(_convert_file)


if __name__ == "__main__":
    run_cli()
