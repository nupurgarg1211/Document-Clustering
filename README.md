# Document-Clustering
This project cluster people according to their description provided in the sample file 

##samples.csv :
It contain fields such as URL,Name of the person,Text related to that person.

Ex.:
* URL:<http://dbpedia.org/resource/Digby_Morrell>	
* NAME:Digby Morrell	
* TEXT:"digby morrell born 10 october 1979 is a former australian rules footballer who played with the kangaroos and carlton in the 
australian football league aflfrom western australia morrell played his early senior football for west perth his 44game senior career
for the falcons spanned 19982000 and he was the clubs leading goalkicker in 2000 at the age of 21 morrell was recruited to the 
australian football league by the kangaroos football club with its third round selection in the 2001 afl rookie draft as a forward he 
twice kicked five goals during his time with the kangaroos the first was in a losing cause against sydney in 2002 and the other the 
following season in a drawn game against brisbaneafter the 2003 season morrell was traded along with david teague to the carlton 
football club in exchange for corey mckernan he played 32 games for the blues before being delisted at the end of 2005 he continued
to play victorian football league vfl football with the northern bullants carltons vflaffiliate in 2006 and acted as playing assistant 
coach in 2007 in 2008 he shifted to the box hill hawks before retiring from playing at the end of the season from 2009 until 2013 
morrell was the senior coach of the strathmore football club in the essendon district football league leading the club to the 2011 
premier division premiership since 2014 he has coached the west coburg football club also in the edflhe currently teaches physical 
education at parade college in melbourne"

##Approach :
* I calculated term frequency for each word in every document(one row is a document here).Term frequency means how many times a word 
appear in a document.
* Then normalized that frequency.
* After this calculated inverse document frequency to avoid the effect of most common words in the text of a documents.
* Then calculated cosine similarity between the documents.
* Based on similarity this project is listing top 3 persons that are related(or have same feature) to a every document.

