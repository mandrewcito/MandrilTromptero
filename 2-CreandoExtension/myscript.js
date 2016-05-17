chrome.browserAction.onClicked.addListener(function (tab) { //Fired when User Clicks ICON
    console.log("ini script");
    if (tab.url.indexOf("https://www.instagram.com/") != -1) { // Inspect whether the place where user clicked matches with our list of URL
        chrome.tabs.executeScript(tab.id, {
            "file": "contentscript.js"
        }, function () { // Execute your code
            console.log("Script Executed .. "); // Notification on Completion
        });
    }
});