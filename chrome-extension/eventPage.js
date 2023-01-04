// Add JavaScript for processes that run in the background
// Examples of code to be included here are: context menus, notifications, etc.

function ensureSendMessage(tabId, message, callback) {
  chrome.tabs.sendMessage(tabId, { ping: true }, function (response) {
    if (response && response.pong) {
      // Content script ready
      chrome.tabs.sendMessage(tabId, message, callback);
    } else {
      chrome.tabs.executeScript(tabId, { file: "content.js" }, function () {
        if (chrome.runtime.lastError) {
          console.error(chrome.runtime.lastError);
          throw Error("Unable to inject script into tab " + tabId);
        }
        chrome.tabs.sendMessage(tabId, message, callback);
      });
    }
  });
}

chrome.runtime.onInstalled.addListener(function () {
  chrome.contextMenus.create({
    title: "Generate alt text for all images",
    contexts: ["all"],
    id: "alto-all",
  });
});

chrome.contextMenus.onClicked.addListener(function (info, tab) {
  ensureSendMessage(tab.id, { id: "alto-all" });
});
