import urllib2


#1h selidaa

url1="https://twitter.com/"
url2=raw_input("sumplirwse to upoloipo meros tou url gia thn 1h selida")
url=url1 + url2
print url

#----------TWEETS------------

request = urllib2.Request(url)

handle = urllib2.urlopen(request)

content=handle.read()

splitted_page = content.split('<span class="ProfileNav-value" data-is-compact="false">',1);

splitted_page =splitted_page[1].split('</span>',1)
Tweets1=splitted_page[0]
#-----------FOLLOWS--------------

split_page= splitted_page[1].split('<span class="ProfileNav-value" data-is-compact="false">',1);

split_page=split_page[1].split('</span>',1)
Follows1=split_page[0]
#---------Followers--------------

split1_page= split_page[1].split('<span class="ProfileNav-value" data-is-compact="true">',1);

split1_page=split1_page[1].split('</span>',1)
Followers1=split1_page[0]
#---------Likes------------------

split2_page= split1_page[1].split('<span class="ProfileNav-value" data-is-compact="false">',1);

split2_page=split2_page[1].split('</span>',1)
Likes1=split2_page[0]



print Tweets1
print Follows1
print Followers1
print Likes1
#2h selida

url3=raw_input("twra gia th 2h")
url4=url1 + url3
print url4
#----------TWEETS------------

request = urllib2.Request(url4)

handle = urllib2.urlopen(request)

content=handle.read()

splitted_page = content.split('<span class="ProfileNav-value" data-is-compact="false">',1);

splitted_page =splitted_page[1].split('</span>',1)
Tweets2=splitted_page[0]
#-----------FOLLOWS--------------

split_page= splitted_page[1].split('<span class="ProfileNav-value" data-is-compact="false">',1);

split_page=split_page[1].split('</span>',1)
Follows2=split_page[0]
#---------Followers--------------

split1_page= split_page[1].split('<span class="ProfileNav-value" data-is-compact="true">',1);

split1_page=split1_page[1].split('</span>',1)
Followers2=split1_page[0]
#---------Likes------------------

split2_page= split1_page[1].split('<span class="ProfileNav-value" data-is-compact="false">',1);

split2_page=split2_page[1].split('</span>',1)
Likes2=split2_page[0]

print Tweets2
print Follows2
print Followers2
print Likes2
a=0
b=0
if Tweets1>Tweets2:
    a=a+1
elif Tweets1<Tweets2:
    b=b+1
else:
    a=a+1
    b=b+1


if Follows1>Follows2:
    a=a+1
elif Follows1<Follows2:
    b=b+1
else:
    a=a+1
    b=b+1

if Followers1>Followers2:
    a=a+1
elif Followers1<Followers2:
    b=b+1
else:
    a=a+1
    b=b+1


if Likes1>Likes2:
    a=a+1
elif Likes1<Likes2:
    b=b+1
else:
    a=a+1
    b=b+1

print "Final Score:",a,"-",b


#den katafera na sugkrinw ta K,M,B



  
      
    


 




