"""
Features for distributor ranking 2.0
1. Weighted Fulfillment
2. Margin
"""

from tqdm import tqdm

import numpy as np
import pandas as pd
import datetime as dt


def calculate_features(df_sb, df_rates, df_store_dc_maps, reset_date,
                       time_interval, logger, group_cols):
    """
    DC-LEVEL: group_cols=['dc_id','distributor_id', 'drug_id']
    FRANCHISEE-LEVEL: group_cols=['store_id','distributor_id', 'drug_id']
    """

    # ====================== WTD.FULFILLMENT CALCULATION ======================

    # BASE FF
    logger.info("Calculating sb-level ff")
    sb_ids = df_sb["sb_id"].unique().tolist()
    df_ff_base = pd.DataFrame()
    pd.options.mode.chained_assignment = None
    for sb_id in tqdm(sb_ids):
        df_temp = df_sb.loc[df_sb["sb_id"] == sb_id]
        df_temp["required_quantity_shift"] = df_temp["required_quantity"].shift(1)
        df_temp["required_quantity_shift"] = np.where(
            df_temp["required_quantity_shift"].isna(),
            df_temp["sb_quantity"], df_temp["required_quantity_shift"])

        try:
            slice_index = df_temp.loc[df_temp["required_quantity_shift"] == 0].index[0]
            # if completely fulfilled, ignore further fulfillment
            df_temp = df_temp.loc[:slice_index - 1]
        except IndexError:
            continue

        df_temp["ff_perc"] = 1 - (df_temp["required_quantity"] / df_temp[
            "required_quantity_shift"])
        df_temp = df_temp.groupby(
            ["sb_id", "sb_created_on", "store_id", "drug_id", "sb_quantity",
             "ordered_dist_id"], as_index=False).agg({"ff_perc": "max"})
        df_ff_base = pd.concat([df_ff_base, df_temp], axis=0)
    pd.options.mode.chained_assignment = 'warn'

    # remove WH, LP, WORKCELL
    df_ff_base = df_ff_base.loc[
        ~df_ff_base["ordered_dist_id"].isin([8105, 76, 5000])]
    df_ff_base.rename({"ordered_dist_id": "distributor_id"}, axis=1, inplace=True)

    # remove inconsistent FF cases
    df_ff_base["ff_perc"] = np.where(df_ff_base["ff_perc"] < 0, 0, df_ff_base["ff_perc"])

    # add store-dc map
    df_ff_base = df_ff_base.merge(df_store_dc_maps[["store_id", "dc_id"]],
                                  on="store_id", how='left')

    # ensure data-type
    df_ff_base["sb_created_on"] = pd.to_datetime(df_ff_base["sb_created_on"])

    # WTD FF
    logger.info("Calculating wtd.ff")
    # get length of 3 period split
    period_length = round(time_interval / 3)

    # p1 : t-1 (latest period)
    # p2 : t-2 period
    # p3 : t-3 period

    p1_end = pd.Timestamp(reset_date - dt.timedelta(6))
    p1_start = p1_end - dt.timedelta(period_length)
    p2_end = p1_start
    p2_start = p2_end - dt.timedelta(period_length)
    p3_end = p2_start
    p3_start = p3_end - dt.timedelta(period_length + 1)

    df_ff_1 = ff_calc(df_ff_base, group_cols, p_start=p1_start, p_end=p1_end,
                      period_flag="p1")
    df_ff_2 = ff_calc(df_ff_base, group_cols, p_start=p2_start, p_end=p2_end,
                      period_flag="p2")
    df_ff_3 = ff_calc(df_ff_base, group_cols, p_start=p3_start, p_end=p3_end,
                      period_flag="p3")

    df_ff_comb = pd.concat([df_ff_1, df_ff_2, df_ff_3], axis=0)

    # count cases where all 3 or 2 or 1 periods data present
    df_ff_period_cnt = df_ff_comb.groupby(group_cols, as_index=False).agg(
        {"period_flag": "count"})
    df_ff_period_cnt.rename({"period_flag": "period_count"}, axis=1,
                            inplace=True)

    # Cases with 3 periods present
    # weighted by 0.5, 0.3, 0.2 for p1, p2, p3 respectively
    df_3p = df_ff_period_cnt.loc[df_ff_period_cnt["period_count"] == 3][
        group_cols]
    df_ff_comb_3p = df_ff_comb.merge(df_3p, on=group_cols, how="inner")
    df_ff_comb_3p['period'] = np.tile(np.arange(1, 4), len(df_ff_comb_3p))[
                              :len(df_ff_comb_3p)]

    df_ff_comb_3p['weights'] = np.where(df_ff_comb_3p['period'] == 1, 0.5, 0)
    df_ff_comb_3p['weights'] = np.where(df_ff_comb_3p['period'] == 2, 0.3,
                                        df_ff_comb_3p['weights'])
    df_ff_comb_3p['weights'] = np.where(df_ff_comb_3p['period'] == 3, 0.2,
                                        df_ff_comb_3p['weights'])

    df_ff_comb_3p["wtd_ff"] = df_ff_comb_3p["ff_perc"] * df_ff_comb_3p["weights"]

    df_ff_comb_3p = df_ff_comb_3p.groupby(group_cols, as_index=False).agg(
        {"wtd_ff": "sum"})

    # Cases with 2 periods present
    # weighted by 0.6, 0.4 for latest, early respectively
    df_2p = df_ff_period_cnt.loc[df_ff_period_cnt["period_count"] == 2][
        group_cols]
    df_ff_comb_2p = df_ff_comb.merge(df_2p, on=group_cols, how="inner")
    df_ff_comb_2p['period'] = np.tile(np.arange(1, 3), len(df_ff_comb_2p))[
                              :len(df_ff_comb_2p)]

    df_ff_comb_2p['weights'] = np.where(df_ff_comb_2p['period'] == 1, 0.6, 0)
    df_ff_comb_2p['weights'] = np.where(df_ff_comb_2p['period'] == 2, 0.4,
                                        df_ff_comb_2p['weights'])

    df_ff_comb_2p["wtd_ff"] = df_ff_comb_2p["ff_perc"] * df_ff_comb_2p["weights"]

    df_ff_comb_2p = df_ff_comb_2p.groupby(group_cols, as_index=False).agg(
        {"wtd_ff": "sum"})

    # Cases with 1 period present
    # weighted by 1 for whatever period present
    df_1p = df_ff_period_cnt.loc[df_ff_period_cnt["period_count"] == 1][group_cols]
    df_ff_comb_1p = df_ff_comb.merge(df_1p, on=group_cols, how="inner")

    df_ff_comb_1p = df_ff_comb_1p[group_cols + ["ff_perc"]]
    df_ff_comb_1p.rename({"ff_perc": "wtd_ff"}, axis=1, inplace=True)

    # combine all
    df_ff_comb = pd.concat([df_ff_comb_3p, df_ff_comb_2p, df_ff_comb_1p], axis=0)

    # ========================== MARGIN CALCULATION ==========================

    logger.info("Calculating margin")
    df_margin = df_rates.loc[(df_rates["avg_mrp"] > 0) & (df_rates["avg_purchase_rate"] > 0)]
    df_margin = df_margin.loc[(df_margin["avg_mrp"] > df_margin["avg_purchase_rate"])]
    df_margin["margin"] = (df_margin["avg_mrp"] - df_margin["avg_purchase_rate"]) / df_margin["avg_mrp"]
    df_margin = df_margin[["distributor_id", "drug_id", "margin"]]

    # ======================== DIST VOLUME CALCULATION ========================

    if group_cols[0] == "dc_id":
        base_lvl = 'dc'
    else:
        base_lvl = 'store'

    logger.info(f"Calculating {base_lvl}-distributor volume")
    df_ff_base["ff_requests"] = np.where(df_ff_base["ff_perc"] > 0, 1, 0)
    df_vol = df_ff_base.groupby(group_cols, as_index=False).agg(
        {"ff_requests": "sum"})

    if base_lvl == 'dc':
        # calculate request volume dc
        request_volume_dc = df_vol.groupby("dc_id", as_index=False).agg(
            total_requests_dc=("ff_requests", "sum"))
        request_volume_dc_dist = df_vol.groupby(
            ["dc_id", "distributor_id"], as_index=False).agg(
            total_requests_dc_dist=("ff_requests", "sum"))

        df_vol = df_vol.merge(request_volume_dc_dist,
                              on=["dc_id", "distributor_id"],
                              how="left")
        df_vol = df_vol.merge(request_volume_dc, on="dc_id", how="left")

        df_vol["request_volume_dc_dist"] = df_vol["total_requests_dc_dist"] / \
                                           df_vol["total_requests_dc"]

        df_vol.drop(["total_requests_dc_dist", "total_requests_dc"], axis=1,
                    inplace=True)

    else:
        # calculate request volume store (franchisee)
        request_volume_store = df_vol.groupby("store_id", as_index=False).agg(
            total_requests_store=("ff_requests", "sum"))
        request_volume_store_dist = df_vol.groupby(
            ["store_id", "distributor_id"], as_index=False).agg(
            total_requests_store_dist=("ff_requests", "sum"))

        df_vol = df_vol.merge(request_volume_store_dist,
                              on=["store_id", "distributor_id"],
                              how="left")
        df_vol = df_vol.merge(request_volume_store, on="store_id", how="left")

        df_vol["request_volume_store_dist"] = df_vol["total_requests_store_dist"] / \
                                              df_vol["total_requests_store"]

        df_vol.drop(["total_requests_store_dist", "total_requests_store"],
                    axis=1, inplace=True)

    # =========================== COMPILE FEATURES ===========================

    logger.info("Compiling all features")

    features = df_ff_comb.merge(df_margin, on=["distributor_id", "drug_id"],
                                how="left")
    features = features.merge(df_vol, on=group_cols, how="left")

    # rounding off to 3 significant digits
    features["wtd_ff"] = np.round(features["wtd_ff"], 3)
    features["margin"] = np.round(features["margin"], 3)
    features[f"request_volume_{base_lvl}_dist"] = np.round(
        features[f"request_volume_{base_lvl}_dist"], 3)

    # assume 0 margin for null cases
    features["margin"] = features["margin"].fillna(0)

    return features


def ff_calc(df_ff_base, group_cols, p_start=None, p_end=None, period_flag="None"):
    # split base data by period
    df_ff = df_ff_base.loc[(df_ff_base["sb_created_on"] > p_start) &
                           (df_ff_base["sb_created_on"] < p_end)]

    df_ff = df_ff.groupby(group_cols, as_index=False).agg({"ff_perc": np.average})
    df_ff["period_flag"] = period_flag

    return df_ff
