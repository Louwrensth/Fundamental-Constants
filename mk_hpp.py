#!/usr/bin/env python
import re
from pathlib import Path
import scipy.version
import scipy.constants._codata as _cd

def make_hpp_sources(output_dir = Path('.')):
    '''Write .hpp source files to an output_dir'''

    ###
    # Traverse physical constant series
    # Produce a header file for each
    for dataset_name, physical_constants in {
        "codata_2002": _cd._physical_constants_2002,
        "codata_2006": _cd._physical_constants_2006,
        "codata_2010": _cd._physical_constants_2010,
        "codata_2014": _cd._physical_constants_2014,
        "codata_2018": _cd._physical_constants_2018,
        "codata_2022": _cd._physical_constants_2022,
    }.items():

        # Namespace begins
        namespace = "codata"
        output_file = output_dir / "{}.hpp".format(dataset_name)

        with output_file.open("w") as file:
            print("Writing {}".format(output_file))
            file.write(
"""/* -----------------------------------------------------------------------------
 * {file_name}
 * Fundamental Physical Constants
 * ------------------------------
 * These constants are taken from CODATA Recommended Values of the Fundamental
 * Physical Constants. https://physics.nist.gov
 * Generated using SciPy version {scipy_version}
 * -----------------------------------------------------------------------------
 */

#ifndef {header_name}_H
#define {header_name}_H

namespace {namespace} {{
""".format(
                    file_name=output_file.name, namespace=namespace,
                    header_name=dataset_name.upper(),
                    scipy_version=scipy.version.full_version
                )
            )
            # Traverse physical constant name,value pairs
            for pretty_key, dict_value in physical_constants.items():

                # Flatten pretty long name:
                # replace all non alphanumeric characters by underscores
                name = re.sub(r"[(),\.]", "", pretty_key)  # first omit parentheses commas and periods
                name = re.sub(r"[^A-z0-9]", "_", name)

                if pretty_key in _cd._obsolete_constants.keys():
                    obsolete = " (obsolete)" if _cd._obsolete_constants[pretty_key] else ""
                else:
                    obsolete = ""

                # Unpack dictionary value items
                value, unit, uncertainty = dict_value
                unit = " " + unit if unit != "" else ""

                # C++ named constant definition
                file.write(
                    "  static const double {} = {};  // ({}){}{}\n".format(name, value, uncertainty, unit, obsolete)
                )

            # Namespace ends
            file.write(
                "}}  // namespace {}\n\n#endif  // {}_H\n".format(namespace, dataset_name.upper())
            )


if __name__ == "__main__":
    make_hpp_sources()
