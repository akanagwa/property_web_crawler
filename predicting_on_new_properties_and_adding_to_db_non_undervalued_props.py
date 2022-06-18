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
page_nze = 5


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


new2.head()


# In[124]:


# replacing nans with random r inorder to allow us to run the function above.
new2['lot_size'] = new2['lot_size'].fillna('r')


# In[125]:


new2['lot_size'] = new2['lot_size'].apply(lambda x: find_number(x))


# In[126]:


new2.head(10)


# In[127]:


new2.isna().sum().sort_values(ascending=False)


# In[128]:


new2['sq_ft'] = new2['sq_ft'].str.replace(',', '')


# In[129]:


new2['sq_ft'] = new2['sq_ft'].fillna('r')


# In[130]:


new2.head()


# In[ ]:


# In[131]:


new2['sq_ft'] = new2['sq_ft'].apply(lambda x: find_number(x))  # .astype('float')


# In[ ]:


# In[132]:


# attempting to replace


# In[ ]:


# In[133]:


# replacing blanks with null
new2 = new2.replace(r'^\s*$', np.nan, regex=True)


# In[134]:


new2['lot_size'] = new2['lot_size'].fillna(0)


# In[135]:


new2


# In[136]:


# trying to replace property types for single-family homes so they are in the right column
new2['lot_size'] = np.where(new2['lot_size'] == 0, new2['sq_ft'], new2['lot_size'])


# In[137]:


new2.head(30)


# In[138]:


def lot_size(x):
    if x > 50:
        return np.nan
    else:
        return x


# In[139]:


new2['lot_size'] = new2['lot_size'].str.replace(',', '')


# In[140]:


new2['lot_size'] = new2['lot_size'].astype('float')


# In[141]:


new2['lot_size'] = new2['lot_size'].apply(lot_size)


# In[142]:


new2.head(30)


# In[143]:


# new2['sq_ft']=new2['sq_ft'].str.replace(',','')


# In[144]:


new2['bath_rooms'] = new2['bath_rooms'].str.replace(',', '')


# In[145]:


##
new2['bath_rooms'] = new2['bath_rooms'].fillna('r')


# In[146]:


new2['bath_rooms'] = new2['bath_rooms'].apply(lambda x: find_number(x))


# In[147]:


new2.head(30)


# In[148]:


new2.info()


# In[149]:


new2['bath_rooms'] = new2['bath_rooms'].str.replace(',', '')


# In[150]:


# replacing blanks with null
new2['bath_rooms'] = new2['bath_rooms'].replace(r'^\s*$', np.nan, regex=True)


# In[151]:


new2['bath_rooms'] = new2['bath_rooms'].astype('float')


# In[152]:


# dropping the bathrooms for two useless rows.
new2 = new2[new2['bath_rooms'] < 100]


# In[153]:


new2.head()


# In[ ]:


# In[154]:


# cleaning bedrooms


# In[155]:


new2['bed_rooms'] = new2['bed_rooms'].apply(lambda x: find_number(x))  # .astype('float')


# In[156]:


new2['bed_rooms'] = new2['bed_rooms'].str.replace(',', '')


# In[157]:


new2['bed_rooms'] = new2['bed_rooms'].astype('float')


# In[158]:


new2 = new2[new2['bed_rooms'] < 100]


# In[ ]:


# In[159]:


new2.info()


# In[160]:


new2['sq_ft'] = new2['sq_ft'].astype('float')


# In[161]:


new2.head(50)


# In[ ]:


# In[162]:


new2['price'] = new2['price'].str.replace(',', '')


# In[163]:


new2['price'] = new2['price'].apply(lambda x: find_number(x)).astype('float')


# In[164]:


new2.head(30)


# In[ ]:


# In[165]:


new2[new2['zip_code'] == '74137']


# In[166]:


##new2['address']=new2['address'].str.replace(' ','')


# In[167]:


new2.isna().sum()


# In[168]:


new2['sq_ft'] = new2['sq_ft'].fillna(new2['sq_ft'].median())


# In[169]:


new2['lot_size'] = new2['lot_size'].fillna(new2['lot_size'].median())


# In[170]:


new2.corr()['price'].sort_values(ascending=False)


# In[171]:


new2.head()


# In[172]:


new2['zip_code'] = new2['zip_code'].str.replace('ahoma Ci', '73121')


# In[173]:


new2['zip_code'] = new2['zip_code'].str.replace('sa', '74114')


# In[174]:


# new2[new2['zip_code']=='sa']


# In[175]:


new2.head()


# In[ ]:


# In[176]:


# the code below creates a daily time stamped csv file from our model predictions
#zname = datetime.datetime.today().strftime(r'C:\Users\arnie\Desktop\Oklahoma_housing_data\oklahoma_realestatesale_%Y%m%d.csv')
# new2.to_csv(zname,index=False)


# In[ ]:


# In[ ]:


# # creating a sqllite database  to store data in

# In[177]:


# In[178]:


# creating a new sqllite database
conn = sqlite3.connect(
    r'C:\Users\arnie\Desktop\business_analytics\PYTHON_FOR_ANALYTICS\Web_Scraping\Latest_version\oklahoma_homes_sale.db')


# ##dropping a sqlite table
# conn.execute('''
# 		drop TABLE homes
#                ''')

# ##deleting records
# conn.execute('''
# 		delete from  homes where unique_id in ('d63036c53','3acec1a3d')
#                ''')
# conn.commit()

# conn.execute('''
# 		drop TABLE homes
#                ''')

# In[179]:


new2.head()


# In[180]:


# attempting to update 528db3a24


# In[181]:


# updatingall existing homes with latest house prices
# frist you have to change values you want to insert to a list
nze = new2[['price', 'unique_id']].values.tolist()


# In[182]:


nze


# In[183]:


# this is sql code that updates all the new home prices
conn.executemany(''' UPDATE homes SET price=?
WHERE unique_id=? ;''', nze)
conn.commit()


# In[ ]:


# In[184]:


# current.to_csv('correctprice.csv',index=False)


# In[ ]:


# In[ ]:


# In[185]:


# only had to run this one time
#new2.to_sql('homes', conn,index=False)


# In[ ]:


# In[186]:


# reading data from sqllite database
current = pd.read_sql('SELECT * FROM homes', conn)


# In[187]:


current.shape


# In[188]:


current.shape


# In[189]:


current.head()


# In[ ]:


# In[ ]:


# In[190]:


new_entry = new2[~new2['unique_id'].isin(current['unique_id'])]


# In[191]:


new_entry


# In[192]:


# new_entry.to_sql('homes',conn,index=False,if_exists='append')


# In[ ]:


# In[193]:


# using current but will replace with new_entry
new2 = new_entry.copy()

new2['zip_code'] = new2['zip_code'].str.replace(' ', '')

# In[194]:


# replacing properties with sq_ft less than 50 with the median sqft


# In[195]:


def sq_ft(x):
    if x < 50:
        return np.nan
    else:
        return x


# In[196]:


new2['sq_ft'] = new2['sq_ft'].apply(sq_ft)


# In[197]:


new2['sq_ft'] = new2['sq_ft'].fillna(new2['sq_ft'].median())


# In[198]:


new2[new2['sq_ft'] < 50]


# In[199]:


# removing spaces from city to allow for filtering.
new2['city'] = new2['city'].str.strip()


# In[200]:


new2['price_per_sq_ft'] = new2['price']/new2['sq_ft']


# In[201]:


# calculating distance between two zipcodes
# Geographical distance is the distance measured along the surface of the earth.
# The formulae  calculate distances between points which are defined by geographical coordinates in
# terms of latitude and longitude. This distance is an element in solving the second (inverse) geodetic problem.
dist = pgeocode.GeoDistance('US')
# adding OU medical center distance to our datafame
new2['devon_zip'] = '73102'
new2['geo_distance_km'] = dist.query_postal_code(
    new2['zip_code'].to_list(), new2['devon_zip'].to_list())


# In[202]:


# bedroom to bathroom ratio
new2['bed_to_bath_ratio'] = new2['bath_rooms']/new2['bed_rooms']


# In[ ]:


# In[ ]:


# # average price by zipcode has to be from the average price of homes in the database.

# In[203]:


# adding median price by zipcode
median_price_byzipcode = current.groupby('zip_code')[['price']].median(
).reset_index().rename({'price': 'median_homeprice_byzip'}, axis=1)


# In[ ]:


# In[204]:


# In[205]:


# adding census zipcode data
zip_census = pd.read_excel(r'C:\Users\arnie\Desktop\OU health stuff\zip_stats.xlsx')


# In[206]:


zip_census.columns = zip_census.columns.str.replace(' ', '')


# In[207]:


zip_census = zip_census.drop('Mean_income', axis=1)


# In[208]:


zip_census = zip_census.rename({'AddressZipCode': 'zip_code'}, axis=1)


# In[209]:


# merging
new3 = new2.merge(median_price_byzipcode, on='zip_code', how='left')


# In[210]:


zip_census['zip_code'] = zip_census['zip_code'].astype(str)


# In[211]:


new4 = new3.merge(zip_census, on='zip_code', how='left')


# In[212]:


# new4['Mean_income']=new4['Mean_income'].astype('float')


# In[213]:


new4['percapitmedianzipprice'] = new4['median_homeprice_byzip']/new4['Population']


# In[ ]:


# In[218]:


###reading in nulls
nulls = pd.read_csv(
    r'C:\Users\arnie\Desktop\business_analytics\PYTHON_FOR_ANALYTICS\Web_Scraping\Latest_version\null.csv')


# In[219]:


nulls.head()


# In[220]:
print(new4.columns)

# for now..leave this , will figure out how to deal with missing values when time comes
# for now..leave this , will figure out how to deal with missing values when time comes
new4['geo_distance_km'] = new4['geo_distance_km'].fillna(nulls['geo_distance_km'].mean())
new4['median_homeprice_byzip'] = new4['median_homeprice_byzip'].fillna(
    nulls['median_homeprice_byzip'].median())
new4['Median_income'] = new4['Median_income'].fillna(nulls['Median_income'].median())
new4['Population'] = new4['Population'].fillna(nulls['Population'].median())
new4['percapitmedianzipprice'] = new4['percapitmedianzipprice'].fillna(
    nulls['percapitmedianzipprice'].median())

# In[221]:


new5 = new4


new5 = new5[new5['price'] < 500000]


# In[223]:


new6 = new5.set_index('unique_id').select_dtypes(exclude=['object'])


# In[ ]:


# In[224]:


# dropping price
new7 = new6.drop('price', axis=1)


# In[225]:


# call saved model
rf_model = joblib.load(
    r'C:\Users\arnie\Desktop\business_analytics\PYTHON_FOR_ANALYTICS\Web_Scraping\Latest_version\rf_final.pkl')


# In[226]:


new5.head()


# In[ ]:


# # first find duplexes that might be a good deal

# In[227]:


a = new5['bed_rooms'] >= 5
# less than 130 is the ideal price per square foot for a good deal on a duplex
b = new5['price_per_sq_ft'] < 130


# In[228]:


duplex = new5[a & b]


# In[229]:


duplex


# In[230]:


# for now we will just email this in the future we will see if it is worth it to add other additions like
# duplex['diffpriceaveragezip']=duplex['price']-duplex['average_homeprice_byzip'] #to see the most likely good deal
# duplex_sort=duplex.sort_values(['price_per_sq_ft']) #helping to find the best deal
# duplex_sort[duplex_sort['property_type']=='Other'] #also helping to find the best deal


# In[231]:


# In[232]:


# emailing available duplexes
recipients = ['arniekanagz@yahoo.com']
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "duplexes"
msg['From'] = 'arniekanagz@yahoo.com'
html = """<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(build_table(duplex, 'blue_light'))
part1 = MIMEText(html, 'html')
msg.attach(part1)
username = str('arniekanagz@yahoo.com')
password = str('bjsnrleduoosdhna')
server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
server.connect("smtp.mail.yahoo.com", 587)
server.starttls()
server.login(username, password)
server.sendmail(msg['From'], emaillist, msg.as_string())
server.quit()


# In[ ]:


# In[ ]:


# In[233]:


try:
    new5['predictions'] = rf_model.predict(new7)
    new5['diff'] = new5['predictions']-new5['price']
    undervalued_sort = new5.sort_values('diff', ascending=False).reset_index(drop=True)
    undervalued_sort = undervalued_sort[undervalued_sort['diff'] > 5000]
    # only return properties that are undervalued, add the rest to the database
    new_entry2 = new_entry[~new_entry['unique_id'].isin(undervalued_sort['unique_id'])]
    new_entry2.to_sql('homes', conn, index=False, if_exists='append')
except:
    recipients = ['arniekanagz@yahoo.com']
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "under_valued_properties"
    msg['From'] = 'arniekanagz@yahoo.com'
    username = str('arniekanagz@yahoo.com')
    password = str('bjsnrleduoosdhna')
    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    server.connect("smtp.mail.yahoo.com", 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(msg['From'], emaillist, msg.as_string())
    server.quit()


# emailing undervalued properties
recipients = ['arniekanagz@yahoo.com']
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "under_valued_properties"
msg['From'] = 'arniekanagz@yahoo.com'
html = """\
<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(build_table(undervalued_sort, 'blue_light'))
part1 = MIMEText(html, 'html')
msg.attach(part1)
username = str('arniekanagz@yahoo.com')
password = str('bjsnrleduoosdhna')
server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
server.connect("smtp.mail.yahoo.com", 587)
server.starttls()
server.login(username, password)
server.sendmail(msg['From'], emaillist, msg.as_string())
server.quit()
