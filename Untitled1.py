#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import requests
import bs4
import csv
import threading
import time
from collections import Counter


def req_validation(link):
    while True:
        
        try:
            req = requests.get(link)
            break
            
        except:
            print(f'Failed to fetch data from {link}')
            print('Trying again in 5 seconds')
            time.sleep(5)
            
    return req



def story(s_lnk, category, w):
    req = req_validation(s_lnk)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    
    try:
        title = soup.select('.bbc-1gvq3vt.e1yj3cbb0')[0].text
    except:
        return
        
    contents_soup = soup.select('.bbc-4wucq3.essoxwk0')
    contents = []

    for c in contents_soup:
        contents.append(c.text)

    contents = ' '.join(contents)
    print(f'Done: {s_lnk}')
    
    w.writerow([title, contents,category])


f = open('stories.csv', mode='w', newline='', encoding='utf-8')
w = csv.writer(f, delimiter=',')
w.writerow(['Title', 'Content', 'Category'])


categories = [('Pakistan','https://www.bbc.com/urdu/topics/cjgn7n9zzq7t'), 
              ('Aas Paas','https://www.bbc.com/urdu/topics/cl8l9mveql2t'), 
              ('World','https://www.bbc.com/urdu/topics/cw57v2pmll9t'), 
              ('Khel','https://www.bbc.com/urdu/topics/c340q0p2585t'), 
              ('Fun Funkaar','https://www.bbc.com/urdu/topics/ckdxnx900n5t'), 
              ('Science','https://www.bbc.com/urdu/topics/c40379e2ymxt'), ]


def scrape():
    for cat_name, cat_link in categories:    
        for n in range(1,6):
            page_link = cat_link + f'?page={n}'
            req = req_validation(page_link)
            soup = bs4.BeautifulSoup(req.text, 'lxml') 

            print(f'Scraping page {n} of {cat_name}')

            lnk_soup = soup.select('.bbc-uk8dsi.emimjbx0')
            links = []
            
            for l in lnk_soup:
                links.append(l['href'])


            if n == 5:
                links = links[:10]
            
            

            threads = []
            for l in links:
                t = threading.Thread(target=story, args=[l, cat_name,w])
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

            print(f'Finished page {n} of {cat_name}\n')
            
        print(f'Finished {cat_name}\n\n')
        
    print('Done...')
    f.close()



    num_unique_words = num_of_unique_words()
    print('\n\n\n')
    print(f'Number of unique words {num_unique_words}\n')

    max_story, min_story = max_min()
    print(f'Max len story {max_story}\n\n')
    print(f'Min len story {max_story}\n\n')
    top_10 = top_10_words()
    print(f'Top 10 unique words {top_10}\n\n')




def num_of_unique_words():
    f = open('stories.csv', encoding='utf-8')
    csv_file = csv.reader(f, delimiter=',')
    all_text = ''
    for row in csv_file:
        row = ' '.join(row)
        all_text += row
        
    unique_words_len = len(set(all_text.split()))
    return unique_words_len




def max_min():
    f = open('stories.csv', encoding='utf-8')
    csv_file = csv.reader(f, delimiter=',')
    
    max_len_story_text = ''
    min_len_story_text = ' '*10000
    
    max_len_story = None
    min_len_story = None
    count = 0
    
    for row in csv_file:
        if count == 0:
            count += 1
            continue
            
        if len(row[1]) > len(max_len_story_text):
            max_len_story_text = row[1]
            max_len_story = row
        if len(row[1]) < len(min_len_story_text):
            min_len_story_text = row[1]
            min_len_story = row
        
        count += 1
        
    return (max_len_story, min_len_story)





def top_10_words():
    f = open('stories.csv', encoding='utf-8')
    csv_file = csv.reader(f, delimiter=',')
    
    all_text = ''
    for row in csv_file:
        row = ' '.join(row)
        all_text += row
    
    c = Counter(all_text.split())
    return c.most_common()[:10]






root = Tk()
root.title('BBC urdu scraping ')
root.configure(background='white')

main_frame = Frame(root, padx=300,pady=300, background="white")
main_frame.grid(row=1, column=1)
label = Label(main_frame,font=('Helvetica', 20), text='Enter link', fg='#333333', bg='white')
label.grid(row=0, column=0, padx=(0,10), sticky='W')
entry = Entry(main_frame,font=('Helvetica', 20), bg='#f0f0f0')
entry.grid(row=0, column=1)
button = Button(main_frame,font=('Helvetica', 17), text='Scrape',fg='white',bg='#4788ff', command=scrape)
button.grid(row=1, column=1, pady=10,sticky='E')
button1 = Button(main_frame,font=('Helvetica', 17), text='max story',fg='white',bg='#4788ff', command=max_min)
button1.grid(row=2, column=1, pady=10,sticky='E')

button2 = Button(main_frame,font=('Helvetica', 17), text='Top 10 words',fg='white',bg='#4788ff', command=top_10_words)
button2.grid(row=3, column=1, pady=10,sticky='E')

button2 = Button(main_frame,font=('Helvetica', 17), text='Unique words',fg='white',bg='#4788ff', command = num_of_unique_words)
button2.grid(row=4, column=1, pady=10,sticky='E')


data = pd.read_csv('stories.csv')
df = pd.DataFrame(data)
df.to_excel('stories.xlsx')
#plt.bar(labels,sizes,width=0.5,color=colors)

#plt.xlabel(xtitle)

#plt.ylabel(ytitle)

plt.title("Number of records for each category")

plt.title('.')
plt.xlabel('Category')
plt.ylabel('Number of records')
plt.style.use('bmh')
plt.show()




root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




