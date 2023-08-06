import logging
import re
import fnmatch
from typing import List, Tuple
import os
import os.path
import sys
from subprocess import Popen, PIPE
import shutil
from xml.etree import ElementTree as ET
import glob
import base64
from typing import Union

SOFFICE_PATH = shutil.which("soffice")
JAVA_PATH = shutil.which("java")
RESOURCES_PATH = os.path.dirname(os.path.abspath(__file__)) + "/resources/"
SAXON_PATH = os.getenv("SAXON_PATH") or (RESOURCES_PATH + "saxon9.jar")
XMLLINT_PATH = shutil.which("xmllint")

if not SOFFICE_PATH:
    sys.exit("Could not find soffice. Is it in your PATH ?")
if not JAVA_PATH:
    sys.exit("Could not find java. Is it in your PATH ?")
if not SAXON_PATH:
    sys.exit(
        "Could not find the Saxon jar. Please set SAXON_PATH environment variable."
    )
if not os.path.isfile(SAXON_PATH):
    sys.exit(
        "Could not find the Saxon jar. Please check your SAXON_PATH environment variable."
    )
if not XMLLINT_PATH:
    sys.exit("Could not find xmllint. Is it in your PATH ?")


def _silent_remove(path: str):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass


def _union_java_output(std_out: bytes, std_err: bytes) -> Union[bytes, str]:
    """
    Java outputs errors to STDOUT ???
    """
    if std_err:
        try:
            out = std_err.decode("utf-8")
            out = out.strip()
            if out:
                return out
        except UnicodeDecodeError:
            return std_err
    if std_out:
        try:
            out = std_out.decode("utf-8")
            out = out.strip()
            if out:
                return out
        except UnicodeDecodeError:
            return std_out
    return "subprocess provided no error output"


def _find_files(what: str, where: str = ".") -> List[str]:
    rule = re.compile(fnmatch.translate(what), re.IGNORECASE)
    return [
        "{}{}{}".format(where, os.path.sep, name)
        for name in os.listdir(where)
        if rule.match(name)
    ]


def _cli_exec(cli_args: list, logger: logging.Logger) -> Tuple[int, bytes, bytes]:
    logger.debug(" ".join(cli_args))
    p = Popen(
        cli_args,
        stdout=PIPE,
        stderr=PIPE,
    )
    out, err = p.communicate()
    err_code = p.returncode
    p.terminate()
    return err_code, out, err


def _clean_transient_files(transient_files: list, keep_them: bool = False):
    if not keep_them:
        for transient_file_path in transient_files:
            _silent_remove(transient_file_path)


def _check_validation_schema(schema_name: str, logger: logging.Logger) -> str:
    valid_validation_schemas = ["metopes", "openedition"]
    if schema_name not in valid_validation_schemas:
        logger.warning(
            f"{schema_name} validation schema not available. Forcing metopes validation schema."
        )
        return "metopes"
    return schema_name


def _write_binary_to_file(
    file_path: str, content: bytes, logger: logging.Logger
) -> bool:
    with open(file_path, "wb") as f:
        f.write(content)
        logger.debug("Wrote {}".format(os.path.basename(file_path)))
    return True


def _process_doc(
    doc_file,
    working_dir: str,
    logger: logging.Logger,
    keep_transient_files: bool = False,
    validation_schema: str = "metopes",
) -> Tuple[bool, Union[str, bytes]]:
    validation_schema = _check_validation_schema(validation_schema, logger)
    doc_file_no_extension = os.path.splitext(doc_file)[0]
    transient_files = []
    #
    # CONVERSION  XML
    #
    transient_files.append(os.path.join(working_dir, doc_file_no_extension + ".xml"))
    return_code, out, err = _cli_exec(
        [
            SOFFICE_PATH,
            "--invisible",
            "--convert-to",
            "xml:OpenDocument Text Flat XML",
            "--outdir",
            working_dir,
            doc_file,
        ],
        logger,
    )

    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        os.rename(
            os.path.join(
                working_dir,
                doc_file_no_extension + ".xml",
            ),
            os.path.join(working_dir, doc_file_no_extension + "_00.xml"),
        )
        logger.debug(
            "Wrote {}".format(os.path.basename(doc_file_no_extension + "_00.xml"))
        )
        transient_files.append(doc_file_no_extension + "_00.xml")

    #
    # TRANSFORMATIONS XSL : 1 cleanup
    #
    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_00.xml",
            RESOURCES_PATH + "cleanup/cleanup.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(doc_file_no_extension + "_01_clean.xml", out, logger):
            transient_files.append(doc_file_no_extension + "_01_clean.xml")
    #
    # TRANSFORMATIONS XSL : 2 normalisation
    #
    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_01_clean.xml",
            RESOURCES_PATH + "normalisation/normalizea.xsl",
        ],
        logger,
    )

    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(
            doc_file_no_extension + "_02a_normalize.xml", out, logger
        ):
            transient_files.append(doc_file_no_extension + "_02a_normalize.xml")

    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_02a_normalize.xml",
            RESOURCES_PATH + "normalisation/normalizeb.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(
            doc_file_no_extension + "_02b_normalize.xml", out, logger
        ):
            transient_files.append(doc_file_no_extension + "_02b_normalize.xml")

    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_02b_normalize.xml",
            RESOURCES_PATH + "normalisation/normalizec.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(
            doc_file_no_extension + "_02c_normalize.xml", out, logger
        ):
            transient_files.append(doc_file_no_extension + "_02c_normalize.xml")

    control_xml = ET.fromstring(out.decode("utf-8"))
    for error_node in control_xml.findall(".//FATAL"):
        logger.fatal(error_node.text)
        _clean_transient_files(transient_files, keep_transient_files)
        return False, "Not OK"

    #
    # TRANSFORMATIONS XSL : 3 enrich
    #

    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_02c_normalize.xml",
            RESOURCES_PATH + "enrich/enrich.xsl",
        ],
        logger,
    )

    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(doc_file_no_extension + "_03_enrich.xml", out, logger):
            transient_files.append(doc_file_no_extension + "_03_enrich.xml")

    control_xml = ET.fromstring(out.decode("utf-8"))
    for error_node in control_xml.findall(".//FATAL"):
        logger.fatal(error_node.text)
        _clean_transient_files(transient_files, keep_transient_files)
        return False, "Not OK"

    #
    # TRANSFORMATIONS XSL : 4 sp
    #

    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_03_enrich.xml",
            RESOURCES_PATH + "floatingText/sp.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(doc_file_no_extension + "_04a_sp.xml", out, logger):
            transient_files.append(doc_file_no_extension + "_04a_sp.xml")

    control_xml = ET.fromstring(out.decode("utf-8"))
    for error_node in control_xml.findall(".//FATAL"):
        logger.fatal(error_node.text)
        _clean_transient_files(transient_files, keep_transient_files)
        return False, "Not OK"
        
    #
    # TRANSFORMATIONS XSL : 4a bis : figure
    #

    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_04a_sp.xml",
            RESOURCES_PATH + "floatingText/figure.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(doc_file_no_extension + "_04abis_fig.xml", out, logger):
            transient_files.append(doc_file_no_extension + "_04abis_fig.xml")

    control_xml = ET.fromstring(out.decode("utf-8"))
    for error_node in control_xml.findall(".//FATAL"):
        logger.fatal(error_node.text)
        _clean_transient_files(transient_files, keep_transient_files)
        return False, "Not OK"

    #
    # TRANSFORMATIONS XSL : 4 floatingText test pour commit news
    #

    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_04abis_fig.xml",
            RESOURCES_PATH + "floatingText/floatingText.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(
            doc_file_no_extension + "_04b_floatingText.xml", out, logger
        ):
            transient_files.append(doc_file_no_extension + "_04b_floatingText.xml")

    control_xml = ET.fromstring(out.decode("utf-8"))
    for error_node in control_xml.findall(".//FATAL"):
        logger.fatal(error_node.text)
        _clean_transient_files(transient_files, keep_transient_files)
        return False, "Not OK"
    #
    # TRANSFORMATIONS XSL : 4 floatingText
    #

    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_04b_floatingText.xml",
            RESOURCES_PATH + "floatingText/hierarchize.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(
            doc_file_no_extension + "_04c_floatingText.xml", out, logger
        ):
            transient_files.append(doc_file_no_extension + "_04c_floatingText.xml")

    #
    # TRANSFORMATIONS XSL : 5 control hierarchy
    #
    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_04c_floatingText.xml",
            RESOURCES_PATH + "control/control-hierarchy.xsl",
        ],
        logger,
    )

    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(
            doc_file_no_extension + "_05_control.xml", out, logger
        ):
            transient_files.append(doc_file_no_extension + "_05_control.xml")

    control_xml = ET.fromstring(out.decode("utf-8"))
    for error_node in control_xml.findall(".//FATAL"):
        logger.fatal(error_node.text)
        _clean_transient_files(transient_files, keep_transient_files)
        return False, "Not OK"

    #
    # TRANSFORMATIONS XSL : 6 hierarchise
    #
    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_05_control.xml",
            RESOURCES_PATH + "hierarchize/hierarchize.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(
            doc_file_no_extension + "_06_hierarchize.xml", out, logger
        ):
            transient_files.append(doc_file_no_extension + "_06_hierarchize.xml")
    #
    # TRANSFORMATIONS XSL : 7 to TEI
    #
    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_06_hierarchize.xml",
            RESOURCES_PATH + "totei-modules/totei.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        if _write_binary_to_file(doc_file_no_extension + "_07_tei.xml", out, logger):
            transient_files.append(doc_file_no_extension + "_07_tei.xml")
    #
    # TRANSFORMATIONS XSL : 7 CONTROL STYLES
    #
    return_code, out, err = _cli_exec(
        [
            JAVA_PATH,
            "-jar",
            SAXON_PATH,
            doc_file_no_extension + "_07_tei.xml",
            RESOURCES_PATH + "control/control-styles.xsl",
        ],
        logger,
    )
    if return_code != 0:
        _clean_transient_files(transient_files, keep_transient_files)
        return False, _union_java_output(out, err)
    else:
        _write_binary_to_file(
            doc_file_no_extension + "_08_tei_metopes.xml", out, logger
        )

    if validation_schema == "metopes":
        #
        # VALIDATION
        #
        return_code, out, err = _cli_exec(
            [
                XMLLINT_PATH,
                #        "--valid",
                "--relaxng",
                RESOURCES_PATH + "schema/metopes.rng",
                doc_file_no_extension + "_08_tei_metopes.xml",
                #       "--noout",
            ],
            logger,
        )
        transient_files.append(doc_file_no_extension + "_08_tei_metopes.xml")
        if return_code != 0:
            logger.error(
                "Validate {} {}".format(
                    os.path.basename(doc_file_no_extension + "_08_tei_metopes.xml"),
                    _union_java_output(out, err),
                )
            )
        else:
            logger.info(
                "Validate {}".format(
                    os.path.basename(
                        doc_file_no_extension
                        + "_08_tei_metopes.xml validates {}".format(validation_schema)
                    )
                )
            )
    elif validation_schema == "openedition":
        #
        # TRANSFORMATIONS XSL : 8 to OpenEdition
        #
        return_code, out, err = _cli_exec(
            [
                JAVA_PATH,
                "-jar",
                SAXON_PATH,
                doc_file_no_extension + "_08_tei_metopes.xml",
                RESOURCES_PATH + "toOpenedition/toOpenedition.xsl",
            ],
            logger,
        )
        if return_code != 0:
            _clean_transient_files(transient_files, keep_transient_files)
            return False, _union_java_output(out, err)
        else:
            _write_binary_to_file(
                doc_file_no_extension + "_09_tei_openedition.xml", out, logger
            )
            transient_files.append(doc_file_no_extension + "_09_tei_openedition.xml")

        #
        # VALIDATION
        #
        return_code, out, err = _cli_exec(
            [
                XMLLINT_PATH,
                #      "--valid",
                "--relaxng",
                RESOURCES_PATH + "schema/openedition.rng",
                doc_file_no_extension + "_09_tei_openedition.xml",
                #     "--noout",
            ],
            logger,
        )
        if return_code != 0:
            logger.error(
                "Validate {} {}".format(
                    os.path.basename(doc_file_no_extension + "_09_tei_openedition.xml"),
                    _union_java_output(out, err),
                )
            )
        else:
            logger.info(
                "Validate {}".format(
                    os.path.basename(
                        doc_file_no_extension
                        + "_09_tei_openedition.xml validates {}".format(
                            validation_schema
                        )
                    )
                )
            )
    #
    # TRAITEMENT DES IMAGES
    #
    for b64_path in glob.glob(working_dir + "/images/*.base64"):
        destination_path, _ = os.path.splitext(b64_path)
        with open(destination_path, "wb") as destination_file:
            with open(b64_path, "rb") as b64_file:
                destination_file.write(base64.decodebytes(b64_file.read()))
        _silent_remove(b64_path)

    if validation_schema == "metopes":
        shutil.copy(
            os.path.join(working_dir, doc_file_no_extension + "_08_tei_metopes.xml"),
            os.path.join(working_dir, doc_file_no_extension + ".xml"),
        )
    if validation_schema == "openedition":
        shutil.copy(
            os.path.join(
                working_dir, doc_file_no_extension + "_09_tei_openedition.xml"
            ),
            os.path.join(working_dir, doc_file_no_extension + ".xml"),
        )

    _clean_transient_files(transient_files, keep_transient_files)

    return True, "All OK"


def doc2tei(working_dir: str, logger: logging.Logger, options: dict = None):
    options = options or {}
    keep_transient_files = False
    if options.get("keep_transient_files", False) == "oui":
        keep_transient_files = True
    success_counter = 0
    failure_counter = 0
    doc_files = _find_files("*.docx", working_dir) + _find_files("*.odt", working_dir)
    logger.info("{} file(s) to convert.".format(len(doc_files)))
    for doc_file in doc_files:
        logger.info("converting {}".format(os.path.basename(doc_file)))
        success, output = _process_doc(
            doc_file,
            working_dir,
            logger,
            keep_transient_files,
            options.get("validation_schema", "metopes"),
        )
        if not success:
            logger.error(
                "could not convert {}. Process output: {}".format(
                    os.path.basename(doc_file), output
                )
            )
            failure_counter = failure_counter + 1
        else:
            success_counter = success_counter + 1
            logger.info("{}: success".format(os.path.basename(doc_file)))
    logger.info("Job done, {} files converted".format(success_counter))


doc2tei.description = {
    "label": "Docx vers TEI",
    "help": "Convertir les fichiers *.docx et *.odt en fichiers *.xml (vocabulaire TEI)",
    "options": [
        {
            "id": "keep_transient_files",
            "label": "garder les fichiers intermédiaires",
            "values": {"oui": "oui", "non": "non"},
            "default": "non",
            "free_input": False,
        },
        {
            "id": "validation_schema",
            "label": "schéma de validation",
            "values": {"metopes": "Métopes", "openedition": "openedition"},
            "default": "metopes",
            "free_input": False,
        },
    ],
}
