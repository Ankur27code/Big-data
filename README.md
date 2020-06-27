<h3 align="center">
Bigdata-project-w2020<br>
Code Clone Detection
<h3>


# Abstract 

<p align="justify">
Code cloning refers to similar or identical fragments of code. Reusing existing code for increasing software productivity is a key element of object oriented programming which makes code clone detection and management a primary concern for the current industry. Consequently, this cloning process may lead to bug propagation that significantly affects the maintenance cost. By considering this problem, detecting code clones  appears as an active area of research. For our project we  used machine learning and similarity search  to detect the similarity between the  code segments on the basis of lexical analysis of programs. We have used the K-Means algorithm (to group the similar code in the same cluster) and Locality Sensitive Hashing to group similar code fragments in the same bucket.
</p>




# 1. Introduction

<p align="justify">
Code clones are fragments of codes which are identical to each other, these clones are generated using copy and paste activities of the programmer, but the main problem with code clones is replication of bugs and difficulties in software maintenance, so it becomes imperative to detect these clones.
</p>


The 4 types of clones are:

* Exact clones (Type 1): Identical code segments except for changes in comments, layouts and whitespaces.

* Renamed clones (Type 2): Code segments which are syntactically or structurally similar other than changes in comments, identifiers, types, literals, and layouts. These clones are also called parameterised clones.  
 
* Near Miss clones (Type 3): Copied pieces with further modification such as addition or removal of statements and changes in whitespaces, identifiers, layouts, comments, and types but outcomes are similar. These clones are also known as gapped clones. 

* Semantic clones (Type 4): Code segments that are functionally similar but implemented by different syntactic variants.

<p align="justify">
The aim of our project is to detect type 1 and type 2 clones. Most of the programmers try to simply replicate their previous work and reuse existing pieces of code. This could propagate many bugs in the software unknowingly, which are very hard to detect once the program reaches a certain level of complexity. With our approach of using machine learning, we want to detect the clones in such a way that it can be used for various other purposes like aspect mining, program understanding, plagiarism detection, code compaction, software evolution analysis, code quality analysis and bug detection. This makes effective and useful part of software analysis. 
</p>  
<p align="justify">
There have been previous works which involved detecting code clones, text based approach was used in work done by [1]. However this was only capable of detecting type 1 clones, Further works also used approaches like token based, graph based[7] and a few[5][6] tried to use machine learning for detecting clones. But most of the approaches were based on classification rather than using clustering and similarity search which are good candidates for finding similar items 
</p>

# 2. Methods and Methodology 

It is further divided into two phases :-

- Data generation 
- Algorithm implementation

# 2.1  Data Preparation
<p align="justify">
There was no available dataset for code clones, so there were no definitive set of features to characterize  these. Therefore we chose the IJADataset which is a collection of java programs and contains 47k files with around 10092k lines of code. 
</p>
We performed the following set of operations to generate data suitable for algorithms.
<p align="justify">
 
- Step 1 :- Injection of code clones in dataset.<br>
 
  * Injecting Type 1 clones(Exact CLones) :- Created multiple copies of the codes, Addition of comments in few codes.
  
  * Injecting Type 2 clones(Renamed CLones):- Modifications in identifier names including Type 1 changes<br>
</p>

- Step 2 :- Generating Features:-

  * Next step was to look for the features which could be used to distinguish each of these programs. Thus we performed lexical analysis using JAVALANG tool on each program present in the dataset, which breaks each program into a set of tokens. Furthermore, we used the count of each token present in a program as the set of features for that particular program.



Consider an example program to add two numbers. After performing lexical analysis, the tokens generated are given below.

![alt text](https://github.com/ankur27aggarwal/dummy/blob/master/Screen%20Shot%202020-04-10%20at%2010.06.02%20PM.png)

<p align="justify">
These lexical tokens were stored in  CodeClone.csv files such that each row represents a different number of tokens present in each source code file. After parsing all the programs, our dataset Contains 56,168 rows (or programs), including 10k duplicates approx and 15 different features.
</p>

![alt text](https://github.com/ankur27aggarwal/dummy/blob/master/Screenshot%202020-04-10%20at%205.22.53%20PM.png)
Here null values indicate features(tokens) which are not present in certain programs.

# 2.2 Algorithms Implemented

Two big challenges that are associated with generated dataset are :-

* Curse Of Dimensionality :- High Dimensionality of the unique characteristic i.e feature vector required to identify clones.

* Cost Of Comparison Operation :- Comparison of instances with all other instances in the dataset for finding similarity is expensive in terms of time and memory.

Due to these two factors we decided to implement K-Means and Locality Sensitive Hashing with their respective variations.

# 2.2.1 K-MEANS ALGORITHM
<p align="justify">
K-means algorithm is an iterative algorithm that tries to partition the dataset into K pre-defined distinct non-overlapping subgroups (clusters) where each data point belongs to only one group. Since clustering is one of the most common exploratory data analysis techniques used to get an intuition about the structure of the data.Therefore, it makes sense to use K-means, as similar codes would be in the same cluster which is our main motivation behind the usage of k-means. For our project we have used the scikit-learn’s implementation of k-means and used the original higher dimensional dataset for clustering.
</p>

<p align="justify">
Number of clusters :- To find the optimal number of clusters we used the elbow method using Inertia(Sum of squared distances of samples to their closest cluster center).
</p>

# Advanced Approach :-

![alt text](https://github.com/ankur27aggarwal/dummy/blob/master/Screenshot%202020-04-10%20at%205.55.52%20PM.png)

This is done in three steps :-

Step 1 :- In this step we reduce the dimensionality by using the same PCA technique mentioned above.

Step 2 :- Dividing input space into smaller subspaces.

Step 3 :- Hashing as a candidate for nearest neighbour search.

# 2.2.2 Locality Sensitive Hashing

Locality-Sensitive Hashing (LSH) is an algorithmic technique that hashes similar input items into the same "buckets" with high probability.
![alt text](https://github.com/ankur27aggarwal/dummy/blob/master/Screenshot%202020-04-10%20at%205.56.37%20PM.png)
For our project we used LSH using Random Projection. Locality Sensitive Hashing solves both the challenges mentioned earlier which are explained as follows :-

* For Challenge 1 :- As shown in the figure the first hash function reduces the dimensionality of the dataset as we project our feature vector onto a lower-dimensional subspace using a random matrix whose columns have unit length.

* For Challenge 2 :-  The second hash function further reduces the dimensionality and thus comparing  each instance with all the other instances on the basis of hash value  gives the exact similar pairs. We use band=1 with buckets containing code clones.

# 3. Results
<p align="justify">

For finding the best value of the number of clusters(k) as discussed above we used the elbow method. We plotted a graph between inertia and number of clusters, as our main aim is to choose k which has a small value of inertia. From the graph given below, we found that after 5 clusters there is not much significant change in inertia thus we chose numbers of clusters as 5.
</p >


<p align="center">
  <img  src="https://github.com/ankur27aggarwal/dummy/blob/master/Screen%20Shot%202020-04-10%20at%2010.32.59%20PM.png"><br>
 Elbow plot w.r.t inertia and number of clusters
</p>


![alt text](https://github.com/ankur27aggarwal/dummy/blob/master/Screenshot%202020-04-10%20at%205.58.10%20PM.png)
<p align="center">
Clustering with k= 5, Plot of points w.r.t to keywords and identifiers.
</p> 



<p align="justify"> 
Drawbacks of choosing number of cluster k=5 :- Our dataset contains around 46k non duplicated programs so ideally it should have around 46k clusters, therefore K=5  won’t be a good choice for clone detection. To deal with the problem of dimensionality we also tried PCA(Principal Component Analysis) dimensionality reduction technique. Results with clustering on dimensionally reduced data were the same,(elbow was at k=5). Thus we used advanced approaches for finding similarity between source codes
</p>

* Compared the performance of both approaches on the basis of execution time.
* Locality sensitive Hashing detected duplicates faster than using Clustering and Hashing together.

| Approach | Execution Time |
| ------ | ------ |
| PCA, K-Means Clustering and Hashing | ~3.71 Seconds |
| Locality Sensitive Hashing Using Random Projection | ~2.16 Seconds |
| Locality Sensitive Hashing Using Gaussian Projection(Scikit learn) | ~1.82 Seconds |

# 4. Discussion and Future work

<p align="justify">
To find the relevance of our solution, we tried to compare our solution with existing works[5][6], but most of the works were classification based and had less number of instances, hence it was inappropriate to compare our work with them. For such problems where we need to find similarity between the elements clustering and similarity search are good candidates. Similarity search is better option for finding exact similars than clustering, as LSH using random projection reduces the dimensionality of dataset and also reduces the computational time.
</p>

<p align="justify">
However, results would have been completely different if we only needed to find near similar instead of exact similars. For example if we changed the values in dot product from float to integer, it gave near similars and buckets reduced drastically. Also, there would have been false positives and false negatives if we would have been finding near similars. We did not have these (false positives and false negatives) in our work,  as we were only finding exact clones or similars. 
</p>

<p align="justify">
Our project works only on syntactic clones, semantic clones can be detected using abstract syntax trees. Thus extracting features from these trees can help extracting the semantic details of the program which can be used as features to detect semantic clones. This is desirable for future work.
</p>


<p align="justify">
Dataset contains 56k instances of java source codes only. We are further looking forward to extend our work for source codes from other programming languages. Thus instances will increase gradually, so we are exploring ways to implement a parallelized version of Locality Sensitive Hashing using random projection. This may give us faster results.
</p>

# 5. References
  1. Chanchal Kumar Roy, James R Cordy, "A Survey on Software Clone Detection Research", Computer and Information Science, vol. 115, no.        541, pp. 115, 2007.
  2. Ritesh V. Patil, Shashank. D. Joshi, Sachin V. Shinde, V. Khanna, "An effective approach using dissimilarity measures to estimate          software code clone", Electrical Electronics Signals Communication and Optimization (EESCO), pp. 1-6, 2015.
  3. Shantanu Saraswat, "Efficient detection of code clones B. Tech", Project under Dr. Amey Karkare CSE Deptt. IIT Kanpur, 2011.
  4. Randy Smith, Susan Horwitz, "Detecting and measuring similarity in code clones", Proceeding of Third International Workshop on            Detection of Software Clones., 2009.
  5. S. Jadon, "Code clones detection using machine learning technique: Support vector machine," 2016 International Conference on              Computing, Communication and Automation (ICCCA), Noida, 2016, pp. 399-303.
  6. A. Sheneamer and J. Kalita, "Semantic Clone Detection Using Machine Learning," 2016 15th IEEE International Conference on Machine          Learning and Applications (ICMLA), Anaheim, CA, 2016, pp. 1024-1028.
  7. Baxter, Ira & Yahin, Andrew & de Moura, Leonardo & Sant'Anna, Marcelo & Bier, Lorraine. (1998). Clone Detection Using Abstract Syntax Trees.. Proc. of International Conference on Software Maintenance. 368-377. 368-377. 10.1109/ICSM.1998.738528.
