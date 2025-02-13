# Output files





---
## Reference Particle Information (`fort.18`)

The file **`fort.18`** contains data related to the reference particle along the beamline.

Note that $p_0 = \sqrt{E_0^2 - (m_0 c^2)^2} / c$ is the reference momentum that is used in other output files.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `phase_ref`: Phase of the reference particle relative (rad)
3. `gamma_ref`: Reference Lorentz factor, defined as $ \gamma_0 = \frac{E_0}{m_0 c^2} $ (dimensionless)
4. `kinetic_energy_ref`: Energy of the reference particle excluding rest mass energy: $E_0 - m_0 c^2$. (MeV)
5. `beta_ref`:  Reference Relativistic velocity factor, $ \beta_0 = v_0/c $. (dimensionless)
6. `max_r`: Maximum radial distance from the beam axis.


---

## RMS Size Information for $x$-plane (`fort.24`)

The file **`fort.24`** contains RMS size information for the $x$-plane.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `mean_x`: Mean position of the beam in the X-plane (meters)
3. `sigma_x`: Root mean square (RMS) size (meters)
4. `mean_px_over_p0`: Mean transverse momentum $p_x/p_0$  (rad)
5. `sigma_px_over_p0`: RMS transverse momentum $\sigma_{p_x}/p_0$ (rad)
6. `twiss_alpha_x`: Twiss alpha parameter in the $x$-plane (dimensionless)
7. `norm_emit_x`: Normalized RMS horizontal emittance (meter-rad)

If `diagnostic=2`, there are additional columns:

8.  `norm_emit_x_90percent`: 90% normalized RMS horizontal emittance (meter-rad)
9.  `norm_emit_x_95percent`: 95% normalized RMS horizontal emittance (meter-rad)
10. `norm_emit_x_99percent`: 99% normalized RMS horizontal emittance (meter-rad)


---

## RMS Size Information for $y$-plane (`fort.25`)

The file **`fort.25`** contains RMS size information for the $y$-plane.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `mean_y`: Mean position of the beam in the $x$-plane (meters)
3. `sigma_y`: Root mean square (RMS) size (meters)
4. `mean_py_over_p0`: Mean transverse momentum $p_y/p_0$ (rad)
5. `sigma_py_over_p0`: RMS transverse momentum $\sigma_{p_y}/p_0$ (rad)
6. `twiss_alpha_y`: Twiss alpha parameter in the $y$-plane (dimensionless)
7. `norm_emit_y`: Normalized RMS vertical mittance in meters-radians (meter-rad)

If `diagnostic=2`, there are additional columns:

8.  `norm_emit_y_90percent`: 90% normalized RMS vertical emittance (meter-rad)
9.  `norm_emit_y_95percent`: 95% normalized RMS vertical emittance (meter-rad)
10. `norm_emit_y_99percent`: 99% normalized RMS vertical emittance (meter-rad)

---

## RMS Size Information for $z$-plane (`fort.26`)

The file **`fort.26`** contains RMS size information for the $z$-plane (longitudinal).

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `mean_phase_deg`: Mean position of the beam in the $z$-plane.
3. `sigma_phase_deg`: Root mean square (RMS) size (degrees)
4. `neg_delta_mean_energy`: $E_0 - E$ where $E_0$ is the reference energy and $E$ is the centroid energy (MeV)
5. `sigma_energy`: RMS energy deviation in (MeV)
6. `twiss_alpha_z`: Twiss alpha parameter for the $z$-plane (dimensionless)
7. `norm_emit_z`: Normalized RMS emittance in (degree-MeV)

If `diagnostic=2`, there are additional columns:

8.  `norm_emit_z_90percent`: 90% normalized RMS longitudinal emittance (degree-MeV)
9.  `norm_emit_z_95percent`: 95% normalized RMS longitudinal emittance (degree-MeV)
10. `norm_emit_z_99percent`: 99% normalized RMS longitudinal emittance (degree-MeV)


---

## Maximum amplitude information (`fort.27`, `diagnostic=1`)

The file **`fort.27`** contains the maximum amplitude information for various beam parameters.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `max_abs_x`:  Maximum horizontal displacement from the beam axis  $\max(|x|)$ (meters)
3. `max_abs_px_over_p0`:  Maximum $x$-plane transverse momentum $\max(|p_x/p_0|)$ (rad)
2. `max_abs_y`:  Maximum vertical displacement from the beam axis $\max(|y|)$ (meters)
3. `max_abs_py_over_p0`:  Maximum $y$-plane transverse momentum $\max(|p_y/p_0|)$ (rad)
6. `max_phase`:  Maximum deviation in phase (deg???)
7. `max_energy_dev`: Maximum deviation in particle energy (MeV)

---

## Maximum amplitude information (`fort.27`, `diagnostic=2`)

The file **`fort.27`** contains the maximum amplitude information for various beam parameters.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `max_abs_x`:  Maximum horizontal displacement from the beam axis  $\max(|x|)$ (meters)
3. `max_abs_gammabeta_x`:  Maximum $x$-plane transverse momentum $\max(|\gamma\beta_x|)$ (dimensionless)
2. `max_abs_y`:  Maximum vertical displacement from the beam axis $\max(|y|)$ (meters)
3. `max_abs_gammabeta_y`:  Maximum $x$-plane transverse momentum $\max(|\gamma\beta_y|)$ (dimensionless)
6. `max_phase`:  Maximum deviation in phase (deg???)
7. `max_gamma_rel`: Maximum deviation in relativistic gamma $\max(|\gamma - \gamma_0)|)$ (dimensionless)

---







## Load Balance and Loss Diagnostic (`fort.28`)

The file **`fort.28`** contains information on load balancing and particle loss diagnostics.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `loadbalance_min_n_particle`: Minimum number of particles assigned to a processing element (dimensionless)
3. `loadbalance_max_n_particle`: Maximum number of particles assigned to a processing element (dimensionless)
4. `n_particle`:  Total number of particles present in the bunch at the given position (dimensionless)

---

## Cubic Root of 3rd Moments of the Beam Distribution (`fort.29`, `diagnostic=1`)

The file **`fort.29`** with `diagnostic=1` contains the cubic root of the third moments of the beam distribution.

Here  $ M_3(x) \equiv\left< (x-\left< x \right>)^3 \right>^{1/3} $, averaging over all particles.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `moment3_x`: Cubic root of the third moment of the horizontal position $M_3(x)$ (meters)
3. `moment3_px_over_p0`: Cubic root of the third moment of the horizontal momentum $M_3(p_x/p_0)$ (rad)
2. `moment3_y`: Cubic root of the third moment of the vertical position $M_3(y)$ (meters)
3. `moment3_py_over_p0`:  Cubic root of the third moment of the vertical momentum $M_3(p_y/p_0)$ (rad)
2. `moment3_phase`: Cubic root of the third moment of the phase $M_3(\phi)$ (deg??)
3. `moment3_energy`: Cubic root of the energy $M_3(E)$ (MeV)

---
## Radius of the Beam Distribution (`fort.29`, `diagnostic=2`)

The file **`fort.29`** with `diagnostic=2`contains radius moments of the beam distribution.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `mean_r`: mean radius (meters)
3. `sigma_r`: rms radius (meters)
4. `mean_r_90percent`: 90 percent mean radius (meters)
5. `mean_r_95percent`: 95 percent mean radius (meters)
6. `mean_r_99percent`: 99 percent mean radius (meters)
7. `max_r_rel`: maximum radius relative to the ($x$, $y$) center of the bunch (meters)



---

## Fourth Root of 4th Moments of the Beam Distribution (`fort.30`, `diagnostic=1`)

The file **`fort.30`** with `diagnostic=1` contains the fourth root of the fourth moments of the beam distribution.

Here  $ M_4(x) \equiv\left< (x-\left< x \right>)^4 \right>^{1/4} $, averaging over all particles.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `moment4_x`: fourth root of the third moment of the horizontal position $M_4(x)$ (meters)
3. `moment4_px_over_p0`: fourth root of the third moment of the horizontal momentum $M_4(p_x/p_0)$ (rad)
2. `moment4_y`: fourth root of the third moment of the vertical position $M_4(y)$ (meters)
3. `moment4_py_over_p0`: fourth root of the third moment of the vertical momentum $M_4(p_y/p_0)$ (rad)
2. `moment4_phase`: fourth root of the third moment of the phase $M_4(\phi)$ (deg??)
3. `moment4_energy`: fourth root of the energy $M_4(E)$ (MeV)

---

## Number of Particles for Each Charge State (`fort.32`)

The file **`fort.32`** contains information on the number of particles for each charge state at different positions along the beamline.

#### Column Descriptions:

1. `z`: longitudinal position along the beamline (meters)
2. `charge_state_n_particle`: Count of particles in each charge state at the given position (dimensionless)





