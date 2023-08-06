"""Models for edges in the network (pipes and lines)
"""
from abc import ABC, abstractmethod
import logging
import math
from typing import Dict, List
from peext.core import MESModel

P_FROM_MW = "p_from_mw"
P_TO_MW = "p_to_mw"

I_FROM_KA = "i_from_ka"
I_TO_KA = "i_to_ka"

VM_FROM_PU = "vm_from_pu"
VM_TO_PU = "vm_to_pu"

VA_FROM_DEGREE = "va_from_degree"
VA_TO_DEGREE = "va_to_degree"

LOADING_PERCENT = "loading_percent"

P_FROM_BAR = "p_from_bar"
P_TO_BAR = "p_to_bar"

T_FROM_K = "t_from_k"
T_TO_K = "t_to_k"

NAME_KEY = "name"

LOSS_KEY = "pl_mw"

HV_P = "p_hv_mw"
LV_P = "p_lv_mw"

MASS_FLOW_FROM_KEY = "mdot_from_kg_per_s"
MASS_FLOW_TO_KEY = "mdot_to_kg_per_s"

DIAMETER_KEY = "diameter_m"
LENGTH_KEY = "length_km"


class EdgeModel(ABC):
    """Base class for an edge."""

    def __init__(self, id, network, history_container=None) -> None:
        """Create an edge model with common properties.

        :param id: the id
        :type id: int
        :param network: the network
        :type network: pandapipes/power-network
        :param nodes: List of nodes, defaults to []
        :type nodes: list, optional
        """
        self._id = id
        self._network = network
        self._nodes = []
        self._history_container = history_container

    @property
    def history(self) -> Dict:
        return self._history_container

    @property
    def nodes(self) -> List:
        """Return all connected nodes.

        :return: list of nodes
        :rtype: List
        """
        return self._nodes

    def add_node(self, node: MESModel, direction="to", dock_point="") -> None:
        """Add a node

        :param node: node to add
        :type node: MESModel
        """
        self._nodes.append((node, direction, dock_point))

    @property
    def id(self):
        return self._id

    def properties_as_dict(self):
        return self._network[self.component_type()].loc[self._id]

    @property
    def network(self):
        return self._network

    @abstractmethod
    def loss_perc(self):
        pass

    def coords(self):
        x = 0
        y = 0
        num_coords = 0
        for node, _, _ in self.nodes:
            coords = node.coords()
            if coords is not None:
                num_coords += 1
                x += coords["x"]
                y += coords["y"]
        return {"x": x / num_coords, "y": y / num_coords} if num_coords > 0 else None


class TrafoEdge(EdgeModel):
    def values_as_dict(self):
        return self._network.res_trafo.loc[self._id]

    def component_type(self):
        return "trafo"

    def name(self):
        return self._network.trafo[NAME_KEY][self._id]

    def loss_perc(self):
        return abs(
            self._network.res_trafo[LOSS_KEY][self._id]
            / max(
                self._network.res_trafo[HV_P][self._id],
                self._network.res_trafo[LV_P][self._id],
            )
        )


class SwitchEdge(EdgeModel):
    def values_as_dict(self):
        return self._network.res_switch.loc[self._id]

    def component_type(self):
        return "switch"

    def name(self):
        return self._network.switch[NAME_KEY][self._id]

    def loss_perc(self):
        return 0


class LineEdge(EdgeModel):
    """Edge model representing a line of pandapower"""

    def __fetch_data(self, attr, time_delta):
        if time_delta != 0:
            if (
                self.network.name not in self.history
                or len(self.history[self.network.name][self.component_type()])
                <= time_delta
            ):
                return None
            if (
                self._id
                not in self.history[self.network.name][self.component_type()][
                    time_delta
                ][attr]
            ):
                logging.error(
                    "Id not in container, but expected! %s %s %s %s %s",
                    time_delta,
                    attr,
                    self._id,
                    self.network.name,
                    str(
                        self.history[self.network.name][self.component_type()][
                            time_delta
                        ][attr]
                    ),
                )
            return self.history[self.network.name][self.component_type()][time_delta][
                attr
            ][self._id]
        return self._network.res_line[attr][self._id]

    def power_start(self, time_delta=0):
        """Return the power transferred at the start of the line

        :return: power in MW
        :rtype: float
        """
        return self.__fetch_data(P_FROM_MW, time_delta)

    def power_end(self, time_delta=0):
        """Return the power transferred at the end of the line

        :return: power in MW
        :rtype: float
        """
        return self.__fetch_data(P_TO_MW, time_delta)

    def current_start(self, time_delta=0):
        """Return the current at the start of the line

        :return: current in KA
        :rtype: float
        """
        return self.__fetch_data(I_FROM_KA, time_delta)

    def current_end(self, time_delta=0):
        """Return the current at the end of the line

        :return: current in KA
        :rtype: float
        """
        return self.__fetch_data(I_TO_KA, time_delta)

    def voltage_magnitude_start(self, time_delta=0):
        """Return the voltage magnitude at the start of the line

        :return: voltage in PU
        :rtype: float
        """
        return self.__fetch_data(VM_FROM_PU, time_delta)

    def voltage_magnitude_end(self, time_delta=0):
        """Return the voltage magnitude at the end of the line

        :return: voltage in PU
        :rtype: float
        """
        return self.__fetch_data(VM_TO_PU, time_delta)

    def voltage_angle_start(self, time_delta=0):
        """Return the voltage angle at the start of the line

        :return: voltage in degree
        :rtype: float
        """
        return self.__fetch_data(VA_FROM_DEGREE, time_delta)

    def voltage_angle_end(self, time_delta=0):
        """Return the voltage angle at the end of the line

        :return: voltage in degree
        :rtype: float
        """
        return self.__fetch_data(VA_TO_DEGREE, time_delta)

    def loading_percent(self, time_delta=0):
        """Return the load of the line

        :return: load in percent
        :rtype: float
        """
        return self.__fetch_data(LOADING_PERCENT, time_delta)

    def loss(self, time_delta=0):
        """Return the loss of the line

        :return: loss in percent
        :rtype: float
        """
        return self.__fetch_data(LOSS_KEY, time_delta)

    def values_as_dict(self):
        return self._network.res_line.loc[self._id]

    def component_type(self):
        return "line"

    def name(self):
        return self._network.line[NAME_KEY][self._id]

    def loss_perc(self):
        return abs(
            self.loss()
            / max(
                self.power_start(),
                self.power_end(),
            )
        )


class PipeEdge(EdgeModel):
    """Edge model representing a pipe of pandapipes"""

    def __fetch_data(self, attr, time_delta):
        if time_delta != 0:
            if (
                self.network.name not in self.history
                or len(self.history[self.network.name][self.component_type()])
                <= time_delta
            ):
                return None
            return self.history[self.network.name][self.component_type()][time_delta][
                attr
            ][self._id]
        return self._network.res_pipe[attr][self._id]

    def pressure_start(self, time_delta=0) -> float:
        """Pressure on the start at the pipe

        :return: pressure in bar
        :rtype: float
        """
        return self.__fetch_data(P_FROM_BAR, time_delta)

    def pressure_end(self, time_delta=0):
        """Pressure at the end at the pipe

        :return: pressure in bar
        :rtype: float
        """
        return self.__fetch_data(P_TO_BAR, time_delta)

    def temp_start(self, time_delta=0):
        """Temp at the start at the pipe

        :return: temp in K
        :rtype: float
        """
        return self.__fetch_data(T_FROM_K, time_delta)

    def temp_end(self, time_delta=0):
        """Temp at the end at the pipe

        :return: temp in K
        :rtype: float
        """
        return self.__fetch_data(T_TO_K, time_delta)

    def flow_start(self, time_delta=0):
        """Mass flow at the start at the pipe

        :return: mass flow in kgps
        :rtype: float
        """
        return self.__fetch_data(MASS_FLOW_FROM_KEY, time_delta)

    def flow_end(self, time_delta=0):
        """Mass flow at the end at the pipe

        :return: mass flow in kgps
        :rtype: float
        """
        return self.__fetch_data(MASS_FLOW_TO_KEY, time_delta)

    def values_as_dict(self):
        return self._network.res_pipe.loc[self._id]

    def component_type(self):
        return "pipe"

    def name(self):
        return self._network.pipe[NAME_KEY][self._id]

    def calc_pipe_heat_loss_perc(self):
        C = 500
        ALPHA = 0.19
        AMBIENT_T = 285
        d = self._network.pipe[DIAMETER_KEY][self._id]
        l = self._network.pipe[LENGTH_KEY][self._id] * 1000
        m = (d / 2) ** 2 * math.pi * l
        delta_t = abs(self.temp_start() - self.temp_end()) + 1
        heat_energy = m * C * delta_t
        delta_ambient = abs(AMBIENT_T - (self.temp_start() + self.temp_end()) / 2)
        power_loss = d * math.pi * l * delta_ambient * ALPHA
        return (power_loss / 360) / heat_energy

    def loss_perc(self):
        return (
            abs(
                (abs(self.flow_end()) - abs(self.flow_start()))
                / max(self.flow_end(), self.flow_start())
            ),
            self.calc_pipe_heat_loss_perc(),
        )


class PumpEdge(EdgeModel):
    """Edge model representing a pump of pandapipes"""

    def values_as_dict(self):
        return self._network.res_pump.loc[self._id]

    def component_type(self):
        return "pump"

    def name(self):
        return self._network.pump[NAME_KEY][self._id]

    def loss_perc(self):
        return 0


class CircPumpPressureEdge(EdgeModel):
    """Edge model representing a circ_pump_pressure of pandapipes"""

    def values_as_dict(self):
        return self._network.res_circ_pump_pressure.loc[self._id]

    def component_type(self):
        return "circ_pump_pressure"

    def name(self):
        return self._network.circ_pump_pressure[NAME_KEY][self._id]

    def loss_perc(self):
        return 0


class CircPumpMassEdge(EdgeModel):
    """Edge model representing a circ_pump_mass of pandapipes"""

    def values_as_dict(self):
        return self._network.res_circ_pump_mass.loc[self._id]

    def component_type(self):
        return "circ_pump_mass"

    def name(self):
        return self._network.circ_pump_mass[NAME_KEY][self._id]

    def loss_perc(self):
        return 0
