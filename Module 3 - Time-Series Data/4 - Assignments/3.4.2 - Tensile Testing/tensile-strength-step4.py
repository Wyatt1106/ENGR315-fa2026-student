import numpy as np
import os
import math
import sys

# Use this Python file's folder as the working directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def parse_tensile_file(path_to_file):
    gage_diameter = -1
    begin_reading = False

    time = []
    displacement = []
    force = []
    strain = []

    with open(path_to_file) as file:
        for line in file:
            if not line.strip():
                continue

            splits = line.strip().split(",")

            if not begin_reading:
                if splits[0] == "Gage Diameter":
                    gage_diameter = float(
                        splits[2].replace('"', "")
                    )

                if splits[0] == "(s)":
                    begin_reading = True

            else:
                time.append(float(splits[0].replace('"', "")))
                displacement.append(
                    float(splits[1].replace('"', ""))
                )
                force.append(float(splits[2].replace('"', "")))
                strain.append(float(splits[3].replace('"', "")))

    return (
        gage_diameter,
        np.asarray(time),
        np.asarray(displacement),
        np.asarray(force),
        np.asarray(strain),
    )


def calculate_stress(force, sample_diameter):
    """
    Convert force in kN to engineering stress in MPa,
    using the original sample diameter in mm.
    """
    cross_sectional_area = math.pi * sample_diameter**2 / 4
    stress = force * 1000 / cross_sectional_area

    return stress


def calculate_max_strength_strain(strain, stress):
    """
    Return ultimate tensile stress and maximum strain.
    """
    ultimate_tensile_stress = np.max(stress)
    fracture_strain = np.max(strain)

    return ultimate_tensile_stress, fracture_strain


def calculate_elastic_modulus(strain, stress):
    """
    Fit the initial stress-strain region up to approximately
    40% of peak stress.

    Return the endpoint index, slope, and intercept.
    """
    peak_index = int(np.argmax(stress))
    target_stress = 0.40 * stress[peak_index]

    # Search before the peak to select the initial loading region.
    loading_stress = stress[:peak_index + 1]
    diffs = np.abs(loading_stress - target_stress)
    linear_index = int(np.argmin(diffs))

    linear_strain = strain[0:linear_index]
    linear_stress = stress[0:linear_index]

    if len(linear_strain) < 2:
        raise ValueError(
            "Too few points in the initial region "
            "to calculate elastic modulus."
        )

    if np.ptp(linear_strain) == 0:
        raise ValueError(
            "The initial strain values do not vary."
        )

    slope, intercept = np.polyfit(
        linear_strain, linear_stress, 1
    )

    return linear_index, slope, intercept


def calculate_percent_offset(slope, strain, stress):
    """
    Calculate the 0.2% offset line and locate the measured
    point closest to its intersection with the stress curve.
    """
    offset = 0.002
    offset_line = slope * (strain - offset)

    distance = np.abs(stress - offset_line)
    intercept_index = int(np.argmin(distance))

    return offset_line, intercept_index


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Select the material and sample.
    material_folder = "1045CR"
    sample_name = "C01A1045CR_1"

    ### Do not modify below this line ###

    path_to_directory = "../../../data/tensile/"
    path_to_samples = path_to_directory + material_folder + "/"
    path_to_file = path_to_samples + sample_name + ".csv"

    sample_diameter, time, displacement, force, strain = (
        parse_tensile_file(path_to_file)
    )

    # Step 1: Calculate stress.
    stress = calculate_stress(force, sample_diameter)

    if stress is None:
        print(
            "Error! No stress returned. "
            "Did you fill in calculate_stress()?"
        )
        sys.exit(-1)

    plt.figure()
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel("Strain (mm/mm)")
    plt.ylabel("Stress (MPa)")
    plt.title("Stress-Strain Curve for Sample " + sample_name)
    plt.show()

    # Step 2: Ultimate tensile strength and fracture strain.
    ultimate_tensile_strength, fracture_strain = (
        calculate_max_strength_strain(strain, stress)
    )

    if ultimate_tensile_strength == -1 or fracture_strain == -1:
        print(
            "Error! Did you complete "
            "calculate_max_strength_strain()?"
        )
        sys.exit(-1)

    print(
        "Ultimate Tensile Stress is",
        ultimate_tensile_strength,
        "MPa",
    )
    print(
        "Fracture Strain is",
        100 * fracture_strain,
        "percent",
    )

    # Step 3: Elastic modulus.
    linear_index, slope, intercept = calculate_elastic_modulus(
        strain, stress
    )

    if linear_index is None or slope is None or intercept is None:
        print(
            "Error! Did you complete "
            "calculate_elastic_modulus()?"
        )
        sys.exit(-1)

    print("Elastic Modulus is", slope / 1000, "GPa")

    # Plot the point near 40% of peak stress.
    plt.figure()
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel("Strain (mm/mm)")
    plt.ylabel("Stress (MPa)")
    plt.title("Stress-Strain Curve for Sample " + sample_name)

    plt.scatter(
        strain[linear_index],
        stress[linear_index],
        marker="v",
        label="Secant Modulus at 40%",
    )

    plt.legend()
    plt.show()

    # Plot the initial region and its best-fit line.
    linear_strain = strain[0:linear_index]
    linear_stress = stress[0:linear_index]

    plt.figure()
    plt.scatter(
        linear_strain,
        linear_stress,
        label="Stress - Strain",
    )
    plt.xlabel("Strain (mm/mm)")
    plt.ylabel("Stress (MPa)")
    plt.title(
        "Linear Region for Sample "
        + sample_name
        + " with best fit"
    )

    best_fit_line = slope * linear_strain + intercept

    plt.plot(
        linear_strain,
        best_fit_line,
        label="Best Linear Fit",
    )

    plt.legend()
    plt.show()

    # Step 4: 0.2% offset yield strength.
    offset_line, intercept_index = calculate_percent_offset(
        slope, strain, stress
    )

    if offset_line is None or intercept_index == -1:
        print(
            "Error! Did you complete "
            "calculate_percent_offset()?"
        )
        sys.exit(-1)

    print(
        "The 0.2% Offset Yield is",
        stress[intercept_index],
        "MPa",
    )

    plt.figure()
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel("Strain (mm/mm)")
    plt.ylabel("Stress (MPa)")
    plt.title(
        "Stress-Strain Curve for Sample "
        + sample_name
        + " with 0.2% Yield"
    )

    plt.plot(
        strain,
        offset_line,
        label="0.2% Offset Yield",
    )

    plt.plot(
        strain[intercept_index],
        stress[intercept_index],
        marker="v",
        linestyle="None",
        label="Yield Strength",
    )

    plt.xlim([-.001, max(strain)])
    plt.ylim([0, 1.1 * max(stress)])
    plt.legend()
    plt.show()

    print("Done!")