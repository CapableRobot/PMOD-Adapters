# PMOD Adapters

Designed by [Capable Robot Components](http://capablerobot.com).  Follow us on [Twitter](http://twitter.com/capablerobot) for product announcements and updates.

---

This repository contains schematics, layout, and bill of materials for various PMOD adapters and interfaces.  This currently includes:

* 2018-09-13 : [CR7CSZ - BeagleWire to PMOD](boards/BeagleWire) 
* 2018-09-13 : [CRRYEK - BeagleWire to Debug PMOD](boards/BeagleWire-Debug)

Additional designed will be added to this repository over time.  

### License

|  | License |
| :---: | --- |
|  | This work is shared under a [Creative Commons Attribution-ShareAlike](https://creativecommons.org/licenses/by-sa/4.0/) License. <br/><br/> You are free to: **Share** - copy and redistribute the material in any medium or format.  **Adapt** - transform and build upon the material for any purpose, even commercially. <br/><br/> Under the following terms: **Attribution** - You must give appropriate credit, provide a link to the license, and indicate if changes were made. **ShareAlike** - You must distribute your contributions under the this same license. |


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

