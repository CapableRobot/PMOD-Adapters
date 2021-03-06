# PMOD Adapters

Designed by [Capable Robot Components](http://capablerobot.com).  Follow us on [Twitter](http://twitter.com/capablerobot) for product announcements and updates.

---

This repository contains schematics, layout, and bill of materials for various PMOD adapters and interfaces.  This currently includes:

* 2019-01-30 : [CRBFH0 - LED Debug](boards/LED-Debug)
* 2019-01-30 : [CR6QEG - PMOD Debug](boards/Debug)
* 2018-09-13 : [CR7CSZ - BeagleWire to PMOD](boards/BeagleWire) 
* 2018-09-13 : [CRRYEK - BeagleWire to Debug PMOD](boards/BeagleWire-Debug)

Additional designed will be added to this repository over time.  

| **Type** | **License** |
| --- | --- |
| Hardware | Copyright Capable Robot Components 2018 <br><br>This documentation describes Open Hardware and is licensed under the [CERN OHL v1.2 or later](https://www.ohwr.org/licenses/cern-ohl/license_versions/v1.2). <br/><br/> You may redistribute and modify this documentation under the terms of the CERN OHL v.1.2.  This documentation is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN OHL v.1.2 for applicable conditions |
| Software | [MIT License](LICENSE.txt) |

More detailed information about the CERN License is available in the [license](license) folder and on the [CERN website](https://www.ohwr.org/projects/cernohl/wiki).

---

### [CRBFH0] LED Debug

| ![Top Render](images/CRBFH0_top.png?raw=true) | ![Bottom Render](images/CRBFH0_bottom.png?raw=true) |
| :-------------: | :-------------: |
| **Top Rendering**    | **Bottom Rendering** |

This PCB allows a single PMOD to control 64 LEDs via a 4:16 address decoder and 4 mask control signals.  It was originally designed by H.Poetzl as part of the [Apertus project](https://www.apertus.org/pmod-debug).  Changes made to this version are:

- Changed 0402 resistors to 0603 packages.
- Changed the N channel MOSFETs from SC75 to SOT23 packages. 
- PCB layout changes to accommodate the larger components.

No schematic changes were made, meaning the PMOD interface is identical.

This board can be ordered at [OSH Park](https://oshpark.com/shared_projects/n7GHOesv) and costs $6.75 for a set of 3.

[![Order from OSH Park](https://oshpark.com/assets/badge-5b7ec47045b78aef6eb9d83b3bac6b1920de805e9a0c227658eac6e19a045b9c.png)](https://oshpark.com/shared_projects/n7GHOesv)

---

### [CR6QEG] PMOD Debug

| ![Top Render](images/CR6QEG_top.png?raw=true) | ![Bottom Render](images/CR6QEG_bottom.png?raw=true) |
| :-------------: | :-------------: |
| **Top Rendering**    | **Bottom Rendering** |

This PCB adapts allows for probing of signals between an FPGA development board an a PMOD peripheral.  

A 2x6 right angle male header should be installed in the `FPGA` header and a 2x6 right angle female header should be installed into the `PMOD` header.

This board can be ordered at [OSH Park](https://oshpark.com/shared_projects/YEDBhzJa) and costs $3.20 for a set of 3.

[![Order from OSH Park](https://oshpark.com/assets/badge-5b7ec47045b78aef6eb9d83b3bac6b1920de805e9a0c227658eac6e19a045b9c.png)](https://oshpark.com/shared_projects/YEDBhzJa)

---

### [CR7CSZ] BeagleWire to PMOD

| ![Top Render](images/CR7CSZ_top.jpg?raw=true) | ![Bottom Render](images/CR7CSZ_bottom.jpg?raw=true) |
| :-------------: | :-------------: |
| **Top Rendering**    | **Bottom Rendering** |

This PCB adapts standard PMOD peripherals to the BeagleWire PMOD connectors.  

The BeagleWire has a reversed pinout wherein the Power and Ground are on the right side of the connector (as you face a female PMOD on the BeagleWire) while all other PMOD hosts have the Power and Ground on the left side of the connector.

A 2x6 right angle male header should be installed in the `BEAGLE` header and a 2x6 right angle female header should be installed into the `PMOD` header.

This board can be ordered at [OSH Park](https://oshpark.com/shared_projects/sm0OcuML) and costs $2.40 for a set of 3.

[![Order from OSH Park](https://oshpark.com/assets/badge-5b7ec47045b78aef6eb9d83b3bac6b1920de805e9a0c227658eac6e19a045b9c.png)](https://oshpark.com/shared_projects/sm0OcuML)

---

### [CRRYEK] BeagleWire to Debug PMOD

| ![Top Render](images/CRRYEK_top.jpg?raw=true) | ![Bottom Render](images/CRRYEK_bottom.jpg?raw=true) |
| :-------------: | :-------------: |
| **Top Rendering**    | **Bottom Rendering** |

This PCB adapts standard PMOD peripherals to the BeagleWire PMOD connectors.  It is similar to the CR7CSZ version but adds an additional 2x6 header (standard PMOD pinout) to aid in probing and debugging signals between the BeagleWire and the PMOD peripheral.

A 2x6 right angle male header should be installed in the `BEAGLE` header and a 2x6 right angle female header should be installed into the `PMOD` header.

This board can be ordered at [OSH Park](https://oshpark.com/shared_projects/SsbzeQ1o) and costs $3.20 for a set of 3.

[![Order from OSH Park](https://oshpark.com/assets/badge-5b7ec47045b78aef6eb9d83b3bac6b1920de805e9a0c227658eac6e19a045b9c.png)](https://oshpark.com/shared_projects/SsbzeQ1o)

