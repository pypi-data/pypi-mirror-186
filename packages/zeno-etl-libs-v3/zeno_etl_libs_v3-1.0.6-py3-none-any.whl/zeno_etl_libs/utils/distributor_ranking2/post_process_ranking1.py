import pandas as pd
import numpy as np


def post_process_ranking_dc(df_drugs, df_store_dc_maps, df_distributors,
                            rank_drug_lvl, rank_drug_type_lvl, final_ranks,
                            weights_dc_drug_lvl, weights_dc_type_lvl):

    # add drug_id dummy column in type lvl
    rank_drug_type_lvl["drug_id"] = np.nan

    # add weights column
    rank_drug_type_lvl["weights"] = str(weights_dc_type_lvl)
    rank_drug_lvl["weights"] = str(weights_dc_drug_lvl)

    # adding details into drug_lvl_df
    rank_drug_lvl = rank_drug_lvl.merge(
        df_drugs[["drug_id", "drug_type", "drug_name"]],
        on="drug_id", how="left")
    rank_drug_lvl = rank_drug_lvl.merge(
        df_store_dc_maps[["dc_id", "dc_name"]].drop_duplicates(),
        on="dc_id", how="left")
    rank_drug_lvl = rank_drug_lvl.merge(
        df_distributors[["distributor_id", "distributor_name"]].drop_duplicates(),
        on="distributor_id", how="left")

    # adding details into drug_type_lvl_df
    rank_drug_type_lvl = rank_drug_type_lvl.merge(
        df_store_dc_maps[["dc_id", "dc_name"]].drop_duplicates(),
        on="dc_id", how="left")
    rank_drug_type_lvl = rank_drug_type_lvl.merge(
        df_distributors[["distributor_id", "distributor_name"]].drop_duplicates(),
        on="distributor_id", how="left")

    # combine drug_lvl and drug_type_lvl df
    ranked_features = pd.concat([rank_drug_lvl, rank_drug_type_lvl], axis=0)

    # add details into final_ranks df
    final_ranks = final_ranks.merge(
        df_store_dc_maps[["dc_id", "dc_name"]].drop_duplicates(),
        on="dc_id", how="left")
    final_ranks = final_ranks.merge(
        df_drugs[["drug_id", "drug_name"]], on="drug_id", how="left")

    # add columns for franchisee rank addition because
    # both dc & franchisee features/ranks needs to be written to same table.
    final_ranks["franchisee_id"] = 1  # zippin id
    final_ranks["store_id"] = np.nan
    final_ranks["store_name"] = ""

    ranked_features["franchisee_id"] = 1  # zippin id
    ranked_features["store_id"] = np.nan
    ranked_features["store_name"] = ""
    ranked_features["request_volume_store_dist"] = np.nan
    ranked_features["rank_store_dist_credit_period"] = np.nan
    ranked_features["rank_store_dist_volume"] = np.nan

    return final_ranks, ranked_features


def post_process_ranking_franchisee(df_drugs, df_store_dc_maps, df_distributors,
                                    rank_drug_lvl, rank_drug_type_lvl,
                                    final_ranks, weights_franchisee_drug_lvl,
                                    weights_franchisee_type_lvl):

    # add drug_id dummy column in type lvl
    rank_drug_type_lvl["drug_id"] = np.nan

    # add weights column
    rank_drug_type_lvl["weights"] = str(weights_franchisee_type_lvl)
    rank_drug_lvl["weights"] = str(weights_franchisee_drug_lvl)

    # adding details into drug_lvl_df
    rank_drug_lvl = rank_drug_lvl.merge(
        df_drugs[["drug_id", "drug_type", "drug_name"]],
        on="drug_id", how="left")
    rank_drug_lvl = rank_drug_lvl.merge(
        df_store_dc_maps[["store_id", "store_name"]].drop_duplicates(),
        on="store_id", how="left")
    rank_drug_lvl = rank_drug_lvl.merge(
        df_distributors[
            ["distributor_id", "distributor_name"]].drop_duplicates(),
        on="distributor_id", how="left")

    # adding details into drug_type_lvl_df
    rank_drug_type_lvl = rank_drug_type_lvl.merge(
        df_store_dc_maps[["store_id", "store_name"]].drop_duplicates(),
        on="store_id",  how="left")
    rank_drug_type_lvl = rank_drug_type_lvl.merge(
        df_distributors[["distributor_id", "distributor_name"]].drop_duplicates(),
        on="distributor_id", how="left")

    # combine drug_lvl and drug_type_lvl df
    ranked_features = pd.concat([rank_drug_lvl, rank_drug_type_lvl], axis=0)

    # add details into final_ranks df
    final_ranks = final_ranks.merge(
        df_store_dc_maps[["store_id", "store_name"]].drop_duplicates(),
        on="store_id", how="left")
    final_ranks = final_ranks.merge(
        df_drugs[["drug_id", "drug_name"]],
        on="drug_id", how="left")

    # add columns for dc rank addition because
    # both dc & franchisee features/ranks needs to be written to same table.
    final_ranks["dc_id"] = np.nan
    final_ranks["dc_name"] = ""
    final_ranks["correction_flags"] = ""

    ranked_features["dc_id"] = np.nan
    ranked_features["dc_name"] = ""
    ranked_features["request_volume_dc_dist"] = np.nan
    ranked_features["rank_dc_dist_credit_period"] = np.nan
    ranked_features["rank_dc_dist_volume"] = np.nan

    return final_ranks, ranked_features
