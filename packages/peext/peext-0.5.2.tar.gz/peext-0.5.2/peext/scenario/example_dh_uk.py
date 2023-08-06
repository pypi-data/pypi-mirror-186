import pandapipes as ppipes
import pandapipes.plotting as plot
from matplotlib import pyplot as plt

BASE_HEAT_BAR = 5
BASE_HEAT_TEMP = 358.15
BASE_RETURN_TEMP = 323.15
BASE_ALPHA = 2.4 * 10**-5
BASE_DIAMETER = 0.658


def create_junctions(
    net_heat, pn_bar, tfluid_k, create_he=False, qext_w=None, name=None
):
    junc_feed_in = ppipes.create_junction(net_heat, pn_bar=pn_bar, tfluid_k=tfluid_k)
    junc_return = ppipes.create_junction(
        net_heat, pn_bar=pn_bar, tfluid_k=BASE_RETURN_TEMP
    )
    if create_he:
        ppipes.create_heat_exchanger(
            net_heat,
            from_junction=junc_return if qext_w < 0 else junc_feed_in,
            to_junction=junc_feed_in if qext_w < 0 else junc_return,
            diameter_m=BASE_DIAMETER,
            qext_w=qext_w,
            name=name,
        )

    return junc_feed_in, junc_return


def create_pipes(
    net_heat,
    first_junc_feed_in,
    first_junc_return,
    second_junc_feed_in,
    second_junc_return,
    length,
):
    v_feed = ppipes.create_junction(
        net_heat, pn_bar=BASE_HEAT_BAR, tfluid_k=BASE_HEAT_TEMP
    )
    ppipes.create_pump(net_heat, first_junc_feed_in, v_feed, std_type="P1")
    return ppipes.create_pipe_from_parameters(
        net_heat,
        from_junction=v_feed,
        to_junction=second_junc_feed_in,
        length_km=length,
        diameter_m=BASE_DIAMETER,
        alpha_w_per_m2k=BASE_ALPHA,
        text_k=BASE_HEAT_BAR,
    ), ppipes.create_pipe_from_parameters(
        net_heat,
        from_junction=first_junc_return,
        to_junction=second_junc_return,
        length_km=length,
        diameter_m=BASE_DIAMETER,
        alpha_w_per_m2k=BASE_ALPHA,
        text_k=BASE_HEAT_BAR,
    )


def heat_example_uk():
    net_heat = ppipes.create_empty_network("heat", fluid="water")
    junc_boiler_1_feed_in, junc_boiler_1_return = create_junctions(
        net_heat,
        BASE_HEAT_BAR,
        BASE_HEAT_TEMP,
        create_he=True,
        qext_w=-4.8 * 10**6,
        name="B1",
    )
    junc_load_1_feed_in, junc_load_1_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=1.0 * 10**6
    )
    create_pipes(
        net_heat,
        junc_boiler_1_feed_in,
        junc_boiler_1_return,
        junc_load_1_feed_in,
        junc_load_1_return,
        0.11,
    )
    junc_load_2_feed_in, junc_load_2_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=0.68 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_1_feed_in,
        junc_load_1_return,
        junc_load_2_feed_in,
        junc_load_2_return,
        0.105,
    )
    junc_load_3_feed_in, junc_load_3_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=3.97 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_2_feed_in,
        junc_load_2_return,
        junc_load_3_feed_in,
        junc_load_3_return,
        0.95,
    )
    junc_load_4_feed_in, junc_load_4_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=0.17 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_2_feed_in,
        junc_load_2_return,
        junc_load_4_feed_in,
        junc_load_4_return,
        0.11,
    )
    junc_load_5_feed_in, junc_load_5_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=1.12 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_4_feed_in,
        junc_load_4_return,
        junc_load_5_feed_in,
        junc_load_5_return,
        0.06,
    )
    junc_load_6_feed_in, junc_load_6_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=1.15 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_4_feed_in,
        junc_load_4_return,
        junc_load_6_feed_in,
        junc_load_6_return,
        0.17,
    )
    junc_load_7_feed_in, junc_load_7_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=3.90 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_6_feed_in,
        junc_load_6_return,
        junc_load_7_feed_in,
        junc_load_7_return,
        0.04,
    )
    create_pipes(
        net_heat,
        junc_load_6_feed_in,
        junc_load_6_return,
        junc_load_7_feed_in,
        junc_load_7_return,
        0.04,
    )
    junc_load_8_feed_in, junc_load_8_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=0.87 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_7_feed_in,
        junc_load_7_return,
        junc_load_8_feed_in,
        junc_load_8_return,
        0.14,
    )
    junc_load_9_feed_in, junc_load_9_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=0.89 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_8_feed_in,
        junc_load_8_return,
        junc_load_9_feed_in,
        junc_load_9_return,
        0.12,
    )
    junc_boiler_2_feed_in, junc_boiler_2_return = create_junctions(
        net_heat,
        BASE_HEAT_BAR,
        BASE_HEAT_TEMP,
        create_he=True,
        qext_w=-16.23 * 10**6,
        name="B2",
    )
    create_pipes(
        net_heat,
        junc_load_9_feed_in,
        junc_load_9_return,
        junc_boiler_2_feed_in,
        junc_boiler_2_return,
        0.1,
    )
    junc_load_10_feed_in, junc_load_10_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=0.28 * 10**6
    )
    create_pipes(
        net_heat,
        junc_boiler_2_feed_in,
        junc_boiler_2_return,
        junc_load_10_feed_in,
        junc_load_10_return,
        0.03,
    )
    junc_load_11_feed_in, junc_load_11_return = create_junctions(
        net_heat, BASE_HEAT_BAR, BASE_HEAT_TEMP, create_he=True, qext_w=2.50 * 10**6
    )
    create_pipes(
        net_heat,
        junc_load_8_feed_in,
        junc_load_8_return,
        junc_load_11_feed_in,
        junc_load_11_return,
        0.08,
    )
    ppipes.create_ext_grid(
        net_heat,
        junction=junc_boiler_1_feed_in,
        p_bar=BASE_HEAT_BAR,
        t_k=BASE_HEAT_TEMP,
        name="Grid Connection Heating Feed In",
    )
    return net_heat


if __name__ == "__main__":
    heat_net = heat_example_uk()
    plot.simple_plot(
        heat_net,
        respect_valves=True,
        show_plot=False,
        plot_sinks=True,
        plot_sources=True,
        heat_exchanger_size=0.5,
        heat_exchanger_color="red",
    )
    plt.savefig("example_heating_uk.pdf")
    ppipes.pipeflow(heat_net, mode="all")
    print(heat_net.res_heat_exchanger)
