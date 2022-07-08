# Maplestory_StarForce_Simulator

## Prerequisite
Download numpy and tqdm to windows/Mac <br/>
Numpy: https://phoenixnap.com/kb/install-numpy <br/>
Tqdm: https://blog.finxter.com/how-to-install-tqdm-in-python/ <br/>

## sfList.py 
Contains library of respectives rates for each star force level <br/>
Source: https://strategywiki.org/wiki/MapleStory/Spell_Trace_and_Star_Force#Star_Force_Enhancement

## calstar.py

### Starforce <br/>
Star Force Enhancement is the additional enhancement after the equipment's upgrade slots are fully used up. <br/>
Infuse stars into your equipment for stat bonuses! This system costs mesos to use.<br/>

#### Success rate table <br/>
![image](https://user-images.githubusercontent.com/51332449/178035149-4ff8be95-e1d6-46c4-bced-e434a2617540.png)<br/>

#### Starforce events <br/>
Starforce events can affect the success rate at different levels or reducing the cost <br/>
Such as: <br/>
- 1+1 stars up to 10 stars: 0 -> 12 stars <br/>
- 30% discount off enhancement cost: 12 -> 15 stars <br/>
- 100% success at 5/10/15: 15 -> 17 stars <br/>

#### Other factors affecting starforce rates and cost <br/>
- Safeguard
- StarCatcher
- MVP Silver/Gold/Diamond/Red

### FailStack <br/>
A Failstack is an indicator of the times you have continuously failed at enhancement <br/>
In Maplestory there is a superstition where they scroll lv 10 weapon with 30% spell trace,<br/>
after x amount of fails, they then star force the intended equipment <br/>


### Without Fail Stack
![image](https://user-images.githubusercontent.com/51332449/178011695-10ed2c72-b2ee-4d59-8aef-bf4a0250754d.png) <br/>
Output: <br/>
![image](https://user-images.githubusercontent.com/51332449/178011936-3e9acacc-8ca6-4735-8a16-8df0fdb8b478.png)<br/>

### With Fail Stack
![image](https://user-images.githubusercontent.com/51332449/178013216-286d1265-8309-4421-855d-c7c3a979e518.png)<br/>
#### Failstack = 0 <br/>
![image](https://user-images.githubusercontent.com/51332449/178012436-e6154cbb-b6ff-480d-a26d-3fed90988249.png)<br/>
#### Failstack = 1 <br/>
![image](https://user-images.githubusercontent.com/51332449/178012568-c3031f8f-3d93-4886-818b-e04ffa79a943.png)<br/>
#### Failstack = 2 <br/>
![image](https://user-images.githubusercontent.com/51332449/178012723-abbe3de6-af80-49ff-991b-b31fc7074aab.png)<br/>
#### Failstack = 3 <br/>
![image](https://user-images.githubusercontent.com/51332449/178012833-ae81139a-60fc-420a-ac9e-d684957bdba6.png)<br/>
#### Failstack = 4 <br/>
![image](https://user-images.githubusercontent.com/51332449/178012916-c7d7d679-ba97-4eee-9b91-72736975b68f.png)<br/>

### See Staring Process
![image](https://user-images.githubusercontent.com/51332449/178033251-ea323ab1-6155-4c8c-a545-909c7c56004e.png)<br/>
Output: <br/>
![image](https://user-images.githubusercontent.com/51332449/178033411-b548b871-8ce3-4cba-a2dc-8de762339972.png)<br/>



