
# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)

purchase_data.head()

## Player Count

* Display the total number of players


# print(purchase_data.columns)
# print(purchase_data.dtypes)

player_count = purchase_data["SN"].nunique()


pd.DataFrame({"Total Players":[player_count]})


#purchase_data["player_count"] = pd.DataFrame(purchase_data, columns=("player_count"))

## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


item_count = purchase_data["Item ID"].nunique()
avg_price = purchase_data["Price"].mean()
purchase_count = purchase_data["Purchase ID"].nunique()
total_revenue = purchase_data["Price"].sum()

#total_revenue


summary_table = pd.DataFrame({"Number of Unique Items":[item_count],
              "Average Price":[avg_price],
              "Number of Purchases":[purchase_count], 
              "Total Revenue":[total_revenue]})


summary_table["Average Price"] = summary_table["Average Price"].map("${:,.2f}".format)
summary_table["Total Revenue"] = summary_table["Total Revenue"].map("${:,.2f}".format)

summary_table = summary_table.loc[:,["Number of Unique Items","Average Price","Number of Purchases","Total Revenue"]]
summary_table

## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed




# Basic Calculations# Basic  
#pcount = purchase_data["Purchase ID"].count()

gender_demographics_totals = purchase_data["Gender"].value_counts()
gender_demographics_percents = gender_demographics_totals / purchase_count * 100

# Data Cleanup
gender_demographics = pd.DataFrame({"Total Count": gender_demographics_totals,
                                    "Percentage of Players": gender_demographics_percents})

gender_demographics = gender_demographics.round(2)

#Data Gender_demographics
gender_demographics


## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

# Basic Calculations# Basic  
gender_purchase_total = purchase_data.groupby(["Gender"]).sum()["Price"].rename("Total Purchase Value")
gender_average = purchase_data.groupby(["Gender"]).mean()["Price"].rename("Average Purchase Value")
gender_counts = purchase_data.groupby(["Gender"]).count()["Price"].rename("Purchase Count")


# Calculate normalized Purchasing
normalized_total = gender_purchase_total / gender_demographics["Total Count"]

# Cleanup
gender_data = pd.DataFrame({"Avg Purchase Total per Person": normalized_total, 
                            "Purchase Count": gender_counts, 
                            "Total Purchase Value": gender_purchase_total, 
                            "Average Purchase Value": gender_average})


gender_data["Average Purchase Value"] = gender_data["Average Purchase Value"].map("${:,.2f}".format)
gender_data["Total Purchase Value"] = gender_data["Total Purchase Value"].map("${:,.2f}".format)
gender_data["Avg Purchase Total per Person"] = gender_data["Avg Purchase Total per Person"].map("${:,.2f}".format)


gender_data = gender_data.loc[:,["Purchase Count","Average Purchase Value","Total Purchase Value","Avg Purchase Total per Person"]]


#Display
gender_data

## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


#Use Cut to categorize players
purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)


age_demographics_totals = purchase_data["Age Ranges"].value_counts()
age_demographics_percents = age_demographics_totals / purchase_count * 100

age_demographics = pd.DataFrame({"Total Count": age_demographics_totals, "Percent of Players": age_demographics_percents})
age_demographics = age_demographics.sort_index()

age_demographics

# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


#Use Cut to categorize players
purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)

age_group = purchase_data.groupby("Age Ranges").count()
age_group = age_group[["Age"]]
age_group = age_group.rename(columns={"Age": "Total Count"})



age_demographics_totals = purchase_data["Age Ranges"].value_counts()
age_demographics_percents = age_group["Total Count"] / purchase_count * 100

age_demographics = pd.DataFrame({"Total Count": age_demographics_totals, "Percent of Players": age_demographics_percents})

age_demographics["Percent of Players"] = age_demographics["Percent of Players"].map("{:,.2f}".format)
age_demographics = age_demographics.sort_index()

age_demographics

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

age_group = purchase_data.groupby("Age Ranges").count()
age_group = age_group[["Age"]]
age_group = age_group.rename(columns={"Age": "Purchase Count"})

age_average_price = purchase_data.groupby("Age Ranges").mean()
age_average_price = age_average_price[["Price"]]
age_average_price = age_average_price.rename(columns={"Price": "Average Purchase Price"})


merge1 = pd.concat([age_average_price, age_group], axis=1)

age_total_purchase = purchase_data.groupby("Age Ranges").sum()
age_total_purchase = age_total_purchase[["Price"]]
age_total_purchase = age_total_purchase.rename(columns={"Price": "Total Purchase Value"})


merge2 = pd.concat([merge1, age_total_purchase], axis=1)

merge2["Average Purchase Total per Person"] = merge2["Total Purchase Value"] / merge2["Purchase Count"]
age_purchases = merge2[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Average Purchase Total per Person"]]

age_purchases["Average Purchase Price"] = age_purchases["Average Purchase Price"].map("${:,.2f}".format)
age_purchases["Total Purchase Value"] = age_purchases["Total Purchase Value"].map("${:,.2f}".format)
age_purchases["Average Purchase Total per Person"] = age_purchases["Average Purchase Total per Person"].map("${:,.2f}".format)


age_purchases

## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



players_df = purchase_data.groupby(["SN"])

top_five_spenders = players_df[["Price"]].sum().nlargest(5,"Price")
top_five_spenders = top_five_spenders.rename(columns={"Price": "Total Purchase Value"})
player_purchases = players_df[["Price"]].count()
player_purchases = player_purchases.rename(columns={"Price": "Purchase Count"})
merge1 = top_five_spenders.join(player_purchases)
average_player_purchase = players_df[["Price"]].mean()
average_player_purchase = average_player_purchase.rename(columns={"Price": "Average Purchase Price"})
merge2 = merge1.join(average_player_purchase)
top_five_spenders = merge2[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]

top_five_spenders["Average Purchase Price"] = top_five_spenders["Average Purchase Price"].map("${:,.2f}".format)
top_five_spenders["Total Purchase Value"] = top_five_spenders["Total Purchase Value"].map("${:,.2f}".format)

top_five_spenders

## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



items_df = purchase_data.groupby(["Item ID","Item Name"])

top_five_items = items_df[["Price"]].count().nlargest(5,"Price")
top_five_items = top_five_items.rename(columns={"Price": "Purchase Count"})
item_prices = items_df[["Price"]].mean()
item_prices = item_prices.rename(columns={"Price": "Item Price"})
merge1 = top_five_items.join(item_prices)
item_purchase_total = items_df[["Price"]].sum()
item_purchase_total = item_purchase_total.rename(columns={"Price": "Total Purchase Value"})
top_five_items = merge1.join(item_purchase_total)

top_five_items["Item Price"] = top_five_items["Item Price"].map("${:,.2f}".format)
top_five_items["Total Purchase Value"] = top_five_items["Total Purchase Value"].map("${:,.2f}".format)

top_five_items

## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame



top_five_item_sales = items_df[["Price"]].sum().nlargest(5,"Price")
top_five_item_sales = top_five_item_sales.rename(columns={"Price": "Total Purchase Value"})
top_five_item_sales
item_purchases = items_df[["Price"]].count()
item_purchases = item_purchases.rename(columns={"Price": "Purchase Count"})
merge1 = top_five_item_sales.join(item_purchases)
item_prices = items_df[["Price"]].mean()
item_prices = item_prices.rename(columns={"Price": "Item Price"})
merge2 = merge1.join(item_prices)
top_five_item_sales = merge2[["Purchase Count", "Item Price", "Total Purchase Value"]]

top_five_item_sales["Item Price"] = top_five_item_sales["Item Price"].map("${:,.2f}".format)
top_five_item_sales["Total Purchase Value"] = top_five_item_sales["Total Purchase Value"].map("${:,.2f}".format)

top_five_item_sales