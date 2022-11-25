// Add JavaScript for processes that run in the background
// Examples of code to be included here are: context menus, notifications, etc.

var contextMenuItem = {
    "id": "alto",
    "title": "Generate alt text",
    "contexts": ["image"]
}
chrome.contextMenus.create(contextMenuItem);

chrome.contextMenus.onClicked.addListener(function (data) {
    console.log(data);
    if (data.menuItemId == "alto") {
        console.log("alto: Context menu item clicked!");
    }
})