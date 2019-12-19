<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Bicing: Understanding stations behaviour
*[Jaume Vicens]*

*[Data Analytics Full-time, Ironhack Barcelona, 20/12/2019]*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project is meant to analyze and understand the behaviour of Bicing bike-sharing service stations in the city of Barcelona by using the Clusters method to identify patterns that can help solving uneven bike distribution, especially at workdays rush hour.

## Hypotheses / Questions
* Bike stations seem to follow certain patterns of how full/empty the station can be depending on the time of the day.
* Depending on their location and on the surroundings, some stations tend to be often full or often empty at rush hour.
* Bicing bike-sharing system based in dock-stations limit the amount of bikes that can be left or taken, being sometimes unable to absorb the demand of users.
* This project pretends to identify these patterns, understand their behaviour and by locating the stations that are more vulnerable to be full or empty in certain times.
* Once patterns are identified and clusters can be located on a map, can the suggested clusters distribution assist on finding a solution to prevent stations meeting users needs?


## Dataset 
* The Dataset has been taken from [Barcelona Open Data](https://opendata-ajuntament.barcelona.cat/data/ca/dataset/estat-estacions-bicing). At some point in November, the dataset was available as .csv file -currently only as 7z-. At the moment to set the project it was expected to be able to use datasets from March to November. 7z files currently available cannot be decompressed at the moment.
* For the project only October data is used.
repo.
* The data in the Dataset includes a record of each of the 400+ stations status recorded every 5-7 minutes.
- Station ID
- Number of bikes available at that certain time, specifying if there are mechanic or electric.
- Status of the station (Is it working? Does it charge e-bikes?).
- Time of updated and reported data.
* At the same time, extracted the Station's location from a web_scrapping file made by [Laurent Guerguy] (https://github.com/laurent-guerguy).

## Cleaning (0_data_cleaning.ipynb)
* The original dataset is pretty clean by default. First thing to be aware of is the format of the datetime columns (in Epoch time), which need to be transformed into %d %m %Y.
* As the analysis focus on weekdays, it is important to identify the weekdays of the time range and extract only the rows that match the workdays.
* The status column is used to verify if the data of the row can be taken into account or not. Rows which status is not "IN_SERVICE" are considered as not useful, hence dropped.
* The focus is in "Station ID", "Num of bikes available", and "Last Updated". Rest of columns are dropped
* The number of bikes available was initially an absolute number. In order to have a better understanding on how likely each station is to be full or empty, those values have been transformed into %.
* The maximum capacity is not provided by the dataset (although ttl column initially indicated) so it has been calculated by using the maximum value each station obtained in that particular month.

#### Datetime handling (1_datetime.ipynb)
* Datetime handling has been the main challenge of the data cleaning process. Rows have been merged/grouped by depending on the time of the day.
* Particularly, data has been aggregated hourly. Obtaining the average amount of bikes for each station, on each particular hour.
* Once this process is done, each hour (from 00:00 to 23:00) becomes a column-feature to build the model.

#### Geolocation features (2_geolocation_cluster_model.ipynb)
* Geolocation in latitude and longitude are added from the bicing_ws_laurent.csv dataset.
* Also added distance of each station from Plaça Catalunya using Geopy.

#### The model features (2_geolocation_cluster_model.ipynb)
The features of the model are then the following:
* 24 columns for each hour of the day and its behaviour. 
* Capacity of the station.
* Distance in KM from the station to Plaça Catalunya.
* Long/Lat coordinates


## Analysis (3_analysis.ipynb)
* Once the data has been organized to have the hourly behaviour, and clustered into the different outputs, it can already be displayed by using different visualisation tools.
* The first insights by plotting the behaviour of the different clutters show clear different patterns of behaviour throughout the day. 
* These patterns, together with map visualisation through Tableau. Help understanding the features that are relevant to be classified in one cluster or the other.

#### The clusters analysis:
* Cluster 1: Stations to be half-full at most part of the day, but generally do not get completely full. Map locates the stations of this cluster below Gran Via and Meridiana, generally in pretty dense and busy areas.
* Cluster 2: Stations of cluster 3 tend to be empty throughout most part of the day. This could be because of the higher elevation of these stations, and also because there might be areas where users tend to take bikes very fast.
* Cluster 3: Stations from this cluster behave as work/educational locations. At morning rush hour the tendency is to get filled by bikes and then it slowly gets empty towards the end of the day. Map proves that they are located near office/university areas.
* Cluster 4: Stations that behave as moderate Residentials, getting emptier at morning rush hour and slowly increasing the % of bikes. Especially located in Sants/Eixample/Sant Andreu/Gràcia.
* Cluster 5: Stations behave as extreme residential locations with more extreme behavior than, for example, Cluster 4. This is due to the fact that these stations are located at areas of Barcelona which have low elevation and purely residential.

## Model Training and Evaluation (2_geolocation_cluster_model.ipynb)
The Model uses KMeans method to cluster the stations based on 29 features. The model has been tested using directly the 29 features and PCAComponents.

The outcome has been very similar (only 2 stations being labeled differently), so initial model with 29 features is accepted for the project.

The model extracts 4 clusters as initially expected, but there is one that behaves unexpectedly (Cluster 2, Low occupation). All of them are evaluated by the .describe() method understanding how does the standard deviation behave (as being aggregates of all the values of the stations involved). Surprisingly, Cluster 2 is the one with the lowest standard deviation, which indicates that those stations behave similarly. 

## Conclusion
Bicing stations tend to follow behavioural patterns on weekdays. Users commute and move in certain patterns that can be identified through the evolution of the bike occupation at each station throughout the day.
By knowing the behaviour of each cluster, and being able to identify and locate them, we can apply optimal solutions to the stations that behave with extreme values, and balance the uneven distribution of users along the city at specific times of the day, especially at rush hour.

## Future Work
#### The Cluster 2 enigma
This project creates a new challenge that was initially not seen when facing the problem. There is a big cluster of stations which have very little amount of bikes throughout the day. For some reason, those stations are always half-empty. Understanding the causality of this behaviour would help to improve the user experience of the users around this cluster.

#### The weekday/weekend & school time / holidays behaviour
* Due to limitations of the data available, only weekdays of one month could be analyzed. This limits the accuracy of the behavior as October could have behaved differently (important to note how October was politically intense with demonstrations). Having data of other months would help confirm behaviours.
* At the same time, weekends behavior seems unknown and hard to initially preview. An analysis on if there are unexpected patterns of behavior would be very helpful.
* Following the same reasoning, understanding if patterns change when the season, or routine changes due to holidays could help understanding Bicing behaviour throughout the whole year...
* ... and ultimately, be able to predict by time-series analysis future behavior, spotting how stations behave in especial events, festivals or holidays.


## Repository
The repository is divided in three main folders:
#### Dataset
Includes the original dataset and the cleaned ones.
* 2019_10_Octubre_BicingNou_ESTACIONS.rar: The original dataset. Due to over 200Mb size, it has been compressed. Please extract the file at the same folder to run it on the notebook.
* October_cleaned.rar: Original dataset extracted null values, unneeded columns and transforming Epoch time. Due to its big size, it has been compressed. Please extract the file at the same folder to run it on the notebook.
* bicing_ws_laurent.csv: Web-scrapping data extracted from [Laurent Guerguy] (https://github.com/laurent-guerguy), which included geolocation of the stations.
* datetime_features.csv: Dataset generated after manipulating the information and aggregating the hourly behaviour. Used for the cluster model.
* clusters.csv: Final dataset with the clusters allocated. Used for visualisations with Pyplot and Tableau.

#### Code
* 0_data_cleaning.ipynb: Extracting the original data and taking the first cleaning steps.
* 1_datetime.ipynb: Manipulating datetime columns and aggregating them into hourly performance.
* 2_geolocation_cluster_model.ipynb: adding geolocation features and building the cluster model.
* 3_analysis.ipynb: visualizing data to extract insights and analyze behaviours.

#### Plots_maps
This folder include the output maps/plots made by analyzing the data. It includes the Tableau file together with the pictures and icons used at the presentation.

## Links
[Repository](https://github.com/jaumevr15/Bicing-Stations-Analysis)  
[Slides](https://slides.com/jaumevicensrivas/bicing_behaviour/fullscreen#/)  
[Trello](https://trello.com/b/qoPUVyn3/bicingstations-analysis)  
