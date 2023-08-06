"""Abstract model classes to be implemented for network driver.
"""
import abc
from typing import Dict, List


class MESModel(abc.ABC):
    """Model of any node/edge."""

    @abc.abstractmethod
    def component_type(self):
        """Return component type (=table name)"""
        pass

    @abc.abstractmethod
    def name(self):
        """Name of the model, to be displayed in visualizations"""
        pass

    @abc.abstractmethod
    def values_as_dict(self):
        """All values of the model as dict"""
        pass

    def properties_as_dict(self):
        return self._network[self.component_type()].loc[self._id]

    @abc.abstractmethod
    def coords(self):
        pass


class RegulatableMESModel(MESModel):
    """Controllable regulatable MES model."""

    def __init__(self, id, network, edges=None) -> None:
        self._id = id
        self._network = network
        self._edges = edges

    def coords(self):
        node_properties = self.properties_as_dict()
        if "bus" in node_properties:
            if "bus_geodata" in self._network:
                return self._network.bus_geodata.loc[node_properties["bus"]]
        elif "junction" in node_properties:
            if "junction_geodata" in self._network:
                return self._network.junction_geodata.loc[node_properties["junction"]]
        return None

    @property
    def id(self):
        return self._id

    @property
    def network(self):
        return self._network

    @property
    def edges(self) -> Dict[str, List]:
        """([gas], [power], [heat])

        :return: dict
        :rtype: Dict
        """
        return self._edges

    @abc.abstractmethod
    def regulation_factor(self) -> float:
        """Getter for the regulation factor

        :return: the regulation factor used for the service control
        :rtype: float
        """
        pass

    @abc.abstractmethod
    def regulate(self, factor: float):
        """Setter for the regulation factor

        :param factor: new factor
        :type factor: float
        """
        pass
