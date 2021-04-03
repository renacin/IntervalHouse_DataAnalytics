![LOGO](https://github.com/renacin/IntervalHouse_DataAnalytics/blob/main/Documents/Images/IH_Logo.png "Interval House Toronto Logo")
<h1 align="center">Data Analytics Project</h1>

Project Contributors:
+ Fazia Mohammed
+ Renacin Matadeen




- - - -
### Table Of Contents ###
Section  | Progress
| :--- | ---:
[1.0 Introduction](https://github.com/renacin/IntervalHouse_DataAnalytics#10-introduction)  | :heavy_check_mark:
[---- 1.1 Data Collection](https://github.com/renacin/IntervalHouse_DataAnalytics#11-data-collection-preparation--exploration)  | :construction_worker:
[---- 1.2 Research Questions & Approach](https://github.com/renacin/IntervalHouse_DataAnalytics#12-research-questions)  | :construction_worker:
[---- 1.3 Deliverables](https://github.com/renacin/IntervalHouse_DataAnalytics#13-deliverables)  | :heavy_multiplication_x:
[---- 1.4 Questions & Resources](https://github.com/renacin/IntervalHouse_DataAnalytics#14-questions--resources)  | :heavy_multiplication_x:




- - - -
### 1.0 Introduction ###

>"Interval House is Canada’s first center for women survivors of intimate partner violence and their children.
Founded in 1973 by a feminist collective, we have always had a pioneering spirit, taking a holistic approach to helping
women and children leave abuse behind and start new lives, free of violence."   

_- [Interval House](https://www.intervalhouse.ca/inside-interval-house/)_

As an ally in the fight against partner violence Interval House has helped improve the lives of many women, and children
over its years of operation. During its deployment, Interval House has also increased its capacity to help; both in
terms of size, as well as pioneering different services that can better help individuals escaping violence.

Data analytics are yet another area that Interval House would like to explore in its constant push to better help its clients.

This project follows an explorative analysis of Interval House data in an attempt to identify, and better serve
areas of need in their present/future client list.

_*This project is explorative and informal in nature; this repository will help track research and discoveries from pertinent datasets._

<br />




### 1.1 Data Collection, Preparation & Exploration ###
Datasets used in this project:

Name Of Dataset  | Data Type | Source | Sensitivity | Notes | Progress
|:---|---:|---:|---:|---:|---:|
Interval House Address Data | CSV | Interval House | Private | Ensure privacy aggregate to both CT, DA level. Turning into a rate *xx/100'000 individuals* | :construction_worker:
Toronto Census Data 2016 | CSV | Stats Canada | Public | Collect On Both CT, DA Level, Clean, And Create A .SHP Version | :construction_worker:
Toronto Census Boundary Areas 2016 | SHP | Stats Canada | Public | Collect Both CT, DA Level | :construction_worker:
City Of Toronto Public Health: COVID-19 Data | CSV | Public Health Toronto | Public | How is this aggregated? Spatial Mismatch? | :construction_worker:

<br />




### 1.2 Research Questions ###
Here are a few research questions that this project hopes to answer.


**Primary Research Questions:**
1. _Where are clients located within the City Of Toronto?_
    + Are there any spatial patterns?
        - What is the catchment area for Interval House?
        - If clients are spatially clustered, why are they in that area?
        - What is the average distance (and standard deviation) between Interval House and a given client?

    + Have client origins changed over time?
        - Has the catchment area changed over time?


2. _Which clients (Rep Via. Dissemination Areas) live within COVID-19 hotspots?_
    + Are there any spatial patterns?
        - What does this suggest about the past/current client list


**Secondary Research Questions:**
1. _Describe the demographics of areas that Interval House reside in_
    + Economics, Ethnicity, Housing Types, Average Income, Mobility?
        - Make the separation between client demographics and census tract demographics; we are looking at the latter

    + _"Birds Of The Feather Flock Together"_
        - Are there similar groups of people in respects to the demographics found in the areas where Interval House clients live?
        - What will a K-Means or other Cluster Analysis reveal?


2. _Do clients face issues accessing Interval House, or other social aid?_
    + Which clients, or more generally which areas are the least serviced in terms of similar aid?
    + What services does Interval House provide that would benefit from an analysis of accessibility?
    + Does Interval House help clients access other resources?
        - What kinds? If so where are they located?
        - Does Interval House provide bridge services to help clients connect to other aid groups?

<br />




### 1.3 Deliverables ###
In Progress

<br />




### 1.4 Questions & Resources ###

**General Questions:**
1. _How will data be standardized, and normalized for population? What technique will be used? How will that influence data?_
    + Will I normalize against the entire population, or just counts of women in a dissemination area?
    + Z-Scores, Max-Min, Etc...

2. _Which cluster analysis technique would be most effective in discovering areas with similar demographics?_
    + Which is better K-Mean, Hierarchical, Etc...

3. _How do we measure client mobility?_
    + Straight Distance (As the crows flies), Networked Distance (Manhattan Distance); Via Transit Route, Or Street Networks?



**Resources Used:**
1. _[Statistics Canada Census](https://www12.statcan.gc.ca/census-recensement/index-eng.cfm)_

<br />




- - - -
### Things To Do ###
Short Term:
+ Research Questions (Add More)
+ Data Collection (Add More)
    - Census Data Clean Up
+ Basic Census Visualization
+ Research Into Effective Techniques

Long Term:
+ Analysis
+ Results
+ Conclusion
