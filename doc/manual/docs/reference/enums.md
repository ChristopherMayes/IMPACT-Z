<!-- This page is generated from spec/impactz.yaml by scripts/generate_reference.py. Do not edit by hand. -->

# Enumerations

Integer flags in the input file with fixed sets of allowed values.

## BoundaryType

| Name | Value |
|------|------:|
| `trans_open_longi_open` | 1 |
| `trans_open_longi_period` | 2 |
| `trans_round_longi_open` | 3 |
| `trans_round_longi_period` | 4 |
| `trans_rect_longi_open` | 5 |
| `trans_rect_longi_period` | 6 |

## DiagnosticType

| Name | Value |
|------|------:|
| `none` | 0 |
| `standard` | 1 |
| `extended` | 2 |

## DistributionType

| Name | Value |
|------|------:|
| `uniform` | 1 |
| `gauss` | 2 |
| `waterBag` | 3 |
| `semiGauss` | 4 |
| `kV` | 5 |
| `unknown` | 6 |
| `read` | 19 |
| `multi_charge_state_waterbag` | 16 |
| `multi_charge_state_gaussian` | 17 |

## GPUFlag

| Name | Value |
|------|------:|
| `disabled` | 0 |
| `enabled` | 5 |

## IntegratorType

| Name | Value |
|------|------:|
| `linear_map` | 1 |
| `runge_kutta` | 2 |

## MultipoleType

| Name | Value |
|------|------:|
| `sextupole` | 2 |
| `octupole` | 3 |
| `decapole` | 4 |

## RFCavityCoordinateType

| Name | Value |
|------|------:|
| `cartesian` | 2 |
| `cylindrical` | 1 |

## RFCavityDataMode

| Name | Value |
|------|------:|
| `discrete` | 1 |
| `both` | 2 |
| `analytical` | 3 |

## WigglerType

| Name | Value |
|------|------:|
| `planar` | 1 |
| `helical` | 2 |
