from peext.edge import PipeEdge
from peext.node import CouplingPoint
import peext.scenario.network as ps
import pandapipes.multinet.control as ppmc
import peext.network as network


def test_feasability_loss():
    mn = ps.create_small_test_multinet()

    # pandapipes error makes this test impossible right now
    ppmc.run_control_multinet.run_control(mn, max_iter=30, mode="all")

    me_network = network.from_panda_multinet(mn)

    for edge in me_network.edges:
        if type(edge) == PipeEdge:
            assert len(edge.loss_perc()) == 2
            assert edge.loss_perc()[0] < 0.5 and edge.loss_perc()[0] >= 0
            assert edge.loss_perc()[1] < 0.5 and edge.loss_perc()[1] >= 0
        else:
            assert edge.loss_perc() < 0.5 and edge.loss_perc() >= 0

    for node in me_network.nodes:
        if isinstance(node, CouplingPoint):
            assert node.loss_perc() < 0.5 and edge.loss_perc() >= 0
