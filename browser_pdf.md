## browser -pdf 
- when we open a pdf in browser under the hood it is html only as can be seen by inspeciotn
- ![image](https://github.com/m0wn1ka/python/assets/127676379/3cd38f65-9bab-4997-9494-ecdeb7bc704e)
- we can go and get the necessary pages contnt by a few commands in console
- ![image](https://github.com/m0wn1ka/python/assets/127676379/4b072f0c-1826-437a-bad2-58127ecafc5b)
- we get the page number to go by calculation (user inputs)
- we fetch the specific element
- add a id to it
- change window.locaion with that fragment
```
a=document.querySelector(".page[data-page-number='2']").innerText

window.open("file:///home/radha/Desktop/html_browser.html#id2","_self") 
```
### doing 
#### resources
- https://www.educative.io/answers/how-to-add-an-id-to-element-in-javascript
- https://developer.mozilla.org/en-US/docs/Web/API/Window/open ---------cantry to open in the same window
-  
#### adding a id attribute in a html page from console
![image](https://github.com/m0wn1ka/python/assets/127676379/ecf90d8e-6b8d-4045-bfb4-56537feec853)

### ...
- window.open () from the aptitude pdf to google,... opens
- a pdf is not allowing opening a local file to open
![image](https://github.com/m0wn1ka/python/assets/127676379/817937e9-1296-4fc5-ba11-45b6d2f1f291)

## resource:///
- on trying to degbugg the issue we see pdfworker.js with som 12000 lines
- ![image](https://github.com/m0wn1ka/python/assets/127676379/afae134c-3643-4bf4-943e-7ef99cc7fabf)

