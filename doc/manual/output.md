# Output files


---
## Reference Particle Information (`fort.18`)

The file **`fort.18`** contains data related to the reference particle along the beamline.

#### Column Descriptions:

1. **Distance (m)** - Longitudinal position along the beamline.
2. **Absolute Phase (radian)** - Phase of the reference particle relative to the RF wave.
3. **Gamma** - Reference Lorentz factor, defined as $ \gamma_0 = \frac{E_0}{m_0 c^2} $.
4. **Reference Kinetic Energy (MeV)** - Energy of the reference particle excluding rest mass energy: $E_0 - m_0 c^2$.
5. **Beta** - Reference Relativistic velocity factor, $ \beta_0 = v_0/c $.
6. **Rmax (m)** - Maximum radial distance from the beam axis.




---

## RMS Size Information for X-plane (`fort.24`)

The file **`fort.24`** contains RMS size information for the X-plane.

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **Centroid Location (m)** - Mean position of the beam in the X-plane.
3. **RMS Size (m)** - Root mean square (RMS) size in meters.
4. **Centroid Momentum (rad)** - Mean transverse momentum in the X-plane.
5. **RMS Momentum (rad)** - RMS transverse momentum in the X-plane.
6. **Twiss Parameter, Alpha** - Twiss alpha parameter for the X-plane.
7. **Normalized RMS Emittance (m-rad)** - Normalized RMS emittance in meters-radians.

---

## RMS Size Information for Y-plane (`fort.25`)

The file **`fort.25`** contains RMS size information for the Y-plane.

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **Centroid Location (m)** - Mean position of the beam in the Y-plane.
3. **RMS Size (m)** - Root mean square (RMS) size in meters.
4. **Centroid Momentum (rad)** - Mean transverse momentum in the Y-plane.
5. **RMS Momentum (rad)** - RMS transverse momentum in the Y-plane.
6. **Twiss Parameter, Alpha** - Twiss alpha parameter for the Y-plane.
7. **Normalized RMS Emittance (m-rad)** - Normalized RMS emittance in meters-radians.

---

## RMS Size Information for Z-plane (`fort.26`)

The file **`fort.26`** contains RMS size information for the Z-plane (longitudinal).

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **Centroid Location (m)** - Mean position of the beam in the Z-plane.
3. **RMS Size (degrees)** - Root mean square (RMS) size in degrees.
4. **Centroid Momentum (MeV)** $E_0 - E$ in MeV, where $E_0$ is the reference energy and $E$ is the centroid energy.
5. **RMS Momentum (MeV)** - RMS energy deviation in MeV.
6. **Twiss Parameter, Alpha** - Twiss alpha parameter for the Z-plane.
7. **Normalized RMS Emittance (degree-MeV)** - Normalized RMS emittance in degree-MeV.


---

## Maximum amplitude information (`fort.27`)

The file **`fort.27`** contains the maximum amplitude information for various beam parameters.

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **Max. X (m)** - Maximum horizontal displacement from the beam axis.
3. **Max. Px (rad)** - Maximum transverse momentum in the X-plane.
4. **Max. Y (m)** - Maximum vertical displacement from the beam axis.
5. **Max. Py (rad)** - Maximum transverse momentum in the Y-plane.
6. **Max. Phase (degree)** - Maximum deviation in phase.
7. **Max. Energy Deviation (MeV)** - Maximum deviation in particle energy.

---

## Load Balance and Loss Diagnostic (`fort.28`)

The file **`fort.28`** contains information on load balancing and particle loss diagnostics.

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **Min # of Particles on a PE** - Minimum number of particles assigned to a processing element (PE).
3. **Max # of Particles on a PE** - Maximum number of particles assigned to a processing element (PE).
4. **Total # of Particles in the Bunch** - Total number of particles present in the bunch at the given position.

---

## Cubic Root of 3rd Moments of the Beam Distribution (`fort.29`)

The file **`fort.29`** contains the cubic root of the third moments of the beam distribution.

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **X (m)** - Cubic root of the third moment of the horizontal position.
3. **Px (rad)** - Cubic root of the third moment of the horizontal momentum.
4. **Y (m)** - Cubic root of the third moment of the vertical position.
5. **Py (rad)** - Cubic root of the third moment of the vertical momentum.
6. **Phase (degree)** - Cubic root of the third moment of the phase.
7. **Energy Deviation (MeV)** - Cubic root of the third moment of the energy deviation.

---

## Beam Distribution Data (`fort.30`)

This file contains beam distribution data at different positions along the beamline.

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **X (m)** - Horizontal position.
3. **Px (rad)** - Horizontal momentum.
4. **Y (m)** - Vertical position.
5. **Py (rad)** - Vertical momentum.
6. **Phase (degree)** - Particle phase relative to the RF wave.
7. **Energy Deviation (MeV)** - Deviation from the reference energy.

---

### Number of Particles for Each Charge State (`fort.32`)

The file **`fort.32`** contains information on the number of particles for each charge state at different positions along the beamline.

#### Column Descriptions:

1. **Z Distance (m)** - Longitudinal position along the beamline.
2. **Number of Particles for Each Charge State** - Count of particles in each charge state at the given position.





