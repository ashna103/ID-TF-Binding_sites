#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dictionary to store TFs and binding sites

tfbs={
    "PDX1":"TCTAAT",
    "MAFA":"TGCA",
    "SP1": "CCGCCC",
    "NFY":"CCAAT",
    "STAT3":"TTCTGGGA"
}


# In[ ]:


#identifying Tfs within seq1

for i in range(seqlen1):
    if seq1[i-3:i+3]== tfbs["PDX1"]:
        print("Transcription factor PDX1 at position:", i-3)
    elif seq1[i-2:i+2]== tfbs["MAFA"] :
        print("Transcription factor MAFA at position:", i-2)
    elif seq1[i-3:i+3]==tfbs["SP1"]:
        print("Transcription factor SP1 at position:", i-3)
    elif seq1[i-3:i+2]==tfbs["NFY"]:
        print("Transcription factor NFY at position:", i-3)
    elif seq1[i-4:i+4]==tfbs["STAT3"]:
            print("Transcription factor STAT3 at position:", i-4)

