# ETL-project

The main goal of this project is to create a database of the players of the videogame FIFA 22. In order to do that, we are going to follow the ETL process:


-*EXTRACT*:
This is the first step of the project and consist in the collection of the data we are going to work with. Firstly, we started scrapping the website https://www.futbin.com/22/players to obtain a general vision of the characteristic of the players, such as medias, pass or shot, through a dataframe. After that, we scrapped a second website (https://sofifa.com/players) to  complete the data of the first research, for example the players's clubs. Finally we forked the following repository of GitHub https://github.com/oozanguner/Fifa22_Player_Segmentation as it has some links that could help us in the future, ath the time of doing the data representation.

For a matter of interested, all the functions we used in this part are located in the folder of code. They are called data1() and data2() and, basically, both of them receive one of th urls we mentioned previously and scrapp them returning a dataframe.


-*TRANSFORM*:
This is the second phase of the project and consist in the cleaning of the dataframe we created during the extraction process. We just changed some types of data to another one more convenient and merged some columns. The result of this is the final dataframe in which we will make our data base.


-*LOAD*:
This is the last step of the project. We created a database in mongo called FIfa22 and a new collection called fifa_players in which we are going to store the player's data.


Here ends this ETL project, however, this is the first phase of a bigger project that it is going to be a model of prediction of the player's market in FIFA 22 Ultimate team.
