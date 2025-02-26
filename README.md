# aviate_ats

In this problem, we want to create a ATS for recruiter, to help recruiters keep a track of job application.

(Note: You just have to implement what is mentioned below, please do not waste time implementing things which are out of scope for this assignment. You will not be evaluated for adding anything extra.)
- You have to use the Django rest framework. Try to utilise the framwork as much as possible. Stick with conventions. Show off your expertise in this technology.
- You need to create a table called "Candidate" with columns: [Name, Age, Gender, Email, Phone number]
- You have to create api endpoints to: create, update and delete a candidate. Also create an api endpoint to Search candidates (Explained in detail below).
- Searching should work on candidates name and should return results sorted based on relevancy. Relevancy is defined as the number of words in the search query that can be found in candidates name.
- Example of searching api: if the search query is “Ajay Kumar yadav” the order of results will be [“Ajay Kumar Yadav”, “Ajay Kumar”, “Ajay Yadav”, “Kumar Yadav”, “Ramesh Yadav”, “Ajay Singh”]
- As we can see in the example above, even if the names are partial matches they are still part of the search result.
- *IMPORTANT*: In order to improve the efficiency of the searching api, you must only use ORM queries to filter and sort the candidates. You can't use python script for either filtering or sorting.