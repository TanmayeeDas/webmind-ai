console.log("✅ WebMind content script loaded!");

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    console.log("📩 Received request:", request);

    if (request.action === "getPageContent") {

        const pageData = {
            title: document.title,
            url: window.location.href,
            text: document.body.innerText
        };

        console.log("📄 Sending page data...");
        console.log("Title:", pageData.title);
        console.log("URL:", pageData.url);
        console.log("Text Length:", pageData.text.length);

        sendResponse(pageData);
    }
});