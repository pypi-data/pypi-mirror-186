# pathCrawler
Small utility because I got tired of typing more than one line to get a recursive list of pathlib.Path objects for a directory.<br>
Install using <pre>py -m pip install pathCrawler</pre>

<br>
pathCrawler contains three functions: crawl, getDirectorySize, and formatSize.<br>
crawl takes a starting directory and returns a recursive list of pathlib.Path objects for all files in the starting directory and its sub folders.<br>
getDirectorySize takes a directory and returns the total size in bytes of the contents of the directory.<br>
formatSize takes a number (presumed to be bytes) and returns it as a string rounded to two decimal places with the appropriate unit suffix.<br>
i.e. 
<pre>
>>> formatSize(132458)
'132.46 kb'
</pre>
