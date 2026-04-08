import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
#
kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())
# depression = df[["depression_pct", "country"]]
# print(depression)
# europe_depression = df[(df["region"] == "Europe") & (df["depression_pct"] > 5)]
# print(europe_depression[["country", "depression_pct"]])

#

# # new_dataframe = df["suicide_rate_per100k"] * df["populations"]
# # print(df[["country", "millions * rate"]])
# gdp_geg_40k = df[df["gpd_geg_40k"] >= 10000]
# gpd_geg_40k = gpd_geg_40k[gpd_geg_40k["mh_system_score"] < 5]
# gpd_geg_40k_low_help["lack_of_care_mln"] = (gpd_geg_40k_low_help["population_millions"] * gpd_geg_40k_low_help["treatment_gap_pct"]/100)
# print(new_dataframe.head())

# top_5 = df.nlargest(5, "depression_pct")
# plt.figure(figsize = (8,4))
# plt.plot(top_5["country"], top_5["depression_pct"], marker='o', linestyle='-', color='red')
# plt.plot(top_5["country"], top_5["anxiety_pct"], marker='s', linestyle='-', color='blue')
# plt.title("Anxiety vs Depression(%)")
# plt.xlabel("Country")
# plt.ylabel("Percents")
# plt.legend(["Anxiety", "Depression"])
# plt.show()


# plt.figure(figsize = (8,4))
# plt.scatter(df["social_media_hours_daily"], df["youth_mh_crisis_score"], color="black", marker="o" )
# plt.title("Mental Health vs Social Media Hours")
# plt.xlabel("Social Media Hours")
# plt.ylabel("Mental Health Crisis Score")
# plt.grid(True, linestyle = "--")
# plt.show()