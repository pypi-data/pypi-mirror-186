# SPDX-FileCopyrightText: 2022 Contributors to the Power Grid Model project <dynamic.grid.calculation@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0
"""
Panda Power Converter
"""
from functools import lru_cache
from typing import Dict, Mapping, MutableMapping, Optional, Tuple, Union

import numpy as np
import pandas as pd
from power_grid_model import Branch3Side, BranchSide, LoadGenType, initialize_array
from power_grid_model.data_types import Dataset

from power_grid_model_io.converters.base_converter import BaseConverter
from power_grid_model_io.data_types import ExtraInfoLookup
from power_grid_model_io.functions import get_winding
from power_grid_model_io.utils.regex import TRAFO3_CONNECTION_RE, TRAFO_CONNECTION_RE

StdTypes = Mapping[str, Mapping[str, Mapping[str, Union[float, int, str]]]]
PandaPowerData = MutableMapping[str, pd.DataFrame]


class PandaPowerConverter(BaseConverter[PandaPowerData]):
    """
    Panda Power Converter
    """

    __slots__ = ("_std_types", "pp_input_data", "pgm_input_data", "idx", "idx_lookup", "next_idx", "system_frequency")

    def __init__(self, std_types: Optional[StdTypes] = None, system_frequency: float = 50.0):
        """
        Prepare some member variables and optionally load "std_types"
        Args:
            std_types: standard type database of possible Line, Transformer and Three Winding Transformer types
            system_frequency: fundamental frequency of the alternating current and voltage in the Network measured in Hz
        """
        super().__init__(source=None, destination=None)
        self._std_types: StdTypes = std_types if std_types is not None else {}
        self.system_frequency: float = system_frequency
        self.pp_input_data: PandaPowerData = {}
        self.pgm_input_data: Dataset = {}
        self.idx: Dict[Tuple[str, Optional[str]], pd.Series] = {}
        self.idx_lookup: Dict[Tuple[str, Optional[str]], pd.Series] = {}
        self.next_idx = 0

    def _parse_data(
        self, data: PandaPowerData, data_type: str, extra_info: Optional[ExtraInfoLookup] = None
    ) -> Dataset:
        """
        Set up for conversion from PandaPower to power-grid-model

        Args:
            data: PandaPowerData, i.e. a dictionary with the components as keys and pd.DataFrames as values, with
            attribute names as columns and their values in the table
            data_type: power-grid-model data type, i.e. "input" or "update"
            extra_info: an optional dictionary where extra component info (that can't be specified in
            power-grid-model data) can be specified

        Returns:
            Converted power-grid-model data
        """

        # Clear pgm data
        self.pgm_input_data = {}
        self.idx_lookup = {}
        self.next_idx = 0

        # Set pandas data
        self.pp_input_data = data

        # Convert
        if data_type == "input":
            self._create_input_data()
        else:
            raise ValueError(f"Data type: '{data_type}' is not implemented")

        # Construct extra_info
        if extra_info is not None:
            self._fill_extra_info(extra_info=extra_info)

        return self.pgm_input_data

    def _serialize_data(self, data: Dataset, extra_info: Optional[ExtraInfoLookup]) -> PandaPowerData:
        """
        Set up for conversion from power-grid-model to PandaPower
        """
        raise NotImplementedError()

    def _create_input_data(self):
        """
        Performs the conversion from PandaPower to power-grid-model by calling individual conversion functions
        """
        self._create_pgm_input_nodes()
        self._create_pgm_input_lines()
        self._create_pgm_input_sources()
        self._create_pgm_input_sym_loads()
        self._create_pgm_input_asym_loads()
        self._create_pgm_input_shunts()
        self._create_pgm_input_transformers()
        self._create_pgm_input_sym_gens()
        self._create_pgm_input_asym_gens()
        self._create_pgm_input_three_winding_transformers()
        self._create_pgm_input_links()
        self._create_pgm_input_storage()
        self._create_pgm_input_impedance()
        self._create_pgm_input_ward()
        self._create_pgm_input_xward()
        self._create_pgm_input_motor()

    def _fill_extra_info(self, extra_info: ExtraInfoLookup):
        for (pp_table, name), indices in self.idx_lookup.items():
            for pgm_id, pp_idx in zip(indices.index, indices):
                if name:
                    extra_info[pgm_id] = {"id_reference": {"table": pp_table, "name": name, "index": pp_idx}}
                else:
                    extra_info[pgm_id] = {"id_reference": {"table": pp_table, "index": pp_idx}}

    def _create_pgm_input_nodes(self):
        """
        This function converts a Bus Dataframe of PandaPower to a power-grid-model Node input array.

        Returns:
            a power-grid-model structured array for the Node component
        """
        assert "node" not in self.pgm_input_data

        pp_busses = self.pp_input_data["bus"]

        if pp_busses.empty:
            return

        pgm_nodes = initialize_array(data_type="input", component_type="node", shape=len(pp_busses))
        pgm_nodes["id"] = self._generate_ids("bus", pp_busses.index)
        pgm_nodes["u_rated"] = self._get_pp_attr("bus", "vn_kv") * 1e3

        self.pgm_input_data["node"] = pgm_nodes

    def _create_pgm_input_lines(self):
        """
        This function converts a Line Dataframe of PandaPower to a power-grid-model Line input array.

        Returns:
            a power-grid-model structured array for the Line component
        """
        assert "line" not in self.pgm_input_data

        pp_lines = self.pp_input_data["line"]

        if pp_lines.empty:
            return

        switch_states = self.get_switch_states("line")
        in_service = self._get_pp_attr("line", "in_service", True)
        length_km = self._get_pp_attr("line", "length_km")
        parallel = self._get_pp_attr("line", "parallel", 1)
        c_nf_per_km = self._get_pp_attr("line", "c_nf_per_km")
        multiplier = length_km / parallel

        pgm_lines = initialize_array(data_type="input", component_type="line", shape=len(pp_lines))
        pgm_lines["id"] = self._generate_ids("line", pp_lines.index)
        pgm_lines["from_node"] = self._get_pgm_ids("bus", pp_lines["from_bus"])
        pgm_lines["from_status"] = in_service & switch_states["from"]
        pgm_lines["to_node"] = self._get_pgm_ids("bus", pp_lines["to_bus"])
        pgm_lines["to_status"] = in_service & switch_states["to"]
        pgm_lines["r1"] = self._get_pp_attr("line", "r_ohm_per_km") * multiplier
        pgm_lines["x1"] = self._get_pp_attr("line", "x_ohm_per_km") * multiplier
        pgm_lines["c1"] = c_nf_per_km * length_km * parallel * 1e-9
        # The formula for tan1 = R_1 / Xc_1 = (g * 1e-6) / (2 * pi * f * c * 1e-9) = g / (2 * pi * f * c * 1e-3)
        pgm_lines["tan1"] = (
            self._get_pp_attr("line", "g_us_per_km", 0) / c_nf_per_km / (2 * np.pi * self.system_frequency * 1e-3)
        )
        pgm_lines["i_n"] = (self._get_pp_attr("line", "max_i_ka") * 1e3) * self._get_pp_attr("line", "df", 1) * parallel

        self.pgm_input_data["line"] = pgm_lines

    def _create_pgm_input_sources(self):
        """
        This function converts External Grid Dataframe of PandaPower to a power-grid-model Source input array.

        Returns:
            a power-grid-model structured array for the Source component
        """
        assert "source" not in self.pgm_input_data

        pp_ext_grid = self.pp_input_data["ext_grid"]

        if pp_ext_grid.empty:
            return

        pgm_sources = initialize_array(data_type="input", component_type="source", shape=len(pp_ext_grid))
        pgm_sources["id"] = self._generate_ids("ext_grid", pp_ext_grid.index)
        pgm_sources["node"] = self._get_pgm_ids("bus", pp_ext_grid["bus"])
        pgm_sources["status"] = self._get_pp_attr("ext_grid", "in_service", True)
        pgm_sources["u_ref"] = self._get_pp_attr("ext_grid", "vm_pu", 1.0)
        pgm_sources["rx_ratio"] = self._get_pp_attr("ext_grid", "rx_max", np.nan)
        pgm_sources["u_ref_angle"] = self._get_pp_attr("ext_grid", "va_degree", 0.0) * (np.pi / 180)
        pgm_sources["sk"] = self._get_pp_attr("ext_grid", "s_sc_max_mva", np.nan) * 1e6

        self.pgm_input_data["source"] = pgm_sources

    def _create_pgm_input_shunts(self):
        """
        This function converts a Shunt Dataframe of PandaPower to a power-grid-model Shunt input array.

        Returns:
            a power-grid-model structured array for the Shunt component
        """
        assert "shunt" not in self.pgm_input_data

        pp_shunts = self.pp_input_data["shunt"]

        if pp_shunts.empty:
            return

        vn_kv = self._get_pp_attr("shunt", "vn_kv", None)
        vn_kv_2 = vn_kv * vn_kv

        step = self._get_pp_attr("shunt", "step", 1)

        pgm_shunts = initialize_array(data_type="input", component_type="shunt", shape=len(pp_shunts))
        pgm_shunts["id"] = self._generate_ids("shunt", pp_shunts.index)
        pgm_shunts["node"] = self._get_pgm_ids("bus", pp_shunts["bus"])
        pgm_shunts["status"] = self._get_pp_attr("shunt", "in_service", 1)
        pgm_shunts["g1"] = self._get_pp_attr("shunt", "p_mw") * step / vn_kv_2
        pgm_shunts["b1"] = -(self._get_pp_attr("shunt", "q_mvar") * step) / vn_kv_2

        self.pgm_input_data["shunt"] = pgm_shunts

    def _create_pgm_input_sym_gens(self):
        """
        This function converts a Static Generator Dataframe of PandaPower to a power-grid-model
        Symmetrical Generator input array.

        Returns:
            a power-grid-model structured array for the Symmetrical Generator component
        """
        assert "sym_gen" not in self.pgm_input_data

        pp_sgens = self.pp_input_data["sgen"]

        if pp_sgens.empty:
            return

        scaling = self._get_pp_attr("sgen", "scaling", 1.0)

        pgm_sym_gens = initialize_array(data_type="input", component_type="sym_gen", shape=len(pp_sgens))
        pgm_sym_gens["id"] = self._generate_ids("sgen", pp_sgens.index)
        pgm_sym_gens["node"] = self._get_pgm_ids("bus", pp_sgens["bus"])
        pgm_sym_gens["status"] = self._get_pp_attr("sgen", "in_service", True)
        pgm_sym_gens["p_specified"] = self._get_pp_attr("sgen", "p_mw") * (1e6 * scaling)
        pgm_sym_gens["q_specified"] = self._get_pp_attr("sgen", "q_mvar", 0.0) * (1e6 * scaling)
        pgm_sym_gens["type"] = LoadGenType.const_power

        self.pgm_input_data["sym_gen"] = pgm_sym_gens

    def _create_pgm_input_asym_gens(self):  # pragma: no cover
        """
        This function converts an Asymmetric Static Generator Dataframe of PandaPower to a power-grid-model
        Asymmetrical Generator input array.

        Returns:
            a power-grid-model structured array for the Asymmetrical Generator component
        """
        # TODO: create unit tests for asym_gen conversion
        assert "asym_gen" not in self.pgm_input_data

        pp_asym_gens = self.pp_input_data["asymmetric_sgen"]

        if pp_asym_gens.empty:
            return

        scaling = self._get_pp_attr("asymmetric_sgen", "scaling")
        multiplier = 1e6 * scaling

        pgm_asym_gens = initialize_array(data_type="input", component_type="asym_gen", shape=len(pp_asym_gens))
        pgm_asym_gens["id"] = self._generate_ids("asymmetric_sgen", pp_asym_gens.index)
        pgm_asym_gens["node"] = self._get_pgm_ids("bus", pp_asym_gens["bus"])
        pgm_asym_gens["status"] = self._get_pp_attr("asymmetric_sgen", "in_service")
        pgm_asym_gens["p_specified"] = (
            np.array(
                self._get_pp_attr("asymmetric_sgen", "p_a_mw"),
                self._get_pp_attr("asymmetric_sgen", "p_b_mw"),
                self._get_pp_attr("asymmetric_sgen", "p_c_mw"),
            )
            * multiplier
        )
        pgm_asym_gens["q_specified"] = (
            np.array(
                self._get_pp_attr("asymmetric_sgen", "q_a_mvar"),
                self._get_pp_attr("asymmetric_sgen", "q_b_mvar"),
                self._get_pp_attr("asymmetric_sgen", "q_c_mvar"),
            )
            * multiplier
        )
        pgm_asym_gens["type"] = LoadGenType.const_power

        self.pgm_input_data["asym_gen"] = pgm_asym_gens

    def _create_pgm_input_sym_loads(self):
        """
        This function converts a Load Dataframe of PandaPower to a power-grid-model
        Symmetrical Load input array. For one load in PandaPower there are three loads in
        power-grid-model created.

        Returns:
            a power-grid-model structured array for the Symmetrical Load component
        """
        assert "sym_load" not in self.pgm_input_data

        pp_loads = self.pp_input_data["load"]

        if pp_loads.empty:
            return

        scaling = self._get_pp_attr("load", "scaling", 1.0)
        in_service = self._get_pp_attr("load", "in_service", True)
        p_mw = self._get_pp_attr("load", "p_mw", 0.0)
        q_mvar = self._get_pp_attr("load", "q_mvar", 0.0)

        n_loads = len(pp_loads)

        pgm_sym_loads = initialize_array(data_type="input", component_type="sym_load", shape=3 * n_loads)

        const_i_multiplier = self._get_pp_attr("load", "const_i_percent", 0) * scaling * (1e-2 * 1e6)
        const_z_multiplier = self._get_pp_attr("load", "const_z_percent", 0) * scaling * (1e-2 * 1e6)
        const_p_multiplier = (1e6 - const_i_multiplier - const_z_multiplier) * scaling

        pgm_sym_loads["id"][:n_loads] = self._generate_ids("load", pp_loads.index, name="const_power")
        pgm_sym_loads["node"][:n_loads] = self._get_pgm_ids("bus", pp_loads["bus"])
        pgm_sym_loads["status"][:n_loads] = in_service
        pgm_sym_loads["type"][:n_loads] = LoadGenType.const_power
        pgm_sym_loads["p_specified"][:n_loads] = const_p_multiplier * p_mw
        pgm_sym_loads["q_specified"][:n_loads] = const_p_multiplier * q_mvar

        pgm_sym_loads["id"][n_loads : 2 * n_loads] = self._generate_ids("load", pp_loads.index, name="const_impedance")
        pgm_sym_loads["node"][n_loads : 2 * n_loads] = self._get_pgm_ids("bus", pp_loads["bus"])
        pgm_sym_loads["status"][n_loads : 2 * n_loads] = in_service
        pgm_sym_loads["type"][n_loads : 2 * n_loads] = LoadGenType.const_impedance
        pgm_sym_loads["p_specified"][n_loads : 2 * n_loads] = const_z_multiplier * p_mw
        pgm_sym_loads["q_specified"][n_loads : 2 * n_loads] = const_z_multiplier * q_mvar

        pgm_sym_loads["id"][-n_loads:] = self._generate_ids("load", pp_loads.index, name="const_current")
        pgm_sym_loads["node"][-n_loads:] = self._get_pgm_ids("bus", pp_loads["bus"])
        pgm_sym_loads["status"][-n_loads:] = in_service
        pgm_sym_loads["type"][-n_loads:] = LoadGenType.const_current
        pgm_sym_loads["p_specified"][-n_loads:] = const_i_multiplier * p_mw
        pgm_sym_loads["q_specified"][-n_loads:] = const_i_multiplier * q_mvar

        self.pgm_input_data["sym_load"] = pgm_sym_loads

    def _create_pgm_input_asym_loads(self):  # pragma: no cover
        """
        This function converts an asymmetric_load Dataframe of PandaPower to a power-grid-model asym_load input array.

        Returns:
            a power-grid-model structured array for the asym_load component
        """
        # TODO: create unit tests for asym_load conversion
        assert "asym_load" not in self.pgm_input_data

        pp_asym_loads = self.pp_input_data["asymmetric_load"]

        if pp_asym_loads.empty:
            return

        scaling = self._get_pp_attr("asymmetric_load", "scaling")
        multiplier = 1e6 * scaling

        pgm_asym_loads = initialize_array(data_type="input", component_type="asym_load", shape=len(pp_asym_loads))
        pgm_asym_loads["id"] = self._generate_ids("asymmetric_load", pp_asym_loads.index)
        pgm_asym_loads["node"] = self._get_pgm_ids("bus", pp_asym_loads["bus"])
        pgm_asym_loads["status"] = self._get_pp_attr("asymmetric_load", "in_service")
        pgm_asym_loads["p_specified"] = (
            np.array(
                self._get_pp_attr("asymmetric_load", "p_a_mw"),
                self._get_pp_attr("asymmetric_load", "p_b_mw"),
                self._get_pp_attr("asymmetric_load", "p_c_mw"),
            )
            * multiplier
        )
        pgm_asym_loads["q_specified"] = (
            np.array(
                self._get_pp_attr("asymmetric_load", "q_a_mvar"),
                self._get_pp_attr("asymmetric_load", "q_b_mvar"),
                self._get_pp_attr("asymmetric_load", "q_c_mvar"),
            )
            * multiplier
        )
        pgm_asym_loads["type"] = LoadGenType.const_power

        self.pgm_input_data["asym_load"] = pgm_asym_loads

    def _create_pgm_input_transformers(self):
        """
        This function converts a Transformer Dataframe of PandaPower to a power-grid-model
        Transformer input array.

        Returns:
            a power-grid-model structured array for the Transformer component
        """
        assert "transformer" not in self.pgm_input_data

        pp_trafo = self.pp_input_data["trafo"]

        if pp_trafo.empty:
            return

        # Check for unsupported pandapower features
        if "tap_dependent_impedance" in pp_trafo.columns and any(pp_trafo["tap_dependent_impedance"]):
            raise RuntimeError("Tap dependent impedance is not supported in Power Grid Model")

        in_service = self._get_pp_attr("trafo", "in_service", True)
        parallel = self._get_pp_attr("trafo", "parallel", 1)
        sn_mva = self._get_pp_attr("trafo", "sn_mva")
        switch_states = self.get_switch_states("trafo")
        winding_types = self.get_trafo_winding_types()

        pgm_transformers = initialize_array(data_type="input", component_type="transformer", shape=len(pp_trafo))
        pgm_transformers["id"] = self._generate_ids("trafo", pp_trafo.index)
        pgm_transformers["from_node"] = self._get_pgm_ids("bus", pp_trafo["hv_bus"])
        pgm_transformers["from_status"] = in_service & switch_states["from"]
        pgm_transformers["to_node"] = self._get_pgm_ids("bus", pp_trafo["lv_bus"])
        pgm_transformers["to_status"] = in_service & switch_states["to"]
        pgm_transformers["u1"] = self._get_pp_attr("trafo", "vn_hv_kv") * 1e3
        pgm_transformers["u2"] = self._get_pp_attr("trafo", "vn_lv_kv") * 1e3
        pgm_transformers["sn"] = sn_mva * parallel * 1e6
        pgm_transformers["uk"] = self._get_pp_attr("trafo", "vk_percent") * 1e-2
        pgm_transformers["pk"] = self._get_pp_attr("trafo", "vkr_percent") * sn_mva * parallel * (1e6 * 1e-2)
        pgm_transformers["i0"] = self._get_pp_attr("trafo", "i0_percent") * 1e-2
        pgm_transformers["p0"] = self._get_pp_attr("trafo", "pfe_kw") * parallel * 1e3
        pgm_transformers["winding_from"] = winding_types["winding_from"]
        pgm_transformers["winding_to"] = winding_types["winding_to"]
        pgm_transformers["clock"] = round(self._get_pp_attr("trafo", "shift_degree", 0.0) / 30) % 12
        pgm_transformers["tap_pos"] = self._get_pp_attr("trafo", "tap_pos", np.nan)
        pgm_transformers["tap_side"] = self._get_transformer_tap_side(pp_trafo["tap_side"])
        pgm_transformers["tap_min"] = self._get_pp_attr("trafo", "tap_min", np.nan)
        pgm_transformers["tap_max"] = self._get_pp_attr("trafo", "tap_max", np.nan)
        pgm_transformers["tap_nom"] = self._get_pp_attr("trafo", "tap_neutral", np.nan)
        pgm_transformers["tap_size"] = self._get_tap_size(pp_trafo)

        self.pgm_input_data["transformer"] = pgm_transformers

    def _create_pgm_input_three_winding_transformers(self):
        """
        This function converts a Three Winding Transformer Dataframe of PandaPower to a power-grid-model
        Three Winding Transformer input array.

        Returns:
            a power-grid-model structured array for the Three Winding Transformer component
        """
        assert "three_winding_transformer" not in self.pgm_input_data

        pp_trafo3w = self.pp_input_data["trafo3w"]

        if pp_trafo3w.empty:
            return

        # Check for unsupported pandapower features
        if "tap_dependent_impedance" in pp_trafo3w.columns and any(pp_trafo3w["tap_dependent_impedance"]):
            raise RuntimeError("Tap dependent impedance is not supported in Power Grid Model")  # pragma: no cover
        if "tap_at_star_point" in pp_trafo3w.columns and any(pp_trafo3w["tap_at_star_point"]):
            raise RuntimeError("Tap at star point is not supported in Power Grid Model")

        sn_hv_mva = self._get_pp_attr("trafo3w", "sn_hv_mva")
        sn_mv_mva = self._get_pp_attr("trafo3w", "sn_mv_mva")
        sn_lv_mva = self._get_pp_attr("trafo3w", "sn_lv_mva")
        in_service = self._get_pp_attr("trafo3w", "in_service", True)

        switch_states = self.get_trafo3w_switch_states(pp_trafo3w)
        winding_type = self.get_trafo3w_winding_types()

        pgm_3wtransformers = initialize_array(
            data_type="input", component_type="three_winding_transformer", shape=len(pp_trafo3w)
        )
        pgm_3wtransformers["id"] = self._generate_ids("trafo3w", pp_trafo3w.index)
        pgm_3wtransformers["node_1"] = self._get_pgm_ids("bus", pp_trafo3w["hv_bus"])
        pgm_3wtransformers["node_2"] = self._get_pgm_ids("bus", pp_trafo3w["mv_bus"])
        pgm_3wtransformers["node_3"] = self._get_pgm_ids("bus", pp_trafo3w["lv_bus"])
        pgm_3wtransformers["status_1"] = in_service & switch_states.iloc[0, :]
        pgm_3wtransformers["status_2"] = in_service & switch_states.iloc[1, :]
        pgm_3wtransformers["status_3"] = in_service & switch_states.iloc[2, :]
        pgm_3wtransformers["u1"] = self._get_pp_attr("trafo3w", "vn_hv_kv") * 1e3
        pgm_3wtransformers["u2"] = self._get_pp_attr("trafo3w", "vn_mv_kv") * 1e3
        pgm_3wtransformers["u3"] = self._get_pp_attr("trafo3w", "vn_lv_kv") * 1e3
        pgm_3wtransformers["sn_1"] = sn_hv_mva * 1e6
        pgm_3wtransformers["sn_2"] = sn_mv_mva * 1e6
        pgm_3wtransformers["sn_3"] = sn_lv_mva * 1e6
        pgm_3wtransformers["uk_12"] = self._get_pp_attr("trafo3w", "vk_hv_percent") * 1e-2
        pgm_3wtransformers["uk_13"] = self._get_pp_attr("trafo3w", "vk_lv_percent") * 1e-2
        pgm_3wtransformers["uk_23"] = self._get_pp_attr("trafo3w", "vk_mv_percent") * 1e-2

        pgm_3wtransformers["pk_12"] = (
            self._get_pp_attr("trafo3w", "vkr_hv_percent") * np.minimum(sn_hv_mva, sn_mv_mva) * (1e-2 * 1e6)
        )

        pgm_3wtransformers["pk_13"] = (
            self._get_pp_attr("trafo3w", "vkr_lv_percent") * np.minimum(sn_hv_mva, sn_lv_mva) * (1e-2 * 1e6)
        )

        pgm_3wtransformers["pk_23"] = (
            self._get_pp_attr("trafo3w", "vkr_mv_percent") * np.minimum(sn_mv_mva, sn_lv_mva) * (1e-2 * 1e6)
        )

        pgm_3wtransformers["i0"] = self._get_pp_attr("trafo3w", "i0_percent") * 1e-2
        pgm_3wtransformers["p0"] = self._get_pp_attr("trafo3w", "pfe_kw") * 1e3
        pgm_3wtransformers["winding_1"] = winding_type["winding_1"]
        pgm_3wtransformers["winding_2"] = winding_type["winding_2"]
        pgm_3wtransformers["winding_3"] = winding_type["winding_3"]
        pgm_3wtransformers["clock_12"] = round(self._get_pp_attr("trafo3w", "shift_mv_degree", 0.0) / 30.0) % 12
        pgm_3wtransformers["clock_13"] = round(self._get_pp_attr("trafo3w", "shift_lv_degree", 0.0) / 30.0) % 12
        pgm_3wtransformers["tap_pos"] = self._get_pp_attr("trafo3w", "tap_pos", np.nan)
        pgm_3wtransformers["tap_side"] = self._get_3wtransformer_tap_side(
            pd.Series(self._get_pp_attr("trafo3w", "tap_side", None))
        )
        pgm_3wtransformers["tap_min"] = self._get_pp_attr("trafo3w", "tap_min", np.nan)
        pgm_3wtransformers["tap_max"] = self._get_pp_attr("trafo3w", "tap_max", np.nan)
        pgm_3wtransformers["tap_nom"] = self._get_pp_attr("trafo3w", "tap_neutral", np.nan)
        pgm_3wtransformers["tap_size"] = self._get_3wtransformer_tap_size(pp_trafo3w)

        self.pgm_input_data["three_winding_transformer"] = pgm_3wtransformers

    def _create_pgm_input_links(self):
        """
        This function takes a Switch Dataframe of PandaPower, extracts the Switches which have Bus to Bus
        connection and converts them to a power-grid-model Link input array.

        Returns:
            a power-grid-model structured array for the Link component
        """
        assert "link" not in self.pgm_input_data

        pp_switches = self.pp_input_data["switch"]

        if pp_switches.empty:
            return

        # This should take all the switches which are b2b
        pp_switches = pp_switches[self._get_pp_attr("switch", "et") == "b"]

        self.pp_input_data["switch_b2b"] = pp_switches

        closed = self._get_pp_attr("switch_b2b", "closed", True)

        pgm_links = initialize_array(data_type="input", component_type="link", shape=len(pp_switches))
        pgm_links["id"] = self._generate_ids("switch", pp_switches.index, name="bus_to_bus")
        pgm_links["from_node"] = self._get_pgm_ids("bus", pp_switches["bus"])
        pgm_links["to_node"] = self._get_pgm_ids("bus", pp_switches["element"])
        pgm_links["from_status"] = closed
        pgm_links["to_status"] = closed

        self.pgm_input_data["link"] = pgm_links

    def _create_pgm_input_storage(self):  # pragma: no cover
        # TODO: create unit tests for the function
        pp_storage = self.pp_input_data["storage"]

        if pp_storage.empty:
            return

        raise NotImplementedError("Storage is not implemented yet!")

    def _create_pgm_input_impedance(self):  # pragma: no cover
        # TODO: create unit tests for the function
        pp_impedance = self.pp_input_data["impedance"]

        if pp_impedance.empty:
            return

        raise NotImplementedError("Impedance is not implemented yet!")

    def _create_pgm_input_ward(self):  # pragma: no cover
        # TODO: create unit tests for the function
        pp_wards = self.pp_input_data["ward"]

        if pp_wards.empty:
            return

        raise NotImplementedError("Ward is not implemented yet!")

    def _create_pgm_input_xward(self):  # pragma: no cover
        # TODO: create unit tests for the function
        pp_xwards = self.pp_input_data["xward"]

        if pp_xwards.empty:
            return

        raise NotImplementedError("Extended Ward is not implemented yet!")

    def _create_pgm_input_motor(self):  # pragma: no cover
        # TODO: create unit tests for the function
        pp_motors = self.pp_input_data["motor"]

        if pp_motors.empty:
            return

        raise NotImplementedError("Motor is not implemented yet!")

    def _generate_ids(self, pp_table: str, pp_idx: pd.Index, name: Optional[str] = None) -> np.arange:
        """
        Generate numerical power-grid-model IDs for a PandaPower component

        Args:
            pp_table: Table name (e.g. "bus")
            pp_idx: PandaPower component identifier

        Returns:
            the generated IDs
        """
        key = (pp_table, name)
        assert key not in self.idx_lookup
        n_objects = len(pp_idx)
        pgm_idx = np.arange(start=self.next_idx, stop=self.next_idx + n_objects, dtype=np.int32)
        self.idx[key] = pd.Series(pgm_idx, index=pp_idx)
        self.idx_lookup[key] = pd.Series(pp_idx, index=pgm_idx)
        self.next_idx += n_objects
        return pgm_idx

    def _get_pgm_ids(self, pp_table: str, pp_idx: Optional[pd.Series] = None, name: Optional[str] = None) -> pd.Series:
        """
        Get numerical power-grid-model IDs for a PandaPower component

        Args:
            pp_table: Table name (e.g. "bus")
            pp_idx: PandaPower component identifier

        Returns:
            the power-grid-model IDs if they were previously generated
        """
        key = (pp_table, name)
        if key not in self.idx:
            raise KeyError(f"No indexes have been created for '{pp_table}' (name={name})!")
        if pp_idx is None:
            return self.idx[key]
        return self.idx[key][pp_idx]

    @staticmethod
    def _get_tap_size(pp_trafo: pd.DataFrame) -> np.ndarray:
        """
        Calculate the "tap size" of Transformers

        Args:
            pp_trafo: PandaPower dataframe with information about the Transformers in
            the Network (e.g. "hv_bus", "i0_percent")

        Returns:
            the "tap size" of Transformers
        """
        tap_side_hv = np.array(pp_trafo["tap_side"] == "hv")
        tap_side_lv = np.array(pp_trafo["tap_side"] == "lv")
        tap_step_multiplier = pp_trafo["tap_step_percent"] * (1e-2 * 1e3)

        tap_size = np.empty(shape=len(pp_trafo), dtype=np.float64)
        tap_size[tap_side_hv] = tap_step_multiplier[tap_side_hv] * pp_trafo["vn_hv_kv"][tap_side_hv]
        tap_size[tap_side_lv] = tap_step_multiplier[tap_side_lv] * pp_trafo["vn_lv_kv"][tap_side_lv]

        return tap_size

    @staticmethod
    def _get_transformer_tap_side(tap_side: np.ndarray) -> np.ndarray:
        """
        Get the enumerated "tap side" of Transformers

        Args:
            tap_side: PandaPower series with information about the "tap_side" attribute

        Returns:
            the enumerated "tap side"
        """
        new_tap_side = np.array(tap_side)
        new_tap_side[new_tap_side == "hv"] = BranchSide.from_side
        new_tap_side[new_tap_side == "lv"] = BranchSide.to_side

        return new_tap_side

    @staticmethod
    def _get_3wtransformer_tap_side(tap_side: pd.Series) -> np.ndarray:
        """
        Get the enumerated "tap side" of Three Winding Transformers

        Args:
            tap_side: PandaPower series with information about the "tap_side" attribute

        Returns:
            the enumerated "tap side"
        """
        new_tap_side = np.array(tap_side)
        new_tap_side[new_tap_side == "hv"] = Branch3Side.side_1
        new_tap_side[new_tap_side == "mv"] = Branch3Side.side_2
        new_tap_side[new_tap_side == "lv"] = Branch3Side.side_3

        return new_tap_side

    @staticmethod
    def _get_3wtransformer_tap_size(pp_3wtrafo: pd.DataFrame) -> np.ndarray:
        """
        Calculate the "tap size" of Three Winding Transformers

        Args:
            pp_3wtrafo: PandaPower dataframe with information about the Three Winding Transformers in
            the Network (e.g. "hv_bus", "i0_percent")

        Returns:
            the "tap size" of Three Winding Transformers
        """
        tap_side_hv = np.array(pp_3wtrafo["tap_side"] == "hv")
        tap_side_mv = np.array(pp_3wtrafo["tap_side"] == "mv")
        tap_side_lv = np.array(pp_3wtrafo["tap_side"] == "lv")

        tap_step_multiplier = pp_3wtrafo["tap_step_percent"] * (1e-2 * 1e3)

        tap_size = np.empty(shape=len(pp_3wtrafo), dtype=np.float64)
        tap_size[tap_side_hv] = tap_step_multiplier[tap_side_hv] * pp_3wtrafo["vn_hv_kv"][tap_side_hv]
        tap_size[tap_side_mv] = tap_step_multiplier[tap_side_mv] * pp_3wtrafo["vn_mv_kv"][tap_side_mv]
        tap_size[tap_side_lv] = tap_step_multiplier[tap_side_lv] * pp_3wtrafo["vn_lv_kv"][tap_side_lv]

        return tap_size

    @staticmethod
    def get_individual_switch_states(component: pd.DataFrame, switches: pd.DataFrame, bus: str) -> pd.Series:
        """
        Get the state of an individual switch. Can be open or closed.

        Args:
            component: PandaPower dataframe with information about the component that is connected to the switch.
            Can be a Line dataframe, Transformer dataframe or Three Winding Transformer dataframe.

            switches: PandaPower dataframe with information about the switches, has
            such attributes as: "element", "bus", "closed"

            bus: name of the bus attribute that the component connects to (e.g "hv_bus", "from_bus", "lv_bus", etc.)

        Returns:
            the "closed" value of a Switch
        """
        switch_state = (
            component[["index", bus]]
            .merge(
                switches,
                how="left",
                left_on=["index", bus],
                right_on=["element", "bus"],
            )
            .fillna(True)
            .set_index(component.index)
        )
        return switch_state["closed"]

    def get_switch_states(self, pp_table: str) -> pd.DataFrame:
        """
        Return switch states of either Lines or Transformers

        Args:
            pp_table: Table name (e.g. "bus")

        Returns:
            the switch states of either Lines or Transformers
        """
        if pp_table == "line":
            element_type = "l"
            bus1 = "from_bus"
            bus2 = "to_bus"
        elif pp_table == "trafo":
            element_type = "t"
            bus1 = "hv_bus"
            bus2 = "lv_bus"
        else:
            raise KeyError(f"Can't get switch states for {pp_table}")

        component = self.pp_input_data[pp_table]
        component["index"] = component.index

        # Select the appropriate switches and columns
        pp_switches = self.pp_input_data["switch"]
        pp_switches = pp_switches[pp_switches["et"] == element_type]
        pp_switches = pp_switches[["element", "bus", "closed"]]

        pp_from_switches = self.get_individual_switch_states(component[["index", bus1]], pp_switches, bus1)
        pp_to_switches = self.get_individual_switch_states(component[["index", bus2]], pp_switches, bus2)

        return pd.DataFrame({"from": pp_from_switches, "to": pp_to_switches})

    def get_trafo3w_switch_states(self, trafo3w: pd.DataFrame) -> pd.DataFrame:
        """
        Return switch states of Three Winding Transformers

        Args:
            trafo3w: PandaPower dataframe with information about the Three Winding Transformers.

        Returns:
            the switch states of Three Winding Transformers
        """
        element_type = "t3"
        bus1 = "hv_bus"
        bus2 = "mv_bus"
        bus3 = "lv_bus"
        trafo3w["index"] = trafo3w.index

        # Select the appropriate switches and columns
        pp_switches = self.pp_input_data["switch"]
        pp_switches = pp_switches[pp_switches["et"] == element_type]
        pp_switches = pp_switches[["element", "bus", "closed"]]

        # Join the switches with the three winding trafo three times, for the hv_bus, mv_bus and once for the lv_bus
        pp_1_switches = self.get_individual_switch_states(trafo3w, pp_switches, bus1)
        pp_2_switches = self.get_individual_switch_states(trafo3w, pp_switches, bus2)
        pp_3_switches = self.get_individual_switch_states(trafo3w, pp_switches, bus3)

        return pd.DataFrame((pp_1_switches, pp_2_switches, pp_3_switches))

    def get_trafo_winding_types(self) -> pd.DataFrame:
        """
        This function extracts Transformers' "winding_type" attribute through "vector_group" attribute or
        through "std_type" attribute.

        Returns:
            the "from" and "to" winding types of a transformer
        """

        @lru_cache
        def vector_group_to_winding_types(vector_group: str) -> pd.Series:
            match = TRAFO_CONNECTION_RE.fullmatch(vector_group)
            if not match:
                raise ValueError(f"Invalid transformer connection string: '{vector_group}'")
            winding_from = get_winding(match.group(1)).value
            winding_to = get_winding(match.group(2)).value
            return pd.Series([winding_from, winding_to])

        @lru_cache
        def std_type_to_winding_types(std_type: str) -> pd.Series:
            return vector_group_to_winding_types(self._std_types["trafo"][std_type]["vector_group"])

        trafo = self.pp_input_data["trafo"]
        if "vector_group" in trafo:
            trafo = trafo["vector_group"].apply(vector_group_to_winding_types)
        else:
            trafo = trafo["std_type"].apply(std_type_to_winding_types)
        trafo.columns = ["winding_from", "winding_to"]
        return trafo

    def get_trafo3w_winding_types(self) -> pd.DataFrame:
        """
        This function extracts Three Winding Transformers' "winding_type" attribute through "vector_group" attribute or
        through "std_type" attribute.

        Returns:
            the three winding types of Three Winding Transformers
        """

        @lru_cache
        def vector_group_to_winding_types(vector_group: str) -> pd.Series:
            match = TRAFO3_CONNECTION_RE.fullmatch(vector_group)
            if not match:
                raise ValueError(f"Invalid transformer connection string: '{vector_group}'")
            winding_1 = get_winding(match.group(1)).value
            winding_2 = get_winding(match.group(2)).value
            winding_3 = get_winding(match.group(3)).value
            return pd.Series([winding_1, winding_2, winding_3])

        @lru_cache
        def std_type_to_winding_types(std_type: str) -> pd.Series:
            return vector_group_to_winding_types(self._std_types["trafo3w"][std_type]["vector_group"])

        trafo3w = self.pp_input_data["trafo3w"]
        if "vector_group" in trafo3w:
            trafo3w = trafo3w["vector_group"].apply(vector_group_to_winding_types)
        else:
            trafo3w = trafo3w["std_type"].apply(std_type_to_winding_types)
        trafo3w.columns = ["winding_1", "winding_2", "winding_3"]
        return trafo3w

    def _get_pp_attr(
        self, table: str, attribute: str, default: Optional[Union[float, bool]] = None
    ) -> Union[np.ndarray, float]:
        """
        Returns the selected PandaPower attribute from the selected PandaPower table.

        Args:
            table: Table name (e.g. "bus")
            attribute: an attribute from the table (e.g "vn_kv")

        Returns:
            the selected PandaPower attribute from the selected PandaPower table
        """
        pp_component_data = self.pp_input_data[table]

        # If the attribute exists, return it
        if attribute in pp_component_data:
            return pp_component_data[attribute]

        # Try to find the std_type value for this attribute
        if self._std_types is not None and table in self._std_types and "std_type" in pp_component_data:
            std_types = self._std_types[table]

            @lru_cache
            def get_std_value(std_type_name: str):
                std_type = std_types[std_type_name]
                if attribute in std_type:
                    return std_type[attribute]
                if default is not None:
                    return default
                raise KeyError(f"No '{attribute}' value for '{table}' with std_type '{std_type_name}'.")

            return pp_component_data["std_type"].apply(get_std_value)

        # Return the default value (assume that broadcasting is handled by the caller / numpy)
        if default is None:
            raise KeyError(f"No '{attribute}' value for '{table}'.")
        return default

    def get_id(self, pp_table: str, pp_idx: int, name: Optional[str] = None) -> int:
        """
        Get a numerical ID previously associated with the supplied table / index combination

        Args:
            pp_table: Table name (e.g. "bus")
            pp_idx: PandaPower component identifier

        Returns:
            The associated id
        """
        return self.idx[(pp_table, name)][pp_idx]

    def lookup_id(self, pgm_id: int) -> Dict[str, Union[str, int]]:
        """
        Retrieve the original name / key combination of a pgm object

        Args:
            pgm_id: a unique numerical ID

        Returns:
            The original table / index combination
        """
        for (table, name), indices in self.idx_lookup.items():
            if pgm_id in indices:
                if name:
                    return {"table": table, "name": name, "index": indices[pgm_id]}
                return {"table": table, "index": indices[pgm_id]}
        raise KeyError(pgm_id)
