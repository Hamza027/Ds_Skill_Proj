# Ds_Skill_Proj
A repository for a project i.e. extracting most required skillset for jobs in Data Science profile using data from Indeed.

**Step 1**: Extract jobs posting Data (job title, company name, link to main job page) from indeed for first 30 pages provided job title and location (Extract_information_BS.py)

The data scrapped from Indeed is in the following format: (saved in Jobs_link.csv)

![Screen Shot 2022-04-13 at 18 36 13](https://user-images.githubusercontent.com/26603682/163238196-45053764-f314-4e05-a5eb-0f06e858a06b.png)


**Step 2**: Get complete job description from each webpage link stored in URL column of the above dataset and store it in a new column in the dataframe (Word_Cloud.ipynb)

The new shape of the dataframe after step 2 is as follows: saved in (Final_Data.csv)

![Screen Shot 2022-04-13 at 18 44 03](https://user-images.githubusercontent.com/26603682/163239371-e38deb92-f012-45ef-8b1c-d028e3300abc.png)



**Step 3**: Match each job description with a list of skills pre stored into a python list (buzz words) to obtain all the skills present in the description. 

After Skill Match the dataframe is in the following shape:

![Screen Shot 2022-04-13 at 18 48 37](https://user-images.githubusercontent.com/26603682/163240207-2f63329c-ad5e-4bc1-8e7a-16447ec95920.png)

**Step 4** Create a Data Corpus by combining all rows from column (Skill_Matches) into a single string and create Word Cloud from the Data Corpus

![Screen Shot 2022-04-13 at 18 51 05](https://user-images.githubusercontent.com/26603682/163240632-8eaa5703-3708-4c9c-90b4-b96e52f53136.png)


Enjoy :) :)
