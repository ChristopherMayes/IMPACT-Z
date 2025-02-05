
## Lattice Elements
---

Each line in this section represents a beamline element, except for lines starting with `!` (comments). Example:

```plaintext
0.062082  1  1  0  1.0  /
0.05  3  1  1  16.44  0  1.0  0.  0.  0.  0.  0.  /
```

Impact-Z has two types of integrator:
- `map`: (linear?) map-based methods
- `rk`: "nonlinear Lorentz", i.e. Runge-Kutta integration of the Lorentz force.

---
### General Notes

- all File `ID` must be less than 1000



---
### **Drift (Type 0)**

#### **Description**
A **Drift** represents a straight beamline segment with no focusing or deflection forces. Particles travel freely without experiencing external fields.

#### **Attributes**
1. **Length (m)** – Specifies the drift length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map between integration steps.
4. **Element Type** – Set to `0` for Drift.
5. **Pipe Radius (m)** – Defines the pipe boundary.

#### **Example**
`0.0620822983935 1 1 0 1.0 /`

This means:
- A **drift** of length **0.062 m**
- **1 integration step**
- **1 map step**
- **Pipe radius** of **1.0 m**

---

###  **Quadrupole (Type 1)**

#### **Description**
A **Quadrupole** provides transverse focusing using a magnetic field gradient. It focuses in one transverse plane while defocusing in the other.

#### **Attributes**
1. **Length (m)** – Specifies the quadrupole length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `1` for Quadrupole.
5. **Field Strength** – Quadrupole focusing strength.
   - `map` integrator: $k_1$ in 1/m$^2$
   - `rk` integrator:  $dB_y/dx$ in T/m
6. **Input Gradient File ID** – Determines whether an external gradient file is used.
7. **Pipe Radius (m)** – Defines the pipe boundary.
8. **Misalignment Errors (x, y) (m)** – Defines position errors.
9. **Rotation Errors (x, y, z) (rad)** – Defines orientation errors.



#### **Example**
`0.05 3 1 1 16.4423850936 0 1.0 0. 0. 0. 0. 0. /`
This means:
- A **quadrupole** of length **0.05 m**
- **3 integration steps**
- **1 map step**
- **Gradient** of **16.44 Tesla/m**
- **Pipe radius** of **1.0 m**
- No misalignment or rotation errors

---

###  **Solenoid (Type 3)**

#### **Description**
A **Solenoid** provides focusing in both transverse planes using a helical magnetic field. It is commonly used in linacs and electron beam transport.

#### **Attributes**
1. **Length (m)** – Specifies the solenoid length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `3` for Solenoid.
5. **Magnetic Field Strength (T)** – Solenoid axial field strength.
6. **Input Field File ID** – Determines whether an external field file is used.
7. **Pipe Radius (m)** – Defines the pipe boundary.
8. **Misalignment Errors (x, y) (m)** – Defines position errors.
9. **Rotation Errors (x, y, z) (rad)** – Defines orientation errors.



#### **Example**
`0.30 4 20 3 5.67 0. 0.014 0. 0. 0. 0. 0. /`

This means:
- A **solenoid** of length **0.30 m**
- **4 integration steps**
- **20 map steps**
- **Axial magnetic field** of **5.67 T**
- **Pipe radius** of **0.014 m**
- No misalignment or rotation errors

---

###  **Dipole (Type 4)**

#### **Description**
A **Dipole** bends the beam trajectory by applying a uniform transverse magnetic field. It is used in beam steering and spectrometers.

#### **Attributes**
1. **Length (m)** – Specifies the dipole length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `4` for Dipole.
5. **Bending Angle (rad)** – The angle through which the dipole bends the beam.
6. **Quadrupole Component (k1)** – Adjusts the focusing strength.
7. **Input Switch** – Determines additional physics options.
8. **Half Gap (m)** – Defines the physical aperture of the dipole.
9. **Pole Face Angles (Entrance, Exit) (rad)** – Defines entrance and exit angles.
10. **Curvature (Entrance, Exit)** – Determines field falloff at pole faces.
11. **Integrated Fringe Field** – Determines the effect of fringe fields.
12. **Misalignment Errors (x, y) (m)** – Defines position errors.
13. **Rotation Errors (x, y, z) (rad)** – Defines orientation errors.



#### **Example**
`1.48524 10 20 4 0.1 0.0 150. 0.014 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 /`

This means:
- A **dipole** of length **1.485 m**
- **10 integration steps**
- **20 map steps**
- **Bending angle** of **0.1 rad**
- **Half gap** of **0.014 m**
- No misalignment or rotation errors


---


###  **Thick Multipole (Type 5)**

`Warning: previously undocumented!!`

#### **Description**
The **Thick Multipole** element represents a higher-order magnetic field component used for beam focusing and correction. It allows for modeling of **sextupole, octupole, and decapole** fields with **finite length** and **numerically integrated field maps**. This element is useful for chromatic correction, beam shaping, and nonlinear optics studies.

#### **Attributes**
1. **Length (m)** – Specifies the physical length of the multipole.
2. **Steps (int)** – Number of **space-charge kicks** applied through the element.
3. **Map Steps (int)** – Number of numerical integration steps used to compute the element’s transfer map.
4. **Multipole Type** – Defines the type of multipole:
   - `2`: `Sextupole`
   - `3`: `Octupole`
   - `4`: `Decapole`
5. **Field Strength (T/mⁿ, optional)** – The strength of the applied magnetic field.
6. **File ID (optional)** – Identifier for an external input data file. (TODO: ???)
7. **Radius (m, optional)** – The radius of the multipole aperture.
8. **X Misalignment (m)** – Displacement in the x-direction.
9. **Y Misalignment (m)** – Displacement in the y-direction.
10.  **X Rotation (rad)** – Rotation about the x-axis.
11.  **Y Rotation (rad)** – Rotation about the y-axis.
12.  **Z Rotation (rad)** – Rotation about the z-axis.


---


###  **Drift Tube Linac (DTL, Type 101)**
#### **Description**
A **Drift Tube Linac (DTL)** is an RF accelerating structure that provides acceleration with periodic quadrupole focusing. It operates at radio frequencies and is typically used in low to medium energy accelerators.

#### **Attributes**
1. **Length (m)** – Specifies the cavity length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `101` for DTL.
5. **Field Scaling** – Scales the RF field strength.
6. **RF Frequency (Hz)** – Operating frequency of the cavity.
7. **Driven Phase (°)** – The phase at which the cavity operates.
8. **Input Field File `ID`**: `int` – Determines whether an external field file is used.
   - `ID`<0: use simple sinisoidal model, only for `map` integrator, with `phase=0` giving maximum energy gain ("on-crest").
   - `ID`>0: read `fort.ID` file with Fourier coefficients, only for `rk` integrator
10. **Pipe Radius (m)** – Defines the cavity aperture.

#### **Example**
`1.48524 10 20 101 1.0 700.0e6 30. 1.0 0.014 /`


---

###  **Coupled Cavity Drift Tube Linac (CCDTL, Type 102)**
#### **Description**
A **CCDTL** is a hybrid structure combining the features of a DTL and a Coupled Cavity Linac (CCL), providing acceleration with improved efficiency over traditional DTLs.

#### **Attributes**
1. **Length (m)** – Specifies the cavity length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `102` for CCDTL.
5. **Field Scaling** – Scales the RF field strength.
6. **RF Frequency (Hz)** – Operating frequency of the cavity.
7. **Driven Phase (°)** – The phase at which the cavity operates.
8. **Input Field File `ID`**: `int` – Determines whether an external field file is used.
   - `ID`<0: use simple sinisoidal model, only for `map` integrator, with `phase=0` giving maximum energy gain ("on-crest").
   - `ID`>0: read `fort.ID` file with Fourier coefficients, only for `rk` integrator
9. **Pipe Radius (m)** – Defines the cavity aperture.

#### **Example**
`1.48524 10 20 102 1.0 700.0e6 30. 1.0 0.014 /`



---

###  **Coupled Cavity Linac (CCL, Type 103)**
#### **Description**
A **CCL** is a high-energy RF accelerating structure with multiple coupled cavities, used in the medium to high energy range of particle accelerators.

#### **Attributes**
1. **Length (m)** – Specifies the cavity length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `103` for CCL.
5. **Field Scaling** – Scales the RF field strength. For `ID` < 0 (map inegrator), this is the average gradient in V/m.
7. **RF Frequency (Hz)** – Operating frequency of the cavity.
8. **Driven Phase (°)** – The phase at which the cavity operates.
9. **Input Field File `ID`**: `int` – Determines whether an external field file is used.
   - `ID`<0: use simple sinisoidal model, only for `map` integrator, with `phase=0` giving maximum energy gain ("on-crest").
   - `ID`>0: read `fort.ID` file with Fourier coefficients, only for `rk` integrator
10. **Pipe Radius (m)** – Defines the cavity aperture.

#### **Example**
`1.48524 10 20 103 1.0 700.0e6 30. 1.0 0.014 /`

This means:
- A **Coupled Cavity Linac (CCL)** of length **1.485 m**
- **10 integration steps**
- **20 map steps**
- **Field scaling** of **1.0**
- **RF frequency** of **700 MHz**
- **Driven phase** of **30°**
- **Pipe radius** of **0.014 m**
- No misalignment or rotation errors





---

###   **Superconducting RF Cavity (Type 104)**

#### **Description**
A **Superconducting RF Cavity** accelerates particles using oscillating electromagnetic fields. It is used in high-energy accelerators for efficient acceleration.

#### **Attributes**
1. **Length (m)** – Specifies the cavity length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `104` for Superconducting Cavity.
5. **Field Scaling** – Scales the RF field strength.
6. **RF Frequency (Hz)** – Operating frequency of the cavity.
7. **Driven Phase (°)** – The phase at which the cavity operates.
8. **Input Field File `ID`**: `int` – Determines whether an external field file is used.
   - `ID`<0: use simple sinisoidal model, only for `map` integrator, with `phase=0` giving maximum energy gain ("on-crest").
   - `ID`>0: read `fort.ID` file with Fourier coefficients, only for `rk` integrator
9. **Pipe Radius (m)** – Defines the cavity aperture.
10. **Misalignment Errors (x, y) (m)** – Defines position errors.
11. **Rotation Errors (x, y, z) (rad)** – Defines orientation errors.



#### **Example**
`0.948049 80 1 104 34000000.0 650000000.0 96.8056476853 1 1.0 /`

This means:
- A **superconducting cavity** of length **0.948 m**
- **80 integration steps**
- **1 map step**
- **Field scaling** of **34,000,000**
- **RF frequency** of **650 MHz**
- **Driven phase** of **96.8°**
- No misalignment or rotation errors

---

### **Solenoid with RF Cavity (Type 105)**
#### **Description**
A **Solenoid with RF Cavity** is a hybrid structure that combines a solenoid magnet with an RF accelerating cavity. It is used for beam transport and acceleration in applications where simultaneous focusing and acceleration are required.

#### **Attributes**
1. **Length (m)** – Specifies the cavity length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `105` for Solenoid with RF Cavity.
5. **Field Scaling** – Scales the RF field strength.
6. **RF Frequency (Hz)** – Operating frequency of the cavity.
7. **Driven Phase (°)** – The phase at which the cavity operates.
8. **Input Field File `ID`**: `int` – Determines whether an external field file is used.
   - `rk` integrator only
   - Requires `ID`>0: read `fort.ID` file with Fourier coefficients
9. **Pipe Radius (m)** – Defines the cavity aperture.
10. **Misalignment Errors (x, y) (m)** – Defines position errors.
11. **Rotation Errors (x, y, z) (rad)** – Defines orientation errors.
12. **Solenoid Field Strength (T)** – Defines the axial magnetic field.
13. **Wakefield Parameters** – Aperture size, gap size, and length for wakefield calculations.

#### **Example**
`1.48524 10 20 105 1.0 700.0e6 30. 1.0 0.014 0. 0. 0. 0. 0. 1. 0. 0. 0. /`
This means:
- A **Solenoid with RF Cavity** of length **1.485 m**
- **10 integration steps**
- **20 map steps**
- **Field scaling** of **1.0**
- **RF frequency** of **700 MHz**
- **Driven phase** of **30°**
- **Pipe radius** of **0.014 m**
- **Solenoid field strength** of **1.0 T**
- No misalignment or rotation errors


---


### **Traveling Wave RF Cavity (Type 106)**
#### **Description**
A **Traveling Wave RF Cavity** is an accelerating structure that operates with a traveling electromagnetic wave, rather than a standing wave. This type of cavity is commonly used in high-energy accelerators and linear colliders, where efficient and continuous acceleration is required.

#### **Attributes**
1. **Length (m)** – Specifies the cavity length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `106` for Traveling Wave RF Cavity.
5. **Field Scaling** – Scales the RF field strength.
6. **RF Frequency (Hz)** – Operating frequency of the cavity.
7. **Driven Phase (°)** – The phase at which the cavity operates.
8. **Input Field File `ID`**: `int` – Determines whether an external field file is used.
   - `rk` integrator only
   - Requires `ID`>0: read `fort.ID` file with Fourier coefficients
9. **Pipe Radius (m)** – Defines the cavity aperture.
10. **Misalignment Errors (x, y) (m)** – Defines position errors.
11. **Rotation Errors (x, y, z) (rad)** – Defines orientation errors.
12. **Phase Advance Parameter** – Controls phase difference between sections of the cavity.
13. **Wakefield Aperture (m)** - aperture for the wakefield calc
14. **Wakefield gap (m)**  - gap for the wakefield calc
15. **Wakefield length (m)**: - lenght for the wakefield calc. The wakefield is disabled if this is zero.

#### **Example**
`1.48524 10 20 106 1.0 700.0e6 30. 1.0 0.014 0. 0. 0. 0. 0. 0.5 0. 0. 0. /`
This means:
- A **Traveling Wave RF Cavity** of length **1.485 m**
- **10 integration steps**
- **20 map steps**
- **Field scaling** of **1.0**
- **RF frequency** of **700 MHz**
- **Driven phase** of **30°**
- **Pipe radius** of **0.014 m**
- **Phase advance parameter** of **0.5**
- No misalignment or rotation errors

---

### **User-Defined RF Cavity (Type 110)**
#### **Description**
A **User-Defined RF Cavity** allows for customized RF field definitions using either analytical functions, discrete data, or a combination of both. This element is useful for specialized RF structures where standard models do not suffice.

#### **Attributes**
1. **Length (m)** – Specifies the cavity length.
2. **Integration Steps** – Number of integration steps across the element.
3. **Map Steps** – Number of steps to calculate the transfer map.
4. **Element Type** – Set to `110` for User-Defined RF Cavity.
5. **Field Scaling** – Scales the RF field strength.
6. **RF Frequency (Hz)** – Operating frequency of the cavity.
7. **Driven Phase (°)** – The phase at which the cavity operates.
8. **Input Field File `ID`** – Read the 3D Cartesian field data from `fort.ID`
9. **X Radius (m)** – Defines the cavity aperture in the X-direction.
10. **Y Radius (m)** – Defines the cavity aperture in the Y-direction.
11. **Misalignment Errors (x, y) (m)** – Defines position errors.
12. **Rotation Errors (x, y, z) (rad)** – Defines orientation errors.
13. **Field Representation Mode** – Determines whether to use discrete data, analytical functions, or both.
14. **Coordinate System** – Specifies whether the field is defined in Cartesian or Cylindrical coordinates.

#### **Example**
`1.48524 10 20 110 1.0 700.0e6 30. 1.0 0.014 0.014 0. 0. 0. 0. 0. 1.0 2.0 /`

This means:
- A **User-Defined RF Cavity** of length **1.485 m**
- **10 integration steps**
- **20 map steps**
- **Field scaling** of **1.0**
- **RF frequency** of **700 MHz**
- **Driven phase** of **30°**
- **X Radius** of **0.014 m**
- **Y Radius** of **0.014 m**
- No misalignment or rotation errors
- **Field representation mode**: **1.0** (discrete data only), **2.0** (both discrete and analytical functions)
- **Coordinate system**: **2.0** (Cartesian), **1.0** (Cylindrical)

*TODO*: description of the field file fomat.




---


### **Centroid Shift (Element -1)**
#### **Description**
The **Centroid Shift** element is used to shift the beam centroid to the axis. This is useful for aligning the beam trajectory within the simulation to ensure symmetry or correct initial misalignments.

#### **Attributes**
1. **Element Type** – Set to `-1` for Centroid Shift.

#### **Example**
`0 0 0 -1`

This means:
- The beam centroid is shifted to the axis.

---
### **Particle Distribution Output (Element -2)**
#### **Description**
The **Particle Distribution Output** element is used to write the particle distribution data into an output file (`fort.N`). This allows for diagnostics, visualization, and further analysis of the particle distribution at a specified point in the simulation.

#### **Attributes**
1. **Element Type** – Set to `-2` for Particle Distribution Output.
2. **File Index (N)** – The index of the output file (`fort.N`).
3. **Sampling Frequency** – Determines how frequently particles are written to the file.

#### **Example**
`0 0 N -2 0.0 10 /`
This means:
- The particle distribution is written to **`fort.N`**.
- **Sampling frequency** of **10** (i.e., every 10th particle is written).
- The output data is in **IMPACT-Z internal units**.

**Note:**  
- `N` must **not** be **5, 6, 24, 25, 26, 27, 29, 30, or 32** (to avoid conflicts with other IMPACT-Z output files).
- If the sampling frequency is **negative**, the output is written in **ImpactT particle format**, where:
  - `z` is **relative position** (instead of absolute position).
  - `pz` is **gamma** (instead of gamma-beta-z).



--- 

### **Density Profile Output (Element -3)**
#### **Description**
The **Density Profile Output** element is used to record the accumulated density distribution along the **R, X, and Y** axes. This information is saved into the files `Xprof.data`, `Yprof.data`, and `RadDens.data`, which can be used for beam diagnostics and visualization.

#### **Attributes**
1. **Element Type** – Set to `-3` for Density Profile Output.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Frame Ranges:**
   - **Xmax (m)** – Maximum x-axis range for the profile.
   - **Pxmax (mc)** – Maximum momentum in the x-direction.
   - **Ymax (m)** – Maximum y-axis range for the profile.
   - **Pymax (mc)** – Maximum momentum in the y-direction.
   - **Zmax (rad)** – Maximum longitudinal phase space range.
   - **Pzmax (mc²)** – Maximum energy deviation range.

#### **Example**
`0 0 0 -3 0.014 0.02 0.02 0.02 0.02 0.02 0.02 /`

This means:
- A **density profile** is written to `Xprof.data`, `Yprof.data`, and `RadDens.data`.
- **Pipe radius** is **0.014 m**.
- **X, Y, Z phase-space ranges** are each set to **0.02 m/rad**.
- **Momentum limits** (Px, Py, Pz) are set to **0.02 mc or mc²**.
- If no frame range is specified, the program will automatically set the range based on the maximum beam amplitude at the given location.


---

### **Density Profile Output (Element -4)**
#### **Description**
The **Density Profile Output** element is used to record the density distribution along the **R, X, and Y** axes, similar to Element `-3`, but the output is written to separate files:  
- `Xprof2.data` for the **X-axis density profile**  
- `Yprof2.data` for the **Y-axis density profile**  
- `RadDens2.data` for the **radial density distribution**  

This output can be used for beam diagnostics and visualization of density profiles at a given simulation location.

#### **Attributes**
1. **Element Type** – Set to `-4` for Density Profile Output.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Frame Ranges:**
   - **Xmax (m)** – Maximum x-axis range for the profile.
   - **Pxmax (mc)** – Maximum momentum in the x-direction.
   - **Ymax (m)** – Maximum y-axis range for the profile.
   - **Pymax (mc)** – Maximum momentum in the y-direction.
   - **Zmax (rad)** – Maximum longitudinal phase space range.
   - **Pzmax (mc²)** – Maximum energy deviation range.

#### **Example**
`0 0 0 -4 0.014 0.02 0.02 0.02 0.02 0.02 0.02 /`

This means:
- A **density profile** is written to `Xprof2.data`, `Yprof2.data`, and `RadDens2.data`.
- **Pipe radius** is **0.014 m**.
- **X, Y, Z phase-space ranges** are each set to **0.02 m/rad**.
- **Momentum limits** (Px, Py, Pz) are set to **0.02 mc or mc²**.
- If no frame range is specified, the program will automatically set the range based on the maximum beam amplitude at the given location.

---

### **2D Phase Space Projection Output (Element -5)**
#### **Description**
The **2D Phase Space Projection Output** element is used to write the **2D projections of the 6D phase space distribution**. The output files contain projections of the beam distribution in various transverse and longitudinal phase space planes.

The data is written to the following files:
- `XY.data` – **X vs Y** projection
- `XPx.data` – **X vs Px** projection
- `XZ.data` – **X vs Z** projection
- `YPy.data` – **Y vs Py** projection
- `YZ.data` – **Y vs Z** projection
- `ZPz.data` – **Z vs Pz** projection

This data is useful for visualizing beam distribution in phase space.

#### **Attributes**
1. **Element Type** – Set to `-5` for 2D Phase Space Projection Output.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Frame Ranges:**
   - **Xmax (m)** – Maximum x-axis range for the profile.
   - **Pxmax (mc)** – Maximum momentum in the x-direction.
   - **Ymax (m)** – Maximum y-axis range for the profile.
   - **Pymax (mc)** – Maximum momentum in the y-direction.
   - **Zmax (rad)** – Maximum longitudinal phase space range.
   - **Pzmax (mc²)** – Maximum energy deviation range.

#### **Example**
`0 0 0 -5 0.014 0.02 0.02 0.02 0.02 0.02 0.02 /`
This means:
- **2D phase space projections** are written to `XY.data`, `XPx.data`, `XZ.data`, `YPy.data`, `YZ.data`, and `ZPz.data`.
- **Pipe radius** is **0.014 m**.
- **X, Y, Z phase-space ranges** are each set to **0.02 m/rad**.
- **Momentum limits** (Px, Py, Pz) are set to **0.02 mc or mc²**.
- If no frame range is specified, the program will automatically set the range based on the maximum beam amplitude at the given location.


---


### **3D Density Output (Element -6)**
#### **Description**
The **3D Density Output** element writes the **3D density distribution** of the beam to an output file (`fort.8`). This data is useful for analyzing the spatial distribution of the beam in **X, Y, and Z** directions at a specific simulation point.

#### **Attributes**
1. **Element Type** – Set to `-6` for 3D Density Output.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Frame Ranges:**
   - **Xmax (m)** – Maximum x-axis range for the profile.
   - **Pxmax (mc)** – Maximum momentum in the x-direction.
   - **Ymax (m)** – Maximum y-axis range for the profile.
   - **Pymax (mc)** – Maximum momentum in the y-direction.
   - **Zmax (rad)** – Maximum longitudinal phase space range.
   - **Pzmax (mc²)** – Maximum energy deviation range.

#### **Example**
`0 0 -6 0.014 0.02 0.02 0.02 0.02 2 0.02 /`

This means:
- **3D density distribution** is written to `fort.8`.
- **Pipe radius** is **0.014 m**.
- **X, Y, Z phase-space ranges** are each set to **0.02 m/rad**.
- **Momentum limits** (Px, Py, Pz) are set to **0.02 mc or mc²**.
- **Zmax** is set to **2 radians**, defining the longitudinal spread.
- If no frame range is specified, the program will automatically set the range based on the maximum beam amplitude at the given location.

---

### **6D Phase Space and Restart Data Output (Element -7)**
#### **Description**
The **6D Phase Space and Restart Data Output** element is used to write the **full 6D phase space information** along with **local computational domain data** to multiple output files (`fort.1000`, `fort.1001`, ..., `fort.(1000+Nprocessor-1)`). This output is useful for **simulation restart**, as well as detailed beam diagnostics.

#### **Attributes**
1. **Element Type** – Set to `-7` for 6D Phase Space and Restart Data Output.
2. **File Index (Base Name)** – Specifies the base filename for output files (default is `1000`).

#### **Example**
`0 0 1000 -7 /`

This means:
- **6D phase space data** is written to files `fort.1000`, `fort.1001`, ..., `fort.(1000+Nprocessor-1)`.
- The **base index** for the filenames is **1000**.
- This data can be used to **restart a simulation from this point**.


---

### **Slice Analysis Output (Element -8)**
#### **Description**
The **Slice Analysis Output** element writes **beam slice properties** to the file `fort.202`. This data includes **current, emittance, mismatch factors, and centroid positions** for **each longitudinal slice** of the beam. It is useful for studying beam properties as a function of longitudinal position.

The output file `fort.202` contains:
- **Bunch length coordinate (m)**
- **Number of particles per slice**
- **Current (A) per slice**
- **X and Y normalized emittance (m-rad) per slice**
- **Energy spread (dE/E)**
- **Uncorrelated energy spread (eV) per slice**
- **Centroid positions (X, Y) per slice**
- **Mismatch factors (X, Y)**

#### **Attributes**
1. **Element Type** – Set to `-8` for Slice Analysis Output.
2. **Number of Slices** – Number of beam slices to divide the beam into.
3. **X Alpha and Beta** – Twiss parameters at the slice analysis location.
4. **Y Alpha and Beta** – Twiss parameters at the slice analysis location.

#### **Example**
`0.0 0 202 -8 101.0 0.1 1.0 0.2 2.0 /`

This means:
- **Slice data** is written to `fort.202`.
- The **beam is divided into 101 slices**.
- **Twiss parameters** at this location:
  - **X-plane**: Alpha = **0.1**, Beta = **1.0 m**
  - **Y-plane**: Alpha = **0.2**, Beta = **2.0 m**
- If Twiss parameters are **not provided**, the mismatch factor should be ignored.

---

### **6D Phase Space Scaling/Mismatch (Element -10)**
#### **Description**
The **6D Phase Space Scaling/Mismatch** element is used to apply **scaling or mismatches** to the beam distribution in all six phase-space coordinates (**X, Px, Y, Py, Z, Pz**). This allows users to control the beam size, divergence, and energy spread at a given simulation point.

#### **Attributes**
1. **Element Type** – Set to `-10` for 6D Phase Space Scaling/Mismatch.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Scaling/Mismatch Parameters:**
   - **Xmis** – Scaling/mismatch factor for **X** position.
   - **Pxmis** – Scaling/mismatch factor for **Px** momentum.
   - **Ymis** – Scaling/mismatch factor for **Y** position.
   - **Pymis** – Scaling/mismatch factor for **Py** momentum.
   - **Tmis** – Scaling/mismatch factor for **Z** position.
   - **Ptmis** – Scaling/mismatch factor for **Pz** momentum.

#### **Example**
`0 0 0 -10 0.014 0.1 0.2 0.3 0.4 0.5 0.6 /`

This means:
- **6D phase space mismatch/scaling is applied**.
- **Pipe radius** is **0.014 m**.
- **Scaling/mismatch factors**:
  - **X**: **0.1**
  - **Px**: **0.2**
  - **Y**: **0.3**
  - **Py**: **0.4**
  - **Z (T)**: **0.5**
  - **Pz (Pt)**: **0.6**

---

### **Beam Collimation (Element -13)**
#### **Description**
The **Beam Collimation** element is used to **collimate (truncate)** the beam based on a **rectangular transverse aperture**. Any particles outside the specified X and Y limits are removed from the simulation, allowing users to model physical apertures, slits, or beam dumps.

#### **Attributes**
1. **Element Type** – Set to `-13` for Beam Collimation.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Collimation Aperture:**
   - **Xmin (m)** – Minimum allowed X position.
   - **Xmax (m)** – Maximum allowed X position.
   - **Ymin (m)** – Minimum allowed Y position.
   - **Ymax (m)** – Maximum allowed Y position.

#### **Example**
`0 0 0 -13 0.014 -0.02 0.02 -0.04 0.04 /`

This means:
- **Beam collimation is applied** using a **rectangular aperture**.
- **Pipe radius** is **0.014 m**.
- **X limits**: **-0.02 m to 0.02 m**.
- **Y limits**: **-0.04 m to 0.04 m**.
- Particles **outside these limits are removed** from the simulation.


---

### **Beam Rotation (Element -18)**
#### **Description**
The **Beam Rotation** element is used to rotate the entire beam **about the longitudinal axis** (Z-axis). This operation is useful for adjusting the beam orientation in phase space or compensating for optical misalignments.

#### **Attributes**
1. **Element Type** – Set to `-18` for Beam Rotation.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Rotation Angle (rad)** – The rotation angle in **radians**.

#### **Example**
`0 0 0 -18 0.014 0.5 /`

This means:
- **Beam rotation is applied** around the **Z-axis**.
- **Pipe radius** is **0.014 m**.
- **Rotation angle** is **0.5 radians**.

---

### **Longitudinal Centroid Shift (Element -19)**
#### **Description**
The **Longitudinal Centroid Shift** element is used to **shift the beam longitudinally** so that the centroid of the bunch satisfies **<Δt> = 0** and **<ΔE> = 0**. This ensures that the reference particle is centered in the bunch, which can be useful for alignment in simulations.

#### **Attributes**
1. **Element Type** – Set to `-19` for Longitudinal Centroid Shift.

#### **Example**
`0 0 0 -19 /`

This means:
- **The beam centroid is shifted** so that **<Δt> = 0** and **<ΔE> = 0**, centering the reference particle in the bunch.

---
### **Energy Spread Increase (Element -20)**
#### **Description**
The **Energy Spread Increase** element is used to **artificially increase the beam's energy spread** by a specified amount. This can be useful for simulating additional energy jitter or compensating for effects such as heating due to wakefields.

#### **Attributes**
1. **Element Type** – Set to `-20` for Energy Spread Increase.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Increased Energy Spread (eV)** – The amount by which the energy spread is increased.

#### **Example**
`0 0 0 -20 0.014 1000.0 /`

This means:
- **Energy spread is artificially increased** by **1000 eV**.
- **Pipe radius** is **0.014 m** (not used in calculations but included for reference).

---

### **Phase Space Randomization (Element -21)**
#### **Description**
The **Phase Space Randomization** element applies **random perturbations** to all six phase-space coordinates (**X, Px, Y, Py, Z, Pz**). This is useful for modeling effects such as beam jitter, scattering, or thermal fluctuations.

#### **Attributes**
1. **Element Type** – Set to `-21` for Phase Space Randomization.
2. **Pipe Radius (m)** – Defines the beam pipe boundary (not used in calculations but included for reference).
3. **Randomization Parameters:**
   - **ΔX (m)** – Random displacement in X.
   - **ΔPx (mc)** – Random variation in Px.
   - **ΔY (m)** – Random displacement in Y.
   - **ΔPy (mc)** – Random variation in Py.
   - **ΔZ (rad)** – Random displacement in Z.
   - **ΔPz (mc²)** – Random variation in Pz.

#### **Example**
`0 0 0 -21 0.014 0.001 0.002 0.0015 0.0025 0.003 0.004 /`

This means:
- **Random perturbations** are applied to **all six phase-space coordinates**.
- **Pipe radius** is **0.014 m** (not used in calculations but included for reference).
- **Random displacements**:
  - **X**: **±0.001 m**
  - **Px**: **±0.002 mc**
  - **Y**: **±0.0015 m**
  - **Py**: **±0.0025 mc**
  - **Z**: **±0.003 rad**
  - **Pz**: **±0.004 mc²**


---
### **Beam Dump (Element -25)**
#### **Description**
The **Beam Dump** element is used to **completely remove all particles** from the simulation. This effectively terminates the beam at a specific location, simulating an absorber or a beamline stop.

#### **Attributes**
1. **Element Type** – Set to `-25` for Beam Dump.

#### **Example**
`0 0 0 -25 /`

This means:
- **All particles are removed** from the simulation at this point.


---


---

### **CSR Track Length Setting (Element -41)**
#### **Description**
The **CSR Track Length Setting** element defines the **tracking length for Coherent Synchrotron Radiation (CSR) effects**. It sets a finite distance over which CSR wakefields are computed, allowing control over the accuracy and computational efficiency of CSR simulations.

#### **Attributes**
1. **Element Type** – Set to `-41` for CSR Track Length Setting.
2. **Tracking Length (m)** – The distance over which CSR wakefields are computed.

#### **Example**
`0 0 0 -41 5.0 /`
This means:
- **CSR wakefields are computed over a tracking length of 5.0 meters**.


---
### **Longitudinal Space Charge Calculation (Element -52)**
#### **Description**
The **Longitudinal Space Charge Calculation** element enables the computation of **space charge effects** in the longitudinal direction. This effect is crucial for accurately modeling beams with high charge densities, especially in low-energy regimes.

#### **Attributes**
1. **Element Type** – Set to `-52` for Longitudinal Space Charge Calculation.
2. **Calculation Mode** – Determines the method used for space charge calculation:
   - `0`: **Disable** longitudinal space charge effects.
   - `1`: **Enable** longitudinal space charge effects using the default model.
3. **Smoothing Parameter** – A factor controlling numerical smoothing of the space charge fields.

#### **Example**
`0 0 0 -52 1 0.1 /`
This means:
- **Longitudinal space charge effects are enabled**.
- **Smoothing parameter** is set to **0.1** to control numerical noise in the space charge calculation.


---

### **Transverse Space Charge Calculation (Element -55)**
#### **Description**
The **Transverse Space Charge Calculation** element enables the computation of **space charge effects** in the **transverse (X-Y) plane**. This effect is critical for accurately modeling high-intensity beams, particularly in low-energy or high-density regimes.

#### **Attributes**
1. **Element Type** – Set to `-55` for Transverse Space Charge Calculation.
2. **Calculation Mode** – Determines the method used for space charge calculation:
   - `0`: **Disable** transverse space charge effects.
   - `1`: **Enable** transverse space charge effects using the default model.
3. **Smoothing Parameter** – A factor controlling numerical smoothing of the space charge fields.

#### **Example**
`0 0 0 -55 1 0.1 /`
This means:
- **Transverse space charge effects are enabled**.
- **Smoothing parameter** is set to **0.1** to control numerical noise in the space charge calculation.


---

### **Simulation Termination (Element -99)**
#### **Description**
The **Simulation Termination** element is used to **explicitly end the simulation**. While simulations typically end when all elements have been processed, this element allows for manual termination at a specific point.

#### **Attributes**
1. **Element Type** – Set to `-99` for Simulation Termination.

#### **Example**
`0 0 0 -99 /`

This means:
- **The simulation is manually terminated** at this point.



