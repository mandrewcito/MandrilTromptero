chrome.browserAction.onClicked.addListener(function(tab) {
console.log("fiin");
chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
    console.log(tabs[0].url);
    URL=tabs[0].url;
var spawn = require('child_process').spawn;
spawn('ls', ['-l']).stdout.on('data', function (data) {
   console.log(data);
});
});
});
