// console.log("✅ WebMind content script loaded!");

// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

//     console.log("📩 Received request:", request);

//     if (request.action === "getPageContent") {

//         const pageData = {
//             title: document.title,
//             url: window.location.href,
//             text: document.body.innerText
//         };

//         console.log("📄 Sending page data...");
//         console.log("Title:", pageData.title);
//         console.log("URL:", pageData.url);
//         console.log("Text Length:", pageData.text.length);

//         sendResponse(pageData);
//     }
// });


console.log("✅ WebMind content script loaded!");

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    console.log("📩 Received request:", request);

    if (request.action === "getPageContent") {

        // Try to extract only the main content
        let contentElement =
            document.querySelector("article") ||
            document.querySelector("main") ||
            document.querySelector('[role="main"]') ||
            document.body;

        let pageText = contentElement.innerText;

        // Clean the text
        pageText = pageText

            // Remove multiple blank lines
            .replace(/\n\s*\n/g, "\n\n")

            // Remove multiple spaces
            .replace(/[ \t]+/g, " ")

            // Remove repeated empty lines
            .replace(/\n{3,}/g, "\n\n")

            .trim();

        const pageData = {

            title: document.title,

            url: window.location.href,

            text: pageText

        };

        console.log("📄 Sending page data...");
        console.log("Title:", pageData.title);
        console.log("URL:", pageData.url);
        console.log("Text Length:", pageData.text.length);

        sendResponse(pageData);
    }
});