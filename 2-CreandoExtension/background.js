chrome.browserAction.onClicked.addListener(function(tab) {
console.log("fiin");
chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
    console.log(tabs[0].url);
    URL=tabs[0].url;
var pathname = window.location.pathname;
var url      = window.location.href; 
console.log(pathname);
console.log(url);
 var fso = new ActiveXObject("Scripting.FileSystemObject");  
var fileObject = fso.OpenTextFile("/home/mandrewcito/WorkOn/blog/1-getInstagram/test/fileExample.txt", 8, true);
f.WriteLine(url);
f.Close;
});
});
