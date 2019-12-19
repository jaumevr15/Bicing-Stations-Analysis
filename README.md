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
* The focus is in "Station ID", "Num of bikes available", and "Last Updated". Rest of columns are dropped.
Describe your full process of data wrangling and cleaning. Document why you chose to fill missing values, extract outliers, or create the variables you did as well as your reasoning behind the process.

## Analysis
* Overview the general steps you went through to analyze your data in order to test your hypothesis.
* Document each step of your data exploration and analysis.
* Include charts to demonstrate the effect of your work.
* If you used Machine Learning in your final project, describe your feature selection process.

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
