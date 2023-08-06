"""Nodes for pandapipes/pandapower networks creating an abstraction for use withing agents.
"""
from peext.core import RegulatableMESModel


MDOT_KG_PER_S = "mdot_kg_per_s"
ACTIVE_POWER = "p_mw"
REACTIVE_POWER = "q_mvar"
VOLTAGE = "vm_pu"
VOLTAGE_ANGLE = "va_degree"
SCALING = "scaling"
CONTROLLER_OBJ_KEY = "object"
NAME_KEY = "name"
HEAT_ENERGY = "heat_energy"
QEXT_W = "qext_w"


class RegulatableController(RegulatableMESModel):
    """Base class for regulatable controller Nodes."""

    def component_type(self):
        return "controller"

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the controller
        :rtype: float [0,1]
        """
        return self._network.controller[CONTROLLER_OBJ_KEY][self._id].regulation

    def regulate(self, factor: float):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        self._network.controller[CONTROLLER_OBJ_KEY][self._id].regulation = factor

    def name(self):
        """Return name of the controller

        :return: the name
        :rtype: str
        """
        return self._network.controller[CONTROLLER_OBJ_KEY][self._id].name

    @property
    def controller(self):
        """Return the represented controller in the network

        :return: controller obj
        :rtype: Obj
        """
        return self._network.controller[CONTROLLER_OBJ_KEY][self._id]

    def coords(self):
        return self.controller.coords


class CouplingPoint(RegulatableController):
    def loss_perc(self):
        return 1 - self.controller.efficiency

    @property
    def networks(self):
        return self.controller.get_all_net_names()


class G2PNode(CouplingPoint):
    """Node representing g2p system. Contains wrapper functions for accessing the relevant information and control variables."""

    def edge_description(self) -> dict:
        return [
            (
                self.controller.name_net_gas,
                self.controller.name_net_power,
                self.controller.efficiency,
            )
        ]

    def power_output(self) -> float:
        """
        :return: Actual mass flow
        :rtype: float
        """
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_gen

    def mdot_kg_per_s(self) -> float:
        """
        :return: Actual mass flow
        :rtype: float
        """
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].gas_cons

    def active_power_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_cap

    def mdot_kg_per_s_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].gas_cap

    def values_as_dict(self):
        return {
            ACTIVE_POWER: self.power_output(),
            MDOT_KG_PER_S: self.gas_consume(),
            "sink": self.network.controller[CONTROLLER_OBJ_KEY][
                self.id
            ].get_gas_consume(self.network),
            "gen": self.network.controller[CONTROLLER_OBJ_KEY][
                self.id
            ].get_power_production(self.network),
        }


class P2GNode(CouplingPoint):
    """Node representing p2g system. Contains wrapper functions for accessing the relevant information and control variables."""

    def edge_description(self) -> dict:
        return [
            (
                self.controller.name_net_power,
                self.controller.name_net_gas,
                self.controller.efficiency,
            )
        ]

    def mdot_kg_per_s(self) -> float:
        """
        :return: Actual mass flow
        :rtype: float
        """
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].mdot_kg_per_s

    def power_load(self) -> float:
        """
        :return: Actual power load
        :rtype: float
        """
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_load

    def active_power(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_load

    def active_power_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_cap

    def mdot_kg_per_s_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].gas_cap

    def values_as_dict(self):
        return {
            MDOT_KG_PER_S: self.mdot_kg_per_s(),
            ACTIVE_POWER: self.power_load(),
            "source": self.network.controller[CONTROLLER_OBJ_KEY][
                self.id
            ].get_source_production(self.network),
            "load": self.network.controller[CONTROLLER_OBJ_KEY][self.id].get_power_load(
                self.network
            ),
        }


class CHPNode(CouplingPoint):
    """Node representing chp with gas turbine system. Contains wrapper functions for accessing the relevant information and control variables."""

    def edge_description(self) -> dict:
        return [
            (
                self.controller.name_net_gas,
                self.controller.name_net_power,
                self.controller.efficiency,
            ),
            (
                self.controller.name_net_gas,
                self.controller.name_net_heat,
                self.controller.heat_efficiency,
            ),
        ]

    def heat_output(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].heat_energy

    def qext_w(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].heat_energy

    def power_output(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_gen

    def active_power(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_gen

    def storage_load(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].storage_load

    def mdot_kg_per_s(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].gas_cons

    def heat_regulation_factor(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].heat_regulation

    def regulate_heat(self, regulation):
        self.network.controller[CONTROLLER_OBJ_KEY][
            self.id
        ].heat_regulation = regulation

    def active_power_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_cap

    def mdot_kg_per_s_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].gas_cap

    def q_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].heat_cap

    def values_as_dict(self):
        return {ACTIVE_POWER: self.power_output(), HEAT_ENERGY: self.heat_output()}

    def state_as_dict(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].state_as_dict()


class P2HNode(CouplingPoint):
    """Node representing P2H."""

    def edge_description(self) -> dict:
        return [
            (
                self.controller.name_net_power,
                self.controller.name_net_heat,
                self.controller.efficiency,
            )
        ]

    def heat_output(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].heat_energy

    def qext_w(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].heat_energy

    def power_load(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_load

    def active_power(self) -> float:
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_load

    def active_power_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].power_cap

    def q_capability(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].heat_cap

    def values_as_dict(self):
        return {ACTIVE_POWER: self.power_load(), HEAT_ENERGY: self.heat_output()}

    def state_as_dict(self):
        return self.network.controller[CONTROLLER_OBJ_KEY][self.id].state_as_dict()


class PowerLoadNode(RegulatableMESModel):
    """Node representing power load."""

    def active_power(self) -> float:
        """
        :return: active power
        :rtype: float
        """
        return self._network.res_load[ACTIVE_POWER][self._id]

    def reactive_power(self) -> float:
        """
        :return: reactive power
        :rtype: float
        """
        return self._network.res_load[REACTIVE_POWER][self._id]

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        self._network.load[SCALING][self._id] = new_scaling

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the load
        :rtype: float [0,1]
        """
        return self._network.load[SCALING][self._id]

    def name(self):
        """Return name of the load

        :return: the name
        :rtype: str
        """
        return self._network.load[NAME_KEY][self._id]

    def active_power_capability(self):
        """Return AP capability

        :return: AP cap
        :rtype: float
        """
        return self._network.load[ACTIVE_POWER][self._id]

    def component_type(self):
        return "load"

    def values_as_dict(self):
        return self._network.res_load.loc[self._id]


class SwitchNode(RegulatableMESModel):
    def regulate(self, _):
        pass

    def regulation_factor(self) -> float:
        return 1

    def name(self):
        """Return name of the ext grid

        :return: the name
        :rtype: str
        """
        return self._network.switch[NAME_KEY][self._id]

    def active_power_capability(self):
        return 0

    def component_type(self):
        return "switch"

    def values_as_dict(self):
        return {}


class SGeneratorNode(RegulatableMESModel):
    """Node representing a static generator"""

    def active_power(self):
        """
        :return: active power
        :rtype: float
        """
        return self._network.res_sgen[ACTIVE_POWER][self._id]

    def reactive_power(self):
        """
        :return: reactive power
        :rtype: float
        """
        return self._network.res_sgen[REACTIVE_POWER][self._id]

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        self._network.sgen[SCALING][self._id] = new_scaling

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the generator
        :rtype: float [0,1]
        """
        return self._network.sgen[SCALING][self._id]

    def name(self):
        """Return name of the gen

        :return: the name
        :rtype: str
        """
        return self._network.sgen[NAME_KEY][self._id]

    def active_power_capability(self):
        """Return AP capability

        :return: AP cap
        :rtype: float
        """
        return self._network.sgen[ACTIVE_POWER][self._id]

    def component_type(self):
        return "sgen"

    def values_as_dict(self):
        return self._network.res_sgen.loc[self._id]


class GeneratorNode(RegulatableMESModel):
    """Node representing a generator"""

    def active_power(self):
        """
        :return: active power
        :rtype: float
        """
        return self._network.res_gen[ACTIVE_POWER][self._id]

    def reactive_power(self):
        """
        :return: reactive power
        :rtype: float
        """
        return self._network.res_gen[REACTIVE_POWER][self._id]

    def voltage(self):
        """
        :return: voltage
        :rtype: [type]
        """
        return self._network.res_gen[VOLTAGE][self._id]

    def voltage_angle(self) -> float:
        """
        :return: voltage angle in degree
        :rtype: float
        """
        return self._network.res_gen[VOLTAGE_ANGLE][self._id]

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        self._network.gen[SCALING][self._id] = new_scaling

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the generator
        :rtype: float [0,1]
        """
        return self._network.gen[SCALING][self._id]

    def name(self):
        """Return name of the gen

        :return: the name
        :rtype: str
        """
        return self._network.gen[NAME_KEY][self._id]

    def active_power_capability(self):
        """Return AP capability

        :return: AP cap
        :rtype: float
        """
        return self._network.gen[ACTIVE_POWER][self._id]

    def component_type(self):
        return "gen"

    def values_as_dict(self):
        return self._network.res_gen.loc[self._id]


class SinkNode(RegulatableMESModel):
    """Node representing a sink"""

    def mdot_kg_per_s(self):
        """
        :return: Actual mass flow
        :rtype: float
        """
        return self._network.res_sink[MDOT_KG_PER_S][self._id]

    def mdot_kg_per_s_capability(self):
        """Return mdot capability

        :return: mass flow cap
        :rtype: float
        """
        return self._network.sink[MDOT_KG_PER_S][self._id]

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        self._network.sink[SCALING][self._id] = new_scaling

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the sink
        :rtype: float [0,1]
        """
        return self._network.sink[SCALING][self._id]

    def name(self):
        """Return name of the sink

        :return: the name
        :rtype: str
        """
        return self._network.sink[NAME_KEY][self._id]

    def component_type(self):
        return "sink"

    def values_as_dict(self):
        return self._network.res_sink.loc[self._id]


class SourceNode(RegulatableMESModel):
    """Node representing a source"""

    def mdot_kg_per_s(self):
        """
        :return: Actual mass flow
        :rtype: float
        """
        return self._network.res_source[MDOT_KG_PER_S][self._id]

    def mdot_kg_per_s_capability(self):
        """Return mdot capability

        :return: mass flow cap
        :rtype: float
        """
        return self._network.source[MDOT_KG_PER_S][self._id]

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        self._network.source[SCALING][self._id] = new_scaling

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the source
        :rtype: float [0,1]
        """
        return self._network.source[SCALING][self._id]

    def name(self):
        """Return name of the source

        :return: the name
        :rtype: str
        """
        return self._network.source[NAME_KEY][self._id]

    def component_type(self):
        return "source"

    def values_as_dict(self):
        return self._network.res_source.loc[self._id]


class HeatExchangerNode(RegulatableMESModel):
    """Node representing a heat exchanger"""

    def __init__(self, id, network, edges=None) -> None:
        super().__init__(id, network, edges)

        self._initial_q = self.qext_w()
        self._scaling = 1

    def mdot_kg_per_s(self):
        """
        :return: Actual mass flow
        :rtype: float
        """
        return self._network.res_heat_exchanger[MDOT_KG_PER_S][self._id]

    def q_capability(self):
        """Return q capability

        :return: q cap
        :rtype: float
        """
        return self._initial_q

    def qext_w(self):
        """Return qext_w

        :return: q cap
        :rtype: float
        """
        return self._network.heat_exchanger[QEXT_W][self._id]

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        self._scaling = new_scaling
        self._network.heat_exchanger.at[self._id, QEXT_W] = (
            new_scaling * self._initial_q
        )

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the heat_exchanger
        :rtype: float [0,1]
        """
        return self._scaling

    def name(self):
        """Return name of the heat_exchanger

        :return: the name
        :rtype: str
        """
        return self._network.heat_exchanger[NAME_KEY][self._id]

    def component_type(self):
        return "heat_exchanger"

    def values_as_dict(self):
        return {
            **self._network.res_heat_exchanger.loc[self._id],
            "qext_w": self._network.heat_exchanger[QEXT_W][self._id],
        }


class ExtGasGrid(RegulatableMESModel):
    """Node representing a ext grid in a gas network"""

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        pass

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the ext grid
        :rtype: float [0,1]
        """
        return 1

    def name(self):
        """Return name of the ext grid

        :return: the name
        :rtype: str
        """
        return self._network.ext_grid[NAME_KEY][self._id]

    def component_type(self):
        return "ext_grid"

    def values_as_dict(self):
        return self._network.res_ext_grid.loc[self._id]


class ExtPowerGrid(RegulatableMESModel):
    """Node representing a ext grid in a power network"""

    def regulate(self, new_scaling):
        """Set the regulation factor.

        :param factor: new regulation factor
        :type factor: float [0,1]
        """
        pass

    def regulation_factor(self) -> float:
        """
        :return: the regulation factor for the ext grid
        :rtype: float [0,1]
        """
        return 1

    def name(self):
        """Return name of the ext grid

        :return: the name
        :rtype: str
        """
        return self._network.ext_grid[NAME_KEY][self._id]

    def component_type(self):
        return "ext_grid"

    def values_as_dict(self):
        return self._network.res_ext_grid.loc[self._id]


class BusNode(RegulatableMESModel):
    def regulate(self, _):
        pass

    def regulation_factor(self) -> float:
        return 1

    def name(self):
        """Return name of the ext grid

        :return: the name
        :rtype: str
        """
        return self._network.bus[NAME_KEY][self._id]

    def active_power_capability(self):
        return 0

    def component_type(self):
        return "bus"

    def values_as_dict(self):
        return self._network.res_bus.loc[self._id]

    def coords(self):
        return self._network.bus_geodata.loc[self._id]


class EmptyBusNode(BusNode):
    pass


class JunctionNode(RegulatableMESModel):
    def regulate(self, _):
        pass

    def regulation_factor(self) -> float:
        return 1

    def mdot_kg_per_s_capability(self):
        return 0

    def name(self):
        """Return name of the junction

        :return: the name
        :rtype: str
        """
        return self._network.junction[NAME_KEY][self._id]

    def component_type(self):
        return "junction"

    def values_as_dict(self):
        return self._network.res_junction.loc[self._id]

    def coords(self):
        return self._network.junction_geodata.loc[self._id]


class EmptyJunctionNode(JunctionNode):
    pass
