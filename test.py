# Document Clustering Part_2

import csv
import math
import heapq

term_freq={}
norm_termfreq={}
observe=[]
inv_docfreq={}
tfidffreq={}
cosin_sim={}
modulus={}
k=3

def read_file():
    f = open('sample.csv')  
    csv_f = csv.reader(f)
    for row in csv_f:
      #  print row[0],row[1],row[15]
        cal_termfrequency(row[1],row[2])


def cal_termfrequency(name,text):
    if name not in term_freq:
        term_freq[name]={}

    temp=text.split(" ")
    for word in temp:
        if word not in term_freq[name]:
            term_freq[name][word]=1
        else:
            term_freq[name][word]+=1
    #cal_normfrequency()


def cal_normfrequency():
    for name in term_freq:
        #print name
        if name not in norm_termfreq:
            norm_termfreq[name]={}
        for word in term_freq[name]:
            norm_termfreq[name][word]=float(term_freq[name][word])/len(term_freq[name])
    #cal_inversedocfreq()


def cal_inversedocfreq():
    for name in term_freq:
        for word in term_freq[name]:
            count=1
            if word not in observe:
                observe.append(word)
                for names in term_freq:
                    if names!=name:
                        if word in term_freq[names]:
                            #print "test"
                            count+=1
                inv_docfreq[word]=math.log((len(term_freq)/(float(1+count))),2)
                    
                    
                
def cal_normtfidffreq():
    for name in term_freq:
        for word in term_freq[name]:
           # print word
            if name not in tfidffreq:
                tfidffreq[name]={}
            tfidffreq[name][word]=norm_termfreq[name][word]*inv_docfreq[word]


def cal_mod():
    for name in tfidffreq:
        mod=0
        for word in tfidffreq[name]:
            mod+=tfidffreq[name][word]*tfidffreq[name][word]
        modulus[name]=math.sqrt(mod)
            
        
    


def cal_cosinesim():
    for name in tfidffreq:
        if name not in cosin_sim:
            cosin_sim[name]={}
        for names in tfidffreq:
            dot=0
            if names!=name:
                #cosin_sim[name][names]=1
                #print modulus[names]*modulus[name]
                for word in tfidffreq[name]:
                    if word in tfidffreq[names]:
                        dot+=tfidffreq[name][word]*tfidffreq[names][word]
                cosin_sim[name][names]=dot/(modulus[name]*modulus[names])


def k_nearest():
    for name in cosin_sim:
        print name+" : "
        #print "similar_word = "
        sorted(cosin_sim[name], key=cosin_sim[name].get, reverse=True)[:k-1]
        top=heapq.nlargest(k, cosin_sim[name], key=cosin_sim[name].get)
        for word in top:
            print word
        print "\n"

read_file()
cal_normfrequency()
cal_inversedocfreq()
cal_normtfidffreq()
cal_mod()
cal_cosinesim()
k_nearest()

#print term_freq
#print norm_termfreq
#print inv_docfreq
#print tfidffreq
#print modulus
#print cosin_sim


