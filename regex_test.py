#!/usr/bin/env python
# coding: utf-8

# In[1]:


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pretty_html_table import build_table
import smtplib
import joblib
import pgeocode
import sqlite3
import re
import hashlib
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime as datetime

# In[2]:


# always enter page number you want
page_nze = 6


# pd.options.display.max_colwidth=None


# In[4]:


# https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK.html?page={}


# In[5]:


# https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK.html?location=Edmond%2C+OK&search_mode=location&SelectedView=listings&LocationGeoId=879183&location_changed=true&ajax&page='+str(urls)


# In[6]:


# Edmond


# In[7]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Edmond.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[8]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[9]:


edmond = pd.DataFrame(housing)
print(edmond)

# In[ ]:


# In[10]:


# oklahoma city


# In[11]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Oklahoma-City.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[12]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[13]:


oklahoma_city = pd.DataFrame(housing)


# In[ ]:


# In[14]:


# Tulsa


# In[15]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Tulsa.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[16]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[17]:


tulsa = pd.DataFrame(housing)


# In[ ]:


# In[18]:


# norman
def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Norman.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[19]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[20]:


norman = pd.DataFrame(housing)


# In[ ]:


# In[21]:


# broken arrow

def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Broken-Arrow.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[22]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[23]:


broken_arrow = pd.DataFrame(housing)


# In[ ]:


# In[24]:


# Lawton

def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Lawton.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[25]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[26]:


lawton = pd.DataFrame(housing)


# In[ ]:


# In[27]:


# Moore

def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Moore.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[28]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[29]:


moore = pd.DataFrame(housing)


# In[ ]:


# In[30]:


# all of oklahoma

def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK.html?page={}'.format(page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[31]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[32]:


all_oklahoma = pd.DataFrame(housing)


# In[ ]:


# In[33]:


# counties
def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Oklahoma-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[34]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[35]:


ok_county = pd.DataFrame(housing)


# In[ ]:


# In[36]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Tulsa-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[37]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[38]:


tu_county = pd.DataFrame(housing)


# In[ ]:


# In[39]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Cleveland-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[40]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[41]:


cl_county = pd.DataFrame(housing)


# In[ ]:


# In[42]:


# norman
def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Canadian-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[43]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[44]:


ca_county = pd.DataFrame(housing)


# In[ ]:


# In[45]:


# all of oklahoma

def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Comanche-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[46]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[47]:


com_county = pd.DataFrame(housing)


# In[ ]:


# In[48]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Rogers-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[49]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[50]:


rog_county = pd.DataFrame(housing)


# In[ ]:


# In[51]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Wagoner-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[52]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[53]:


wag_county = pd.DataFrame(housing)


# In[ ]:


# In[54]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Payne-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[55]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[56]:


pay_county = pd.DataFrame(housing)


# In[ ]:


# In[57]:


def get_page_data(page):
    print('page:', page)

    url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/OK/Pottawatomie-County.html?page={}'.format(
        page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    address = []
    address_element = soup.find_all(class_='address-container')
    for item in address_element:
        address.append(item.text)

    price = []
    price_element = soup.find_all(class_='price')
    for item in price_element:
        price.append(item.text)

    characteristics = []
    charac_element = soup.find_all(class_='item-info-cnt')  # characteristics-cnt
    for item in charac_element:
        characteristics.append(item.text)

    final = []
    for address, price, characteristics in zip(address, price, characteristics):
        final.append({'address': address, 'price': price, 'characteristics': characteristics})
        #print (final)

    # final=[[address,characteristics]]

    return final


# In[58]:


housing = []
for page in range(1, page_nze):
    oklahoma = get_page_data(page)
    housing.extend(oklahoma)


# In[59]:


potta_county = pd.DataFrame(housing)


# In[ ]:


# In[60]:


new = pd.concat([edmond, oklahoma_city, tulsa, norman, broken_arrow, lawton, moore, all_oklahoma, ok_county,
                tu_county, cl_county, ca_county, com_county, rog_county, wag_county, pay_county, potta_county], axis=0)


# In[ ]:


# In[61]:


new.head()


# In[62]:


new[new["address"].str.contains("Pheasant")]


# In[63]:


new[new['address'] == '\r\n 2600 Bobwhite Trail, Edmond, OK 73025\r\n']


# In[64]:


new['price'] = new['price'].map(lambda x: str(x)[21:-17])


# In[65]:


pd.options.display.max_colwidth = None


# In[66]:


new.head()


# def char_split(x):
#     return x.str.split('\n')

# In[67]:


new.info()


# In[68]:


new['characteristics'] = new['characteristics'].str.split('\n')


# In[69]:


new.head()


# In[70]:


# new2=new


# In[71]:


#new=new.replace(r'\s+|\\n', ' ', regex=True)


# In[72]:


new['zip_code'] = new['address'].str.split(",", expand=True)[2].str[4:12]


# In[73]:


new['city'] = new['address'].str.split(',', expand=True)[1]


# In[74]:


new['bed_rooms'] = new['characteristics'].str[4]


# In[75]:


new['bath_rooms'] = new['characteristics'].str[7]


# In[76]:


new['sq_ft'] = new['characteristics'].str[10]


# In[77]:


new['lot_size'] = new['characteristics'].str[13]


# In[78]:


new['property_type'] = new['characteristics'].str[16]


# In[ ]:


# In[ ]:


# In[ ]:


# In[79]:


new.drop(columns=['characteristics'], inplace=True)


# In[ ]:


# In[ ]:


# In[ ]:


# In[80]:


# new=pd.read_csv('new.csv',thousands='.')
new = new.replace(r'\s+|\\n', ' ', regex=True)


# In[81]:


new = new.replace(r'^\s*$', np.nan, regex=True)


# In[82]:


new[new['zip_code'] == '73505']


# # saving file for future use
# ##new.to_csv('new.csv',index=False)

# In[83]:


# new.to_csv('new.csv',index=False)


# In[84]:


# In[85]:


# new=pd.read_csv('new.csv')


# In[86]:


new.head()


# In[ ]:


# In[87]:


# fill the missing


# In[88]:


new['property_type'].value_counts()


# In[89]:


# filling null property types with 0 for np where clause
new['property_type'].fillna(0, inplace=True)


# In[90]:


new.head(30)


# In[ ]:


# In[ ]:


# In[ ]:


# In[91]:


# trying to replace property types for single-family homes so they are in the right column
new['property_type'] = np.where(new['property_type'] == 0, new['lot_size'], new['property_type'])


# In[92]:


new.head(30)


# In[93]:


new['property_type'].value_counts()


# In[94]:


new[new['zip_code'] == '74014']


# In[ ]:


# In[95]:


# trying to get residential missing property types moved from lot size to property type
new.head(30)


# In[96]:


# filling null property types with 0 for np where clause
# new['lot_size'].fillna(0,inplace=True)


# In[97]:


# new['property_type']=np.where(new['property_type']==0,new['lot_size'],new['property_type'])


# In[98]:


# trying to replace property types for single-family homes so they are in the right column
# new['lot_size']=np.where(new['lot_size']==0,new['sq_ft'],new['lot_size'])


# In[ ]:


# In[99]:


# filling null property types with 0 for np where clause
new['property_type'].fillna(0, inplace=True)


# In[100]:


new['property_type'] = np.where(new['property_type'] == 0, new['sq_ft'], new['property_type'])


# In[101]:


new.head(30)


# In[102]:


# after this point rememeber to run the property code above again


# In[103]:


new.head(30)


# In[ ]:


# In[104]:


new['property_type'].value_counts()


# In[ ]:


# In[105]:


# removing all whitespace from address
new['address'] = new['address'].str.replace(' ', '')


# In[106]:


# removing all whitespaces form property_type column
new['property_type'] = new['property_type'].str.replace(' ', '')


# In[107]:


new[new['property_type'] == 'Residential'].sort_values('address').head(30)


# In[108]:


# there are a lot of duplicates and need to keep that in mind
new[new['address'] == '1020NE33rdTerrace,Moore,OK73160']


# In[109]:


# creating a unique indentifier based on the addresses in order to drop duplicates


# In[110]:


new['unique_id'] = [hashlib.sha1(str.encode(str(i))).hexdigest() for i in new['address']]
new['unique_id'] = new['unique_id'].str[0:9]


# In[ ]:


# In[111]:


new[new['zip_code'] == '73505'].sort_values('unique_id').head(30)


# In[112]:


new2 = new.drop_duplicates(subset='unique_id')


# In[113]:


new2.head(20)


# In[114]:


new2[new2['unique_id'] == '43b7b2a9f']


# In[115]:


new2[new2['zip_code'] == '73505']


# In[116]:


new2['property_type'].value_counts()


# In[117]:


# keeping only single family homes and residential homes
#new2=new[(new['property_type']=='Residential') |  (new['property_type']=='Single-FamilyHome')]


# In[ ]:


# In[118]:


new2.head(30)


# In[119]:


new2['lot_size'] = new2['lot_size'].str.replace(' ', '')


# In[120]:


new2.info()


# In[121]:


new2.head(20)


# In[122]:


def find_number(text):
    num = re.findall(r'[.,0-9]+', text)
    return " ".join(num)


# In[123]:
pd.options.display.max_columns = None


print(new2.head())
