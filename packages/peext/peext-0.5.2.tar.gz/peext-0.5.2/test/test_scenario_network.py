import simbench

import peext.scenario.network as ps
import pandapipes.multinet.control as ppmc


def test_convergence_simple_network():
    mn = ps.create_small_test_multinet()

    # pandapipes error makes this test impossible right now
    ppmc.run_control_multinet.run_control(mn, max_iter=30, mode="all")


def test_convergence_coupled_district_network():
    multinet = ps.create_super_district_coupled_network(0.7)

    # pandapipes error makes this test impossible right now
    # ppmc.run_control_multinet.run_control(multinet, max_iter = 30, mode='all')


def test_generate_network_based_on_power():
    pp_net = simbench.get_simbench_net("1-MV-urban--1-no_sw")

    mn = ps.generate_multi_network_based_on_power_net(pp_net, 1 / 2, 1 / 3)

    assert mn is not None


def test_generate_network_based_on_power_conv():
    mn = ps.generate_multi_network_based_on_simbench("1-MV-urban--1-no_sw", 1, 1)

    assert mn is not None
