# Coordinates



## Phase space

Impact-Z exposes 
1. x
2. px/p0
3. y
4. py/p0
5. phase_deg = (t - t0) * f0 * 360
6. E0 - E

Internally it uses:
1. x * 2 π f0  / c (dimensionless)
2. gamma*beta_x 



## Distribution outut (-2)

1st col: x normalized by c/omega
2nd col: Px normalized by mc, here this column has to be divided by gamma beta to convert to unit
radian
3rd col: y normalized by c/omega
4th col: Py normalized by mc, here this column has to be divided by gamma beta to convert to unit
radian
5th col: phase (radian)
6th col: kinetic energy deviation (E0 -E) normalized by mc^2
7th col: q/m, for an electron, q = -1, m = 0.511001e6
8th col: charge per macro-particle (Coulomb per particle)
9th col: particle id