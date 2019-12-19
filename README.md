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
* At the same time, extracted the Station's location from a web_scrapping file made by Laurent Guerguy (github:laurent-guerguy).

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

## Model Training and Evaluation
*Include this section only if you chose to include ML in your project.*
* Describe how you trained your model, the results you obtained, and how you evaluated those results.

## Conclusion
* Summarize your results. What do they mean?
* What can you say about your hypotheses?
* Interpret your findings in terms of the questions you try to answer.

## Future Work
Address any questions you were unable to answer, or any next steps or future extensions to your project.

## Workflow
Outline the workflow you used in your project. What were the steps?
How did you test the accuracy of your analysis and/or machine learning algorithm?

## Organization
How did you organize your work? Did you use any tools like a trello or kanban board?

What does your repository look like? Explain your folder and file structure.

## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project.


[Repository](https://github.com/)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/en)  
