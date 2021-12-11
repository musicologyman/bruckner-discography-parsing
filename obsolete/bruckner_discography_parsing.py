# coding: utf-8
from html_utils import *
html_files
html_files.sort()
html_files
RAW_INPUT_FILE = html_files[4]
soup = get_soup_from_file(RAW_INPUT_FILE)
divs_with_click_attr = soup.find_all("div[onclick]")
len(divs_with_click_attr)
all_divs = soup.find_all("div")
div[1]
all_divs[1]
all_divs[2]
len(all_divs)
soup.find_all('div')
soup
get_ipython().run_line_magic('whos', '')
html_files = list_html_files()
html_files.sort()
html_files[:5]
html_files[3]
soup = get_soup_from_file(html_files[3])
divs = soup.find_all("div")
divs
def has_onclick(tag):
    return tag.has_attr("onclick")
    
clickables = doc.find_all(has_onclick)
clickables = soup.find_all(has_onclick)
len(clickables)
clickables[0].attrs
clickables[1].attrs
clickables[1].tag
clickables[1].name
for c in clickables:print(c.name)
div[0].attrs
clickables[0].attrs
for c in clickables:
    del c.['onclick']
for c in clickables:
    del c['onclick']
    
for c in clickables:print(f"{c.name}: {c.attrs}")
def has_class_attribute(tag):
    tag.has_attr("class")
    
has_class = soup.find_all(has_class_attribute)
len(has_class)
def has_class_attribute(tag):
    return tag.has_attr("class")
    
has_class = soup.find_all(has_class_attribute)
len(has_class)
for c in has_class:del c['class']
c[0].attrs
c[0]
has_class[0].attrs
has_class[1].attrs
len(has_class[1].attrs)
has_class[2].attrs
for t in has_class[:10]:print(t.name)
print(has_class[3])
head_tags = {c.name for c in soup.head.children}
head_tags
head
soup.head
soup.body
all_scripts = soup.find_all("script")
len(all_scripts)
all_scripts[1].extract()
all_scripts[0].extract()
soup.find_all("script")
all_tables = soup.find_all("table")
len(all_tables)
all_tables[0]
links = soup.find_all("link")
len(links)
links[1].extract()
link[0].extract()
links[0].extract()
images = soup.find_all("img")
len(images)
for i in range(9, -1, -1):
    extracted_text = images[i].extract()
    
get_ipython().run_line_magic('whos', '')
import inspect
dir(inspect)
get_ipython().run_line_magic('whos', '')
write_html_file(soup.prettify(), "andreae-bruckner-discography.html")
write_html_file("andreae-bruckner-discography.html",soup.prettify())
write_html_file("andreae-bruckner-discography.html",soup.prettify())
help(soup.prettify)
html = soup.prettify()
help(inspect)
help(write_html_file)
write_html_file("andreae_bruckner_discography.html", soup)
get_ipython().system('code andreae_bruckner_discography.html')
unordered_lists = soup.find_all("ul")
len(unordered_lists)
ul = unordered_lists[0]
ul
lis = ul.find_all("li")
len(lis)
for i in range(14):
    div = soup.new_tag("div")
    div['style'] = "font-size:22px;font-weight:bold"
    div.string = f"Unordered_list_{i:02}"
    lis[i].insert_before(div)
    
get_ipython().run_line_magic('history', '-n 83-92')
get_ipython().run_line_magic('rep', '87')
write_html_file("andreae_bruckner_discography.html", soup)
for i in range(14):
    print(lis[i].previous_sibling)
    
bad_divs = [lis[i].previous_sibling for i in range(14)]
bad_divs
for d in bad_divs:
    d.decompose()
    
get_ipython().run_line_magic('history', '-n 90-101')
get_ipython().run_line_magic('rep', '98')
write_html_file("andreae_bruckner_discography.html", soup)
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('history', '-n 80-100')
get_ipython().run_line_magic('rep', '95')
for i in range(14):
    div = soup.new_tag("div")
    div['style'] = "font-size:22px;font-weight:bold"
    div.string = f"Unordered_list_{i:02}"
    unordered_lists[i].insert_before(div)
    
get_ipython().run_line_magic('rep', '98')
write_html_file("andreae_bruckner_discography.html", soup)
unordered_lists[0].decompose()
write_html_file("andreae_bruckner_discography_2.html", soup)
soup.body is None
soup.body.style
soup.body.style.decompose()
len(soup.body.children)
len(list(soup.body.children))
for e in soup.body.children:
    print(e.name, end=" ")
    if e.has_attr["id"]:
        print(f"id="{e['id']}")
for e in soup.body.children:
    print(e.name, end=" ")
    if e.has_attr["id"]:
        print(f"id="{e.tag['id']}")
for e in soup.body.children:
    print(e.name, end=" ")
    if e.has_attr["id"]:
        id = e['id']
        print(f"{e.bdddd´bbtaghh['id']}")
for e in soup.body.children:
    print(e.name, end=" ")
    if e.has_attr["id"]:
        id = e['id']
        print(f"id=\"{id}\"")
        
soup.children
list(soup.children)
list(soup.descendants)
for e in soup.body.descendants:
    print(e.name, end=" ")
    if e.has_attr["id"]:
        id = e['id']
        print(f"id=\"{id}\"")
        
for e in soup.body.descendants:
    print(e.name, end=" ")
    try:
        if e.has_attr["id"]:
            id = e['id']
            print(f"id=\"{id}\"")
    except:
        print("")
        
        
for e in soup.body.descendants:
    if not e.name: continue
    print(e.name, end=" ")
    try:
        if e.has_attr["id"]:
            id = e['id']
            print(f"id=\"{id}\"")
    except:
        print("")
        
        
for e in soup.body.descendants:
    if not e.name: continue
    print(e.name, end=" ")
    try:
        if e.has_attr("id"):
            id = e['id']
            print(f"id=\"{id}\"")
    except:
        print("")
        
        
for e in soup.body.descendants:
    if not e.name: continue
    print(e.name, end=" ")
   
    if e.has_attr("id"):
        id = e['id']
        print(f"id=\"{id}\"")
        
for e in soup.body.children:
    if not e.name: continue
    print(e.name, end=" ")
   
    if e.has_attr("id"):
        id = e['id']
        print(f"id=\"{id}\"")
        
for e in soup.body.children[0].children:
    if not e.name: continue
    print(e.name, end=" ")
   
    if e.has_attr("id"):
        id = e['id']
        print(f"id=\"{id}\"")
        
for e in soup.body.div.children:
    if not e.name: continue
    print(e.name, end=" ")
   
    if e.has_attr("id"):
        id = e['id']
        print(f"id=\"{id}\"")
        
kids = soup.body.div.children
for k in kids:
    if k.has_attr("id") and k["id"] != "contentwrapper":
        k.decompose()
        
list(kids)
for t in list(kids):
    print(t.tag)
    
for t in list(kids):
    print(t.name)
    
kid_list = =list(kids)
kid_list = list(kids)
kid_list
get_ipython().run_line_magic('history', '-n 130-140')
get_ipython().run_line_magic('rep', '134')
kids = soup.body.div.children
kids
kid_list = list(kids)
kid_list[0]
kid_list[1]
kid_list[1].decompose()
id_list[2]
kid_list[2]
kid_list[2].decompose()
kid_list[0]
kid_list[3]
kid_list[3].decompose()
dir(kid_list[2])
inspect.getmro(kid_list[2])
inspect.getmro(kid_list[2].__class__)
get_ipython().run_line_magic('history', '-n 120-140')
get_ipython().run_line_magic('history', '-n 100-120')
get_ipython().run_line_magic('rep', '111')
write_html_file("andreae_bruckner_discography.html", soup)
soup = get_soup_from_file("andreae_bruckner_discography.html)
soup = get_soup_from_file("andreae_bruckner_discography.html")
kids = [e for e in soup.body.children]
len(kids)
for k in kids:
    try:
        print(k.tag)
    except:
        print("not an element")
        
k[0]
k[1]
kids[1]
kids[0]
type(kids[0])

        
from bs4.element import NavigableString
type(kids[1])
type(kids[2])
type(kids[3])
kids[1].name
kids[1].has_attr('id')
kids[1]['id']
len(list(kids[1].children))
anchors = soup.body.find_all("a")
len(anchors)
for a in anchors:
    print(a.string)
    
for a in anchors:
    print(a.stripped_string)
    
    
for a in anchors:
    print(a.stripped_strings)
    
    
for a in anchors:
    print(list(a.stripped_strings))
    
    
for a in anchors:
    contents = list(a.stripped_strings)
    if len(contents) > 0:
        print(contents)
        
for a in anchors:
    contents = list(a.stripped_strings)
    if len(contents) > 1:
        print(contents)
        
for a in anchors:
    contents = list(a.stripped_strings)[0]
    a.insert_before(contents)
    a.decompose()
        
get_ipython().run_line_magic('history', '-n 170-188')
get_ipython().run_line_magic('history', '-n 160-169')
get_ipython().run_line_magic('rep', '162')
write_html_file("andreae_bruckner_discography.html", soup)
