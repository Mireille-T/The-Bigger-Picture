// Add JavaScript for processes that run in the background
// Examples of code to be included here are: context menus, notifications, etc.

var contextMenuItem = {
    "id": "TheBiggerPicture",
    "title": "Generate alt text",
    "contexts": ["image"]
}
chrome.contextMenus.create(contextMenuItem);

chrome.contextMenus.onClicked.addListener(function (data) {
    console.log(data);
    if (data.menuItemId == "TheBiggerPicture") {
        console.log("The Bigger Picture: Context menu item clicked!");
    }
})