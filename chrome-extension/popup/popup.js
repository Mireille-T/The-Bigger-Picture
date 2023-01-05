const settings = {}; // in-page cache of setting changes

window.addEventListener("load", event => {
    revertSettings();

    document.getElementById("save-btn").addEventListener("click", saveSettings);
    document.getElementById("revert-btn").addEventListener("click", revertSettings);
})

function saveSettings() {
    settings.autogen = document.getElementById("auto-gen-toggle").checked;
    settings.lazyload = document.getElementById("lazy-load-toggle").checked;
    settings.language = document.getElementById("languages").value;
    chrome.storage.sync.set({settings});
}

function revertSettings() {
    chrome.storage.sync.get("settings", function (result) {
        // If result is null, use default values
        try {
            document.getElementById("auto-gen-toggle").checked = result.settings.autogen;
        } catch (error) {
            document.getElementById("auto-gen-toggle").checked = true;
        }

        try {
            document.getElementById("lazy-load-toggle").checked = result.settings.lazyload;
        } catch (error) {
            document.getElementById("lazy-load-toggle").checked = true;
        }

        try {
            document.getElementById("languages").value = result.settings.language;
        } catch (error) {
            document.getElementById("languages").value = "en";
        }
    });
}