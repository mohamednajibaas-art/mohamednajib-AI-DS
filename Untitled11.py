#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
labels=['apple','banana','cherry','mango']
sizes =[30,25,20,25]
plt.pie(sizes,labels = labels,autopct = '%1.1f%%')
plt.title('fruit distribution')
plt.show()


# In[12]:


import matplotlib.pyplot as plt
labels = ['chrome','firefox','edge','safari']
sizes = [65,20,10,5]
plt.pie(sizes,labels = labels,autopct = '%1.1f%%')
plt.title('BROWSCV USAGE SHARE')
plt.show()


# In[19]:


import matplotlib.pyplot as plt
students  = ['A','B','C','D']
marks = [78,85,90,88]
plt.plot(students,marks,  marker='o')
plt.title('STUDENTS MARK')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()

