#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#function to identify TFs within a sequence
def tfinder(filename):
    
    #open, read and close file
    read_seq=open(filename,'r')
    dnaseq=read_seq.read().strip()
    read_seq.close()
    
    #save sequence length and other variables
    seqlen=len(dnaseq)
    
    #dictionary of TFs and their respective binding sites
    tfbs={
    "PDX1":"TCTAAT",
    "MAFA":"TGCA",
    "SP1": "CCGCCC",
    "NFY":"CCAAT",
    "STAT3":"TTCTGGGA"}
    
    #looking for TF binding sites within a sequence
    for i in range(seqlen):
        if dnaseq[i-3:i+3]== tfbs["PDX1"]:
            print("Transcription factor PDX1 at position:", i-3)
        elif dnaseq[i-2:i+2]== tfbs["MAFA"] :
            print("Transcription factor MAFA at position:", i-2)
        elif dnaseq[i-3:i+3]==tfbs["SP1"]:
            print("Transcription factor SP1 at position:", i-3)
        elif dnaseq[i-3:i+2]==tfbs["NFY"]:
            print("Transcription factor NFY at position:", i-3)
        elif dnaseq[i-4:i+4]==tfbs["STAT3"]:
            print("Transcription factor STAT3 at position:", i-4)

    
#results
tfinder('seq1.txt')  
tfinder('seq3.txt')
    

