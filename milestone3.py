import gradio as gr
from transformers import pipeline

# Instantiate translation pipeline
tran_pip = pipeline("translation_en_to_de")

# Example translation with max_length
result = tran_pip("I like icecream", max_length=512)
print(result)

ccfile = open("transcription.txt", "r")
f = open("translation.txt", "a")

stuff = []
for aline in ccfile:
    stuff = aline.split()
fin = ""
for i in stuff:
    result = tran_pip(i, max_length=512)
    fin += " " + result[0]['translation_text']
    

f.write(f)
print(fin)  
ccfile.close()

if __name__ == "__main__":
    main()
